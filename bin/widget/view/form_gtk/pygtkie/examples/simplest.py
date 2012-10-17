import gtk
from pygtkie import IEHtmlView


window = gtk.Window(gtk.WINDOW_TOPLEVEL)
window.resize(800, 600)
ie = IEHtmlView();
window.add(ie)
ie.show()
window.show()
    
ie.SetDocument("""This is an IE page hosted by <a href="http://www.python.org">python</a>')""")

gtk.main()        
