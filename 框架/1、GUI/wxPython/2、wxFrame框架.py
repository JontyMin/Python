# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/20 13:08
# 文件名称 ：2、wxFrame框架.py
# 开发工具 ：PyCharm

# 使用wx.Frame框架
# wx.Frame是所有框架的父类 当创建wx.Frame的子类时 子类应该调用其父类的构造器wx.Frame.__init__()
import wx
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title="创建Frame",pos=(100,100),size=(300,300))

if __name__ == "__main__":
    app = wx.App()  # 初始化应用
    frame=MyFrame(parent=None,id=-1)  # 实例化并传参
    frame.Show()  # 显示窗口
    app.MainLoop()  # 调用主循环方法