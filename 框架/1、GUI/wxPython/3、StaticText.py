# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/20 13:09
# 文件名称 ：3、StaticText.py
# 开发工具 ：PyCharm

# StaticText文本类
import wx
class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title="创建StaticText类", pos=(100, 100), size=(400, 250))
        panel = wx.Panel(self)  # 创建画板
        # 创建标题 设置字体
        title = wx.StaticText(panel, label='Python之禅', pos=(100, 20))
        font = wx.Font(16, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        title.SetFont(font)
        # 创建文本
        wx.StaticText(panel, label='优美胜于丑陋', pos=(50, 50))
        wx.StaticText(panel, label='明了胜于隐晦', pos=(50, 70))
        wx.StaticText(panel, label='简洁胜于复杂', pos=(50, 90))
        wx.StaticText(panel, label='复杂胜于凌乱', pos=(50, 110))
        wx.StaticText(panel, label='扁平胜于嵌套', pos=(50, 130))
        wx.StaticText(panel, label='间隔胜于紧凑', pos=(50, 150))
        wx.StaticText(panel, label='可读性很重要', pos=(50, 170))

if __name__ == "__main__":
    app = wx.App()  # 初始化应用
    frame = MyFrame(parent=None, id=-1)  # 实例化并传参
    frame.Show()  # 显示窗口
    app.MainLoop()  # 调用主循环方法