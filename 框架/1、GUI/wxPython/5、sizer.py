# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/20 13:11
# 文件名称 ：5、sizer.py
# 开发工具 ：PyCharm

"""
控件的几何位置时固定的 绝对位置 当窗口调整时 界面会变得不美观
wxPython中——sizer 尺寸器
sizer时用于自动布局一组窗口控件的算法

BoxSizer 在一条水平或垂直线上的窗口部件的布局 当尺寸改变时
控制窗口部件的行为很灵活 常用于嵌套的样式
"""

import wx
class MyFrame(wx.Frame):
    def __init__(self, parent: object, id: object) -> object:
        wx.Frame.__init__(self,parent,id,'用户登录',size=(400,300))
        # 创建面板
        panel = wx.Panel(self)
        self.title = wx.StaticText(panel,label="请输入用户名和密码")
        # 添加容器 纵向排列
        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.title,proportion=0,flag=wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER,border = 15)
        panel.SetSizer(vsizer)

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None ,id = -1)
    frame.Show()
    app.MainLoop()
