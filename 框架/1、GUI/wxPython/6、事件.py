# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/20 13:14
# 文件名称 ：6、事件.py
# 开发工具 ：PyCharm

import wx


# 事件 用户执行的动作叫做事件 event 比如单击按钮 就是一个单击事件

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title='创建TextCtr类', size=(400, 300))
        # 创建面板
        panel = wx.Panel(self)
        # 创建文本和输入框
        self.title = wx.StaticText(panel, label='请输入用户名和密码')
        self.label_user = wx.StaticText(panel, label='用户名:')
        self.text_user = wx.TextCtrl(panel, style=wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel, label='密  码:')
        self.text_pwd = wx.TextCtrl(panel, style=wx.TE_PASSWORD)

        # 创建按钮
        self.bt_commit = wx.Button(panel, label='确定')
        self.bt_commit.Bind(wx.EVT_BUTTON, self.OnclickSubmit)
        self.bt_cancel = wx.Button(panel, label='取消')

        # 添加容器 容器中的控件横向排列
        hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_user.Add(self.label_user, proportion=0, flag=wx.ALL, border=5)
        hsizer_user.Add(self.text_user, proportion=1, flag=wx.ALL, border=5)
        hsizer_pwd = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_pwd.Add(self.label_pwd, proportion=0, flag=wx.ALL, border=5)
        hsizer_pwd.Add(self.text_pwd, proportion=1, flag=wx.ALL, border=5)
        hsizer_btn = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_btn.Add(self.bt_commit, proportion=0, flag=wx.ALIGN_CENTER, border=5)
        hsizer_btn.Add(self.bt_cancel, proportion=0, flag=wx.ALIGN_CENTER, border=5)

        # 添加容器 容器中控件纵向排列
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.title, proportion=0, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER, border=15)
        vsizer_all.Add(hsizer_user, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)
        vsizer_all.Add(hsizer_pwd, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)
        vsizer_all.Add(hsizer_btn, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=15)
        panel.SetSizer(vsizer_all)

    def OnclickSubmit(self, event):
        """
        单击确定按钮，执行方法
        :param event:
        :return:
        """
        username = self.text_user.GetValue()  # 获取用户名
        password = self.text_pwd.GetValue()  # 获取密码
        if username == "" or password == "":
            wx.MessageBox("用户名或密码不能为空")
        elif username == 'admin' and password == '123':
            wx.MessageBox("登录成功")
        else:
            wx.MessageBox("用户名或密码不匹配")


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)  # 实例化并传参
    frame.Show()
    app.MainLoop()

