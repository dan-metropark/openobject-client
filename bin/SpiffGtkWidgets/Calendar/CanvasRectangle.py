# -*- coding: utf-8 -*-
##############################################################################
# Copyright (C) 2008-2011 Samuel Abels
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License
# version 3 as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

import hippo
import gobject
from SpiffGtkWidgets import color
import sys

class CanvasRectangle(hippo.CanvasBox):
    """
    A canvas item that draws a rectangle, optionally with rounded corners.
    """
    __gproperties__ = {
        'radius-top-left':     (gobject.TYPE_LONG,
                                'top left radius',
                                'radius of the top left corner',
                                0,
                                sys.maxint,
                                10,
                                gobject.PARAM_READWRITE),
        'radius-top-right':    (gobject.TYPE_LONG,
                                'top right radius',
                                'radius of the top right corner',
                                0,
                                sys.maxint,
                                10,
                                gobject.PARAM_READWRITE),
        'radius-bottom-left':  (gobject.TYPE_LONG,
                                'bottom left radius',
                                'radius of the bottom left corner',
                                0,
                                sys.maxint,
                                10,
                                gobject.PARAM_READWRITE),
        'radius-bottom-right': (gobject.TYPE_LONG,
                                'bottom right radius',
                                'radius of the bottom right corner',
                                0,
                                sys.maxint,
                                10,
                                gobject.PARAM_READWRITE),
    }

    def __init__(self, **kwargs):
        """
        Constructor.
        """
        self.property_names = ('radius-top-left',
                               'radius-top-right',
                               'radius-bottom-left',
                               'radius-bottom-right')
        self.radius_top_left     = 10
        self.radius_top_right    = 10
        self.radius_bottom_left  = 10
        self.radius_bottom_right = 10
        hippo.CanvasBox.__init__(self, **kwargs)


    def do_get_property(self, property):
        if property.name in self.property_names:
            return self.__getattribute__(property.name.replace('-', '_'))
        else:
            raise AttributeError, 'unknown property %s' % property.name


    def do_set_property(self, property, value):
        if property.name in self.property_names:
            return self.__setattr__(property.name.replace('-', '_'), value)
        else:
            raise AttributeError, 'unknown property %s' % property.name


    def do_paint_below_children(self, ctx, rect):
        (width, height) = self.get_allocation()

        ctx.set_source_rgba(*color.to_rgba(self.props.color))
        x,y,w,h = self.align(width, height)
        ctx.rectangle(x,y,w,h)
        ctx.clip()
        rtl  = self.props.radius_top_left
        rtr  = self.props.radius_top_right
        rbl  = self.props.radius_bottom_left
        rbr  = self.props.radius_bottom_right
#        #  A****BQ
#        # H      C
#        # *      *
#        # G      D
#        #  F****E
        ctx.move_to(x+rtl,y)                      # A
        ctx.line_to(x+w-rtr,y)                    # B
        ctx.curve_to(x+w,y,x+w,y,x+w,y+rtr)       # C, both control points at Q
        ctx.line_to(x+w,y+h-rbr)                  # D
        ctx.curve_to(x+w,y+h,x+w,y+h,x+w-rbr,y+h) # E
        ctx.line_to(x+rbl,y+h)                    # F
        ctx.curve_to(x,y+h,x,y+h,x,y+h-rbl)       # G
        ctx.line_to(x,y+rtl)                      # H
        ctx.curve_to(x,y,x,y,x+rtl,y)     
        ctx.close_path()       
        ctx.fill_preserve()

gobject.type_register(CanvasRectangle)
