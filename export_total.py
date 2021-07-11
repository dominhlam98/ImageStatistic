from imageFunc import Image
from summaryFunc import SummaryImage
from export import export_csv_image
import cv2
import os
import pandas as pd

separate_img_dir = 'D:\\Data\\Learning\\ImageStatistic\\separate_image_test'
csv_dir = 'D:\\Data\\Learning\\ImageStatistic\\CSV'

if os.path.exists(csv_dir) == False:
  os.mkdir(csv_dir)

for subdir in os.listdir(separate_img_dir):
  separate_path = separate_img_dir + '\\' + subdir
  sum_reg = sum_success = sum_fail = 0
  
  csv_path = csv_dir + '\\' + subdir
  if os.path.exists(csv_path) == False:
    os.mkdir(csv_path)

  for subdir1 in os.listdir(separate_path):
    img_dir = separate_path + '\\' + subdir1
    export_csv_image(img_dir, csv_path, subdir1, subdir1)

    


