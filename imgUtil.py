#!/usr/bin/python
# -*-coding: utf-8 -*-
from matplotlib import pyplot as plt
import cv2


def on_press(event):
    if event.inaxes is None:
        print("none")
        return
    # 在鼠标的当前位置绘制一个点
    ax.scatter(event.xdata, event.ydata)
    # 更新画板
    fig.canvas.draw()


if __name__ == "__main__":
    fileN = '/Users/echosun/duck/a.png'
    img = cv2.imread(fileN)
    cv2.imshow('img', img)
    fig = plt.figure()
    fig.canvas.mpl_connect("button_press_event", on_press)
    ax = fig.add_subplot(121)
    ax1 = fig.add_subplot(122)
    ax.imshow(img)
    ax1.imshow(img)
    plt.axis("off")
    plt.show()
