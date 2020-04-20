# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/20 16:06
# 文件名称 ：1、网络请求.py
# 开发工具 ：PyCharm

# urllib
# import urllib.request
#
# # 打开指定需要爬取的页面 通过get请求获取百度的内容网页
# response = urllib.request.urlopen('http://www.baidu.com')
# html = response.read()
# print(html)


# 通过使用urllib.request模块的post请求实现获取网页信息的内容
import urllib.parse
import urllib.request

# 将数据使用urlencode编码处理后，再使用encoding设置为utf-8编码
data = bytes(urllib.parse.urlencode({'word': "hello"}), encoding='utf8')
# 打开指定需要爬取的网页
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
html = response.read()  # 读取网页代码
print(html)  # 打印读取内容
