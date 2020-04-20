# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/20 14:39
# 文件名称 ：2、基本使用.py
# 开发工具 ：PyCharm

# 制作一个跳跃小球游戏

import sys  # 导入sys模块
import pygame  # 导入pygame模块

pygame.init()  # 初始化pygame
size = width, height = 640, 480  # 设置窗口
screen = pygame.display.set_mode(size)  # 显示窗口
color = (0,0,0)  # 设置颜色

ball = pygame.image.load("ball.png")  # 加载图片
ballrect = ball.get_rect()  # 获取矩形区域

speed=[5,5]  # 设置移动的x，y轴
clock = pygame.time.Clock()  # 设置时钟

# 执行死循环，确保窗口一致显示
while True:
    clock.tick(60)
    # 检查事件
    for event in pygame.event.get():
        if event.type==pygame.QUIT:  # 如果单击关闭窗口
            sys.exit()


    ballrect=ballrect.move(speed)  # 移动小球
    if ballrect.left<0 or ballrect.right>width:
        speed[0]=-speed[0]
    if ballrect.top<0 or ballrect.bottom>height:
        speed[1]=-speed[1]

    screen.fill(color)  # 填充颜色
    screen.blit(ball,ballrect)  # 将图片滑窗口上
    pygame.display.flip()   # 更新全部显示
pygame.quit()


"""
上述代码中 添加了轮询事件检测 pygame.event.get()方法能够获取事件队列
使用for...in...语句遍历事件 然后根据type属性判断事件类型
"""
