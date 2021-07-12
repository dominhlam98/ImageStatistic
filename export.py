from export_func import export_csv_image
import cv2
import os
import pandas as pd

img_dir = 'D:\\Data\\Learning\\ImageStatistic\\separate_image_test\\bf88a72c-fe72-4550-a8c2-6ccad831727c ### 9de53fe2-2591-496e-b5ba-a9c894381ea7 (man)\\success'
csv_dir = 'D:\\Data\\Learning\\ImageStatistic\\CSVA'
    
# Uncomment this line, img_dir is img directory, csv_dir is destination csv directory, "ea1a2c91-f485-4eab-9ddf-2c56249393ca" is csv name, "success" is extra name
export_csv_image(img_dir, csv_dir, "ea1a2c91-f485-4eab-9ddf-2c56249393ca", "success")