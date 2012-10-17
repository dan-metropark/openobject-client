# -*- coding: mbcs -*-
# Created by makepy.py version 0.4.97
# By python version 2.5.2 (r252:60911, Mar 27 2008, 17:57:18) [MSC v.1310 32 bit (Intel)]
# From type library 'shdocvw.dll'
# On Sat Jun 07 15:09:51 2008
"""Microsoft Internet Controls"""
makepy_version = '0.4.97'
python_version = 0x20502f0

import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{EAB22AC0-30C1-11CF-A7EB-0000C05BAE0B}')
MajorVersion = 1
MinorVersion = 1
LibraryFlags = 8
LCID = 0x0

class constants:
    CSC_NAVIGATEBACK              =0x2        # from enum CommandStateChangeConstants
    CSC_NAVIGATEFORWARD           =0x1        # from enum CommandStateChangeConstants
    CSC_UPDATECOMMANDS            =-1         # from enum CommandStateChangeConstants
    OLECMDEXECOPT_DODEFAULT       =0x0        # from enum OLECMDEXECOPT
    OLECMDEXECOPT_DONTPROMPTUSER  =0x2        # from enum OLECMDEXECOPT
    OLECMDEXECOPT_PROMPTUSER      =0x1        # from enum OLECMDEXECOPT
    OLECMDEXECOPT_SHOWHELP        =0x3        # from enum OLECMDEXECOPT
    OLECMDF_DEFHIDEONCTXTMENU     =0x20       # from enum OLECMDF
    OLECMDF_ENABLED               =0x2        # from enum OLECMDF
    OLECMDF_INVISIBLE             =0x10       # from enum OLECMDF
    OLECMDF_LATCHED               =0x4        # from enum OLECMDF
    OLECMDF_NINCHED               =0x8        # from enum OLECMDF
    OLECMDF_SUPPORTED             =0x1        # from enum OLECMDF
    OLECMDID_ALLOWUILESSSAVEAS    =0x2e       # from enum OLECMDID
    OLECMDID_CLEARSELECTION       =0x12       # from enum OLECMDID
    OLECMDID_CLOSE                =0x2d       # from enum OLECMDID
    OLECMDID_COPY                 =0xc        # from enum OLECMDID
    OLECMDID_CUT                  =0xb        # from enum OLECMDID
    OLECMDID_DELETE               =0x21       # from enum OLECMDID
    OLECMDID_DONTDOWNLOADCSS      =0x2f       # from enum OLECMDID
    OLECMDID_ENABLE_INTERACTION   =0x24       # from enum OLECMDID
    OLECMDID_FIND                 =0x20       # from enum OLECMDID
    OLECMDID_FOCUSVIEWCONTROLS    =0x39       # from enum OLECMDID
    OLECMDID_FOCUSVIEWCONTROLSQUERY=0x3a       # from enum OLECMDID
    OLECMDID_GETPRINTTEMPLATE     =0x34       # from enum OLECMDID
    OLECMDID_GETZOOMRANGE         =0x14       # from enum OLECMDID
    OLECMDID_HIDETOOLBARS         =0x18       # from enum OLECMDID
    OLECMDID_HTTPEQUIV            =0x22       # from enum OLECMDID
    OLECMDID_HTTPEQUIV_DONE       =0x23       # from enum OLECMDID
    OLECMDID_NEW                  =0x2        # from enum OLECMDID
    OLECMDID_ONTOOLBARACTIVATED   =0x1f       # from enum OLECMDID
    OLECMDID_ONUNLOAD             =0x25       # from enum OLECMDID
    OLECMDID_OPEN                 =0x1        # from enum OLECMDID
    OLECMDID_PAGEACTIONBLOCKED    =0x37       # from enum OLECMDID
    OLECMDID_PAGEACTIONUIQUERY    =0x38       # from enum OLECMDID
    OLECMDID_PAGESETUP            =0x8        # from enum OLECMDID
    OLECMDID_PASTE                =0xd        # from enum OLECMDID
    OLECMDID_PASTESPECIAL         =0xe        # from enum OLECMDID
    OLECMDID_PREREFRESH           =0x27       # from enum OLECMDID
    OLECMDID_PRINT                =0x6        # from enum OLECMDID
    OLECMDID_PRINT2               =0x31       # from enum OLECMDID
    OLECMDID_PRINTPREVIEW         =0x7        # from enum OLECMDID
    OLECMDID_PRINTPREVIEW2        =0x32       # from enum OLECMDID
    OLECMDID_PROPERTIES           =0xa        # from enum OLECMDID
    OLECMDID_PROPERTYBAG2         =0x26       # from enum OLECMDID
    OLECMDID_REDO                 =0x10       # from enum OLECMDID
    OLECMDID_REFRESH              =0x16       # from enum OLECMDID
    OLECMDID_SAVE                 =0x3        # from enum OLECMDID
    OLECMDID_SAVEAS               =0x4        # from enum OLECMDID
    OLECMDID_SAVECOPYAS           =0x5        # from enum OLECMDID
    OLECMDID_SELECTALL            =0x11       # from enum OLECMDID
    OLECMDID_SETDOWNLOADSTATE     =0x1d       # from enum OLECMDID
    OLECMDID_SETPRINTTEMPLATE     =0x33       # from enum OLECMDID
    OLECMDID_SETPROGRESSMAX       =0x19       # from enum OLECMDID
    OLECMDID_SETPROGRESSPOS       =0x1a       # from enum OLECMDID
    OLECMDID_SETPROGRESSTEXT      =0x1b       # from enum OLECMDID
    OLECMDID_SETTITLE             =0x1c       # from enum OLECMDID
    OLECMDID_SHOWFIND             =0x2a       # from enum OLECMDID
    OLECMDID_SHOWMESSAGE          =0x29       # from enum OLECMDID
    OLECMDID_SHOWPAGEACTIONMENU   =0x3b       # from enum OLECMDID
    OLECMDID_SHOWPAGESETUP        =0x2b       # from enum OLECMDID
    OLECMDID_SHOWPRINT            =0x2c       # from enum OLECMDID
    OLECMDID_SHOWSCRIPTERROR      =0x28       # from enum OLECMDID
    OLECMDID_SPELL                =0x9        # from enum OLECMDID
    OLECMDID_STOP                 =0x17       # from enum OLECMDID
    OLECMDID_STOPDOWNLOAD         =0x1e       # from enum OLECMDID
    OLECMDID_UNDO                 =0xf        # from enum OLECMDID
    OLECMDID_UPDATECOMMANDS       =0x15       # from enum OLECMDID
    OLECMDID_UPDATEPAGESTATUS     =0x30       # from enum OLECMDID
    OLECMDID_ZOOM                 =0x13       # from enum OLECMDID
    secureLockIconMixed           =0x1        # from enum SecureLockIconConstants
    secureLockIconSecure128Bit    =0x6        # from enum SecureLockIconConstants
    secureLockIconSecure40Bit     =0x3        # from enum SecureLockIconConstants
    secureLockIconSecure56Bit     =0x4        # from enum SecureLockIconConstants
    secureLockIconSecureFortezza  =0x5        # from enum SecureLockIconConstants
    secureLockIconSecureUnknownBits=0x2        # from enum SecureLockIconConstants
    secureLockIconUnsecure        =0x0        # from enum SecureLockIconConstants
    SWFO_COOKIEPASSED             =0x4        # from enum ShellWindowFindWindowOptions
    SWFO_INCLUDEPENDING           =0x2        # from enum ShellWindowFindWindowOptions
    SWFO_NEEDDISPATCH             =0x1        # from enum ShellWindowFindWindowOptions
    SWC_3RDPARTY                  =0x2        # from enum ShellWindowTypeConstants
    SWC_BROWSER                   =0x1        # from enum ShellWindowTypeConstants
    SWC_CALLBACK                  =0x4        # from enum ShellWindowTypeConstants
    SWC_EXPLORER                  =0x0        # from enum ShellWindowTypeConstants
    READYSTATE_COMPLETE           =0x4        # from enum tagREADYSTATE
    READYSTATE_INTERACTIVE        =0x3        # from enum tagREADYSTATE
    READYSTATE_LOADED             =0x2        # from enum tagREADYSTATE
    READYSTATE_LOADING            =0x1        # from enum tagREADYSTATE
    READYSTATE_UNINITIALIZED      =0x0        # from enum tagREADYSTATE

class DShellNameSpaceEvents:
    CLSID = CLSID_Sink = IID('{55136806-B2DE-11D1-B9F2-00A0C98BC547}')
    coclass_clsid = IID('{2F2F1F96-2BC1-4B1C-BE28-EA3774F4676A}')
    _public_methods_ = [] # For COM Server support
    _dispid_to_func_ = {
                4 : "OnInitialized",
                2 : "OnSelectionChange",
                3 : "OnDoubleClick",
                1 : "OnFavoritesSelectionChange",
        }

    def __init__(self, oobj = None):
        if oobj is None:
            self._olecp = None
        else:
            import win32com.server.util
            from win32com.server.policy import EventHandlerPolicy
            cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
            cp=cpc.FindConnectionPoint(self.CLSID_Sink)
            cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
            self._olecp,self._olecp_cookie = cp,cookie
    def __del__(self):
        try:
            self.close()
        except pythoncom.com_error:
            pass
    def close(self):
        if self._olecp is not None:
            cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
            cp.Unadvise(cookie)
    def _query_interface_(self, iid):
        import win32com.server.util
        if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

    # Event Handlers
    # If you create handlers, they should have the following prototypes:
#    def OnInitialized(self):
#    def OnSelectionChange(self):
#    def OnDoubleClick(self):
#    def OnFavoritesSelectionChange(self, cItems=defaultNamedNotOptArg, hItem=defaultNamedNotOptArg, strName=defaultNamedNotOptArg, strUrl=defaultNamedNotOptArg
#            , cVisits=defaultNamedNotOptArg, strDate=defaultNamedNotOptArg, fAvailableOffline=defaultNamedNotOptArg):


class DShellWindowsEvents:
    """Event interface for IShellWindows"""
    CLSID = CLSID_Sink = IID('{FE4106E0-399A-11D0-A48C-00A0C90A8F39}')
    coclass_clsid = IID('{9BA05972-F6A8-11CF-A442-00A0C90A8F39}')
    _public_methods_ = [] # For COM Server support
    _dispid_to_func_ = {
              201 : "OnWindowRevoked",
              200 : "OnWindowRegistered",
        }

    def __init__(self, oobj = None):
        if oobj is None:
            self._olecp = None
        else:
            import win32com.server.util
            from win32com.server.policy import EventHandlerPolicy
            cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
            cp=cpc.FindConnectionPoint(self.CLSID_Sink)
            cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
            self._olecp,self._olecp_cookie = cp,cookie
    def __del__(self):
        try:
            self.close()
        except pythoncom.com_error:
            pass
    def close(self):
        if self._olecp is not None:
            cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
            cp.Unadvise(cookie)
    def _query_interface_(self, iid):
        import win32com.server.util
        if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

    # Event Handlers
    # If you create handlers, they should have the following prototypes:
#    def OnWindowRevoked(self, lCookie=defaultNamedNotOptArg):
#        """A new window was revoked."""
#    def OnWindowRegistered(self, lCookie=defaultNamedNotOptArg):
#        """A new window was registered."""


class DWebBrowserEvents:
    """Web Browser Control Events (old)"""
    CLSID = CLSID_Sink = IID('{EAB22AC2-30C1-11CF-A7EB-0000C05BAE0B}')
    coclass_clsid = IID('{C08AFD90-F2A1-11D1-8455-00A0C91F3880}')
    _public_methods_ = [] # For COM Server support
    _dispid_to_func_ = {
              101 : "OnNavigateComplete",
              103 : "OnQuit",
              201 : "OnFrameNavigateComplete",
              108 : "OnProgressChange",
              110 : "OnWindowResize",
              109 : "OnWindowMove",
              104 : "OnDownloadComplete",
              107 : "OnNewWindow",
              111 : "OnWindowActivate",
              102 : "OnStatusTextChange",
              200 : "OnFrameBeforeNavigate",
              204 : "OnFrameNewWindow",
              105 : "OnCommandStateChange",
              106 : "OnDownloadBegin",
              113 : "OnTitleChange",
              100 : "OnBeforeNavigate",
              112 : "OnPropertyChange",
        }

    def __init__(self, oobj = None):
        if oobj is None:
            self._olecp = None
        else:
            import win32com.server.util
            from win32com.server.policy import EventHandlerPolicy
            cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
            cp=cpc.FindConnectionPoint(self.CLSID_Sink)
            cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
            self._olecp,self._olecp_cookie = cp,cookie
    def __del__(self):
        try:
            self.close()
        except pythoncom.com_error:
            pass
    def close(self):
        if self._olecp is not None:
            cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
            cp.Unadvise(cookie)
    def _query_interface_(self, iid):
        import win32com.server.util
        if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

    # Event Handlers
    # If you create handlers, they should have the following prototypes:
#    def OnNavigateComplete(self, URL=defaultNamedNotOptArg):
#        """Fired when the document being navigated to becomes visible and enters the navigation stack."""
#    def OnQuit(self, Cancel=defaultNamedNotOptArg):
#        """Fired when application is quiting."""
#    def OnFrameNavigateComplete(self, URL=defaultNamedNotOptArg):
#        """Fired when a new hyperlink is being navigated to in a frame."""
#    def OnProgressChange(self, Progress=defaultNamedNotOptArg, ProgressMax=defaultNamedNotOptArg):
#        """Fired when download progress is updated."""
#    def OnWindowResize(self):
#        """Fired when window has been sized."""
#    def OnWindowMove(self):
#        """Fired when window has been moved."""
#    def OnDownloadComplete(self):
#        """Download of page complete."""
#    def OnNewWindow(self, URL=defaultNamedNotOptArg, Flags=defaultNamedNotOptArg, TargetFrameName=defaultNamedNotOptArg, PostData=defaultNamedNotOptArg
#            , Headers=defaultNamedNotOptArg, Processed=defaultNamedNotOptArg):
#        """Fired when a new window should be created."""
#    def OnWindowActivate(self):
#        """Fired when window has been activated."""
#    def OnStatusTextChange(self, Text=defaultNamedNotOptArg):
#        """Statusbar text changed."""
#    def OnFrameBeforeNavigate(self, URL=defaultNamedNotOptArg, Flags=defaultNamedNotOptArg, TargetFrameName=defaultNamedNotOptArg, PostData=defaultNamedNotOptArg
#            , Headers=defaultNamedNotOptArg, Cancel=defaultNamedNotOptArg):
#        """Fired when a new hyperlink is being navigated to in a frame."""
#    def OnFrameNewWindow(self, URL=defaultNamedNotOptArg, Flags=defaultNamedNotOptArg, TargetFrameName=defaultNamedNotOptArg, PostData=defaultNamedNotOptArg
#            , Headers=defaultNamedNotOptArg, Processed=defaultNamedNotOptArg):
#        """Fired when a new window should be created."""
#    def OnCommandStateChange(self, Command=defaultNamedNotOptArg, Enable=defaultNamedNotOptArg):
#        """The enabled state of a command changed"""
#    def OnDownloadBegin(self):
#        """Download of a page started."""
#    def OnTitleChange(self, Text=defaultNamedNotOptArg):
#        """Document title changed."""
#    def OnBeforeNavigate(self, URL=defaultNamedNotOptArg, Flags=defaultNamedNotOptArg, TargetFrameName=defaultNamedNotOptArg, PostData=defaultNamedNotOptArg
#            , Headers=defaultNamedNotOptArg, Cancel=defaultNamedNotOptArg):
#        """Fired when a new hyperlink is being navigated to."""
#    def OnPropertyChange(self, Property=defaultNamedNotOptArg):
#        """Fired when the PutProperty method has been called."""


class DWebBrowserEvents2:
    """Web Browser Control events interface"""
    CLSID = CLSID_Sink = IID('{34A715A0-6587-11D0-924A-0020AFC7AC4D}')
    coclass_clsid = IID('{C08AFD90-F2A1-11D1-8455-00A0C91F3880}')
    _public_methods_ = [] # For COM Server support
    _dispid_to_func_ = {
              227 : "OnUpdatePageStatus",
              270 : "OnFileDownload",
              104 : "OnDownloadComplete",
              250 : "OnBeforeNavigate2",
              269 : "OnSetSecureLockIcon",
              108 : "OnProgressChange",
              271 : "OnNavigateError",
              105 : "OnCommandStateChange",
              268 : "OnClientToHostWindow",
              113 : "OnTitleChange",
              266 : "OnWindowSetWidth",
              259 : "OnDocumentComplete",
              256 : "OnMenuBar",
              272 : "OnPrivacyImpactedStateChange",
              112 : "OnPropertyChange",
              255 : "OnToolBar",
              260 : "OnTheaterMode",
              265 : "OnWindowSetTop",
              102 : "OnStatusTextChange",
              263 : "OnWindowClosing",
              257 : "OnStatusBar",
              262 : "OnWindowSetResizable",
              251 : "OnNewWindow2",
              273 : "OnNewWindow3",
              226 : "OnPrintTemplateTeardown",
              225 : "OnPrintTemplateInstantiation",
              258 : "OnFullScreen",
              253 : "OnQuit",
              264 : "OnWindowSetLeft",
              267 : "OnWindowSetHeight",
              252 : "OnNavigateComplete2",
              106 : "OnDownloadBegin",
              254 : "OnVisible",
        }

    def __init__(self, oobj = None):
        if oobj is None:
            self._olecp = None
        else:
            import win32com.server.util
            from win32com.server.policy import EventHandlerPolicy
            cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
            cp=cpc.FindConnectionPoint(self.CLSID_Sink)
            cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
            self._olecp,self._olecp_cookie = cp,cookie
    def __del__(self):
        try:
            self.close()
        except pythoncom.com_error:
            pass
    def close(self):
        if self._olecp is not None:
            cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
            cp.Unadvise(cookie)
    def _query_interface_(self, iid):
        import win32com.server.util
        if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

    # Event Handlers
    # If you create handlers, they should have the following prototypes:
#    def OnUpdatePageStatus(self, pDisp=defaultNamedNotOptArg, nPage=defaultNamedNotOptArg, fDone=defaultNamedNotOptArg):
#        """Fired when a page is spooled. When it is fired can be changed by a custom template."""
#    def OnFileDownload(self, Cancel=defaultNamedNotOptArg):
#        """Fired to indicate the File Download dialog is opening"""
#    def OnDownloadComplete(self):
#        """Download of page complete."""
#    def OnBeforeNavigate2(self, pDisp=defaultNamedNotOptArg, URL=defaultNamedNotOptArg, Flags=defaultNamedNotOptArg, TargetFrameName=defaultNamedNotOptArg
#            , PostData=defaultNamedNotOptArg, Headers=defaultNamedNotOptArg, Cancel=defaultNamedNotOptArg):
#        """Fired before navigate occurs in the given WebBrowser (window or frameset element). The processing of this navigation may be modified."""
#    def OnSetSecureLockIcon(self, SecureLockIcon=defaultNamedNotOptArg):
#        """Fired to indicate the security level of the current web page contents"""
#    def OnProgressChange(self, Progress=defaultNamedNotOptArg, ProgressMax=defaultNamedNotOptArg):
#        """Fired when download progress is updated."""
#    def OnNavigateError(self, pDisp=defaultNamedNotOptArg, URL=defaultNamedNotOptArg, Frame=defaultNamedNotOptArg, StatusCode=defaultNamedNotOptArg
#            , Cancel=defaultNamedNotOptArg):
#        """Fired when a binding error occurs (window or frameset element)."""
#    def OnCommandStateChange(self, Command=defaultNamedNotOptArg, Enable=defaultNamedNotOptArg):
#        """The enabled state of a command changed."""
#    def OnClientToHostWindow(self, CX=defaultNamedNotOptArg, CY=defaultNamedNotOptArg):
#        """Fired to request client sizes be converted to host window sizes"""
#    def OnTitleChange(self, Text=defaultNamedNotOptArg):
#        """Document title changed."""
#    def OnWindowSetWidth(self, Width=defaultNamedNotOptArg):
#        """Fired when the host window should change its width"""
#    def OnDocumentComplete(self, pDisp=defaultNamedNotOptArg, URL=defaultNamedNotOptArg):
#        """Fired when the document being navigated to reaches ReadyState_Complete."""
#    def OnMenuBar(self, MenuBar=defaultNamedNotOptArg):
#        """Fired when the menubar should be shown/hidden"""
#    def OnPrivacyImpactedStateChange(self, bImpacted=defaultNamedNotOptArg):
#        """Fired when the global privacy impacted state changes"""
#    def OnPropertyChange(self, szProperty=defaultNamedNotOptArg):
#        """Fired when the PutProperty method has been called."""
#    def OnToolBar(self, ToolBar=defaultNamedNotOptArg):
#        """Fired when the toolbar  should be shown/hidden"""
#    def OnTheaterMode(self, TheaterMode=defaultNamedNotOptArg):
#        """Fired when theater mode should be on/off"""
#    def OnWindowSetTop(self, Top=defaultNamedNotOptArg):
#        """Fired when the host window should change its Top coordinate"""
#    def OnStatusTextChange(self, Text=defaultNamedNotOptArg):
#        """Statusbar text changed."""
#    def OnWindowClosing(self, IsChildWindow=defaultNamedNotOptArg, Cancel=defaultNamedNotOptArg):
#        """Fired when the WebBrowser is about to be closed by script"""
#    def OnStatusBar(self, StatusBar=defaultNamedNotOptArg):
#        """Fired when the statusbar should be shown/hidden"""
#    def OnWindowSetResizable(self, Resizable=defaultNamedNotOptArg):
#        """Fired when the host window should allow/disallow resizing"""
#    def OnNewWindow2(self, ppDisp=defaultNamedNotOptArg, Cancel=defaultNamedNotOptArg):
#        """A new, hidden, non-navigated WebBrowser window is needed."""
#    def OnNewWindow3(self, ppDisp=defaultNamedNotOptArg, Cancel=defaultNamedNotOptArg, dwFlags=defaultNamedNotOptArg, bstrUrlContext=defaultNamedNotOptArg
#            , bstrUrl=defaultNamedNotOptArg):
#        """A new, hidden, non-navigated WebBrowser window is needed."""
#    def OnPrintTemplateTeardown(self, pDisp=defaultNamedNotOptArg):
#        """Fired when a print template destroyed."""
#    def OnPrintTemplateInstantiation(self, pDisp=defaultNamedNotOptArg):
#        """Fired when a print template is instantiated."""
#    def OnFullScreen(self, FullScreen=defaultNamedNotOptArg):
#        """Fired when fullscreen mode should be on/off"""
#    def OnQuit(self):
#        """Fired when application is quiting."""
#    def OnWindowSetLeft(self, Left=defaultNamedNotOptArg):
#        """Fired when the host window should change its Left coordinate"""
#    def OnWindowSetHeight(self, Height=defaultNamedNotOptArg):
#        """Fired when the host window should change its height"""
#    def OnNavigateComplete2(self, pDisp=defaultNamedNotOptArg, URL=defaultNamedNotOptArg):
#        """Fired when the document being navigated to becomes visible and enters the navigation stack."""
#    def OnDownloadBegin(self):
#        """Download of a page started."""
#    def OnVisible(self, Visible=defaultNamedNotOptArg):
#        """Fired when the window should be shown/hidden"""


from win32com.client import DispatchBaseClass
class IScriptErrorList(DispatchBaseClass):
    """Script Error List Interface"""
    CLSID = IID('{F3470F24-15FD-11D2-BB2E-00805FF7EFCA}')
    coclass_clsid = IID('{EFD01300-160F-11D2-BB2E-00805FF7EFCA}')

    def advanceError(self):
        return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), (),)

    def canAdvanceError(self):
        return self._oleobj_.InvokeTypes(12, LCID, 1, (3, 0), (),)

    def canRetreatError(self):
        return self._oleobj_.InvokeTypes(13, LCID, 1, (3, 0), (),)

    def getAlwaysShowLockState(self):
        return self._oleobj_.InvokeTypes(23, LCID, 1, (3, 0), (),)

    def getDetailsPaneOpen(self):
        return self._oleobj_.InvokeTypes(19, LCID, 1, (3, 0), (),)

    def getErrorChar(self):
        return self._oleobj_.InvokeTypes(15, LCID, 1, (3, 0), (),)

    def getErrorCode(self):
        return self._oleobj_.InvokeTypes(16, LCID, 1, (3, 0), (),)

    def getErrorLine(self):
        return self._oleobj_.InvokeTypes(14, LCID, 1, (3, 0), (),)

    def getErrorMsg(self):
        # Result is a Unicode object - return as-is for this version of Python
        return self._oleobj_.InvokeTypes(17, LCID, 1, (8, 0), (),)

    def getErrorUrl(self):
        # Result is a Unicode object - return as-is for this version of Python
        return self._oleobj_.InvokeTypes(18, LCID, 1, (8, 0), (),)

    def getPerErrorDisplay(self):
        return self._oleobj_.InvokeTypes(21, LCID, 1, (3, 0), (),)

    def retreatError(self):
        return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), (),)

    def setDetailsPaneOpen(self, fDetailsPaneOpen=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), ((3, 0),),fDetailsPaneOpen
            )

    def setPerErrorDisplay(self, fPerErrorDisplay=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), ((3, 0),),fPerErrorDisplay
            )

    _prop_map_get_ = {
    }
    _prop_map_put_ = {
    }

class ISearch(DispatchBaseClass):
    """Enumerated Search"""
    CLSID = IID('{BA9239A4-3DD5-11D2-BF8B-00C04FB93661}')
    coclass_clsid = None

    _prop_map_get_ = {
        "Id": (1610743809, 2, (8, 0), (), "Id", None),
        "Title": (1610743808, 2, (8, 0), (), "Title", None),
        "URL": (1610743810, 2, (8, 0), (), "URL", None),
    }
    _prop_map_put_ = {
    }

class ISearchAssistantOC(DispatchBaseClass):
    """ISearchAssistantOC Interface"""
    CLSID = IID('{72423E8F-8011-11D2-BE79-00A0C9A83DA1}')
    coclass_clsid = None

    def AddNextMenuItem(self, bstrText=defaultNamedNotOptArg, idItem=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), ((8, 1), (3, 1)),bstrText
            , idItem)

    def EncodeString(self, bstrValue=defaultNamedNotOptArg, bstrCharSet=defaultNamedNotOptArg, bUseUTF8=defaultNamedNotOptArg):
        # Result is a Unicode object - return as-is for this version of Python
        return self._oleobj_.InvokeTypes(25, LCID, 1, (8, 0), ((8, 1), (8, 1), (11, 1)),bstrValue
            , bstrCharSet, bUseUTF8)

    def FindComputer(self):
        return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), (),)

    def FindFilesOrFolders(self):
        return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), (),)

    def FindOnWeb(self):
        return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), (),)

    def FindPeople(self):
        return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), (),)

    def FindPrinter(self):
        return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), (),)

    def GetProperty(self, bPerLocale=defaultNamedNotOptArg, bstrName=defaultNamedNotOptArg):
        # Result is a Unicode object - return as-is for this version of Python
        return self._oleobj_.InvokeTypes(10, LCID, 1, (8, 0), ((11, 1), (8, 1)),bPerLocale
            , bstrName)

    def GetSearchAssistantURL(self, bSubstitute=defaultNamedNotOptArg, bCustomize=defaultNamedNotOptArg):
        # Result is a Unicode object - return as-is for this version of Python
        return self._oleobj_.InvokeTypes(18, LCID, 1, (8, 0), ((11, 1), (11, 1)),bSubstitute
            , bCustomize)

    def IsRestricted(self, bstrGuid=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((8, 1),),bstrGuid
            )

    def NETDetectNextNavigate(self):
        return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), (),)

    def NavigateToDefaultSearch(self):
        return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), (),)

    def NotifySearchSettingsChanged(self):
        return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), (),)

    def PutFindText(self, FindText=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), ((8, 1),),FindText
            )

    def PutProperty(self, bPerLocale=defaultNamedNotOptArg, bstrName=defaultNamedNotOptArg, bstrValue=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((11, 1), (8, 1), (8, 1)),bPerLocale
            , bstrName, bstrValue)

    def ResetNextMenu(self):
        return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), (),)

    def SetDefaultSearchUrl(self, bstrUrl=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((8, 1),),bstrUrl
            )

    _prop_map_get_ = {
        "ASProvider": (20, 2, (8, 0), (), "ASProvider", None),
        "ASSetting": (21, 2, (3, 0), (), "ASSetting", None),
        "InWebFolder": (8, 2, (11, 0), (), "InWebFolder", None),
        "SearchAssistantDefault": (6, 2, (11, 0), (), "SearchAssistantDefault", None),
        # Method 'Searches' returns object of type 'ISearches'
        "Searches": (7, 2, (9, 0), (), "Searches", '{47C922A2-3DD5-11D2-BF8B-00C04FB93661}'),
        "ShellFeaturesEnabled": (5, 2, (11, 0), (), "ShellFeaturesEnabled", None),
        "Version": (24, 2, (3, 0), (), "Version", None),
    }
    _prop_map_put_ = {
        "ASProvider": ((20, LCID, 4, 0),()),
        "ASSetting": ((21, LCID, 4, 0),()),
        "EventHandled": ((11, LCID, 4, 0),()),
    }

class ISearchAssistantOC2(DispatchBaseClass):
    """ISearchAssistantOC2 Interface"""
    CLSID = IID('{72423E8F-8011-11D2-BE79-00A0C9A83DA2}')
    coclass_clsid = None

    def AddNextMenuItem(self, bstrText=defaultNamedNotOptArg, idItem=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), ((8, 1), (3, 1)),bstrText
            , idItem)

    def EncodeString(self, bstrValue=defaultNamedNotOptArg, bstrCharSet=defaultNamedNotOptArg, bUseUTF8=defaultNamedNotOptArg):
        # Result is a Unicode object - return as-is for this version of Python
        return self._oleobj_.InvokeTypes(25, LCID, 1, (8, 0), ((8, 1), (8, 1), (11, 1)),bstrValue
            , bstrCharSet, bUseUTF8)

    def FindComputer(self):
        return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), (),)

    def FindFilesOrFolders(self):
        return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), (),)

    def FindOnWeb(self):
        return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), (),)

    def FindPeople(self):
        return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), (),)

    def FindPrinter(self):
        return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), (),)

    def GetProperty(self, bPerLocale=defaultNamedNotOptArg, bstrName=defaultNamedNotOptArg):
        # Result is a Unicode object - return as-is for this version of Python
        return self._oleobj_.InvokeTypes(10, LCID, 1, (8, 0), ((11, 1), (8, 1)),bPerLocale
            , bstrName)

    def GetSearchAssistantURL(self, bSubstitute=defaultNamedNotOptArg, bCustomize=defaultNamedNotOptArg):
        # Result is a Unicode object - return as-is for this version of Python
        return self._oleobj_.InvokeTypes(18, LCID, 1, (8, 0), ((11, 1), (11, 1)),bSubstitute
            , bCustomize)

    def IsRestricted(self, bstrGuid=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((8, 1),),bstrGuid
            )

    def NETDetectNextNavigate(self):
        return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), (),)

    def NavigateToDefaultSearch(self):
        return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), (),)

    def NotifySearchSettingsChanged(self):
        return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), (),)

    def PutFindText(self, FindText=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), ((8, 1),),FindText
            )

    def PutProperty(self, bPerLocale=defaultNamedNotOptArg, bstrName=defaultNamedNotOptArg, bstrValue=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((11, 1), (8, 1), (8, 1)),bPerLocale
            , bstrName, bstrValue)

    def ResetNextMenu(self):
        return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), (),)

    def SetDefaultSearchUrl(self, bstrUrl=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((8, 1),),bstrUrl
            )

    _prop_map_get_ = {
        "ASProvider": (20, 2, (8, 0), (), "ASProvider", None),
        "ASSetting": (21, 2, (3, 0), (), "ASSetting", None),
        "InWebFolder": (8, 2, (11, 0), (), "InWebFolder", None),
        "SearchAssistantDefault": (6, 2, (11, 0), (), "SearchAssistantDefault", None),
        # Method 'Searches' returns object of type 'ISearches'
        "Searches": (7, 2, (9, 0), (), "Searches", '{47C922A2-3DD5-11D2-BF8B-00C04FB93661}'),
        "ShellFeaturesEnabled": (5, 2, (11, 0), (), "ShellFeaturesEnabled", None),
        "ShowFindPrinter": (26, 2, (11, 0), (), "ShowFindPrinter", None),
        "Version": (24, 2, (3, 0), (), "Version", None),
    }
    _prop_map_put_ = {
        "ASProvider": ((20, LCID, 4, 0),()),
        "ASSetting": ((21, LCID, 4, 0),()),
        "EventHandled": ((11, LCID, 4, 0),()),
    }

class ISearchAssistantOC3(DispatchBaseClass):
    """ISearchAssistantOC3 Interface"""
    CLSID = IID('{72423E8F-8011-11D2-BE79-00A0C9A83DA3}')
    coclass_clsid = IID('{2E71FD0F-AAB1-42C0-9146-6D2C4EDCF07D}')

    def AddNextMenuItem(self, bstrText=defaultNamedNotOptArg, idItem=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), ((8, 1), (3, 1)),bstrText
            , idItem)

    def EncodeString(self, bstrValue=defaultNamedNotOptArg, bstrCharSet=defaultNamedNotOptArg, bUseUTF8=defaultNamedNotOptArg):
        # Result is a Unicode object - return as-is for this version of Python
        return self._oleobj_.InvokeTypes(25, LCID, 1, (8, 0), ((8, 1), (8, 1), (11, 1)),bstrValue
            , bstrCharSet, bUseUTF8)

    def FindComputer(self):
        return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), (),)

    def FindFilesOrFolders(self):
        return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), (),)

    def FindOnWeb(self):
        return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), (),)

    def FindPeople(self):
        return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), (),)

    def FindPrinter(self):
        return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), (),)

    def GetProperty(self, bPerLocale=defaultNamedNotOptArg, bstrName=defaultNamedNotOptArg):
        # Result is a Unicode object - return as-is for this version of Python
        return self._oleobj_.InvokeTypes(10, LCID, 1, (8, 0), ((11, 1), (8, 1)),bPerLocale
            , bstrName)

    def GetSearchAssistantURL(self, bSubstitute=defaultNamedNotOptArg, bCustomize=defaultNamedNotOptArg):
        # Result is a Unicode object - return as-is for this version of Python
        return self._oleobj_.InvokeTypes(18, LCID, 1, (8, 0), ((11, 1), (11, 1)),bSubstitute
            , bCustomize)

    def IsRestricted(self, bstrGuid=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((8, 1),),bstrGuid
            )

    def NETDetectNextNavigate(self):
        return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), (),)

    def NavigateToDefaultSearch(self):
        return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), (),)

    def NotifySearchSettingsChanged(self):
        return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), (),)

    def PutFindText(self, FindText=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), ((8, 1),),FindText
            )

    def PutProperty(self, bPerLocale=defaultNamedNotOptArg, bstrName=defaultNamedNotOptArg, bstrValue=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((11, 1), (8, 1), (8, 1)),bPerLocale
            , bstrName, bstrValue)

    def ResetNextMenu(self):
        return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), (),)

    def SetDefaultSearchUrl(self, bstrUrl=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((8, 1),),bstrUrl
            )

    _prop_map_get_ = {
        "ASProvider": (20, 2, (8, 0), (), "ASProvider", None),
        "ASSetting": (21, 2, (3, 0), (), "ASSetting", None),
        "InWebFolder": (8, 2, (11, 0), (), "InWebFolder", None),
        "SearchAssistantDefault": (6, 2, (11, 0), (), "SearchAssistantDefault", None),
        "SearchCompanionAvailable": (27, 2, (11, 0), (), "SearchCompanionAvailable", None),
        # Method 'Searches' returns object of type 'ISearches'
        "Searches": (7, 2, (9, 0), (), "Searches", '{47C922A2-3DD5-11D2-BF8B-00C04FB93661}'),
        "ShellFeaturesEnabled": (5, 2, (11, 0), (), "ShellFeaturesEnabled", None),
        "ShowFindPrinter": (26, 2, (11, 0), (), "ShowFindPrinter", None),
        "UseSearchCompanion": (28, 2, (11, 0), (), "UseSearchCompanion", None),
        "Version": (24, 2, (3, 0), (), "Version", None),
    }
    _prop_map_put_ = {
        "ASProvider": ((20, LCID, 4, 0),()),
        "ASSetting": ((21, LCID, 4, 0),()),
        "EventHandled": ((11, LCID, 4, 0),()),
        "UseSearchCompanion": ((28, LCID, 4, 0),()),
    }

class ISearches(DispatchBaseClass):
    """Searches Enum"""
    CLSID = IID('{47C922A2-3DD5-11D2-BF8B-00C04FB93661}')
    coclass_clsid = None

    # Result is of type ISearch
    def Item(self, index=defaultNamedOptArg):
        """Return the specified search"""
        ret = self._oleobj_.InvokeTypes(1610743810, LCID, 1, (9, 0), ((12, 17),),index
            )
        if ret is not None:
            ret = Dispatch(ret, u'Item', '{BA9239A4-3DD5-11D2-BF8B-00C04FB93661}', UnicodeToString=0)
        return ret

    _prop_map_get_ = {
        "Count": (1610743808, 2, (3, 0), (), "Count", None),
        "Default": (1610743809, 2, (8, 0), (), "Default", None),
    }
    _prop_map_put_ = {
    }
    def __iter__(self):
        "Return a Python iterator for this object"
        ob = self._oleobj_.InvokeTypes(-4,LCID,1,(13, 10),())
        return win32com.client.util.Iterator(ob, '{BA9239A4-3DD5-11D2-BF8B-00C04FB93661}')
    def _NewEnum(self):
        "Create an enumerator from this object"
        return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,1,(13, 10),()),'{BA9239A4-3DD5-11D2-BF8B-00C04FB93661}')
    def __getitem__(self, index):
        "Allow this class to be accessed as a collection"
        if not self.__dict__.has_key('_enum_'):
            self.__dict__['_enum_'] = self._NewEnum()
        return self._enum_.__getitem__(index)
    #This class has Count() property - allow len(ob) to provide this
    def __len__(self):
        return self._ApplyTypes_(*(1610743808, 2, (3, 0), (), "Count", None))
    #This class has a __len__ - this is needed so 'if object:' always returns TRUE.
    def __nonzero__(self):
        return True

class IShellFavoritesNameSpace(DispatchBaseClass):
    """IShellFavoritesNameSpace Interface"""
    CLSID = IID('{55136804-B2DE-11D1-B9F2-00A0C98BC547}')
    coclass_clsid = None

    def CreateSubscriptionForSelection(self):
        """method CreateSubscriptionForSelection"""
        return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), (),)

    def DeleteSubscriptionForSelection(self):
        """method DeleteSubscriptionForSelection"""
        return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), (),)

    def Export(self):
        """method Export"""
        return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), (),)

    def Import(self):
        """method Import"""
        return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), (),)

    def InvokeContextMenuCommand(self, strCommand=defaultNamedNotOptArg):
        """method InvokeContextMenuCommand"""
        return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((8, 1),),strCommand
            )

    def MoveSelectionDown(self):
        """method MoveSelectionDown"""
        return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), (),)

    def MoveSelectionTo(self):
        """method MoveSelectionTo"""
        return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), (),)

    def MoveSelectionUp(self):
        """method MoveSelectionUp"""
        return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), (),)

    def NewFolder(self):
        """method NewFolder"""
        return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), (),)

    def ResetSort(self):
        """method ResetSort"""
        return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), (),)

    def SetRoot(self, bstrFullPath=defaultNamedNotOptArg):
        """old, use put_Root() instead"""
        return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((8, 1),),bstrFullPath
            )

    def Synchronize(self):
        """method Synchronize"""
        return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), (),)

    _prop_map_get_ = {
        "SubscriptionsEnabled": (10, 2, (11, 0), (), "SubscriptionsEnabled", None),
    }
    _prop_map_put_ = {
    }

class IShellNameSpace(DispatchBaseClass):
    """IShellNameSpace Interface"""
    CLSID = IID('{E572D3C9-37BE-4AE2-825D-D521763E3108}')
    coclass_clsid = IID('{2F2F1F96-2BC1-4B1C-BE28-EA3774F4676A}')

    def CreateSubscriptionForSelection(self):
        """method CreateSubscriptionForSelection"""
        return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), (),)

    def DeleteSubscriptionForSelection(self):
        """method DeleteSubscriptionForSelection"""
        return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), (),)

    def Expand(self, var=defaultNamedNotOptArg, iDepth=defaultNamedNotOptArg):
        """expands item specified depth"""
        return self._oleobj_.InvokeTypes(25, LCID, 1, (24, 0), ((12, 1), (3, 0)),var
            , iDepth)

    def Export(self):
        """method Export"""
        return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), (),)

    def Import(self):
        """method Import"""
        return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), (),)

    def InvokeContextMenuCommand(self, strCommand=defaultNamedNotOptArg):
        """method InvokeContextMenuCommand"""
        return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((8, 1),),strCommand
            )

    def MoveSelectionDown(self):
        """method MoveSelectionDown"""
        return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), (),)

    def MoveSelectionTo(self):
        """method MoveSelectionTo"""
        return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), (),)

    def MoveSelectionUp(self):
        """method MoveSelectionUp"""
        return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), (),)

    def NewFolder(self):
        """method NewFolder"""
        return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), (),)

    def ResetSort(self):
        """method ResetSort"""
        return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), (),)

    def SelectedItems(self):
        """collection of selected items"""
        ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), (),)
        if ret is not None:
            ret = Dispatch(ret, u'SelectedItems', None, UnicodeToString=0)
        return ret

    def SetRoot(self, bstrFullPath=defaultNamedNotOptArg):
        """old, use put_Root() instead"""
        return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((8, 1),),bstrFullPath
            )

    def SetViewType(self, iType=defaultNamedNotOptArg):
        """set view type"""
        return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), ((3, 1),),iType
            )

    def Synchronize(self):
        """method Synchronize"""
        return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), (),)

    def UnselectAll(self):
        """unselects all items"""
        return self._oleobj_.InvokeTypes(26, LCID, 1, (24, 0), (),)

    _prop_map_get_ = {
        "Columns": (21, 2, (8, 0), (), "Columns", None),
        "CountViewTypes": (22, 2, (3, 0), (), "CountViewTypes", None),
        "Depth": (17, 2, (3, 0), (), "Depth", None),
        "EnumOptions": (14, 2, (3, 0), (), "EnumOptions", None),
        "Flags": (19, 2, (19, 0), (), "Flags", None),
        "Mode": (18, 2, (3, 0), (), "Mode", None),
        "Root": (16, 2, (12, 0), (), "Root", None),
        "SelectedItem": (15, 2, (9, 0), (), "SelectedItem", None),
        "SubscriptionsEnabled": (10, 2, (11, 0), (), "SubscriptionsEnabled", None),
        "TVFlags": (20, 2, (19, 0), (), "TVFlags", None),
    }
    _prop_map_put_ = {
        "Columns": ((21, LCID, 4, 0),()),
        "Depth": ((17, LCID, 4, 0),()),
        "EnumOptions": ((14, LCID, 4, 0),()),
        "Flags": ((19, LCID, 4, 0),()),
        "Mode": ((18, LCID, 4, 0),()),
        "Root": ((16, LCID, 4, 0),()),
        "SelectedItem": ((15, LCID, 4, 0),()),
        "TVFlags": ((20, LCID, 4, 0),()),
    }

class IShellUIHelper(DispatchBaseClass):
    """Shell UI Helper Control Interface"""
    CLSID = IID('{729FE2F8-1EA8-11D1-8F85-00C04FC2FBE1}')
    coclass_clsid = IID('{64AB4BB7-111E-11D1-8F79-00C04FC2FBE1}')

    def AddChannel(self, URL=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), ((8, 1),),URL
            )

    def AddDesktopComponent(self, URL=defaultNamedNotOptArg, Type=defaultNamedNotOptArg, Left=defaultNamedOptArg, Top=defaultNamedOptArg
            , Width=defaultNamedOptArg, Height=defaultNamedOptArg):
        return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((8, 1), (8, 1), (16396, 17), (16396, 17), (16396, 17), (16396, 17)),URL
            , Type, Left, Top, Width, Height
            )

    def AddFavorite(self, URL=defaultNamedNotOptArg, Title=defaultNamedOptArg):
        return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((8, 1), (16396, 17)),URL
            , Title)

    def AutoCompleteAttach(self, Reserved=defaultNamedOptArg):
        return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((16396, 17),),Reserved
            )

    def AutoCompleteSaveForm(self, Form=defaultNamedOptArg):
        return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((16396, 17),),Form
            )

    def AutoScan(self, strSearch=defaultNamedNotOptArg, strFailureUrl=defaultNamedNotOptArg, pvarTargetFrame=defaultNamedOptArg):
        return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((8, 1), (8, 1), (16396, 17)),strSearch
            , strFailureUrl, pvarTargetFrame)

    def ImportExportFavorites(self, fImport=defaultNamedNotOptArg, strImpExpPath=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((11, 1), (8, 1)),fImport
            , strImpExpPath)

    def IsSubscribed(self, URL=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((8, 1),),URL
            )

    def NavigateAndFind(self, URL=defaultNamedNotOptArg, strQuery=defaultNamedNotOptArg, varTargetFrame=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((8, 1), (8, 1), (16396, 1)),URL
            , strQuery, varTargetFrame)

    def RefreshOfflineDesktop(self):
        return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), (),)

    def ResetFirstBootMode(self):
        return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), (),)

    def ResetSafeMode(self):
        return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), (),)

    def ShowBrowserUI(self, bstrName=defaultNamedNotOptArg, pvarIn=defaultNamedNotOptArg):
        return self._ApplyTypes_(13, 1, (12, 0), ((8, 1), (16396, 1)), u'ShowBrowserUI', None,bstrName
            , pvarIn)

    _prop_map_get_ = {
    }
    _prop_map_put_ = {
    }

class IShellWindows(DispatchBaseClass):
    """Definition of interface IShellWindows"""
    CLSID = IID('{85CB6900-4D95-11CF-960C-0080C7F4EE85}')
    coclass_clsid = IID('{9BA05972-F6A8-11CF-A442-00A0C90A8F39}')

    def FindWindowSW(self, pvarloc=defaultNamedNotOptArg, pvarlocRoot=defaultNamedNotOptArg, swClass=defaultNamedNotOptArg, pHWND=pythoncom.Missing
            , swfwOptions=defaultNamedNotOptArg):
        """Find the window based on the location"""
        return self._ApplyTypes_(1610743816, 1, (9, 0), ((16396, 1), (16396, 1), (3, 1), (16387, 2), (3, 1)), u'FindWindowSW', None,pvarloc
            , pvarlocRoot, swClass, pHWND, swfwOptions)

    def Item(self, index=defaultNamedOptArg):
        """Return the shell window for the given index"""
        ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((12, 17),),index
            )
        if ret is not None:
            ret = Dispatch(ret, u'Item', None, UnicodeToString=0)
        return ret

    def OnActivated(self, lCookie=defaultNamedNotOptArg, fActive=defaultNamedNotOptArg):
        """Notifies the activation"""
        return self._oleobj_.InvokeTypes(1610743815, LCID, 1, (24, 0), ((3, 1), (11, 1)),lCookie
            , fActive)

    def OnCreated(self, lCookie=defaultNamedNotOptArg, punk=defaultNamedNotOptArg):
        """Notifies on creation and frame name set"""
        return self._oleobj_.InvokeTypes(1610743817, LCID, 1, (24, 0), ((3, 1), (13, 1)),lCookie
            , punk)

    def OnNavigate(self, lCookie=defaultNamedNotOptArg, pvarloc=defaultNamedNotOptArg):
        """Notifies the new location"""
        return self._oleobj_.InvokeTypes(1610743814, LCID, 1, (24, 0), ((3, 1), (16396, 1)),lCookie
            , pvarloc)

    def ProcessAttachDetach(self, fAttach=defaultNamedNotOptArg):
        """Used by IExplore to register different processes"""
        return self._oleobj_.InvokeTypes(1610743818, LCID, 1, (24, 0), ((11, 1),),fAttach
            )

    def Register(self, pid=defaultNamedNotOptArg, HWND=defaultNamedNotOptArg, swClass=defaultNamedNotOptArg, plCookie=pythoncom.Missing):
        """Register a window with the list"""
        return self._ApplyTypes_(1610743811, 1, (24, 0), ((9, 1), (3, 1), (3, 1), (16387, 2)), u'Register', None,pid
            , HWND, swClass, plCookie)

    def RegisterPending(self, lThreadId=defaultNamedNotOptArg, pvarloc=defaultNamedNotOptArg, pvarlocRoot=defaultNamedNotOptArg, swClass=defaultNamedNotOptArg
            , plCookie=pythoncom.Missing):
        """Register a pending open with the list"""
        return self._ApplyTypes_(1610743812, 1, (24, 0), ((3, 1), (16396, 1), (16396, 1), (3, 1), (16387, 2)), u'RegisterPending', None,lThreadId
            , pvarloc, pvarlocRoot, swClass, plCookie)

    def Revoke(self, lCookie=defaultNamedNotOptArg):
        """Remove a window from the list"""
        return self._oleobj_.InvokeTypes(1610743813, LCID, 1, (24, 0), ((3, 1),),lCookie
            )

    _prop_map_get_ = {
        "Count": (1610743808, 2, (3, 0), (), "Count", None),
    }
    _prop_map_put_ = {
    }
    # Default method for this class is 'Item'
    def __call__(self, index=defaultNamedOptArg):
        """Return the shell window for the given index"""
        ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((12, 17),),index
            )
        if ret is not None:
            ret = Dispatch(ret, '__call__', None, UnicodeToString=0)
        return ret

    # str(ob) and int(ob) will use __call__
    def __unicode__(self, *args):
        try:
            return unicode(self.__call__(*args))
        except pythoncom.com_error:
            return repr(self)
    def __str__(self, *args):
        return str(self.__unicode__(*args))
    def __int__(self, *args):
        return int(self.__call__(*args))
    def __iter__(self):
        "Return a Python iterator for this object"
        ob = self._oleobj_.InvokeTypes(-4,LCID,1,(13, 10),())
        return win32com.client.util.Iterator(ob, None)
    def _NewEnum(self):
        "Create an enumerator from this object"
        return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,1,(13, 10),()),None)
    def __getitem__(self, index):
        "Allow this class to be accessed as a collection"
        if not self.__dict__.has_key('_enum_'):
            self.__dict__['_enum_'] = self._NewEnum()
        return self._enum_.__getitem__(index)
    #This class has Count() property - allow len(ob) to provide this
    def __len__(self):
        return self._ApplyTypes_(*(1610743808, 2, (3, 0), (), "Count", None))
    #This class has a __len__ - this is needed so 'if object:' always returns TRUE.
    def __nonzero__(self):
        return True

class IWebBrowser(DispatchBaseClass):
    """Web Browser interface"""
    CLSID = IID('{EAB22AC1-30C1-11CF-A7EB-0000C05BAE0B}')
    coclass_clsid = IID('{8856F961-340A-11D0-A96B-00C04FD705A2}')

    def GoBack(self):
        """Navigates to the previous item in the history list."""
        return self._oleobj_.InvokeTypes(100, LCID, 1, (24, 0), (),)

    def GoForward(self):
        """Navigates to the next item in the history list."""
        return self._oleobj_.InvokeTypes(101, LCID, 1, (24, 0), (),)

    def GoHome(self):
        """Go home/start page."""
        return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), (),)

    def GoSearch(self):
        """Go Search Page."""
        return self._oleobj_.InvokeTypes(103, LCID, 1, (24, 0), (),)

    def Navigate(self, URL=defaultNamedNotOptArg, Flags=defaultNamedOptArg, TargetFrameName=defaultNamedOptArg, PostData=defaultNamedOptArg
            , Headers=defaultNamedOptArg):
        """Navigates to a URL or file."""
        return self._oleobj_.InvokeTypes(104, LCID, 1, (24, 0), ((8, 1), (16396, 17), (16396, 17), (16396, 17), (16396, 17)),URL
            , Flags, TargetFrameName, PostData, Headers)

    def Refresh(self):
        """Refresh the currently viewed page."""
        return self._oleobj_.InvokeTypes(-550, LCID, 1, (24, 0), (),)

    def Refresh2(self, Level=defaultNamedOptArg):
        """Refresh the currently viewed page."""
        return self._oleobj_.InvokeTypes(105, LCID, 1, (24, 0), ((16396, 17),),Level
            )

    def Stop(self):
        """Stops opening a file."""
        return self._oleobj_.InvokeTypes(106, LCID, 1, (24, 0), (),)

    _prop_map_get_ = {
        "Application": (200, 2, (9, 0), (), "Application", None),
        "Busy": (212, 2, (11, 0), (), "Busy", None),
        "Container": (202, 2, (9, 0), (), "Container", None),
        "Document": (203, 2, (9, 0), (), "Document", None),
        "Height": (209, 2, (3, 0), (), "Height", None),
        "Left": (206, 2, (3, 0), (), "Left", None),
        "LocationName": (210, 2, (8, 0), (), "LocationName", None),
        "LocationURL": (211, 2, (8, 0), (), "LocationURL", None),
        "Parent": (201, 2, (9, 0), (), "Parent", None),
        "Top": (207, 2, (3, 0), (), "Top", None),
        "TopLevelContainer": (204, 2, (11, 0), (), "TopLevelContainer", None),
        "Type": (205, 2, (8, 0), (), "Type", None),
        "Width": (208, 2, (3, 0), (), "Width", None),
    }
    _prop_map_put_ = {
        "Height": ((209, LCID, 4, 0),()),
        "Left": ((206, LCID, 4, 0),()),
        "Top": ((207, LCID, 4, 0),()),
        "Width": ((208, LCID, 4, 0),()),
    }

class IWebBrowser2(DispatchBaseClass):
    """Web Browser Interface for IE4."""
    CLSID = IID('{D30C1661-CDAF-11D0-8A3E-00C04FC9E26E}')
    coclass_clsid = IID('{C08AFD90-F2A1-11D1-8455-00A0C91F3880}')

    def ClientToWindow(self, pcx=defaultNamedNotOptArg, pcy=defaultNamedNotOptArg):
        """Converts client sizes into window sizes."""
        return self._ApplyTypes_(301, 1, (24, 0), ((16387, 3), (16387, 3)), u'ClientToWindow', None,pcx
            , pcy)

    def ExecWB(self, cmdID=defaultNamedNotOptArg, cmdexecopt=defaultNamedNotOptArg, pvaIn=defaultNamedOptArg, pvaOut=defaultNamedOptArg):
        """IOleCommandTarget::Exec"""
        return self._ApplyTypes_(502, 1, (24, 0), ((3, 1), (3, 1), (16396, 17), (16396, 19)), u'ExecWB', None,cmdID
            , cmdexecopt, pvaIn, pvaOut)

    def GetProperty(self, Property=defaultNamedNotOptArg):
        """Retrieve the Associated value for the property vtValue in the context of the object."""
        return self._ApplyTypes_(303, 1, (12, 0), ((8, 1),), u'GetProperty', None,Property
            )

    def GoBack(self):
        """Navigates to the previous item in the history list."""
        return self._oleobj_.InvokeTypes(100, LCID, 1, (24, 0), (),)

    def GoForward(self):
        """Navigates to the next item in the history list."""
        return self._oleobj_.InvokeTypes(101, LCID, 1, (24, 0), (),)

    def GoHome(self):
        """Go home/start page."""
        return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), (),)

    def GoSearch(self):
        """Go Search Page."""
        return self._oleobj_.InvokeTypes(103, LCID, 1, (24, 0), (),)

    def Navigate(self, URL=defaultNamedNotOptArg, Flags=defaultNamedOptArg, TargetFrameName=defaultNamedOptArg, PostData=defaultNamedOptArg
            , Headers=defaultNamedOptArg):
        """Navigates to a URL or file."""
        return self._oleobj_.InvokeTypes(104, LCID, 1, (24, 0), ((8, 1), (16396, 17), (16396, 17), (16396, 17), (16396, 17)),URL
            , Flags, TargetFrameName, PostData, Headers)

    def Navigate2(self, URL=defaultNamedNotOptArg, Flags=defaultNamedOptArg, TargetFrameName=defaultNamedOptArg, PostData=defaultNamedOptArg
            , Headers=defaultNamedOptArg):
        """Navigates to a URL or file or pidl."""
        return self._oleobj_.InvokeTypes(500, LCID, 1, (24, 0), ((16396, 1), (16396, 17), (16396, 17), (16396, 17), (16396, 17)),URL
            , Flags, TargetFrameName, PostData, Headers)

    def PutProperty(self, Property=defaultNamedNotOptArg, vtValue=defaultNamedNotOptArg):
        """Associates vtValue with the name szProperty in the context of the object."""
        return self._oleobj_.InvokeTypes(302, LCID, 1, (24, 0), ((8, 1), (12, 1)),Property
            , vtValue)

    def QueryStatusWB(self, cmdID=defaultNamedNotOptArg):
        """IOleCommandTarget::QueryStatus"""
        return self._oleobj_.InvokeTypes(501, LCID, 1, (3, 0), ((3, 1),),cmdID
            )

    def Quit(self):
        """Exits application and closes the open document."""
        return self._oleobj_.InvokeTypes(300, LCID, 1, (24, 0), (),)

    def Refresh(self):
        """Refresh the currently viewed page."""
        return self._oleobj_.InvokeTypes(-550, LCID, 1, (24, 0), (),)

    def Refresh2(self, Level=defaultNamedOptArg):
        """Refresh the currently viewed page."""
        return self._oleobj_.InvokeTypes(105, LCID, 1, (24, 0), ((16396, 17),),Level
            )

    def ShowBrowserBar(self, pvaClsid=defaultNamedNotOptArg, pvarShow=defaultNamedOptArg, pvarSize=defaultNamedOptArg):
        """Set BrowserBar to Clsid"""
        return self._oleobj_.InvokeTypes(503, LCID, 1, (24, 0), ((16396, 1), (16396, 17), (16396, 17)),pvaClsid
            , pvarShow, pvarSize)

    def Stop(self):
        """Stops opening a file."""
        return self._oleobj_.InvokeTypes(106, LCID, 1, (24, 0), (),)

    _prop_map_get_ = {
        "AddressBar": (555, 2, (11, 0), (), "AddressBar", None),
        "Application": (200, 2, (9, 0), (), "Application", None),
        "Busy": (212, 2, (11, 0), (), "Busy", None),
        "Container": (202, 2, (9, 0), (), "Container", None),
        "Document": (203, 2, (9, 0), (), "Document", None),
        "FullName": (400, 2, (8, 0), (), "FullName", None),
        "FullScreen": (407, 2, (11, 0), (), "FullScreen", None),
        "HWND": (-515, 2, (3, 0), (), "HWND", None),
        "Height": (209, 2, (3, 0), (), "Height", None),
        "Left": (206, 2, (3, 0), (), "Left", None),
        "LocationName": (210, 2, (8, 0), (), "LocationName", None),
        "LocationURL": (211, 2, (8, 0), (), "LocationURL", None),
        "MenuBar": (406, 2, (11, 0), (), "MenuBar", None),
        "Name": (0, 2, (8, 0), (), "Name", None),
        "Offline": (550, 2, (11, 0), (), "Offline", None),
        "Parent": (201, 2, (9, 0), (), "Parent", None),
        "Path": (401, 2, (8, 0), (), "Path", None),
        "ReadyState": (-525, 2, (3, 0), (), "ReadyState", None),
        "RegisterAsBrowser": (552, 2, (11, 0), (), "RegisterAsBrowser", None),
        "RegisterAsDropTarget": (553, 2, (11, 0), (), "RegisterAsDropTarget", None),
        "Resizable": (556, 2, (11, 0), (), "Resizable", None),
        "Silent": (551, 2, (11, 0), (), "Silent", None),
        "StatusBar": (403, 2, (11, 0), (), "StatusBar", None),
        "StatusText": (404, 2, (8, 0), (), "StatusText", None),
        "TheaterMode": (554, 2, (11, 0), (), "TheaterMode", None),
        "ToolBar": (405, 2, (3, 0), (), "ToolBar", None),
        "Top": (207, 2, (3, 0), (), "Top", None),
        "TopLevelContainer": (204, 2, (11, 0), (), "TopLevelContainer", None),
        "Type": (205, 2, (8, 0), (), "Type", None),
        "Visible": (402, 2, (11, 0), (), "Visible", None),
        "Width": (208, 2, (3, 0), (), "Width", None),
    }
    _prop_map_put_ = {
        "AddressBar": ((555, LCID, 4, 0),()),
        "FullScreen": ((407, LCID, 4, 0),()),
        "Height": ((209, LCID, 4, 0),()),
        "Left": ((206, LCID, 4, 0),()),
        "MenuBar": ((406, LCID, 4, 0),()),
        "Offline": ((550, LCID, 4, 0),()),
        "RegisterAsBrowser": ((552, LCID, 4, 0),()),
        "RegisterAsDropTarget": ((553, LCID, 4, 0),()),
        "Resizable": ((556, LCID, 4, 0),()),
        "Silent": ((551, LCID, 4, 0),()),
        "StatusBar": ((403, LCID, 4, 0),()),
        "StatusText": ((404, LCID, 4, 0),()),
        "TheaterMode": ((554, LCID, 4, 0),()),
        "ToolBar": ((405, LCID, 4, 0),()),
        "Top": ((207, LCID, 4, 0),()),
        "Visible": ((402, LCID, 4, 0),()),
        "Width": ((208, LCID, 4, 0),()),
    }
    # Default property for this class is 'Name'
    def __call__(self):
        return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
    # str(ob) and int(ob) will use __call__
    def __unicode__(self, *args):
        try:
            return unicode(self.__call__(*args))
        except pythoncom.com_error:
            return repr(self)
    def __str__(self, *args):
        return str(self.__unicode__(*args))
    def __int__(self, *args):
        return int(self.__call__(*args))

class IWebBrowserApp(DispatchBaseClass):
    """Web Browser Application Interface."""
    CLSID = IID('{0002DF05-0000-0000-C000-000000000046}')
    coclass_clsid = IID('{C08AFD90-F2A1-11D1-8455-00A0C91F3880}')

    def ClientToWindow(self, pcx=defaultNamedNotOptArg, pcy=defaultNamedNotOptArg):
        """Converts client sizes into window sizes."""
        return self._ApplyTypes_(301, 1, (24, 0), ((16387, 3), (16387, 3)), u'ClientToWindow', None,pcx
            , pcy)

    def GetProperty(self, Property=defaultNamedNotOptArg):
        """Retrieve the Associated value for the property vtValue in the context of the object."""
        return self._ApplyTypes_(303, 1, (12, 0), ((8, 1),), u'GetProperty', None,Property
            )

    def GoBack(self):
        """Navigates to the previous item in the history list."""
        return self._oleobj_.InvokeTypes(100, LCID, 1, (24, 0), (),)

    def GoForward(self):
        """Navigates to the next item in the history list."""
        return self._oleobj_.InvokeTypes(101, LCID, 1, (24, 0), (),)

    def GoHome(self):
        """Go home/start page."""
        return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), (),)

    def GoSearch(self):
        """Go Search Page."""
        return self._oleobj_.InvokeTypes(103, LCID, 1, (24, 0), (),)

    def Navigate(self, URL=defaultNamedNotOptArg, Flags=defaultNamedOptArg, TargetFrameName=defaultNamedOptArg, PostData=defaultNamedOptArg
            , Headers=defaultNamedOptArg):
        """Navigates to a URL or file."""
        return self._oleobj_.InvokeTypes(104, LCID, 1, (24, 0), ((8, 1), (16396, 17), (16396, 17), (16396, 17), (16396, 17)),URL
            , Flags, TargetFrameName, PostData, Headers)

    def PutProperty(self, Property=defaultNamedNotOptArg, vtValue=defaultNamedNotOptArg):
        """Associates vtValue with the name szProperty in the context of the object."""
        return self._oleobj_.InvokeTypes(302, LCID, 1, (24, 0), ((8, 1), (12, 1)),Property
            , vtValue)

    def Quit(self):
        """Exits application and closes the open document."""
        return self._oleobj_.InvokeTypes(300, LCID, 1, (24, 0), (),)

    def Refresh(self):
        """Refresh the currently viewed page."""
        return self._oleobj_.InvokeTypes(-550, LCID, 1, (24, 0), (),)

    def Refresh2(self, Level=defaultNamedOptArg):
        """Refresh the currently viewed page."""
        return self._oleobj_.InvokeTypes(105, LCID, 1, (24, 0), ((16396, 17),),Level
            )

    def Stop(self):
        """Stops opening a file."""
        return self._oleobj_.InvokeTypes(106, LCID, 1, (24, 0), (),)

    _prop_map_get_ = {
        "Application": (200, 2, (9, 0), (), "Application", None),
        "Busy": (212, 2, (11, 0), (), "Busy", None),
        "Container": (202, 2, (9, 0), (), "Container", None),
        "Document": (203, 2, (9, 0), (), "Document", None),
        "FullName": (400, 2, (8, 0), (), "FullName", None),
        "FullScreen": (407, 2, (11, 0), (), "FullScreen", None),
        "HWND": (-515, 2, (3, 0), (), "HWND", None),
        "Height": (209, 2, (3, 0), (), "Height", None),
        "Left": (206, 2, (3, 0), (), "Left", None),
        "LocationName": (210, 2, (8, 0), (), "LocationName", None),
        "LocationURL": (211, 2, (8, 0), (), "LocationURL", None),
        "MenuBar": (406, 2, (11, 0), (), "MenuBar", None),
        "Name": (0, 2, (8, 0), (), "Name", None),
        "Parent": (201, 2, (9, 0), (), "Parent", None),
        "Path": (401, 2, (8, 0), (), "Path", None),
        "StatusBar": (403, 2, (11, 0), (), "StatusBar", None),
        "StatusText": (404, 2, (8, 0), (), "StatusText", None),
        "ToolBar": (405, 2, (3, 0), (), "ToolBar", None),
        "Top": (207, 2, (3, 0), (), "Top", None),
        "TopLevelContainer": (204, 2, (11, 0), (), "TopLevelContainer", None),
        "Type": (205, 2, (8, 0), (), "Type", None),
        "Visible": (402, 2, (11, 0), (), "Visible", None),
        "Width": (208, 2, (3, 0), (), "Width", None),
    }
    _prop_map_put_ = {
        "FullScreen": ((407, LCID, 4, 0),()),
        "Height": ((209, LCID, 4, 0),()),
        "Left": ((206, LCID, 4, 0),()),
        "MenuBar": ((406, LCID, 4, 0),()),
        "StatusBar": ((403, LCID, 4, 0),()),
        "StatusText": ((404, LCID, 4, 0),()),
        "ToolBar": ((405, LCID, 4, 0),()),
        "Top": ((207, LCID, 4, 0),()),
        "Visible": ((402, LCID, 4, 0),()),
        "Width": ((208, LCID, 4, 0),()),
    }
    # Default property for this class is 'Name'
    def __call__(self):
        return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
    # str(ob) and int(ob) will use __call__
    def __unicode__(self, *args):
        try:
            return unicode(self.__call__(*args))
        except pythoncom.com_error:
            return repr(self)
    def __str__(self, *args):
        return str(self.__unicode__(*args))
    def __int__(self, *args):
        return int(self.__call__(*args))

class _SearchAssistantEvents:
    CLSID = CLSID_Sink = IID('{1611FDDA-445B-11D2-85DE-00C04FA35C89}')
    coclass_clsid = IID('{2E71FD0F-AAB1-42C0-9146-6D2C4EDCF07D}')
    _public_methods_ = [] # For COM Server support
    _dispid_to_func_ = {
                2 : "OnNewSearch",
                1 : "OnNextMenuSelect",
        }

    def __init__(self, oobj = None):
        if oobj is None:
            self._olecp = None
        else:
            import win32com.server.util
            from win32com.server.policy import EventHandlerPolicy
            cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
            cp=cpc.FindConnectionPoint(self.CLSID_Sink)
            cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
            self._olecp,self._olecp_cookie = cp,cookie
    def __del__(self):
        try:
            self.close()
        except pythoncom.com_error:
            pass
    def close(self):
        if self._olecp is not None:
            cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
            cp.Unadvise(cookie)
    def _query_interface_(self, iid):
        import win32com.server.util
        if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

    # Event Handlers
    # If you create handlers, they should have the following prototypes:
#    def OnNewSearch(self):
#    def OnNextMenuSelect(self, idItem=defaultNamedNotOptArg):


from win32com.client import CoClassBaseClass
class CScriptErrorList(CoClassBaseClass): # A CoClass
    CLSID = IID('{EFD01300-160F-11D2-BB2E-00805FF7EFCA}')
    coclass_sources = [
    ]
    coclass_interfaces = [
        IScriptErrorList,
    ]
    default_interface = IScriptErrorList

# This CoClass is known by the name 'InternetExplorer.Application.1'
class InternetExplorer(CoClassBaseClass): # A CoClass
    # Internet Explorer Application.
    CLSID = IID('{0002DF01-0000-0000-C000-000000000046}')
    coclass_sources = [
        DWebBrowserEvents2,
        DWebBrowserEvents,
    ]
    default_source = DWebBrowserEvents2
    coclass_interfaces = [
        IWebBrowser2,
        IWebBrowserApp,
    ]
    default_interface = IWebBrowser2

# This CoClass is known by the name 'SearchAssistantOC.SearchAssistantOC.1'
class SearchAssistantOC(CoClassBaseClass): # A CoClass
    # Internet Explorer SearchAssistantOC Class
    CLSID = IID('{B45FF030-4447-11D2-85DE-00C04FA35C89}')
    coclass_sources = [
        _SearchAssistantEvents,
    ]
    default_source = _SearchAssistantEvents
    coclass_interfaces = [
        ISearchAssistantOC3,
    ]
    default_interface = ISearchAssistantOC3

class ShellBrowserWindow(CoClassBaseClass): # A CoClass
    # Shell Browser Window.
    CLSID = IID('{C08AFD90-F2A1-11D1-8455-00A0C91F3880}')
    coclass_sources = [
        DWebBrowserEvents2,
        DWebBrowserEvents,
    ]
    default_source = DWebBrowserEvents2
    coclass_interfaces = [
        IWebBrowser2,
        IWebBrowserApp,
    ]
    default_interface = IWebBrowser2

# This CoClass is known by the name 'ShellNameSpace.ShellNameSpace.1'
class ShellNameSpace(CoClassBaseClass): # A CoClass
    # Internet Explorer ShellNameSpace Class
    CLSID = IID('{55136805-B2DE-11D1-B9F2-00A0C98BC547}')
    coclass_sources = [
        DShellNameSpaceEvents,
    ]
    default_source = DShellNameSpaceEvents
    coclass_interfaces = [
        IShellNameSpace,
    ]
    default_interface = IShellNameSpace

# This CoClass is known by the name 'SearchAssistantOC.SearchAssistantOC.1'
class ShellSearchAssistantOC(CoClassBaseClass): # A CoClass
    # Shell SearchAssistantOC Class
    CLSID = IID('{2E71FD0F-AAB1-42C0-9146-6D2C4EDCF07D}')
    coclass_sources = [
        _SearchAssistantEvents,
    ]
    default_source = _SearchAssistantEvents
    coclass_interfaces = [
        ISearchAssistantOC3,
    ]
    default_interface = ISearchAssistantOC3

# This CoClass is known by the name 'ShellNameSpace.ShellNameSpace.1'
class ShellShellNameSpace(CoClassBaseClass): # A CoClass
    # Shell ShellNameSpace Class
    CLSID = IID('{2F2F1F96-2BC1-4B1C-BE28-EA3774F4676A}')
    coclass_sources = [
        DShellNameSpaceEvents,
    ]
    default_source = DShellNameSpaceEvents
    coclass_interfaces = [
        IShellNameSpace,
    ]
    default_interface = IShellNameSpace

# This CoClass is known by the name 'Shell.UIHelper.1'
class ShellUIHelper(CoClassBaseClass): # A CoClass
    CLSID = IID('{64AB4BB7-111E-11D1-8F79-00C04FC2FBE1}')
    coclass_sources = [
    ]
    coclass_interfaces = [
        IShellUIHelper,
    ]
    default_interface = IShellUIHelper

class ShellWindows(CoClassBaseClass): # A CoClass
    # ShellDispatch Load in Shell Context
    CLSID = IID('{9BA05972-F6A8-11CF-A442-00A0C90A8F39}')
    coclass_sources = [
        DShellWindowsEvents,
    ]
    default_source = DShellWindowsEvents
    coclass_interfaces = [
        IShellWindows,
    ]
    default_interface = IShellWindows

# This CoClass is known by the name 'Shell.Explorer.2'
class WebBrowser(CoClassBaseClass): # A CoClass
    # WebBrowser Control
    CLSID = IID('{8856F961-340A-11D0-A96B-00C04FD705A2}')
    coclass_sources = [
        DWebBrowserEvents2,
        DWebBrowserEvents,
    ]
    default_source = DWebBrowserEvents2
    coclass_interfaces = [
        IWebBrowser2,
        IWebBrowser,
    ]
    default_interface = IWebBrowser2

# This CoClass is known by the name 'Shell.Explorer.1'
class WebBrowser_V1(CoClassBaseClass): # A CoClass
    # WebBrowser Control
    CLSID = IID('{EAB22AC3-30C1-11CF-A7EB-0000C05BAE0B}')
    coclass_sources = [
        DWebBrowserEvents2,
        DWebBrowserEvents,
    ]
    default_source = DWebBrowserEvents
    coclass_interfaces = [
        IWebBrowser2,
        IWebBrowser,
    ]
    default_interface = IWebBrowser

IScriptErrorList_vtables_dispatch_ = 1
IScriptErrorList_vtables_ = [
    (( u'advanceError' , ), 10, (10, (), [ ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
    (( u'retreatError' , ), 11, (11, (), [ ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
    (( u'canAdvanceError' , u'pfCanAdvance' , ), 12, (12, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
    (( u'canRetreatError' , u'pfCanRetreat' , ), 13, (13, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
    (( u'getErrorLine' , u'plLine' , ), 14, (14, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
    (( u'getErrorChar' , u'plChar' , ), 15, (15, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
    (( u'getErrorCode' , u'plCode' , ), 16, (16, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
    (( u'getErrorMsg' , u'pstr' , ), 17, (17, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
    (( u'getErrorUrl' , u'pstr' , ), 18, (18, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
    (( u'getAlwaysShowLockState' , u'pfAlwaysShowLocked' , ), 23, (23, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
    (( u'getDetailsPaneOpen' , u'pfDetailsPaneOpen' , ), 19, (19, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
    (( u'setDetailsPaneOpen' , u'fDetailsPaneOpen' , ), 20, (20, (), [ (3, 0, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
    (( u'getPerErrorDisplay' , u'pfPerErrorDisplay' , ), 21, (21, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
    (( u'setPerErrorDisplay' , u'fPerErrorDisplay' , ), 22, (22, (), [ (3, 0, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ISearch_vtables_dispatch_ = 1
ISearch_vtables_ = [
    (( u'Title' , u'pbstrTitle' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
    (( u'Id' , u'pbstrId' , ), 1610743809, (1610743809, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
    (( u'URL' , u'pbstrUrl' , ), 1610743810, (1610743810, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
]

ISearchAssistantOC_vtables_dispatch_ = 1
ISearchAssistantOC_vtables_ = [
    (( u'AddNextMenuItem' , u'bstrText' , u'idItem' , ), 1, (1, (), [ (8, 1, None, None) , 
            (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
    (( u'SetDefaultSearchUrl' , u'bstrUrl' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
    (( u'NavigateToDefaultSearch' , ), 3, (3, (), [ ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
    (( u'IsRestricted' , u'bstrGuid' , u'pVal' , ), 4, (4, (), [ (8, 1, None, None) , 
            (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
    (( u'ShellFeaturesEnabled' , u'pVal' , ), 5, (5, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
    (( u'SearchAssistantDefault' , u'pVal' , ), 6, (6, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
    (( u'Searches' , u'ppid' , ), 7, (7, (), [ (16393, 10, None, "IID('{47C922A2-3DD5-11D2-BF8B-00C04FB93661}')") , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
    (( u'InWebFolder' , u'pVal' , ), 8, (8, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
    (( u'PutProperty' , u'bPerLocale' , u'bstrName' , u'bstrValue' , ), 9, (9, (), [ 
            (11, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
    (( u'GetProperty' , u'bPerLocale' , u'bstrName' , u'pbstrValue' , ), 10, (10, (), [ 
            (11, 1, None, None) , (8, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
    (( u'EventHandled' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
    (( u'ResetNextMenu' , ), 12, (12, (), [ ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
    (( u'FindOnWeb' , ), 13, (13, (), [ ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
    (( u'FindFilesOrFolders' , ), 14, (14, (), [ ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
    (( u'FindComputer' , ), 15, (15, (), [ ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
    (( u'FindPrinter' , ), 16, (16, (), [ ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
    (( u'FindPeople' , ), 17, (17, (), [ ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
    (( u'GetSearchAssistantURL' , u'bSubstitute' , u'bCustomize' , u'pbstrValue' , ), 18, (18, (), [ 
            (11, 1, None, None) , (11, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
    (( u'NotifySearchSettingsChanged' , ), 19, (19, (), [ ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
    (( u'ASProvider' , u'pProvider' , ), 20, (20, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
    (( u'ASProvider' , u'pProvider' , ), 20, (20, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
    (( u'ASSetting' , u'pSetting' , ), 21, (21, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
    (( u'ASSetting' , u'pSetting' , ), 21, (21, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
    (( u'NETDetectNextNavigate' , ), 22, (22, (), [ ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
    (( u'PutFindText' , u'FindText' , ), 23, (23, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
    (( u'Version' , u'pVersion' , ), 24, (24, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
    (( u'EncodeString' , u'bstrValue' , u'bstrCharSet' , u'bUseUTF8' , u'pbstrResult' , 
            ), 25, (25, (), [ (8, 1, None, None) , (8, 1, None, None) , (11, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
]

ISearchAssistantOC2_vtables_dispatch_ = 1
ISearchAssistantOC2_vtables_ = [
    (( u'ShowFindPrinter' , u'pbShowFindPrinter' , ), 26, (26, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

ISearchAssistantOC3_vtables_dispatch_ = 1
ISearchAssistantOC3_vtables_ = [
    (( u'SearchCompanionAvailable' , u'pbAvailable' , ), 27, (27, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
    (( u'UseSearchCompanion' , u'pbUseSC' , ), 28, (28, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
    (( u'UseSearchCompanion' , u'pbUseSC' , ), 28, (28, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
]

ISearches_vtables_dispatch_ = 1
ISearches_vtables_ = [
    (( u'Count' , u'plCount' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
    (( u'Default' , u'pbstrDefault' , ), 1610743809, (1610743809, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
    (( u'Item' , u'index' , u'ppid' , ), 1610743810, (1610743810, (), [ (12, 17, None, None) , 
            (16393, 10, None, "IID('{BA9239A4-3DD5-11D2-BF8B-00C04FB93661}')") , ], 1 , 1 , 4 , 1 , 36 , (3, 0, None, None) , 0 , )),
    (( u'_NewEnum' , u'ppunk' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
]

IShellFavoritesNameSpace_vtables_dispatch_ = 1
IShellFavoritesNameSpace_vtables_ = [
    (( u'MoveSelectionUp' , ), 1, (1, (), [ ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
    (( u'MoveSelectionDown' , ), 2, (2, (), [ ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
    (( u'ResetSort' , ), 3, (3, (), [ ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
    (( u'NewFolder' , ), 4, (4, (), [ ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
    (( u'Synchronize' , ), 5, (5, (), [ ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
    (( u'Import' , ), 6, (6, (), [ ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
    (( u'Export' , ), 7, (7, (), [ ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
    (( u'InvokeContextMenuCommand' , u'strCommand' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
    (( u'MoveSelectionTo' , ), 9, (9, (), [ ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
    (( u'SubscriptionsEnabled' , u'pBool' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
    (( u'CreateSubscriptionForSelection' , u'pBool' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
    (( u'DeleteSubscriptionForSelection' , u'pBool' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
    (( u'SetRoot' , u'bstrFullPath' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
]

IShellNameSpace_vtables_dispatch_ = 1
IShellNameSpace_vtables_ = [
    (( u'EnumOptions' , u'pgrfEnumFlags' , ), 14, (14, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
    (( u'EnumOptions' , u'pgrfEnumFlags' , ), 14, (14, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
    (( u'SelectedItem' , u'pItem' , ), 15, (15, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
    (( u'SelectedItem' , u'pItem' , ), 15, (15, (), [ (9, 1, None, None) , ], 1 , 4 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
    (( u'Root' , u'pvar' , ), 16, (16, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
    (( u'Root' , u'pvar' , ), 16, (16, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
    (( u'Depth' , u'piDepth' , ), 17, (17, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
    (( u'Depth' , u'piDepth' , ), 17, (17, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
    (( u'Mode' , u'puMode' , ), 18, (18, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
    (( u'Mode' , u'puMode' , ), 18, (18, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
    (( u'Flags' , u'pdwFlags' , ), 19, (19, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
    (( u'Flags' , u'pdwFlags' , ), 19, (19, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
    (( u'TVFlags' , u'dwFlags' , ), 20, (20, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
    (( u'TVFlags' , u'dwFlags' , ), 20, (20, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
    (( u'Columns' , u'bstrColumns' , ), 21, (21, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
    (( u'Columns' , u'bstrColumns' , ), 21, (21, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
    (( u'CountViewTypes' , u'piTypes' , ), 22, (22, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
    (( u'SetViewType' , u'iType' , ), 23, (23, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
    (( u'SelectedItems' , u'ppid' , ), 24, (24, (), [ (16393, 10, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
    (( u'Expand' , u'var' , u'iDepth' , ), 25, (25, (), [ (12, 1, None, None) , 
            (3, 0, None, None) , ], 1 , 1 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
    (( u'UnselectAll' , ), 26, (26, (), [ ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
]

IShellUIHelper_vtables_dispatch_ = 1
IShellUIHelper_vtables_ = [
    (( u'ResetFirstBootMode' , ), 1, (1, (), [ ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 64 , )),
    (( u'ResetSafeMode' , ), 2, (2, (), [ ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 64 , )),
    (( u'RefreshOfflineDesktop' , ), 3, (3, (), [ ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 64 , )),
    (( u'AddFavorite' , u'URL' , u'Title' , ), 4, (4, (), [ (8, 1, None, None) , 
            (16396, 17, None, None) , ], 1 , 1 , 4 , 1 , 40 , (3, 0, None, None) , 0 , )),
    (( u'AddChannel' , u'URL' , ), 5, (5, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
    (( u'AddDesktopComponent' , u'URL' , u'Type' , u'Left' , u'Top' , 
            u'Width' , u'Height' , ), 6, (6, (), [ (8, 1, None, None) , (8, 1, None, None) , 
            (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , ], 1 , 1 , 4 , 4 , 48 , (3, 0, None, None) , 0 , )),
    (( u'IsSubscribed' , u'URL' , u'pBool' , ), 7, (7, (), [ (8, 1, None, None) , 
            (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
    (( u'NavigateAndFind' , u'URL' , u'strQuery' , u'varTargetFrame' , ), 8, (8, (), [ 
            (8, 1, None, None) , (8, 1, None, None) , (16396, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
    (( u'ImportExportFavorites' , u'fImport' , u'strImpExpPath' , ), 9, (9, (), [ (11, 1, None, None) , 
            (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
    (( u'AutoCompleteSaveForm' , u'Form' , ), 10, (10, (), [ (16396, 17, None, None) , ], 1 , 1 , 4 , 1 , 64 , (3, 0, None, None) , 0 , )),
    (( u'AutoScan' , u'strSearch' , u'strFailureUrl' , u'pvarTargetFrame' , ), 11, (11, (), [ 
            (8, 1, None, None) , (8, 1, None, None) , (16396, 17, None, None) , ], 1 , 1 , 4 , 1 , 68 , (3, 0, None, None) , 0 , )),
    (( u'AutoCompleteAttach' , u'Reserved' , ), 12, (12, (), [ (16396, 17, None, None) , ], 1 , 1 , 4 , 1 , 72 , (3, 0, None, None) , 64 , )),
    (( u'ShowBrowserUI' , u'bstrName' , u'pvarIn' , u'pvarOut' , ), 13, (13, (), [ 
            (8, 1, None, None) , (16396, 1, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
]

IShellWindows_vtables_dispatch_ = 1
IShellWindows_vtables_ = [
    (( u'Count' , u'Count' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
    (( u'Item' , u'index' , u'Folder' , ), 0, (0, (), [ (12, 17, None, None) , 
            (16393, 10, None, None) , ], 1 , 1 , 4 , 1 , 32 , (3, 0, None, None) , 0 , )),
    (( u'_NewEnum' , u'ppunk' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
    (( u'Register' , u'pid' , u'HWND' , u'swClass' , u'plCookie' , 
            ), 1610743811, (1610743811, (), [ (9, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 64 , )),
    (( u'RegisterPending' , u'lThreadId' , u'pvarloc' , u'pvarlocRoot' , u'swClass' , 
            u'plCookie' , ), 1610743812, (1610743812, (), [ (3, 1, None, None) , (16396, 1, None, None) , (16396, 1, None, None) , 
            (3, 1, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 64 , )),
    (( u'Revoke' , u'lCookie' , ), 1610743813, (1610743813, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 64 , )),
    (( u'OnNavigate' , u'lCookie' , u'pvarloc' , ), 1610743814, (1610743814, (), [ (3, 1, None, None) , 
            (16396, 1, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 64 , )),
    (( u'OnActivated' , u'lCookie' , u'fActive' , ), 1610743815, (1610743815, (), [ (3, 1, None, None) , 
            (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 64 , )),
    (( u'FindWindowSW' , u'pvarloc' , u'pvarlocRoot' , u'swClass' , u'pHWND' , 
            u'swfwOptions' , u'ppdispOut' , ), 1610743816, (1610743816, (), [ (16396, 1, None, None) , (16396, 1, None, None) , 
            (3, 1, None, None) , (16387, 2, None, None) , (3, 1, None, None) , (16393, 10, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 64 , )),
    (( u'OnCreated' , u'lCookie' , u'punk' , ), 1610743817, (1610743817, (), [ (3, 1, None, None) , 
            (13, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 64 , )),
    (( u'ProcessAttachDetach' , u'fAttach' , ), 1610743818, (1610743818, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 64 , )),
]

IWebBrowser_vtables_dispatch_ = 1
IWebBrowser_vtables_ = [
    (( u'GoBack' , ), 100, (100, (), [ ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
    (( u'GoForward' , ), 101, (101, (), [ ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
    (( u'GoHome' , ), 102, (102, (), [ ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
    (( u'GoSearch' , ), 103, (103, (), [ ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
    (( u'Navigate' , u'URL' , u'Flags' , u'TargetFrameName' , u'PostData' , 
            u'Headers' , ), 104, (104, (), [ (8, 1, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , 
            (16396, 17, None, None) , (16396, 17, None, None) , ], 1 , 1 , 4 , 4 , 44 , (3, 0, None, None) , 0 , )),
    (( u'Refresh' , ), -550, (-550, (), [ ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
    (( u'Refresh2' , u'Level' , ), 105, (105, (), [ (16396, 17, None, None) , ], 1 , 1 , 4 , 1 , 52 , (3, 0, None, None) , 0 , )),
    (( u'Stop' , ), 106, (106, (), [ ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
    (( u'Application' , u'ppDisp' , ), 200, (200, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
    (( u'Parent' , u'ppDisp' , ), 201, (201, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
    (( u'Container' , u'ppDisp' , ), 202, (202, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
    (( u'Document' , u'ppDisp' , ), 203, (203, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
    (( u'TopLevelContainer' , u'pBool' , ), 204, (204, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
    (( u'Type' , u'Type' , ), 205, (205, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
    (( u'Left' , u'pl' , ), 206, (206, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
    (( u'Left' , u'pl' , ), 206, (206, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
    (( u'Top' , u'pl' , ), 207, (207, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
    (( u'Top' , u'pl' , ), 207, (207, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
    (( u'Width' , u'pl' , ), 208, (208, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
    (( u'Width' , u'pl' , ), 208, (208, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
    (( u'Height' , u'pl' , ), 209, (209, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
    (( u'Height' , u'pl' , ), 209, (209, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
    (( u'LocationName' , u'LocationName' , ), 210, (210, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
    (( u'LocationURL' , u'LocationURL' , ), 211, (211, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
    (( u'Busy' , u'pBool' , ), 212, (212, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
]

IWebBrowser2_vtables_dispatch_ = 1
IWebBrowser2_vtables_ = [
    (( u'Navigate2' , u'URL' , u'Flags' , u'TargetFrameName' , u'PostData' , 
            u'Headers' , ), 500, (500, (), [ (16396, 1, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , 
            (16396, 17, None, None) , (16396, 17, None, None) , ], 1 , 1 , 4 , 4 , 208 , (3, 0, None, None) , 0 , )),
    (( u'QueryStatusWB' , u'cmdID' , u'pcmdf' , ), 501, (501, (), [ (3, 1, None, None) , 
            (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 212 , (3, 0, None, None) , 0 , )),
    (( u'ExecWB' , u'cmdID' , u'cmdexecopt' , u'pvaIn' , u'pvaOut' , 
            ), 502, (502, (), [ (3, 1, None, None) , (3, 1, None, None) , (16396, 17, None, None) , (16396, 19, None, None) , ], 1 , 1 , 4 , 2 , 216 , (3, 0, None, None) , 0 , )),
    (( u'ShowBrowserBar' , u'pvaClsid' , u'pvarShow' , u'pvarSize' , ), 503, (503, (), [ 
            (16396, 1, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , ], 1 , 1 , 4 , 2 , 220 , (3, 0, None, None) , 0 , )),
    (( u'ReadyState' , u'plReadyState' , ), -525, (-525, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 4 , )),
    (( u'Offline' , u'pbOffline' , ), 550, (550, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 228 , (3, 0, None, None) , 0 , )),
    (( u'Offline' , u'pbOffline' , ), 550, (550, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
    (( u'Silent' , u'pbSilent' , ), 551, (551, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 236 , (3, 0, None, None) , 0 , )),
    (( u'Silent' , u'pbSilent' , ), 551, (551, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
    (( u'RegisterAsBrowser' , u'pbRegister' , ), 552, (552, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 244 , (3, 0, None, None) , 0 , )),
    (( u'RegisterAsBrowser' , u'pbRegister' , ), 552, (552, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
    (( u'RegisterAsDropTarget' , u'pbRegister' , ), 553, (553, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 252 , (3, 0, None, None) , 0 , )),
    (( u'RegisterAsDropTarget' , u'pbRegister' , ), 553, (553, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
    (( u'TheaterMode' , u'pbRegister' , ), 554, (554, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 260 , (3, 0, None, None) , 0 , )),
    (( u'TheaterMode' , u'pbRegister' , ), 554, (554, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
    (( u'AddressBar' , u'Value' , ), 555, (555, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 268 , (3, 0, None, None) , 0 , )),
    (( u'AddressBar' , u'Value' , ), 555, (555, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
    (( u'Resizable' , u'Value' , ), 556, (556, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 276 , (3, 0, None, None) , 0 , )),
    (( u'Resizable' , u'Value' , ), 556, (556, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
]

IWebBrowserApp_vtables_dispatch_ = 1
IWebBrowserApp_vtables_ = [
    (( u'Quit' , ), 300, (300, (), [ ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
    (( u'ClientToWindow' , u'pcx' , u'pcy' , ), 301, (301, (), [ (16387, 3, None, None) , 
            (16387, 3, None, None) , ], 1 , 1 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
    (( u'PutProperty' , u'Property' , u'vtValue' , ), 302, (302, (), [ (8, 1, None, None) , 
            (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
    (( u'GetProperty' , u'Property' , u'pvtValue' , ), 303, (303, (), [ (8, 1, None, None) , 
            (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
    (( u'Name' , u'Name' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
    (( u'HWND' , u'pHWND' , ), -515, (-515, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
    (( u'FullName' , u'FullName' , ), 400, (400, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
    (( u'Path' , u'Path' , ), 401, (401, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
    (( u'Visible' , u'pBool' , ), 402, (402, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
    (( u'Visible' , u'pBool' , ), 402, (402, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
    (( u'StatusBar' , u'pBool' , ), 403, (403, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
    (( u'StatusBar' , u'pBool' , ), 403, (403, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
    (( u'StatusText' , u'StatusText' , ), 404, (404, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
    (( u'StatusText' , u'StatusText' , ), 404, (404, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 180 , (3, 0, None, None) , 0 , )),
    (( u'ToolBar' , u'Value' , ), 405, (405, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
    (( u'ToolBar' , u'Value' , ), 405, (405, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 188 , (3, 0, None, None) , 0 , )),
    (( u'MenuBar' , u'Value' , ), 406, (406, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
    (( u'MenuBar' , u'Value' , ), 406, (406, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 196 , (3, 0, None, None) , 0 , )),
    (( u'FullScreen' , u'pbFullScreen' , ), 407, (407, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
    (( u'FullScreen' , u'pbFullScreen' , ), 407, (407, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 204 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
    '{47C922A2-3DD5-11D2-BF8B-00C04FB93661}' : ISearches,
    '{9BA05972-F6A8-11CF-A442-00A0C90A8F39}' : ShellWindows,
    '{2F2F1F96-2BC1-4B1C-BE28-EA3774F4676A}' : ShellShellNameSpace,
    '{2E71FD0F-AAB1-42C0-9146-6D2C4EDCF07D}' : ShellSearchAssistantOC,
    '{72423E8F-8011-11D2-BE79-00A0C9A83DA2}' : ISearchAssistantOC2,
    '{72423E8F-8011-11D2-BE79-00A0C9A83DA1}' : ISearchAssistantOC,
    '{EFD01300-160F-11D2-BB2E-00805FF7EFCA}' : CScriptErrorList,
    '{BA9239A4-3DD5-11D2-BF8B-00C04FB93661}' : ISearch,
    '{64AB4BB7-111E-11D1-8F79-00C04FC2FBE1}' : ShellUIHelper,
    '{1611FDDA-445B-11D2-85DE-00C04FA35C89}' : _SearchAssistantEvents,
    '{F3470F24-15FD-11D2-BB2E-00805FF7EFCA}' : IScriptErrorList,
    '{0002DF01-0000-0000-C000-000000000046}' : InternetExplorer,
    '{0002DF05-0000-0000-C000-000000000046}' : IWebBrowserApp,
    '{B45FF030-4447-11D2-85DE-00C04FA35C89}' : SearchAssistantOC,
    '{72423E8F-8011-11D2-BE79-00A0C9A83DA3}' : ISearchAssistantOC3,
    '{8856F961-340A-11D0-A96B-00C04FD705A2}' : WebBrowser,
    '{55136804-B2DE-11D1-B9F2-00A0C98BC547}' : IShellFavoritesNameSpace,
    '{55136805-B2DE-11D1-B9F2-00A0C98BC547}' : ShellNameSpace,
    '{55136806-B2DE-11D1-B9F2-00A0C98BC547}' : DShellNameSpaceEvents,
    '{FE4106E0-399A-11D0-A48C-00A0C90A8F39}' : DShellWindowsEvents,
    '{34A715A0-6587-11D0-924A-0020AFC7AC4D}' : DWebBrowserEvents2,
    '{EAB22AC1-30C1-11CF-A7EB-0000C05BAE0B}' : IWebBrowser,
    '{EAB22AC2-30C1-11CF-A7EB-0000C05BAE0B}' : DWebBrowserEvents,
    '{EAB22AC3-30C1-11CF-A7EB-0000C05BAE0B}' : WebBrowser_V1,
    '{85CB6900-4D95-11CF-960C-0080C7F4EE85}' : IShellWindows,
    '{C08AFD90-F2A1-11D1-8455-00A0C91F3880}' : ShellBrowserWindow,
    '{D30C1661-CDAF-11D0-8A3E-00C04FC9E26E}' : IWebBrowser2,
    '{729FE2F8-1EA8-11D1-8F85-00C04FC2FBE1}' : IShellUIHelper,
    '{E572D3C9-37BE-4AE2-825D-D521763E3108}' : IShellNameSpace,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
    '{72423E8F-8011-11D2-BE79-00A0C9A83DA2}' : 'ISearchAssistantOC2',
    '{55136804-B2DE-11D1-B9F2-00A0C98BC547}' : 'IShellFavoritesNameSpace',
    '{0002DF05-0000-0000-C000-000000000046}' : 'IWebBrowserApp',
    '{BA9239A4-3DD5-11D2-BF8B-00C04FB93661}' : 'ISearch',
    '{47C922A2-3DD5-11D2-BF8B-00C04FB93661}' : 'ISearches',
    '{EAB22AC1-30C1-11CF-A7EB-0000C05BAE0B}' : 'IWebBrowser',
    '{72423E8F-8011-11D2-BE79-00A0C9A83DA1}' : 'ISearchAssistantOC',
    '{85CB6900-4D95-11CF-960C-0080C7F4EE85}' : 'IShellWindows',
    '{D30C1661-CDAF-11D0-8A3E-00C04FC9E26E}' : 'IWebBrowser2',
    '{F3470F24-15FD-11D2-BB2E-00805FF7EFCA}' : 'IScriptErrorList',
    '{72423E8F-8011-11D2-BE79-00A0C9A83DA3}' : 'ISearchAssistantOC3',
    '{729FE2F8-1EA8-11D1-8F85-00C04FC2FBE1}' : 'IShellUIHelper',
    '{E572D3C9-37BE-4AE2-825D-D521763E3108}' : 'IShellNameSpace',
}


NamesToIIDMap = {
    'IShellFavoritesNameSpace' : '{55136804-B2DE-11D1-B9F2-00A0C98BC547}',
    'IScriptErrorList' : '{F3470F24-15FD-11D2-BB2E-00805FF7EFCA}',
    'ISearchAssistantOC3' : '{72423E8F-8011-11D2-BE79-00A0C9A83DA3}',
    '_SearchAssistantEvents' : '{1611FDDA-445B-11D2-85DE-00C04FA35C89}',
    'IWebBrowserApp' : '{0002DF05-0000-0000-C000-000000000046}',
    'IShellUIHelper' : '{729FE2F8-1EA8-11D1-8F85-00C04FC2FBE1}',
    'DShellWindowsEvents' : '{FE4106E0-399A-11D0-A48C-00A0C90A8F39}',
    'DWebBrowserEvents' : '{EAB22AC2-30C1-11CF-A7EB-0000C05BAE0B}',
    'IShellNameSpace' : '{E572D3C9-37BE-4AE2-825D-D521763E3108}',
    'IShellWindows' : '{85CB6900-4D95-11CF-960C-0080C7F4EE85}',
    'DWebBrowserEvents2' : '{34A715A0-6587-11D0-924A-0020AFC7AC4D}',
    'DShellNameSpaceEvents' : '{55136806-B2DE-11D1-B9F2-00A0C98BC547}',
    'ISearch' : '{BA9239A4-3DD5-11D2-BF8B-00C04FB93661}',
    'ISearches' : '{47C922A2-3DD5-11D2-BF8B-00C04FB93661}',
    'IWebBrowser' : '{EAB22AC1-30C1-11CF-A7EB-0000C05BAE0B}',
    'ISearchAssistantOC2' : '{72423E8F-8011-11D2-BE79-00A0C9A83DA2}',
    'ISearchAssistantOC' : '{72423E8F-8011-11D2-BE79-00A0C9A83DA1}',
    'IWebBrowser2' : '{D30C1661-CDAF-11D0-8A3E-00C04FC9E26E}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)

