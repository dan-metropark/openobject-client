## Example shows how to implement starting page with your custom commands
# Link can be a custom command which can be evaluated in  OnBeforeNavigate callback

import gtk
from pygtkie import IEHtmlView,IEHtmlViewCallback

class ClickCallback(IEHtmlViewCallback):
    def OnContextMenu(self, source_element):
        print "we dont want to show the context menu"
        return False            
        
    def  OnBeforeNavigate(self, dest):
        print "OnBeforeNavigate: " , dest
        if dest.find("python")>0:
            return False #go on with the page
        else:
            return True #block the page
            
        
window = gtk.Window(gtk.WINDOW_TOPLEVEL)
window.resize(800, 600)
ie = IEHtmlView();
ie.setHtmlViewCallback( ClickCallback() )
window.add(ie)
ie.show()
window.show()
    
ie.SetDocument("""only links to python page will work <a href="http://www.python.org">python</a>')
<br><a href="http://google.com">google</a>""")

gtk.main()        
