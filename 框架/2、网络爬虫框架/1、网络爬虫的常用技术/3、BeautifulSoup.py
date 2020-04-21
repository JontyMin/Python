# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/21 10:21
# 文件名称 ：3、BeautifulSoup.py
# 开发工具 ：PyCharm

# BeautifulSoup 用于提取html/xml中的数据
from bs4 import BeautifulSoup
html_doc ="""
<html>
<head>
<title>
The Dormouse's story
</title>
</head>
<body>
<a href="https://www.baidu.com">百度</a>
</body>
</html>
"""

# 创建beautifulSoup对象 获取页面正文
soup = BeautifulSoup(html_doc,features='lxml')
print(soup)

# 可以通过打开html文件的方式进行解析
soup = BeautifulSoup(open('index.html'),'lxml')
print(soup.prettify())