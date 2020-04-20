# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/20 9:06
# 文件名称 ：1、wxPython.py
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
# import wx
# app = wx.App()
# frame = wx.Frame(None,title = "Hello wxPython")
# frame.Show()
# app.MainLoop()


# 使用wx.Frame框架
# wx.Frame是所有框架的父类 当创建wx.Frame的子类时 子类应该调用其父类的构造器wx.Frame.__init__()
# import wx
# class MyFrame(wx.Frame):
#     def __init__(self,parent,id):
#         wx.Frame.__init__(self,parent,id,title="创建Frame",pos=(100,100),size=(300,300))

# if __name__ == "__main__":
#     app = wx.App()  # 初始化应用
#     frame=MyFrame(parent=None,id=-1)  # 实例化并传参
#     frame.Show()  # 显示窗口
#     app.MainLoop()  # 调用主循环方法


# StaticText文本类
# import wx
# class MyFrame(wx.Frame):
#     def __init__(self, parent, id):
#         wx.Frame.__init__(self, parent, id, title="创建StaticText类", pos=(100, 100), size=(400, 250))
#         panel = wx.Panel(self)  # 创建画板
#         # 创建标题 设置字体
#         title = wx.StaticText(panel, label='Python之禅', pos=(100, 20))
#         font = wx.Font(16, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
#         title.SetFont(font)
#         # 创建文本
#         wx.StaticText(panel, label='优美胜于丑陋', pos=(50, 50))
#         wx.StaticText(panel, label='明了胜于隐晦', pos=(50, 70))
#         wx.StaticText(panel, label='简洁胜于复杂', pos=(50, 90))
#         wx.StaticText(panel, label='复杂胜于凌乱', pos=(50, 110))
#         wx.StaticText(panel, label='扁平胜于嵌套', pos=(50, 130))
#         wx.StaticText(panel, label='间隔胜于紧凑', pos=(50, 150))
#         wx.StaticText(panel, label='可读性很重要', pos=(50, 170))
#
# if __name__ == "__main__":
#     app = wx.App()  # 初始化应用
#     frame = MyFrame(parent=None, id=-1)  # 实例化并传参
#     frame.Show()  # 显示窗口
#     app.MainLoop()  # 调用主循环方法


# TextCtrl 输入文本类 Button按钮类
import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title='创建TextCtr类', size=(400, 300))
        # 创建面板
        panel = wx.Panel(self)
        # 创建文本和输入框
        self.title = wx.StaticText(panel, label='请输入用户名和密码', pos=(140, 20))
        self.label_user = wx.StaticText(panel, label='用户名:', pos=(50, 50))
        self.text_user = wx.TextCtrl(panel, pos=(100, 50), size=(235, 25), style=wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel, label='密  码:', pos=(50, 90))
        self.text_pwd = wx.TextCtrl(panel, pos=(100, 90), size=(235, 25), style=wx.TE_PASSWORD)

        # 创建按钮
        self.bt_commit = wx.Button(panel,label = '确定',pos = (105,130))
        self.bt_cancle = wx.Button(panel,label = '取消',pos = (195,130))

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)  # 实例化并传参
    frame.Show()
    app.MainLoop()

"""

"""