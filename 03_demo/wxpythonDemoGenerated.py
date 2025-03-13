# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class Designed_wxPythonDemoFrame
###########################################################################

class Designed_wxPythonDemoFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Hi, I'm wxPython!"), pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        m_listBoxChoices = [ _(u"Choice0"), _(u"Choice1"), _(u"Choice2"), _(u"Choice3"), _(u"Choice4"), _(u"Choice5"), _(u"Choice6"), _(u"Choice7"), _(u"Choice8"), _(u"Choice9"), _(u"Choice10"), _(u"Choice11") ]
        self.m_listBox = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBoxChoices, 0 )
        bSizer2.Add( self.m_listBox, 1, wx.ALL|wx.EXPAND, 5 )

        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button2 = wx.Button( self, wx.ID_ANY, _(u"<"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_button2, 0, wx.ALL, 5 )

        self.m_gauge = wx.Gauge( self, wx.ID_ANY, 11, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        self.m_gauge.SetValue( 6 )
        bSizer4.Add( self.m_gauge, 1, wx.ALL, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, _(u">"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_button3, 0, wx.ALL, 5 )


        bSizer2.Add( bSizer4, 0, wx.EXPAND, 5 )


        bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, _(u"Close"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_button1, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_listBox.Bind( wx.EVT_LISTBOX, self.OnListBox )
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnButttonLeft )
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnButtonRight )
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnCloseButtonClick )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnListBox( self, event ):
        event.Skip()

    def OnButttonLeft( self, event ):
        event.Skip()

    def OnButtonRight( self, event ):
        event.Skip()

    def OnCloseButtonClick( self, event ):
        event.Skip()


###########################################################################
## Class Designed_DrawingFrame
###########################################################################

class Designed_DrawingFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        self.m_drawingPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5.Add( self.m_drawingPanel, 1, wx.EXPAND |wx.ALL, 0 )


        self.SetSizer( bSizer5 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_SIZE, self.OnChangedSize )
        self.m_drawingPanel.Bind( wx.EVT_PAINT, self.OnPanelPaint )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnChangedSize( self, event ):
        event.Skip()

    def OnPanelPaint( self, event ):
        event.Skip()


