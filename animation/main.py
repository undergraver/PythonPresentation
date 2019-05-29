from generated.IdleProject import *
import wx

class MainFrame(MyFrame1):
    def __init__(self,parent=None):
        self.counter = 1
        return super().__init__(parent)

    def OnIdle( self, event ):
        print("OnIdle {}".format(self.counter))
        self.counter += 1
        per = 2000
        modRes = self.counter % per

        dc = wx.ClientDC(self.m_panel)
        dc.Clear()
        w,h = dc.GetSize()

        xpos = w / 2
        radius = 10
        ypos = radius +  h * modRes / per
        dc.DrawCircle(xpos,ypos,radius)

        event.RequestMore()


class MyApp(wx.App):
    def __init__(self):
        super().__init__()
        wx.IdleEvent.SetMode(wx.IDLE_PROCESS_SPECIFIED)
    def OnInit(self):
        return True


if __name__=="__main__":
    app = MyApp()
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
