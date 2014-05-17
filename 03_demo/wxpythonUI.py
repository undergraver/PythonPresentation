#!/usr/bin/env python

# This code is under BSD 2-clause license

from wxpythonDemoGenerated import *
import wx

class wxPythonDemoFrame(Designed_wxPythonDemoFrame):
    def __init__(self,parent=None):
        Designed_wxPythonDemoFrame.__init__(self,parent)
        self.m_listBox.Select(5)

    def OnListBox( self, event ):
        position = self.m_listBox.GetSelection()
        self.m_gauge.SetValue(position)

    def OnCloseButtonClick( self, event ):
        self.Close()

    def OnButttonLeft( self, event ):
        position = self.m_gauge.GetValue()
        if position > 0:
            position = position - 1
            self.m_gauge.SetValue(position)
            self.m_listBox.Select(position)
    
    def OnButtonRight( self, event ):
        position = self.m_gauge.GetValue()
        if position < self.m_gauge.GetRange():
            position = position + 1
            self.m_gauge.SetValue(position)
            self.m_listBox.Select(position)


app = wx.PySimpleApp()
frame = wxPythonDemoFrame()
frame.Show()
app.MainLoop()
