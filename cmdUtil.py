#!/usr/bin/python
# -*-coding: utf-8 -*-

import os
import time
import subprocess

imgFolder = '/Users/echosun/duck/WechatGameTemp/'
getImgCmd = 'adb shell /system/bin/screencap -p > ' + imgFolder


def get_tempimg():
    temp_img_name = time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.png'
    os.system(getImgCmd + temp_img_name)
    print(getImgCmd + temp_img_name)
    return temp_img_name


def device_exist():
    print("===Sta===")
    if os.system('adb devices') != 0:
        Exception("Error!")
        print("ADB Not Found!")
        exit()
    print("===End===")
    device_list = os.popen('adb devices')
    x = device_list.readlines()
    for line in x:
        if line.index('device') > 0:
            return True
    return False


# tap <x> <y> (Default: touchscreen)
def screen_tap(x, y):
    os.system('adb shell input tap ' + str(x) + ' ' + str(y))


# swipe <x1> <y1> <x2> <y2> [duration(ms)] (Default: touchscreen)
def screen_swipe(x, y, ms):
    os.system('adb shell input swipe ' + str(x) + ' ' + str(y) + ' ' + str(x) + ' ' + str(y) + str(ms))


if __name__ == '__main__':
    if device_exist():
        screen_tap(609, 1554)
        time.sleep(1)
        screen_swipe(609, 1554, 1)
    print(123)
    # print(device_exist())
    # print(get_tempimg())
