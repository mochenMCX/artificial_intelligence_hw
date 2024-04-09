import os
from unittest import result
import cv2
import utils
import numpy as np
import matplotlib.pyplot as plt


def detect(dataPath, clf):
    """
    Please read detectData.txt to understand the format. Load the image and get
    the face images. Transfer the face images to 19 x 19 and grayscale images.
    Use clf.classify() function to detect faces. Show face detection results.
    If the result is True, draw the green box on the image. Otherwise, draw
    the red box on the image.
      Parameters:A
        dataPath: the path of detectData.txt
      Returns:
        No returns.
    """
    # Begin your code (Part 4)
    file_part = dataPath.split('/')
    part_path = '/'.join(file_part[:-1])
    with open(dataPath) as file:
      line_list = [line.rstrip() for line in file]
    line_idx = 0
    while line_idx < len(line_list):
      target_name, times = line_list[line_idx].split()
      img = cv2.imread(os.path.join(part_path, target_name), cv2.IMREAD_GRAYSCALE)
      img_show = cv2.imread(os.path.join(part_path, target_name), cv2.COLOR_GRAY2BGR)

      for i in range(1, int(times)+1):
        coord = [int(float(val)) for val in line_list[line_idx+i].split()]
        img_crop = img[coord[1]:(coord[1] + coord[3]), coord[0]:(coord[0] + coord[2])].copy()
        fin = cv2.resize(img_crop, (19, 19))
        jud = clf.classify(fin)
        if jud:
          obj = {"face":[coord[0], coord[1], coord[0]+coord[2], coord[1]+coord[3]]}
          cv2.rectangle(img_show, (obj['face'][0], obj['face'][1]), (obj['face'][2], obj['face'][3]), (0, 255, 0), 2)
        else:
          obj = {"nonface":[coord[0], coord[1], coord[0]+coord[2], coord[1]+coord[3]]}
          cv2.rectangle(img_show, (obj["nonface"][0], obj["nonface"][1]), (obj["nonface"][2], obj['nonface'][3]), (0, 0, 255), 2)
      line_idx += (int(times) + 1)
      cv2.imshow("Window", img_show)
      cv2.waitKey(0)
    
    # raise NotImplementedError("To be implemented")
    # End your code (Part 4)
