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

from widget.view import interface
from tools import ustr, node_attributes
import gtk
import gettext
import common
from common import openerp_gtk_builder, gtk_signal_decorator
import gobject
from datetime import datetime, date

from SpiffGtkWidgets import Calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta
import time
import math

import rpc
from rpc import RPCProxy
import logging
import widget.model.field as wmodel_fields
import tools

DT_SERVER_FORMATS = {
          'datetime': '%Y-%m-%d %H:%M:%S',
          'date': '%Y-%m-%d',
          'time': '%H:%M:%S'
        }

COLOR_PALETTE = ['#f57900', '#cc0000', '#d400a8', '#75507b', '#3465a4', '#73d216', '#c17d11', '#edd400',
                 '#fcaf3e', '#ef2929', '#ff00c9', '#ad7fa8', '#729fcf', '#8ae234', '#e9b96e', '#fce94f',
                 '#ff8e00', '#ff0000', '#b0008c', '#9000ff', '#0078ff', '#00ff00', '#e6ff00', '#ffff00',
                 '#905000', '#9b0000', '#840067', '#510090', '#0000c9', '#009b00', '#9abe00', '#ffc900',]

_colorline = ['#%02x%02x%02x' % (25+((r+10)%11)*23,5+((g+1)%11)*20,25+((b+4)%11)*23) for r in range(11) for g in range(11) for b in range(11) ]
def choice_colors(n):
    if n > len(COLOR_PALETTE):
        return _colorline[0:-1:len(_colorline)/(n+1)]
    elif n:
        return COLOR_PALETTE[:n]
    return []

class TinyEvent(Calendar.Event):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

        super(TinyEvent, self).__init__(**kwargs)

    def __repr__(self):
        r = []
        for x in self.__dict__:
            r.append("%s: %r" % (x, self.__dict__[x]))
        return '<TinyEvent::\n\t' + "\n\t".join(r) + '\n>'

class TinyCalModel(Calendar.Model):
    def add_events(self, events):
        for event in events:
            assert event    is not None
            assert event.id is None
            self.events[self.next_event_id] = event
            event.id = self.next_event_id
            self.next_event_id += 1
        # Force view update
        self.emit('event-added', None)

    def remove_events(self):
        self.events = {}
        # Force view update
        self.emit('event-removed', None)


class ViewCalendar(object):
    TV_COL_ID = 0
    TV_COL_COLOR = 1
    TV_COL_LABEL = 2
    TV_COL_TOGGLE = 3

    def __init__(self, model, axis, fields, attrs):
        self.ui = openerp_gtk_builder('openerp.ui', ['widget_view_calendar'])
        self.widget = self.ui.get_object('widget_view_calendar')

        self._label_current = self.ui.get_object('label_current')
        self._radio_month = self.ui.get_object('radio_month')
        self._radio_week = self.ui.get_object('radio_week')
        self._radio_day = self.ui.get_object('radio_day')
        self._small_calendar = self.ui.get_object('calendar_small')
        self._calendar_treeview = self.ui.get_object('calendar_treeview')

        mode = attrs.get('mode','month')
        self.log = logging.getLogger('calender')
        self.fields = fields
        self.attrs = attrs
        self.axis = axis
        self.screen = None
        if mode == 'day':
            self._radio_day.set_active(True)
        elif mode == 'week':
            self._radio_week.set_active(True)
        else:
            self._radio_month.set_active(True)
        self.mode = mode
        self.modex = mode

        self.cal_model = TinyCalModel()
        self.cal_view = Calendar.Calendar(self.cal_model, mode)
        self.cal_view.connect('event-clicked', self._on_event_clicked)
        self.cal_view.connect('do_month_back_forward', self._back_forward)
        self.cal_view.connect('day-selected', self._change_small)

        vbox = self.ui.get_object('cal_vbox')
        vbox.pack_start(self.cal_view)
        vbox.show_all()

        self.process = False
        self.ui.connect_signals({
            'on_but_forward_clicked': gtk_signal_decorator(self._back_forward, 1),
            'on_but_back_clicked': gtk_signal_decorator(self._back_forward, -1),
            'on_but_today_clicked': self._today,
            'on_calendar_small_day_selected_double_click': gtk_signal_decorator(self._change_small, False, False),
            'on_button_day_clicked': gtk_signal_decorator(self._change_view, 'day'),
            'on_button_week_clicked': gtk_signal_decorator(self._change_view, 'week'),
            'on_button_month_clicked': gtk_signal_decorator(self._change_view, 'month'),
        })
        self.date = datetime.today()
        self.string = attrs.get('string', '')
        self.date_start = attrs.get('date_start')
        self.date_delay = attrs.get('date_delay')
        self.date_stop = attrs.get('date_stop')
        self.color_field = attrs.get('color')
        self.color_field_custom = attrs.get('color_custom', 'color')
        self.color_model = False
        self.color_filters = {}
        self.colors = {}

        self.day_length = int(attrs.get('day_length', 8))
        self.models = None
        self.models_record_group = None

        if self.color_field:
            self.color_model = gtk.ListStore(str, str, str, gobject.TYPE_BOOLEAN)
            self._calendar_treeview.set_model(self.color_model)
            self._calendar_treeview.get_selection().set_mode(gtk.SELECTION_NONE)

            for c in (self.TV_COL_ID, self.TV_COL_COLOR):
                column = gtk.TreeViewColumn(None, gtk.CellRendererText(), text=c)
                self._calendar_treeview.append_column(column)
                column.set_visible(False)

            # Row toogle
            renderer = gtk.CellRendererToggle()
            renderer.set_property('activatable', True)
            renderer.connect('toggled', self._treeview_toggled, self.color_model, self.color_filters)
            column = gtk.TreeViewColumn(None, renderer)
            column.add_attribute(renderer, "active", self.TV_COL_TOGGLE)
            column.set_cell_data_func(renderer, self._treeview_setter)
            self._calendar_treeview.append_column(column)

            renderer = gtk.CellRendererText()
            column = gtk.TreeViewColumn(None, renderer, text=self.TV_COL_LABEL)
            col_label = gtk.Label('')
            col_label.set_markup('<b>%s</b>' % self.fields[self.color_field]['string'])
            col_label.show()
            column.set_widget(col_label)
            column.set_cell_data_func(renderer, self._treeview_setter)
            self._calendar_treeview.append_column(column)

    def _treeview_toggled(self, renderer, path, model, color_filters):
        it = model.get_iter(path)
        curval = model.get(it, self.TV_COL_TOGGLE)[0]
        newval = not curval
        model.set(it, self.TV_COL_TOGGLE, newval)

        value = model.get(it, self.TV_COL_ID)
        if isinstance(value, (tuple,list)):
            value = value[0]

        # update filters
        if not newval:
            # remove from filter
            try:
                color_filters.pop(value)
            except KeyError:
                # item anymore in dictionary
                pass
        else:
            # add to filter
            color_filters[value] = True

        self.display(None, force=True)

    def _treeview_setter(self, column, cell, store, iter):
        color = store.get_value(iter, self.TV_COL_COLOR)
        if isinstance(cell, gtk.CellRendererText):
            cell.set_property('background', str(color))
        elif isinstance(cell, gtk.CellRendererToggle):
            cell.set_property('cell-background', str(color))

    def add_to_treeview(self, name, value, color):
        value = str(value)
        model = self._calendar_treeview.get_model()
        for row in model:
            if row[self.TV_COL_ID] == value:
                return  # id already in the treeview
        iter = model.append()
        model.set(iter, self.TV_COL_ID, value,
                        self.TV_COL_COLOR, color,
                        self.TV_COL_LABEL, name,
                        self.TV_COL_TOGGLE, False)

    def _change_small(self, widget, date_selected, hippo_event, *args, **argv):
        if isinstance(widget, gtk.Calendar):
            t = list(widget.get_date())
            t[1] += 1
        else:
            t = list(date_selected.timetuple()[:3])
        self.date = datetime(*t[0:6])
        self.display(None)

        # if action = double click
        if hippo_event and hippo_event.button == 1:
            if hippo_event.count == 1: # simple clic
                # simply display new current day
                return
            elif hippo_event.count >= 2: # double clic or more
                self.screen.context.update({'default_' +self.date_start:self.date.strftime('%Y-%m-%d %H:%M:%S')})
                self.screen.switch_view(mode='form')
                self.screen.new()

    def _today(self, widget, *args, **argv):
        self.date = datetime.today()
        self.display(None)

    def _back_forward(self, widget, type, *args, **argv):
        if self.mode == 'day':
            self.date = self.date + relativedelta(days=type)
        if self.mode == 'week':
            self.date = self.date + relativedelta(weeks=type)
        if self.mode == 'month':
            self.date = self.date + relativedelta(months=type)
        self.screen.search_filter()
        self.display(None)

    def _change_view(self, widget, type, *args, **argv):
        if self.process or self.mode == type:
            return True
        self.process = True
        self.mode = type
        self.display(None, force=True)
        self.process = False
        return True

    def _on_event_clicked(self, calendar, calendar_event, hippo_event):
        if hippo_event.button == 1 and hippo_event.count >= 2:
            # user have double clicked
            self.screen.current_model = calendar_event.model
            self.screen.switch_view(mode='form')

    def __update_colors(self):
        if self.color_field:
            self.colors = self._get_colors(self.models, self.color_field, self.color_field_custom)

    def _get_colors(self, models, color_field, color_field_custom):
        auto_color_count = 0 # how many color do we need to generate auto.
        colors = {}

        for model in models:
            name = value = key = model.value[color_field]
            if isinstance(key, (tuple, list)):
                value, name = key
                key = tuple(key)

            if key in colors:
                # already present skip
                continue

            # if field is many2one, try to get color from object
            # 'color' field
            field_color = None
            field_widget = model.mgroup.mfields.get(color_field, False)
            if value and field_widget and field_widget.attrs['type'] == 'many2one':
                fproxy = RPCProxy(field_widget.attrs['relation'])
                try:
                    fdata = fproxy.read(value, [color_field_custom])
                    if fdata:
                        field_color = fdata.get(color_field_custom) and str(fdata.get(color_field_custom)) or None
                except Exception, e:
                    #TODO: Need to limit exception
                    self.log.exception(e)
                    pass

            if not field_color:
                # increment total color to generate
                auto_color_count += 1

            colors[key] = (name, value, field_color)

        auto_colors = choice_colors(auto_color_count)
        colors_idx = 0
        for key, value in colors.items():
            color_value = value[2]
            if not color_value:
                color_value = auto_colors[colors_idx]
                colors_idx += 1
            colors[key] = (value[0], value[1], color_value)
        # return new colors
        return colors

    def display(self, models, force=False):
        if models:
            self.models = models.models
            self.models_record_group = models
            self.cal_model.remove_events()
            if self.models:
                self.__update_colors()
                self.cal_model.add_events(self.__get_events())
                self.modex = self.mode
                self.mode = self.mode == 'month' and 'week' or 'month'
                self.refresh()
                self.mode = self.modex
        elif force == True:
            self.cal_model.remove_events()
            self.cal_model.add_events(self.__get_events())
        self.refresh()

    def refresh(self):
        t = self.date.timetuple()
        from tools import ustr
        from locale import getlocale
        sysencoding = getlocale()[1]

        if self.mode == 'month':
            self._radio_month.set_active(True)
            self.cal_view.range = self.cal_view.RANGE_MONTH
            self._label_current.set_text(ustr(self.date.strftime('%B %Y'), sysencoding))
        elif self.mode == 'week':
            self._radio_week.set_active(True)
            self.cal_view.range = self.cal_view.RANGE_WEEK
            self._label_current.set_text(_('Week') + ' ' + self.date.strftime('%W, %Y'))
        elif self.mode == 'day':
            self._radio_day.set_active(True)
            self.cal_view.range = self.cal_view.RANGE_CUSTOM
            d1 = datetime(*t[:3])
            d2 = Calendar.util.end_of_day(d1)
            self.cal_view.active_range = self.cal_view.visible_range = d1, d2
            self._label_current.set_text(ustr(self.date.strftime('%A %x'), sysencoding))

        self.cal_view.selected = date(*list(t)[:3])
        self._small_calendar.select_month(t[1]-1,t[0])
        self._small_calendar.select_day(t[2])

        self.cal_view.refresh()


    def __get_events(self):
        do_color_filtering = len(self.color_filters.keys()) and True or False
        color_filters = self.color_filters

        events = []
        for model in self.models:
            filter_state = 'keep'
            if do_color_filtering:
                model_value = model.value.get(self.color_field, False)
                if isinstance(model_value, (tuple,list)):
                    model_value = str(model_value[0])
                if model_value and model_value not in color_filters:
                    filter_state = 'skip'

            if filter_state == 'skip':
                # We need to skip this item
                continue


            e = self.__get_event(model)
            if e:
                if e.color_info:
                    self.add_to_treeview(*e.color_info)
                events.append(e)
        return events

    def __convert(self, event, date_start_fmt, date_stop_fmt):

        fields = [x for x in [(self.date_start, date_start_fmt), (self.date_stop, date_stop_fmt)] if x[0]]
        for fld, fmt in fields:
            typ = self.fields[fld]['type']
            if event[fld] and fmt:
                event[fld] = time.strptime(event[fld][:19], fmt)

            # default start/stop time is 9:00 AM / 5:00 PM
            # if you set it to 0:00, then Calendar.Event removes 1 second to date_stop,
            # which sets it back to the day before at 23:59:59
            if typ == 'date' and event[fld]:
                ds = list(event[fld])
                if fld == self.date_start:
                    ds[3] = 9
                elif fld == self.date_stop:
                    ds[3] = 17
                event[fld] = tuple(ds)

    def __get_event(self, model):

        event = model.value.copy()
        # Converts the dates according to the timezone in calendar view
        date_start_fmt = self.date_start and DT_SERVER_FORMATS[self.fields[self.date_start]['type']] or False
        date_stop_fmt = self.date_stop and DT_SERVER_FORMATS[self.fields[self.date_stop]['type']] or False
        if date_start_fmt:
            event[self.date_start] = tools.datetime_util.server_to_local_timestamp(event.get(self.date_start), date_start_fmt, date_start_fmt, tz_offset=True, ignore_unparsable_time=False)
        if date_stop_fmt:
            event[self.date_stop] = tools.datetime_util.server_to_local_timestamp(event.get(self.date_stop), date_stop_fmt, date_stop_fmt, tz_offset=True, ignore_unparsable_time=False)
        self.__convert(event, date_start_fmt=date_start_fmt, date_stop_fmt=date_stop_fmt)

        caption = ''
        description = []
        starts = None
        ends = None

        if self.axis:

            f = self.axis[0]
            s = event[f]

            if isinstance(s, (tuple, list)): s = s[-1]

            caption = ustr(s)

            for f in self.axis[1:]:
                s = event[f]
                if isinstance(s, (tuple, list)): s = s[-1]

                description += [ustr(s)]

        starts = event.get(self.date_start)
        ends = event.get(self.date_delay) or 1.0
        span = 0

        if starts and ends:

            n = 0
            h = ends or 1

            if ends == self.day_length: span = 1

            if ends > self.day_length:
                n = ends / self.day_length
                h = ends % self.day_length

                n = int(math.floor(n))

                if n > 0:
                    if not h:
                        n = n - 1
                    span = n + 1

            ends= time.localtime(time.mktime(starts)+(h * 60 * 60) + (n * 24 * 60 * 60))

        if starts and self.date_stop:

            ends = event.get(self.date_stop)
            if not ends:
                ends = time.localtime(time.mktime(starts) + 60 * 60)

            tds = time.mktime(starts)
            tde = time.mktime(ends)

            if tds >= tde:
                tde = tds + 60 * 60
                ends = time.localtime(tde)

            n = (tde - tds) / (60 * 60)

            if n > self.day_length:
                span = math.floor(n / 24.)

        if not starts:
            return None

        color_key = event.get(self.color_field)
        if isinstance(color_key, list):
            color_key = tuple(color_key)
        color_info = self.colors.get(color_key)
        color = color_info and color_info[2] or 'black'
        description = ', '.join(description).strip()
        all_day = self.mode == 'month' and True or span > 0
        return TinyEvent(model=model,
                         caption=caption.strip(),
                         start=datetime(*starts[:7]),
                         end=datetime(*ends[:7]),
                         description=description,
                         dayspan=span,
                         all_day=all_day,
                         color_info=color_info,
                         bg_color = (all_day or self.mode != 'month') and color or 'white',
                         text_color = (all_day or self.mode != 'month') and 'black' or color,
        )



class parser_calendar(interface.parser_interface):
    def parse(self, model, root_node, fields):
        attrs = node_attributes(root_node)
        self.title = attrs.get('string', 'Calendar')

        axis = []
        axis_data = {}
        for node in root_node:
            node_attrs = node_attributes(node)
            if node.tag == 'field':
                axis.append(str(node_attrs['name']))
                axis_data[str(node_attrs['name'])] = node_attrs

        view = ViewCalendar(model, axis, fields, attrs)

        return view, {}, [], ''

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

