# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/20 14:32
# 文件名称 ：1、初识pygame.py
# 开发工具 ：PyCharm

# pygame 是跨平台的Python模块 专为电子游戏设计 包含图像，声音
# 安装pygame  pip install pygame

# 示例
import sys
import pygame

pygame.init()   # 初始化pygame
size = width,height = 320,240   # 设置窗口
screen = pygame.display.set_mode(size)  # 显示窗口

# 执行死循环 确保窗口一直显示
while True:
    # 检查事件
    for event in pygame.event.get():  # 遍历所有事件
        if event.type==pygame.QUIT:   # 如果单击关闭窗体 则退出
            sys.exit()

pygame.quit()   # 退出pygame