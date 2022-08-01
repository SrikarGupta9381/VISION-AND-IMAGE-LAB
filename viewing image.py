# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 08:32:23 2022

@author: BATCH1
"""

from skimage import io
img = io.imread('C:/Users/batch1/Desktop/vision and image/21MID0004_2.JPG')
io.imshow(img)


#three ways to visualize the image(skimage, pyplot, opencv)
from matplotlib import pyplot as plt  #using pyplot (can control the visual display(size of the image))
plt.imshow(img)
plt.imshow(img, cmap="hot")  # Cmap tell us in what color we need to show the image

#cmap is applied to the grey scale image, convey the message in easy way

img_gray=io.imread('C:/Users/batch1/Desktop/vision and image/21MID0004_2.JPG', as_gray=True) #if True is not given then the image is of unsigned integer

plt.imshow(img_gray, cmap="hot")
plt.imshow(img_gray, cmap="jet")

plt.imshow(img_gray, cmap="Blues")