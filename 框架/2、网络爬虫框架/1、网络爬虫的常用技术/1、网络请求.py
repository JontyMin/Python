# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/20 16:06
# 文件名称 ：1、网络请求.py
# 开发工具 ：PyCharm

# urllib
import urllib.request

# 打开指定需要爬取的页面 通过get请求获取百度的内容网页
response = urllib.request.urlopen('http://www.baidu.com')
html = response.read()
print(html)


# 通过使用urllib.request模块的post请求实现获取网页信息的内容
import urllib.parse
import urllib.request

# 将数据使用urlencode编码处理后，再使用encoding设置为utf-8编码
data = bytes(urllib.parse.urlencode({'word': "hello"}), encoding='utf8')
# 打开指定需要爬取的网页
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
html = response.read()  # 读取网页代码
print(html)  # 打印读取内容


"""
urllib3
线程安全
连接池s
客户端SSL/TLS验证
使用多部分编码上传文件
Helpers用于重试请求并处理HTTP重定向
支持gzip和delate编码
支持 HTTP和SOCKS代理
100%测试覆盖率
"""

import urllib3

# 创建PoolManager对象 用于处理与线程池的连接以及线程安全的所有细节
http = urllib3.PoolManager()
# 对需要爬取的网页发送请求
# response = http.request('GET','https://www.baidu.com')

# post请求
response = http.request('post','http://httpbin.org/post',fields={'word':'hello'})
print(response.data)

# requests
import requests

# get请求
response = requests.get('http://www.baidu.com')
print(response.status_code)  # 打印状态码
print(response.url)  # 打印请求url
print(response.headers)  # 打印头部信息
print(response.cookies)  # 打印cookie信息
print(response.text)   # 文本形式打印源码
print(response.content)  # 字节流形式打印源码

# post请求
data = {'hello':'world'}  # 表单参数
# 对需要爬取的网页发送请求
response = requests.post('http://httpbin.org/post',data=data)
print(response.content)

"""
requests提供了多种网络请求方式
request.put()       # put请求
request.delete()    # delete请求
request.head()      # head请求
request.options()   # options请求
"""

# 如果参数是跟在?后面的 requests模块提供了传递参数的方法 允许使用params关键字传参
# 以一个字符串字典来提供这些参数

import requests

payload = {'key1':'value1','key2':'value2'}
# 对需要进行爬取的网页发送请求
response = requests.get('http://httpbin.org/get',params=payload)
print(response.content)
