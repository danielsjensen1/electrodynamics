import wx
from matplotlib.patches import FancyArrow
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
import numpy as np


class MplCanvasFrame(wx.Frame):
    def __init__(self, xlims=(-10e0, 10e0)):
        wx.Frame.__init__(self, None, wx.ID_ANY, title="Spherical Mirrors",
                          size=(640, 480))
        #  Usual Matplotlib functions
        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        #  Plot the mirror and optical axes
        self.mirror()
        self.ax.axhline(y=0, xmin=0, xmax=1, color='grey')
        self.ax.set_xlim(xlims)
        #  Initialize the FigureCanvas, mapping the figure to the Wx backend
        self.canvas=FigureCanvas(self, wx.ID_ANY, self.fig)
        #  Create a BoxSizer for windows layout
        self.sizer=wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT|wx.TOP|wx.EXPAND)
        #  Create the navigation toolbar
        self.toolbar=NavigationToolbar2Wx(self.canvas)
        self.toolbar.Realize()
        self.sizer.Add(self.toolbar, 0, wx.LEFT|wx.EXPAND)
        self.toolbar.Show()
        #  Set the layout sizer
        self.SetSizer(self.sizer)
        self.Fit()

    def mirror(self, R=5e0, theta=np.radians(45e0), numpts=100):
        theta=np.linspace(-theta, theta, numpts)
        x=R*np.cos(theta)-R
        y=R*np.sin(theta)
        self.ax.plot(x, y, color='blue')
        self.f=R/2e0
        self.ax.plot((-self.f,), (0e0,), ls='None', marker='.',
                     color='blue')

    def objimg(self, so=6e0, ho=2e0):
        object=FancyArrow(-so, 0e0, 0e0, ho, length_includes_head=True,
                            width=abs(ho)/10e0, head_width=abs(ho)/3e0,
                            head_length=abs(ho)/3e0, color='red')
        self.ax.add_patch(object)
        si=1/(1e0/self.f-1/so)
        hi=-si/so*ho
        print('hi=', hi, 'si=', si)
        image=FancyArrow(-si, 0e0, 0e0, hi, length_includes_head=True,
                            width=abs(hi)/10e0, head_width=abs(hi)/3e0,
                            head_length=abs(hi)/3e0, color='grey')
        self.ax.add_patch(image)

class MplApp(wx.App):
    def OnInit(self):
        frame=MplCanvasFrame()
        frame.objimg()
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

if __name__=='__main__':
    mplapp=MplApp(False)
    mplapp.MainLoop()
