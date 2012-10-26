import gtk
import gobject
from gtk import gdk
import pygtk

from OleInPlaceImpl import *  
#import generated.shdocvw as shdocvw           #generated by makepy.py
from   generated.shdocvw import *
import generated.mshtml  as mshtml            #generated by makepy.py

import win32com.client.connect  
import win32com.server.util as util
import DataIStream

from IEHtmlViewCallback import IEHtmlViewCallback



### IE hosting documentation via COM 
### http://msdn.microsoft.com/en-us/library/aa752038(VS.85).aspx - IWebBrowser
### http://msdn.microsoft.com/en-us/library/bb498651(VS.85).aspx - MSHTML

class IEHtmlElement(object):
    def __init__(self, com_html_element):
        self.com_element = com_html_element
        
    def getName(self):
        return self.com_element.tagName
    
    def getAttr(self, name):
        return self.com_element.getAttribute(name)
    
    def scrollViewTo(self, top_of_view = True):
        self.com_element.scrollIntoView(top_of_view)
            
            
class IEHtmlDocument(object):
    def __init__(self, iedocument):
        self.ieDocument = iedocument
    
    def getElementById(self,id):
        el = self.ieDocument.getElementById(id)
        if el is None:
            return None
        return IEHtmlElement(el)
        
             
      
            
class BrowserCB(DWebBrowserEvents2): 
    def __init__(self, oobj):
        DWebBrowserEvents2.__init__(self, oobj)
        self.browser = oobj
        self.htmlViewCallback = None

    def setHtmlViewCallback(self, callback):
        self.htmlViewCallback = callback        
        
    def OnBeforeNavigate2(self, pDisp, URL, Flags, TargetFrameName, PostData, Headers, Cancel):
        if self.htmlViewCallback is not None:
            if self.htmlViewCallback.OnBeforeNavigate(URL) == True:
                return None, None, None, None, None, True #do not navigate there
        return None, None, None, None, None, False 
     
        
    def OnNewWindow3(self, ppDisp=defaultNamedNotOptArg, Cancel=defaultNamedNotOptArg, dwFlags=defaultNamedNotOptArg, bstrUrlContext=defaultNamedNotOptArg
           , bstrUrl=defaultNamedNotOptArg):
        
        if self.htmlViewCallback is not None:
            if self.htmlViewCallback.OnNewWindow(bstrUrl) == True:
                return None, True                
        return None, True
    
    def OnCommandStateChange(self, Command=defaultNamedNotOptArg, Enable=defaultNamedNotOptArg):
        """ Usefull for finding out whether GoBack or GoForward is possible"""
        #print "OnCommandStateChange ", Command, Enable
        pass

        
class DocumentCB(mshtml.HTMLDocumentEvents2): 
    def __init__(self, oobj):
        mshtml.HTMLDocumentEvents2.__init__(self, oobj)
        self.Document = oobj
        self.htmlViewCallback = None

    def generic_callback(self, cb_name, pEvtObj=defaultNamedNotOptArg):
        if self.htmlViewCallback is None or not hasattr(self.htmlViewCallback, cb_name):
            return True #continue like normal

        html_element = None
        if self.Document.parentWindow.event.srcElement is not None:
            html_element = IEHtmlElement(self.Document.parentWindow.event.srcElement)
        return getattr(self.htmlViewCallback, cb_name)(pEvtObj, html_element)
        
    def setHtmlViewCallback(self, callback):
        self.htmlViewCallback = callback
                        
    def Ononmouseup(self, pEvtObj=defaultNamedNotOptArg):
        pass

    def Ononbeforeupdate(self, pEvtObj=defaultNamedNotOptArg):
        pass
        
    def Ononclick(self, pEvtObj=defaultNamedNotOptArg):
        return self.generic_callback('Ononclick', pEvtObj)

    def Ononcontextmenu(self, pEvtObj=defaultNamedNotOptArg):
        if self.htmlViewCallback is None:
            return True #display the default context menu
        html_element = None
        if self.Document.parentWindow.event.srcElement is not None:
            html_element = IEHtmlElement(self.Document.parentWindow.event.srcElement)
        return self.htmlViewCallback.OnContextMenu(html_element)
    
    def Ononfocusout(self, pEvtObj=defaultNamedNotOptArg):
        return self.generic_callback('Ononfocusout', pEvtObj)
    
    def Ononrowenter(self, pEvtObj=defaultNamedNotOptArg):
        pass

    def Ononfocusin(self, pEvtObj=defaultNamedNotOptArg):
        return self.generic_callback('Ononfocusin', pEvtObj)
    
    def Ononkeypress(self, pEvtObj=defaultNamedNotOptArg):
        pass

    def Ononkeyup(self, pEvtObj=defaultNamedNotOptArg):
        pass

    def Ononkeydown(self, pEvtObj=defaultNamedNotOptArg):
        pass
        
class IEHtmlBaseView(gtk.DrawingArea):
    def __init__(self):
        gobject.type_register(IEHtmlBaseView)
        gtk.Widget.__init__(self)
        self.ole_frame = None
        self.hwnd = None
        self.callback = None
        self.browser2 = None
        self.content = None
        self.docEventSink = None
        self.eventSink = None
        self.set_property("can-focus", True)
        self.connect("focus", self.on_focus)
        
        self.connect("focus_in_event", self.fcs_i)
        self.connect("focus_out_event", self.fcs_o)
        self.connect("expose-event", self.fcs)

    def show(self):
        self.window.show()

    def fcs(self, widget, direction, user_param1 = None, user_param2 = None):
        return False
    
    def fcs_i(self, widget, direction, user_param1 = None, user_param2 = None):
        return False
                
    def fcs_o(self, widget, direction, user_param1 = None, user_param2 = None):
        return False

    def on_focus(self, widget, direction, user_param1 = None, user_param2 = None):
        self.window.focus()
        return False   

        
                    
    def do_realize(self):
        """Called when the widget should create all of its
        windowing resources.  We will create our gtk.gdk.Window.
        """
        self.set_flags(self.flags() | gtk.REALIZED)
        self.window = gdk.Window(
                self.get_parent_window(),
                width=self.allocation.width,
                height=self.allocation.height,
                window_type=gdk.WINDOW_CHILD,
                wclass=gdk.INPUT_OUTPUT,
                event_mask=self.get_events() | gdk.EXPOSURE_MASK
                                             | gdk.LEAVE_NOTIFY_MASK
                                             | gdk.BUTTON1_MOTION_MASK 
                                             | gdk.BUTTON_PRESS_MASK
                                             | gtk.gdk.FOCUS_CHANGE_MASK
                                             | gtk.gdk.POINTER_MOTION_MASK
                                             | gtk.gdk.POINTER_MOTION_HINT_MASK)
        
        # Associate the gdk.Window with ourselves, Gtk+ needs a reference
        # between the widget and the gdk window
        self.window.set_user_data(self)
        self.hwnd = self.window.handle

        # Attach the style to the gdk.Window, a style contains colors and
        # GC contextes used for drawing
        self.style.attach(self.window)
        self.style.set_background(self.window, gtk.STATE_NORMAL)
        self.window.move_resize(*self.allocation)
        
        browser = pythoncom.CoCreateInstance("{8856F961-340A-11D0-A96B-00C04FD705A2}",
                                             None,
                                             pythoncom.CLSCTX_INPROC_SERVER | pythoncom.CLSCTX_INPROC_HANDLER,
                                             axcontrol.IID_IOleObject)
        self.browser = browser
        site = wrap(SimpleSite(self), axcontrol.IID_IOleClientSite)#, useDispatcher=debugging)

        browser.SetClientSite(site)
        axcontrol.OleSetContainedObject(self.browser, True)
        rect = win32gui.GetWindowRect(self.hwnd)
        browser.DoVerb(axcontrol.OLEIVERB_SHOW, None, site, - 1, self.hwnd, rect)
        b2 = Dispatch(browser.QueryInterface(pythoncom.IID_IDispatch))
        self.browser2 = b2
        self.eventSink = BrowserCB(self.browser2)
            
        b2.Left = 0
        b2.Top = 0
        if (not self.allocation):
            b2.Width = rect[2]
            b2.Height = rect[3]
        else:
            b2.Width = self.allocation.width
            b2.Height = self.allocation.height
        self.browser2.Navigate2("about:blank")
        
        if self.content is not None:
            self.SetDocument(self.content)
            
        if self.callback is not None:
            self.setHtmlViewCallback(self.callback)               
        self.grab_focus()
            


    def do_unrealize(self):
        if self.docEventSink is not None:
            self.docEventSink.close()
        self.eventSink.close()
        self.browser.Close(axcontrol.OLECLOSE_NOSAVE)
        self.window.destroy()        
        self.browser = None
        self.browser2 = None
        

    def do_size_allocate(self, allocation):
        self.allocation = allocation
        if (self.browser2 is not None):
            self.browser2.Width = allocation.width
            self.browser2.Height = allocation.height
            if self.flags() & gtk.REALIZED:
                    self.window.move_resize(*allocation)
                
    def setHtmlViewCallback(self, callback):     
        self.callback = callback;
        if self.eventSink is not None:   
            self.eventSink.setHtmlViewCallback(callback)
        if self.docEventSink is not None:
            self.docEventSink.setHtmlViewCallback(callback)            
        
    def Navigate2(self, page):
        self.page = page
        #self.content = None
        self.browser2.Navigate2(page)
        
    def GoBack(self):
        self.browser2.GoBack()
                
    def GoForward(self):
        self.browser2.GoForward()
        
    def SetDocument(self, content):
        """ needs to load the document from a stream otherwise links are not interpreted
            (within a page) could have further benefits like loading pictures.
            However never tried.
        """
        self.content = content
        if (self.browser2 is not None):
            if self.docEventSink is None:
                self.docEventSink =   DocumentCB(self.browser2.Document)
                if self.callback is not None:
                    self.docEventSink.setHtmlViewCallback(self.callback)    
            
            #the stream method of loading seems to result in ValueErrors:
            #  PyGStream::Read: returned data longer than expected
            #followed by a pythoncom error:
            #  Unexpected exception in gateway method 'Read'
            #this happens when the string is of any significant (non-trivial) length
            #stream.Load(util.wrap(DataIStream.DataIStream(content)))
            #stream=self.browser2.Document._oleobj_.QueryInterface(pythoncom.IID_IPersistStreamInit)

            #the open/write/close method doesn't work too well either,
            # because anchors will be broken in this case
            #self.browser2.Document.open()
            #self.browser2.Document.write(content)
            #self.browser2.Document.close()

            #so, we create a tempfile that deletes on exit
            import os, tempfile, atexit
            def unlink_temp(f_name):
                os.unlink(f_name)
            fd, f_name = tempfile.mkstemp()
            atexit.register(unlink_temp, f_name)
            f = os.fdopen(fd, "w+b")
            f.write(content)
            f.close()
            self.Navigate2('file:///' + f_name)
            
    def GetDocument(self):
        if (self.browser2 is not None):
            if (self.browser2.Document is not None):
                return IEHtmlDocument(self.browser2.Document )
        return None       
                         

class IEHtmlView():
    """ IEHtmlBaseView wrapper class, to handle exposure events that inherited gtk objects don't seem to get
    NOTE: the widget must be added to other gtk objects via class's widget attribute
    TODO: find a better way to do this, preferrably without a wrapper
    """
    def __init__(self):
        self.widget = gtk.HBox()
        self.ie = IEHtmlBaseView()
        #self.widget.pack_start(self.ie, expand=True, fill=True, padding=0)
        self.widget.add(self.ie)
        self.widget.connect("expose-event", self.on_exposed_exposer)

    def on_exposed_exposer(self, widget, direction, user_param1 = None, user_param2 = None):
        self.ie.show()

    def do_realize(self):
        """Called when the widget should create all of its
        windowing resources.  We will create our gtk.gdk.Window.
        """
        self.widget.do_realize(self)
        self.ie.do_realize()
        

    def do_unrealize(self):
        self.widget.do_unrealize(self)
        self.ie.do_unrealize()

    def do_size_allocate(self, allocation):
        alloc = self.widget.get_allocation()
        self.widget.do_size_allocate(self.widget, alloc)
        return self.ie.do_size_allocate(allocation)

    def setHtmlViewCallback(self, callback):
        return self.ie.setHtmlViewCallback(callback)

    def Navigate2(self, page):
        return self.ie.Navigate2(page)

    def GoBack(self):
        return self.ie.GoBack()

    def GoForward(self):
        return self.ie.GoForward()

    def SetDocument(self, content):
        return self.ie.SetDocument(content)

    def GetDocument(self):
        return self.ie.GetDocument()
                                                                                            
if __name__ == '__main__':   
    window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    window.resize(800, 600)
    ie = IEHtmlView();
    window.add(ie)
    ie.show()
    window.show()    
    ie.browser2.Navigate2("about:blank")
    ie.SetDocument("""This is an IE page hosted by <a href="http://www.python.org">python</a>')
    <br>(you can also specify a URL on the command-line...)""")

    gtk.main()        

        
         