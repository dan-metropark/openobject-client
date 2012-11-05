# -*- coding: utf-8 -*-

"""

Requirements:
	windows (IE):
		pygtk 2.24.2 (2.24.0 has rendering issues)
		IE 8 or greater (support for anything lower not implemented)
			lower versions:
				-must use OnClick instead of OnBeforeNavigate2
				-don't show embedded images
	other (linux):
		pywebkitgtk
"""

import gtk

import interface
import locale
import options

import re
import os
import sys
import webbrowser
import urlparse

import rpc
import service
import cgi
import common
import base64
import tempfile
import printer

if sys.platform == 'win32':
	from pygtkie import IEHtmlView, IEHtmlViewCallback
	class IEWikiCallback(IEHtmlViewCallback):
		""" IE wiki callback class
		callbacks here for for both browser & document callbacks
		(hence the name, IEHtmlViewCallback)
		"""
		def __init__(self, widget, *args, **kwargs):
			""" expects an html widget to handle web requests """
			self.widget = widget
			return super(IEWikiCallback, self).__init__(*args, **kwargs)
			
		def OnBeforeNavigate(self, dest):
			d = dest.split('#')	#people don't use #'s in file names; if they do, they shouldn't  :)
			drive, tail = os.path.splitdrive(dest)
			if len(d) and os.path.exists(d[0]):
				return False	#continue w/ original navigation
			elif os.path.exists(drive):
				#this is an internal url
				import base64
				try:	#decode request
					base, url_encoded = os.path.split(tail)
					url_path = base64.b64decode(url_encoded)
				except Exception as e:
					url_path = tail
				parse_results = urlparse.ParseResult(scheme='internal', netloc='',
					path=url_path, params='', query='', fragment='')
				dest = urlparse.urlunparse(parse_results)
			if self.widget:
				url = urlparse.urlparse(dest)
				#TODO: see if we need to turn the results into a bool value
				#the browser seems to hide itself on new windows
				return self.widget.navigation_requested(url)
			return False	#continue w/ original navigation

		def Ononfocusout(self, event, html_element):
			self.widget._focus_out()
			return True

		def Ononfocusin(self, event, html_element):
			#self.widget._focus_out()
			return False

class html(interface.widget_interface):
	
	def __init__(self, window, parent, model, attrs={}, label=None):
		interface.widget_interface.__init__(self, window, parent, model, attrs, label_ebox=label)

		#setup web label
		orientation = attrs.get('orientation', 'horizontal')
		if orientation == 'vertical':
			self.wiki_label = gtk.HBox(homogeneous=False, spacing=0)
		else:
			self.wiki_label = gtk.VBox()
		l = gtk.Label('<b>View/Preview</b>')
		l.set_use_markup(True)
		l.set_alignment(0.0, 0.5)
		eb = gtk.EventBox()
		eb.set_events(gtk.gdk.BUTTON_PRESS_MASK)
		eb.add(l)
		#container.trans_box_label.append((eb, text, None))
		self.wiki_label.pack_start(eb)
		if orientation == 'vertical':
			vsep = gtk.VSeparator()
			rowspan = int(attrs.get('rowspan', '1'))
			vsep.set_size_request(1, 20*rowspan)
			self.wiki_label.pack_start(vsep, False, False, 5)
			xoptions = gtk.SHRINK
		else:
			xoptions = False
			self.wiki_label.pack_start(gtk.HSeparator())
		
		#setup web view
		self.wiki_scroller = gtk.ScrolledWindow()
		self.wiki_scroller.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
		self.wiki_scroller.set_shadow_type(gtk.SHADOW_NONE)
		#self.wiki_scroller.set_size_request(-1, 80)
		import sys
		if sys.platform == 'win32':
			from pygtkie import IEHtmlView
			self.wiki_browser = IEHtmlView()
			self.wiki_browser.setHtmlViewCallback(IEWikiCallback(self))
			self.wiki_scroller.add_with_viewport(self.wiki_browser.widget)
		else:
			import webkit
			self.wiki_browser = webkit.WebView()
			self.wiki_browser.connect('navigation-requested', lambda x,y,z: self._webkit_navigation_requested(x, y, z))
			self.wiki_scroller.add(self.wiki_browser)

		#setup edit label
		orientation = attrs.get('orientation', 'horizontal')
		if orientation == 'vertical':
			self.edit_label = gtk.HBox(homogeneous=False, spacing=0)
		else:
			self.edit_label = gtk.VBox()
		l = gtk.Label('<b>Edit</b>')
		l.set_use_markup(True)
		l.set_alignment(0.0, 0.5)
		eb = gtk.EventBox()
		eb.set_events(gtk.gdk.BUTTON_PRESS_MASK)
		eb.add(l)
		#container.trans_box_label.append((eb, text, None))
		self.edit_label.pack_start(eb)
		if orientation == 'vertical':
			vsep = gtk.VSeparator()
			rowspan = int(attrs.get('rowspan', '1'))
			vsep.set_size_request(1, 20*rowspan)
			self.edit_label.pack_start(vsep, False, False, 5)
			xoptions = gtk.SHRINK
		else:
			xoptions = False
			self.edit_label.pack_start(gtk.HSeparator())
		#setup edit view
		self.edit_scroller = gtk.ScrolledWindow()
		self.edit_scroller.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
		#self.edit_scroller.set_shadow_type(gtk.SHADOW_NONE)
		#self.edit_scroller.set_size_request(-1, 80)

		self.edit_tv = gtk.TextView()
		self.edit_tv.set_property("can-focus", True)
		self.edit_tv.set_wrap_mode(gtk.WRAP_WORD)
		#add menu & focus handlers
		self.edit_tv.connect('populate-popup', self._menu_open)
		self.edit_tv.set_accepts_tab(False)
		self.edit_tv.connect('focus-out-event', lambda x,y: self._focus_out())
		#detect & add spellcheck
		if options.options['client.form_text_spellcheck']:
			try:
				import gtkspell
				gtkspell.Spell(self.edit_tv).set_language(locale.getlocale()[0])
			except:
				# No word list may not be found for the language
				pass
		#add view/preview update handler
		self.edit_tv.connect('focus-out-event', lambda x, y: self.update_wiki_browser())
		self.edit_scroller.add(self.edit_tv)

		#put it all together
		self.widget = gtk.HBox()
		self.wiki_fields = gtk.VBox(homogeneous=False, spacing=0)
		self.wiki_fields.pack_start(self.wiki_label, expand=False, fill=False, padding=2)
		self.wiki_fields.pack_start(self.wiki_scroller, expand=True, fill=True, padding=2)
		
		self.edit_fields = gtk.VBox(homogeneous=False, spacing=0)
		self.edit_fields.pack_start(self.edit_label, expand=False, fill=False, padding=2)
		self.edit_fields.pack_start(self.edit_scroller, expand=True, fill=True, padding=2)

		#TODO: make some pretty labels, then show them off; they're hideous
		self.widget.pack_start(self.wiki_fields, expand=True, fill=True, padding=2)
		self.widget.pack_start(self.edit_fields, expand=True, fill=True, padding=2)

		if attrs.get('readonly'):
			self.wiki_label.hide()
			self.edit_fields.hide()
		
		#show it all
		self.widget.show_all()

	def update_wiki_browser(self):
		id = False
		buffer = self.edit_tv.get_buffer()
		iter_start = buffer.get_start_iter()
		iter_end = buffer.get_end_iter()
		data = buffer.get_text(iter_start, iter_end, False)
		html_data = data
		
		if sys.platform == 'win32':
			#urlencode internal links
			import lxml
			from lxml import etree
			import base64
			from StringIO import StringIO
			try:
				html_parser = etree.HTMLParser()
				dom = etree.parse(StringIO(html_data), html_parser)
				for link in dom.findall(".//a"):
					href = link.get("href", '')
					if href.startswith('/') and '?' in href:
						#this is an internal tag w/ parameters
						#base64encode it (because ie's file:// can't handle parameters)
						link.set('href', base64.b64encode(href))
				html_data = etree.tostring(dom.getroot(), pretty_print=True, method='html')
			except lxml.etree.XMLSyntaxError as e:
				#poorly formated / empty; create a basic filler (so it doesn't trigger an file download)
				html_data = '<html><head></head><body></body></html>'
				pass
			self.wiki_browser.SetDocument(html_data)
			self._focus_out()
		else:
			self.wiki_browser.load_html_string(html_data, 'internal:///')
		
		

	def _webkit_navigation_requested(self, view, frame, networkRequest):
		# get uri from request object
		uri=networkRequest.get_uri()

		# load the page
		url = urlparse.urlparse(uri)
		return self.navigation_requested(url)

	def navigation_requested(self, url):
		if url.scheme == 'internal':
			url = urlparse.urlparse(url.path, scheme='http')
			#parse internal; if nothing, load internally
			query = urlparse.parse_qs(url.query)
			actions = [a for a in url.path.split('/') if a]
			if actions and actions[0] == 'openerp':
				#an internal action
				if actions[1] in ['form', 'tree'] and actions[2] in ['view', 'edit']:
					#form view request
					view_type = actions[1]
					id = int(query.get('id', [0])[0])
					#TODO: move name parsing server-side
					name = query.get('name', [False])[0]
					model = query.get('model', [''])[0]
					if name:
						#lookup id
						proxy = rpc.RPCProxy(model)
						ids = proxy.name_search(name, [], 'ilike', {})
						if len(ids):
							id = ids[0][0]
						else:
							try:
								id = int(name)
							except:
								id = 0
					if model:
						action = {
								'view_mode': 'form',
								'view_type': view_type,
								'res_model': model,
								'type': 'ir.actions.act_window',
								'nodestroy': True,
						}
						if id:
							action['res_id'] = [id]
						obj = service.LocalService('action.main')
						obj._exec_action(action, {}, {})
						#alternatively, we could use our own api:
						#obj = service.LocalService('api.main')
						#res = obj.action(action)
						return 1
				elif actions[1] == 'wiki' and actions[2] == 'getfile':
					# Add the filename from the field with the filename attribute in the view
					filename = query.get('file', 'file')[0]
					proxy = rpc.RPCProxy('ir.attachment')
					ids = proxy.search([('datas_fname','=',filename.strip()), ('res_model','=','wiki.wiki')])
					if len(ids) > 0:	#open/save image
						file_data = proxy.read(ids, ['datas', 'datas_fname', 'res_model', 'res_id'])[0]
						data = file_data['datas']
						#ask what they want to do with the file (convoluted, I know)
						msg = 'What would you like to do with this file?'
						ui = common.openerp_gtk_builder('openerp.ui', ['win_quest_3b'])
						win = ui.get_object('win_quest_3b')
						l = ui.get_object('label')
						l_height, l_width = l.size_request()
						l.set_label(msg)
						(expand, fill, padding, pack_type) = l.parent.query_child_packing(l)
						l.parent.set_child_packing(l, True, fill, padding, pack_type)
						l.set_property('width_request', -1)
						l.set_property('height_request', -1)
						o = ui.get_object('button82')	#open/yes
						o.set_label(gtk.STOCK_OPEN)
						o.set_use_stock(True)
						s = ui.get_object('button83')	#save_as/no
						s.set_label(gtk.STOCK_SAVE_AS)
						s.set_use_stock(True)

						parent=service.LocalService('gui.main').window
						win.set_transient_for(parent)
						win.set_icon(common.OPENERP_ICON)
						l_new_height, l_new_width = l.size_request()
						win_height, win_width = win.size_request()
						win.resize(win_height + l_new_height - l_height, win_width + l_new_width - l_width)

						response = win.run()
						win.destroy()
						if response == gtk.RESPONSE_NO:
							filename = common.file_selection(
								_('Save As...'),
								parent=self._window,
								action=gtk.FILE_CHOOSER_ACTION_SAVE,
								filename=filename
							)
							if filename:	#save file
								fp = file(filename,'wb+')
								fp.write(base64.decodestring(data))
								fp.close()
						elif response == gtk.RESPONSE_YES:
							ext = os.path.splitext(filename)[1][1:]
							(fileno, fp_name) = tempfile.mkstemp('.'+ext, 'openerp_')

							os.write(fileno, base64.decodestring(data))
							os.close(fileno)

							printer.printer.print_file(fp_name, ext, preview=True)
						
						return 1	#we're done; consume event

			return 0	#ignore these; let them load internally
		else:	#open in a web browser
			webbrowser.open(urlparse.urlunparse(url))
		return 1


	def _readonly_set(self, value):
		interface.widget_interface._readonly_set(self, value)
		self.edit_tv.set_editable(not value)
		if value:	#it's read only
			self.wiki_label.hide()
			self.edit_fields.hide()
		else:
			self.widget.show_all()

	def _color_widget(self):
		return self.edit_tv

	def grab_focus(self):
		return self.edit_tv.grab_focus()

	def set_value(self, model, model_field):
		buffer = self.edit_tv.get_buffer()
		iter_start = buffer.get_start_iter()
		iter_end = buffer.get_end_iter()
		current_text = buffer.get_text(iter_start,iter_end,False)
		model_field.set_client(model, current_text or False)

	def display(self, model, model_field):
		super(html, self).display(model, model_field)
		value = model_field and model_field.get(model)
		if not value:
			value=''
		buffer = self.edit_tv.get_buffer()
		buffer.delete(buffer.get_start_iter(), buffer.get_end_iter())
		iter_start = buffer.get_start_iter()
		id = False
		buffer.insert(iter_start, value)
		self.update_wiki_browser()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: