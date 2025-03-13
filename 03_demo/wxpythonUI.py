#!/usr/bin/env python

# This code is under BSD 2-clause license

from wxpythonDemoGenerated import *
import wx
import random

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


class DrawingFrame(Designed_DrawingFrame):
    def __init__(self,parent=None):
        Designed_DrawingFrame.__init__(self,parent)
    def OnPanelPaint(self,event):
        window = self.m_drawingPanel
        dc = wx.PaintDC(window)
        #dc.BeginDrawing()

        #self.DrawCornerLines(dc)
        self.DrawChessTable(dc)
        self.DrawRandomCircles(dc)

        #dc.EndDrawing()

    def DrawCornerLines(self,dc):
        (w,h) = dc.GetSize()
        xstep = w//30
        if w < 2*xstep or h <= 0:
            return
        
        xstart = 0
        xend = w-1
        x = xstart
        while x <= xend:
            dc.DrawLine(0,0,x,h-1)
            dc.DrawLine(w-1,0,x,h-1)
            x+= xstep

    def DrawChessTable(self,dc):
        (w,h) = dc.GetSize()
        space = 10
        xwidth = (w-2*space)//8
        ywidth = (h-2*space)//8

        if xwidth <= 0 or ywidth <= 0:
            return

        squareSize = ywidth
        if xwidth < ywidth:
            squareSize = xwidth
        
        xstart = (w - squareSize*8) // 2
        xend = xstart + 8*squareSize
        ystart = (h - squareSize*8) // 2
        yend = ystart + 8*squareSize

        for xindex in range(9):
            x = xstart + xindex*squareSize  
            dc.DrawLine(x,ystart,x,yend)

        for yindex in range(9):
            y = ystart + yindex*squareSize
            dc.DrawLine(xstart,y,xend,y)

        #whiteColor = wx.Colour(255,255,255)
        #blackColor = wx.Colour(0,0,0)

        whiteColor = wx.Colour(160,82,45)
        blackColor = wx.Colour(255,228,181)

        colors = [ whiteColor, blackColor ]

        for xindex in range(8):
            x = xstart + xindex*squareSize  
            for yindex in range(8):
                y = ystart + yindex*squareSize
                col = colors[(xindex+yindex) % 2]
                dc.SetBrush(wx.Brush(col))
                dc.DrawRectangle(x,y,squareSize,squareSize)

    def DrawRandomCircles(self,dc):
        (w,h) = dc.GetSize()

        numberOfCircles = 1000
        for numCircle in range(numberOfCircles):
            centerx = random.randint(0,w)
            centery = random.randint(0,h)
            radius = random.randint(5,min(w,h)/10)
            red = random.randint(80,255)
            green = random.randint(80,255)
            blue = random.randint(80,255)
            color = wx.Colour(red,green,blue)
            dc.SetBrush(wx.Brush(color))
            dc.DrawCircle(centerx,centery,radius)

app = wx.PySimpleApp()

frame = wxPythonDemoFrame()
#frame = DrawingFrame()

frame.Show()
app.MainLoop()

