# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import common
import gtk
import interface
import form_gtk
import tree_gtk
import graph_gtk
import calendar_gtk
import diagram_gtk

from form import ViewForm
from list import ViewList
from graph import ViewGraph
from calendar import ViewCalendar
from diagram import ViewDiagram

import sys
import form_gtk.html as html

parsers = {
    'form' : (form_gtk.parser_form, ViewForm),
    'tree' : (tree_gtk.parser_tree, ViewList),
    'graph': (graph_gtk.parser_graph, ViewGraph),
    'calendar' : (calendar_gtk.parser_calendar, ViewCalendar),
    'diagram' : (diagram_gtk.parser_diagram, ViewDiagram),
}

class widget_parse(interface.parser_interface):
	def on_widget_click(self, widget, event, window):
		if not len(html.registered_widgets):
			return False	#continue; we don't need to go through all of this
		
		w = widget.get_parent_window()
		# used on win32 platform because by default a gtk application does not grab control from native win32 control
		if not widget.has_focus():
			#get current state
			#state = w.get_state()	#this should tell us what we want, but it doesn't
			try:
				#we must rely on a state event monitor,
				# which may not even be the same window as the parent window
				state = window.fsm.window_state
				max_mask = gtk.gdk.WINDOW_STATE_MAXIMIZED
				full_mask = gtk.gdk.WINDOW_STATE_FULLSCREEN
				fullscreen = full_mask & state == full_mask
				maximized = max_mask & state == max_mask
			except Exception as e:
				fullscreen = False
				maximized = False

			#focus on window while retaining window state
			w.focus()
			#TODO: figure out a better way to resolve this
			if fullscreen:
				w.fullscreen()
			elif maximized:
				w.maximize()
			#focus on widget
			widget.grab_focus()
        
	def parse(self, screen, node, fields, toolbar={}, submenu={}, name=False, help={}):
		if node is not None:
			if node.tag not in parsers:
				raise Exception(_("This type (%s) is not supported by the GTK client !") % node.tag)
			widget_parser, view_parser = parsers[node.tag]
			# Select the parser for the view (form, tree, graph, calendar)
			widget = widget_parser(self.window, self.parent, self.attrs, screen)
			def make_clickable(widget):
				try:
					widget.set_property("can-focus", True)
					widget.add_events(gtk.gdk.BUTTON_PRESS_MASK)
					widget.connect("button_press_event", self.on_widget_click, self.window)
					children = widget.get_children()
				except Exception as e:
					children = []
				for child in children:
					make_clickable(child)
			
			wid, child, buttons, on_write = widget.parse(screen.resource, node, fields)
			if sys.platform == 'win32':
				#only go through this rigamarole on windows machines; it's not needed elsewhere
				for name, w in child.iteritems():
					try:
						make_clickable(w.widget)
					except AttributeError as e:
						#the 'hours' field in tasks returns a tuple; not an object containing a widget...
						#TODO: do something about that (if it poses a problem)
						pass
			duplicated_fields = []
			[duplicated_fields.append(field) for field, count in widget.field_list.iteritems() if count>1]
			if duplicated_fields:
				field_str =  ', '.join(duplicated_fields)
				view = node.tag.capitalize()
				view_str = "\n View:"
				if not name:
					name = ''
					view_str = ''
				msg = " <b>%s</b> view has duplicate field: <b>%s</b>\n Model: <b>%s</b> %s <b>%s</b>\n The duplicated fields will be simply ignored !"
				var = (view, field_str, screen.resource, view_str, name)
				common.message( _(msg) % var,
				_('View Error!'), type=gtk.MESSAGE_ERROR, parent=None, msg_to_xml=False)
			if isinstance(wid, calendar_gtk.EmptyCalendar):
				view_parser = calendar_gtk.DummyViewCalendar
			screen.set_on_write(on_write)
			res = view_parser(self.window, screen, wid, child, buttons, toolbar, submenu, help=help)
			res.title = widget.title
			return res
		raise Exception(_("No valid view found for this object!"))

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

