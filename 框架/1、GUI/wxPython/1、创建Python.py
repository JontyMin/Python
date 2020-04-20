# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/20 13:07
# 文件名称 ：1、创建Python.py
# 开发工具 ：PyCharm

# 安装wxPython pip install -U wxPython
# import wx  # 导入wxPython
# class App(wx.App):
#     # 初始化这个方法
#     def OnInit(self):
#         frame = wx.Frame(parent=None,title="Hello wxPython")  # 创建窗口
#         frame.Show()  # 显示窗口
#         return True
#
# if __name__ =='__main__':
#     app = App()
#     app.MainLoop()  # 调用App类的MainLoop()主循环方法

"""
如果系统中只有一个窗体的话 可以不用创建子类 直接使用wx.app
"""
import wx
app = wx.App()
frame = wx.Frame(None,title = "Hello wxPython")
frame.Show()
app.MainLoop()