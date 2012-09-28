# -*- coding: utf-8 -*-

""" supplies a local api interface for other programs to utilize """

import translate
import rpc

import service
import options
import common

import tools
import re
import xmlrpclib
import base64

from multiprocessing import Process, Manager
from multiprocessing.managers import BaseManager, SyncManager
from SimpleXMLRPCServer import SimpleXMLRPCServer
from urlparse import urlparse
import atexit
import thread
import time

import gobject
from collections import deque

api = None

def echo(fn):
	#a debugging tool intended to be used as a function decorator
	from itertools import chain
	def wrapped(*v, **k):
		name = fn.__name__
		print "%s(%s)" % (name, ", ".join(map(repr, chain(v, k.values()))))
		results = fn(*v, **k)
		print results
		return results
	return wrapped

class api_main(service.Service):
	def __init__(self, name='api.main', audience='api.*'):
		#initialize service
		service.Service.__init__(self, name, audience)
		self.terminated = False
		self.m = SyncManager(address=('', 50005))
		self.m.start()
		global api
		api = self.m.dict()
		api['session'] = {
			'url': rpc.session._url,
			'db': rpc.session.db,
			'uid': rpc.session.uid,
			#'obj': rpc.session._obj,
			'passwd': rpc.session._passwd,
			'uname': rpc.session.uname,
		}
		api['actions'] = deque()
		self.p = Process(target=api_main.run, args=(self, ))
		self.p.start()
		atexit.register(api_main.destroy, (self))
		#NOTE: threads here aren't really useful when they're trapped by the GIL  :(
		#self.t = thread.start_new_thread(api_main.sync, (self, ))

		gobject.timeout_add(int(2) * 1000, self.sig_watch)

	@staticmethod
	def action(action, context=False):
		""" queues an action for execution
			actions are formated in the same fashion they are on the server
			@param action a dictionary of action variables
				example:
					action = {
						'name': "Support",
						'view_mode': 'form',
						'view_type': 'form',
						'res_model': 'crm.metro.helpdesk',
						'res_id': helpdesk_id,
						'type': 'ir.actions.act_window',
						'nodestroy': True,
						'domain': '[]',
						'context': context,
					}
			@param context a dictionary of context variables
		"""
		global api
		print 'received action: ', action, context
		try:
			if not context:
				context = {}
			queue = api.get('actions')
			queue.append((action, context))
			api.update({'actions': queue})
		except Exception as e:
			print e
			raise

		return True
	
	@staticmethod
	def execute(model, method, *args):
		#create local session
		try:
			parsed_url = urlparse(api['session']['url'])
			uname = api['session']['uname']
			passwd = api['session']['passwd']
			hostname = parsed_url.hostname
			port = parsed_url.port
			scheme = parsed_url.scheme if parsed_url.scheme else 'http'
			db = api['session']['db']
			url = scheme + '://' + hostname + ':' + str(port)
		except AttributeError as e:
			#likely hasn't logged in yet
			raise AttributeError('Not logged in / No user credentials found')
		## execute request
		try:
			server_common = xmlrpclib.ServerProxy ('%s/xmlrpc/common' % url)
			uid = server_common.login(db, uname, passwd)
			#replace localhost with the address of the server
			server = xmlrpclib.ServerProxy('%s/xmlrpc/object' % url)

			#NOTE: due to the lack of introspection, we're just going to have to use the examples they've given us,
			# inspect existing client behavior, existing code base,
			# and/or fire up wireshark to see what arguments are available, and how they're used
			#NOTE: they appear to follow their ORM counter-parts (listed before their function calls)
			# http://doc.openerp.com/v6.0/developer/2_5_Objects_Fields_Methods/methods.html (doesn't list all of them)
			# openerp-server/osv/orm.py (lists all of them)
			res = server.execute(db, uid, passwd, model, method, *args)
		except TypeError as e:
			raise TypeError(e.message + '  Are we logged in?')
		
		#this would be the rpc session version of the above... if we could ever figure
		# out how it works...
		#protocol = scheme + '://' if scheme else ''
		#session = rpc.rpc_session()
		#session.login(uname, passwd, hostname, port, protocol, db)
		#res = session.rpc_exec_auth('/object', method, model, *args) or False
		#session.logout()
		#destroy local session
		return res

	def destroy(self):
		self.terminated = True
		self.p.terminate()
		self.p.join()

	def run(self):
		#print 'initializing local api'
		#export any methods we want to export
		#self.exportMethod(self.win_add)

		#start rpc server
		server = SimpleXMLRPCServer(("localhost", 8005))
		server.register_introspection_functions()
		server.register_function(api_main.execute)
		server.register_function(api_main.action)
		#print server.funcs.keys()
		#print 'serving forever'
		server.serve_forever()
		#print 'done serving'

	def sig_watch(self):
		#watch for & fulfill requests
		
		global api
		
		try:
			api['session'] = {
				'url': rpc.session._url,
				'db': rpc.session.db,
				'uid': rpc.session.uid,
				#'obj': rpc.session._obj,
				'passwd': rpc.session._passwd,
				'uname': rpc.session.uname,
			}

			#check if there's an action that needs to be performed
			api_deq = api.get('actions', False)
			#print 'what we have in the deque: ', str(api_deq)
			while api_deq:
				#perform action
				action, context = api_deq.popleft()
				if not context:
					context = {}
				#print 'performing action: ', action, context
				try:
					obj = service.LocalService('action.main')
					obj._exec_action(action, {}, context)
				except Exception as e:
					print e
				finally:
					api.update({'actions': api_deq})
				api_deq = api.get('actions', False)
		except Exception as e:
			pass	#we're done
		
		gobject.timeout_add(int(2) * 1000, self.sig_watch)

api_main()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

