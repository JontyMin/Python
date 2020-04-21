# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/21 9:34
# 文件名称 ：2、请求headers处理.py
# 开发工具 ：PyCharm


# 有时候在请求网页时 发现无论是get还是post请求以及其他请求方式
# 都会出现403错误 这种情况是由于服务器拒绝了我们的访问
# 这是网页为了防止恶意采集数据 设置的反爬虫
# 这个时候就需要模拟 浏览器头部信息来进行访问

import requests
url = 'https://www.baidu.com'
headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
response = requests.get(url,headers)
print(response.content)

# 网络超时
import requests

# 循环发送50次请求
for a in range(1,50):
    try:
        # 设置超时为0.5秒
        response = requests.get('https://www.baidu.com',timeout=0.5)  # 0.5秒内未作出响应则超时
        print(response.status_code)
    except Exception as e:
        print('异常'+str(2))

import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException

for a in range(1,50):
    try:
        response = requests.get('https://www.baidu.com/',timeout=0.5)
        print(response.status_code)
    except ReadTimeout:
        print('timeout')
    except HTTPError:
        print('HttpError')
    except RequestException:
        print('reqerror')


# 代理服务
# 在爬取网页的过程中 经常会出现不久前可以爬取的网页现在无法爬取了
# 这是因为IP被爬取网站的服务器所屏蔽了 此时可以使用代理服务
import requests
proxy = {'http':'122.114.31.177:808','https':'122.114.31.177:808'}  # 设置代理IP
# 对需要爬取的网页发送请求
response = requests.get('http://www.mingrisoft.com',proxy)
print(response.content)
