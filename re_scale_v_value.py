import os
import cv2
import pandas as pd
import matplotlib.pyplot as plt
from imageFunc import ImageClass

img_dir = 'D:\\Data\\Learning\\ImageStatistic\\SeparateImageFaceIssue\\9 10\\fail'
csv_dir = 'D:\\Data\\Learning\\ImageStatistic\\ScaleImage140'


for file_name in os.listdir(img_dir):
  file_path = img_dir + '\\' + file_name
  
  image = cv2.imread(file_path)
  image_func = ImageClass(file_path, file_name, image, 300)
  image_func.setHsvImage()
  image_func.setHsv()
  print('AverageV: ' + str(image_func.averageV))
  
  maxV = 140
  offset = maxV - round(image_func.averageV)
  image_func.reScaleV(maxV, offset)
  
  rgbimg = cv2.cvtColor(image_func.hsvImage, cv2.COLOR_HSV2BGR)
  
  if os.path.exists(csv_dir) == False:
    os.mkdir(csv_dir)
  os.chdir(csv_dir)
  cv2.imwrite(file_name, rgbimg)
  print('Save image: ' + file_name)