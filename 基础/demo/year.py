# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/13 16:24
# 文件名称 ：year.py
# 开发工具 ：PyCharm

year = [89, 34, 23, 12, 65]
for index, value in enumerate(year):
    if str(value) != '0':
        year[index] = int('19' + str(value))
    else:
        year[index] = int('200' + str(value))
year.sort()
print(year)
