
__all__ = """\
IEHtmlViewCallback
""".split()



class IEHtmlViewCallback(object):

    def  OnBeforeNavigate(self, dest):
        """ return True or False"""
        pass
    
    
    def  OnNewWindow(self, dest):
        """ return True or False"""
        pass
    
    def OnContextMenu(self, source_element):
        """ return True or False -false if you dont want the 
        default menu to be processed
        @param source_element None or IHtmlElement instace"""
        pass
        