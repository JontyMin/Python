# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/20 13:10
# 文件名称 ：4、TextCtrl.py
# 开发工具 ：PyCharm

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
