#!/usr/bin/python
# -*-coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/Users/echosun/duck/a.png')
GrayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
r1, thresh1 = cv2.threshold(GrayImage, 127, 255, cv2.THRESH_BINARY)
r2, thresh2 = cv2.threshold(GrayImage, 127, 255, cv2.THRESH_BINARY_INV)
r3, thresh3 = cv2.threshold(GrayImage, 127, 255, cv2.THRESH_TRUNC)
r4, thresh4 = cv2.threshold(GrayImage, 127, 255, cv2.THRESH_TOZERO)
r5, thresh5 = cv2.threshold(GrayImage, 127, 255, cv2.THRESH_TOZERO_INV)
titles = ['Gray Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [GrayImage, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
