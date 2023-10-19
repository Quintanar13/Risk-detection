#SVM for weapon detection

import os
import numpy
import cv2
import matplotlib as plt

dir = 'Dataset_post/test'

categories = ['cats','dogs']

for category in categories:
    path = os.path.join(dir,category)

    for img in os.listdir(path):
        imgpath = os.path.join(path,img)
        w_img = cv2.imread(imgpath,0)