#taken from pywin32 example container_ie.py

from win32com.axcontrol import axcontrol
from win32com.server.exception import COMException
from win32com.server.util import wrap
from win32com.client import Dispatch

import pythoncom
import win32con
import win32gui
import winerror
import win32api



IOleClientSite_methods = """SaveObject GetMoniker GetContainer ShowObject
                            OnShowWindow RequestNewObjectLayout""".split()

IOleInPlaceSite_methods = """GetWindow ContextSensitiveHelp CanInPlaceActivate
                             OnInPlaceActivate OnUIActivate GetWindowContext
                             Scroll OnUIDeactivate OnInPlaceDeactivate
                             DiscardUndoState DeactivateAndUndo
                             OnPosRectChange""".split()

IOleInPlaceFrame_methods = """GetWindow ContextSensitiveHelp GetBorder
                              RequestBorderSpace SetBorderSpace
                              SetActiveObject InsertMenus SetMenu
                              RemoveMenus SetStatusText EnableModeless
                              TranslateAccelerator""".split()
                              
                           


class SimpleSite:
    _com_interfaces_ = [axcontrol.IID_IOleClientSite,
                        axcontrol.IID_IOleInPlaceSite]
    _public_methods_ = IOleClientSite_methods + IOleInPlaceSite_methods
    def __init__(self, host_window):
        self.hw = host_window

    # IID_IOleClientSite methods
    def SaveObject(self):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def GetMoniker(self, dwAssign, which):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def GetContainer(self):
        raise COMException(hresult=winerror.E_NOINTERFACE)

    def ShowObject(self):
        pass

    def OnShowWindow(self, fShow):
        pass

    def RequestNewObjectLayout(self):
        raise COMException(hresult=winerror.E_NOTIMPL)

    # IID_IOleInPlaceSite methods
    def GetWindow(self):
        return self.hw.hwnd

    def ContextSensitiveHelp(self, fEnter):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def CanInPlaceActivate(self):
        pass # we can

    def OnInPlaceActivate(self):
        pass

    def OnUIActivate(self):
        pass
    def GetWindowContext(self):
        # return IOleInPlaceFrame, IOleInPlaceUIWindow, rect, clip_rect, frame_info
        # where frame_info is (fMDIApp, hwndFrame, hAccel, nAccel)
        return self.hw.ole_frame, None, (0, 0, 0, 0), (0, 0, 0, 0), (True, self.hw.hwnd, None, 0)

    def Scroll(self, size):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def OnUIDeactivate(self, fUndoable):
        pass

    def OnInPlaceDeactivate(self):
        pass

    def DiscardUndoState(self):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def DeactivateAndUndo(self):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def OnPosRectChange(self, rect):
        browser_ob = self.hw.browser.QueryInterface(axcontrol.IID_IOleInPlaceObject)
        browser_ob.SetObjectRects(rect, rect)

class SimpleFrame:
    #_com_interfaces_ = [axcontrol.IID_IOleInPlaceFrame]
    _public_methods_ = IOleInPlaceFrame_methods

    def __init__(self, host_window):
        self.hw = host_window

    def GetWindow(self):
        return self.hw.hwnd

    def ContextSensitiveHelp(self, fEnterMode):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def GetBorder(self):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def RequestBorderSpace(self, widths):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def SetBorderSpace(self, widths):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def SetActiveObject(self, ob, name):
        pass

    def InsertMenus(self, hmenuShared, menuWidths):
        raise COMException(hresult=winerror.E_NOTIMPL)

    def SetMenu(self, hmenuShared, holemenu, hwndActiveObject):
        pass

    def RemoveMenus(self, hmenuShared):
        pass

    def SetStatusText(self, statusText):
        pass

    def EnableModeless(self, fEnable):
        pass

    def TranslateAccelerator(self, msg, wID):
        raise COMException(hresult=winerror.E_NOTIMPL)
