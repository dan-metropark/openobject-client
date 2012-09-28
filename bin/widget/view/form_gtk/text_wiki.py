# -*- coding: utf-8 -*-

import gtk

import interface
import locale
import options

import re
import wikimarkup
import webkit
import os
import webbrowser
import urlparse

import rpc
import service
import cgi
import common
import base64
import tempfile
import printer

#from openerp.widgets import register_widget
#from openerp.widgets.form import Text

_image = re.compile(r'img:(.*)\.(.*)', re.UNICODE)
_rss = re.compile(r'rss:(.*)\.(.*)', re.UNICODE)
_attach = re.compile(r'attach:(.*)\.(.*)', re.UNICODE)
_internalLinks = re.compile(r'\[\[.*\]\]', re.UNICODE)
_edit = re.compile(r'edit:(.*)\|(.*)', re.UNICODE)
_view = re.compile(r'view:(.*)\|(.*)', re.UNICODE)

class WikiParser(wikimarkup.Parser):
	def parse(self, text, id):
		text = text.replace('&nbsp;', 'n-b-s-p')
		text = text.replace('&amp;', 'n-a-m-p')
		text = text.replace('&','&amp;')
		text = text.replace('n-b-s-p', '&nbsp;')
		text = text.replace('n-a-m-p', '&amp;')
		text = text.replace('<code>', '<pre>')
		text = text.replace('</code>', '</pre>')

		text = wikimarkup.to_unicode(text)
		text = self.strip(text)

		text = super(WikiParser, self).parse(text)
		text = self.addImage(text, id)
		text = self.attachDoc(text, id)
		text = self.recordLink(text)
		text = self.viewRecordLink(text)
		text = self.addInternalLinks(text)
		#TODO : already implemented but we will implement it later after releasing the 5.0
		#text = self.addRss(text, id)
		return text

	def viewRecordLink(self, text):
		def record(path):
			record = path.group().replace('view:','').split("|")
			model = record[0]
			text = record[1].replace('\r','').strip()
			label = "View Record"
			if len(record) > 2:
				label = record[2]
			
			proxy = rpc.RPCProxy(model)
			ids = proxy.name_search(text, [], 'ilike', {})
			if len(ids):
				id = ids[0][0]
			else:
				try:
					id = int(text)
				except:
					id = 0
			return "[[/openerp/form/view?model=%s&amp;id=%d | %s]]" % (model, id, label)

		bits = _view.sub(record, text)
		return bits

	def addRss(self, text, id):
		def addrss(path):
			rssurl = path.group().replace('rss:','')
			import rss.feedparser as feedparser
			data = feedparser.parse(rssurl)
			values = "<h2>%s</h2><br/>" % (data.feed.title)
			values += "%s<br/>" % (data.channel.description)
			for entry in data['entries']:
				values += "<h3><a href='%s'> %s </a></h3><br/>" % (entry.link, entry.title)
				values += "%s <br/>" % (entry.summary)

			return values

		bits = _rss.sub(addrss, text)
		return bits

	def attachDoc(self, text, id):
		#NOTE: id seems to be empty
		#TODO: determine open/save, or trigger a dialog to ask whether to open/save
		#refer: binary.py (widget/view/form_gtk)
		def document(path):
			file = path.group().replace('attach:','')
			if file.startswith('http') or file.startswith('ftp'):
				return "<a href='%s'>Download File</a>" % (file)
			else:
				proxy = rpc.RPCProxy('ir.attachment')
				ids = proxy.search([('datas_fname','=',file.strip()), ('res_model','=','wiki.wiki')])
				if len(ids) > 0:
					return "<a href='/openerp/wiki/getfile?file=%s&amp;id=%d'>%s</a>" % (file, id, file)
				else:	#ignore it; we don't know where it came from or whether whoever it is has privileges
					#we could expand this later
					return 'File not available: %s' % cgi.escape(file)
		bits = _attach.sub(document, text)
		return bits

	def addImage(self, text, id):
		#NOTE: id seems to be empty
		def image(path):
			file = path.group().replace('img:','')
			if file.startswith('http') or file.startswith('ftp'):
				return "<img src='%s'/>" % (file)
			else:
				#check if image is attached to wiki page
				proxy = rpc.RPCProxy('ir.attachment')
				ids = proxy.search([('datas_fname','=',file.strip()), ('res_model','=','wiki.wiki')])
				if len(ids) > 0:	#add image
					img_data = proxy.read(ids, ['datas', 'datas_fname', 'res_model', 'res_id'])[0]
					img_type = os.path.splitext(img_data['datas_fname'])[1].strip('.')
					return "<img src='data:image/%s;base64,%s'/>" % (img_type, img_data['datas'])
				else:	#ignore it; we don't know where it came from or whether whoever it is has privileges
					#we could expand this later
					return 'Image not available: %s' % cgi.escape(file)
		bits = _image.sub(image, text)
		return bits

	def recordLink(self, text):
		def record(path):
			record = path.group().replace('edit:','').split("|")
			model = record[0]
			text = record[1].replace('\r','').strip()
			label = "Edit Record"
			if len(record) > 2:
				label = record[2]
			proxy = rpc.RPCProxy(model)
			ids = proxy.name_search(text, [], '=', {})
			if len(ids):
				id = ids[0][0]
			else:
				try:
					id = int(text)
				except:
					id = 0
			return "[[/openerp/form/edit?model=%s&amp;id=%d | %s]]" % (model, id, label)

		bits = _edit.sub(record, text)
		return bits

	def addInternalLinks(self, text):
		proxy = rpc.RPCProxy('wiki.wiki')

		def link(path):
			link = path.group().replace('[','').replace('[','').replace(']','').replace(']','').split("|")
			name_to_search = link[0].strip()
			mids = proxy.search([('name','ilike', name_to_search)])
			link_str = ""
			if mids:
				if len(link) == 2:
					link_str = "<a href='/openerp/form/view?model=wiki.wiki&amp;id=%s'>%s</a>" % (mids[0], link[1])
				elif len(link) == 1:
					link_str = "<a href='/openerp/form/view?model=wiki.wiki&amp;id=%s'>%s</a>" % (mids[0], link[0])
			else:
				if len(link) == 2:
					link_str = "<a href='%s'>%s</a>" % (link[0], link[1])
				elif len(link) == 1:
					link_str = "<a href='/openerp/form/edit?model=wiki.wiki&amp;id=False'>%s</a>" % (link[0])

			return link_str

		bits = _internalLinks.sub(link, text)
		return bits

def wiki2html(text, showToc, id):
	p = WikiParser(show_toc=showToc)
	return p.parse(text, id)


class text_wiki(interface.widget_interface):
	def __init__(self, window, parent, model, attrs={}, label=None):
		interface.widget_interface.__init__(self, window, parent, model, attrs, label_ebox=label)

		#setup notebook
		self.widget = gtk.HBox(spacing=3)
		self.notebook = gtk.Notebook()
		
		#setup web view
		self.wiki_label = gtk.Label('View/Preview')
		self.wiki_scroller = gtk.ScrolledWindow()
		self.wiki_scroller.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
		self.wiki_scroller.set_shadow_type(gtk.SHADOW_NONE)
		self.wiki_scroller.set_size_request(-1, 80)
		self.wiki_browser = webkit.WebView()
		self.wiki_browser.connect('navigation-requested', lambda x,y,z: self._navigation_requested(x, y, z))
		#put web notebook page together
		self.wiki_scroller.add(self.wiki_browser)
		self.notebook.append_page(self.wiki_scroller, self.wiki_label)
		
		#setup edit view
		self.edit_label = gtk.Label('Edit')
		self.edit_scroller = gtk.ScrolledWindow()
		self.edit_scroller.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
		self.edit_scroller.set_shadow_type(gtk.SHADOW_NONE)
		self.edit_scroller.set_size_request(-1, 80)

		self.edit_tv = gtk.TextView()
		self.edit_tv.set_wrap_mode(gtk.WRAP_WORD)
		#add menu & focus handlers
		self.edit_tv.connect('populate-popup', self._menu_open)
		self.edit_tv.set_accepts_tab(False)
		self.edit_tv.connect('focus-out-event', lambda x,y: self._focus_out())
		#detect & add spellcheck
		if not attrs.get('readonly'):
			if options.options['client.form_text_spellcheck']:
				try:
					import gtkspell
					gtkspell.Spell(self.edit_tv).set_language(locale.getlocale()[0])
				except:
					# No word list may not be found for the language
					pass
		#add view/preview update handler
		b = self.wiki_browser
		
		self.edit_tv.connect('focus-out-event', lambda x, y: self.update_wiki_browser())
		
		#put edit notebook page together
		self.edit_scroller.add(self.edit_tv)
		self.notebook.append_page(self.edit_scroller, self.edit_label)

		self.widget.pack_start(self.notebook)
		#show it all
		self.widget.show_all()

	def update_wiki_browser(self):
		id = False
		buffer = self.edit_tv.get_buffer()
		iter_start = buffer.get_start_iter()
		iter_end = buffer.get_end_iter()
		data = buffer.get_text(iter_start, iter_end, False)
		html = wiki2html(data, True, id)
		#TODO: put the css on the server, and use it from there
		dir_path = os.path.dirname(__file__)
		css_path = os.path.join(dir_path, 'css/wiki.css')
		with open(css_path) as f:
			css_data = f.read()
		html = '''<html><head><style type='text/css'>%s</style></head><body>%s</body></html>''' % (css_data, html)
		self.wiki_browser.load_html_string(html, 'internal:///')

	def _navigation_requested(self, view, frame, networkRequest):
		# get uri from request object
		uri=networkRequest.get_uri()
		
		# load the page
		url = urlparse.urlparse(uri)
		if url.scheme == 'internal':
			url = urlparse.urlparse(url.path, scheme='http')
			#parse internal; if nothing, load internally
			query = urlparse.parse_qs(url.query)
			actions = [a for a in url.path.split('/') if a]
			if actions and actions[0] == 'openerp':
				#an internal action
				if actions[1] == 'form' and actions[2] in ['view', 'edit']:
					#form view request
					id = int(query.get('id', [0])[0])
					model = query.get('model', [''])[0]
					if model:
						action = {
								'view_mode': 'form',
								'view_type': 'form',
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
			webbrowser.open(uri)
		return 1


	def _readonly_set(self, value):
		interface.widget_interface._readonly_set(self, value)
		self.edit_tv.set_editable(not value)

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
		super(text_wiki, self).display(model, model_field)
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