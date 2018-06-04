import wx

app=wx.App(True)#可带参数，为true将输出和错误重新定向到窗口和false为控制台，默认为false


#每个wxpython的程序必须有一个wx.app对象。
frame=wx.Frame(None,-1,title='hello world',pos=(100,0),size=(1000,800))
#frame.Centre()
frame.Show()


#进入循环,等待响应
app.MainLoop()
