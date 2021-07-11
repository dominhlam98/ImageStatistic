from imageFunc import ImageClass
from summaryFunc import SummaryImage
import cv2
import os
import pandas as pd

img_dir = 'D:\\Data\\Learning\\ImageStatistic\\separate_image\\bf88a72c-fe72-4550-a8c2-6ccad831727c ### 9de53fe2-2591-496e-b5ba-a9c894381ea7 (man)\\2.success'
csv_dir = 'D:\\Data\\Learning\\ImageStatistic\\CSV'
csv_name = "csv1"

def export_image_array(csv_dir, cal_brightness_value_name, imageArray, column, image_status):
  image_csv_dir = csv_dir + '\\' + cal_brightness_value_name
  if os.path.exists(image_csv_dir) == False:
    os.mkdir(image_csv_dir)
    
  rowArray = []
  rowCnt = 0
  for imageEl in imageArray:
    rowCnt += 1
    row = imageEl.getRow(rowCnt, imageEl.filename, image_status)
    rowArray.append(row)
    
    img = cv2.imread(imageEl.filedir)
    image_file_name = str(rowCnt) + '_' + imageEl.filename
    os.chdir(image_csv_dir)
    cv2.imwrite(image_file_name, img)
    print('Save image: ' + image_file_name)
    
  os.chdir(csv_dir)
  excel = pd.DataFrame(rowArray, columns= column)
  excel.to_csv(cal_brightness_value_name, index=False, na_rep='')

def export_csv_image(img_dir=img_dir, csv_dir=csv_dir, csv_name=csv_name, image_status=''):
  if os.path.exists(csv_dir) == False:
    os.mkdir(csv_dir)

  column = ['No.', 'File name', 'Image Status', 'Min H', 'Max H', 'Sum H', 'Average H',
                                        'Min S', 'Max S', 'Sum S', 'Average S',
                                        'Min V', 'Max V', 'Sum V', 'Average V',
                                        'L From LAB', 'Luminance', 'Way 1', 'Way 2', 'Way 3', 'Way 4', 'Way 5',
                                        'Min R', 'Max R', 'Sum R', 'Average R',
                                        'Min G', 'Max G', 'Sum G', 'Average G',
                                        'Min B', 'Max B', 'Sum B', 'Average B', ]

  count = 0
  imageArray = []
  for filename in os.listdir(img_dir):
    path = img_dir + '\\' + filename
    count += 1
    
    image = cv2.imread(path)
    
    imageFunc = ImageClass(path, filename, image, 300)
    imageFunc.setRgb()
    imageFunc.setHsvImage()
    imageFunc.setHsv()
    imageFunc.calLFromLAB()
    imageFunc.calLuminance()
    imageFunc.calWay1()
    imageFunc.calWay2()
    imageFunc.calWay3()
    imageFunc.calWay4()
    imageFunc.calWay5()
    
    imageArray.append(imageFunc)
    print('Extract: ' + str(count) + ' images')
    
  imageArray.sort(key=lambda x: x.averageV, reverse=True)
  export_image_array(csv_dir, 'averageV', imageArray, column, image_status)
  
  imageArray.sort(key=lambda x: x.lfromLAB, reverse=True)
  export_image_array(csv_dir, 'lfromLAB', imageArray, column, image_status)
  
  imageArray.sort(key=lambda x: x.luminance, reverse=True)
  export_image_array(csv_dir, 'luminance', imageArray, column, image_status)
  
  imageArray.sort(key=lambda x: x.way1, reverse=True)
  export_image_array(csv_dir, 'way1', imageArray, column, image_status)
  
  imageArray.sort(key=lambda x: x.way2, reverse=True)
  export_image_array(csv_dir, 'way2', imageArray, column, image_status)
  
  imageArray.sort(key=lambda x: x.way3, reverse=True)
  export_image_array(csv_dir, 'way3', imageArray, column, image_status)
  
  imageArray.sort(key=lambda x: x.way4, reverse=True)
  export_image_array(csv_dir, 'way4', imageArray, column, image_status)
  
  imageArray.sort(key=lambda x: x.way5, reverse=True)
  export_image_array(csv_dir, 'way5', imageArray, column, image_status)
    
# Uncomment this line, img_dir is img directory, csv_dir is destination csv directory, "ea1a2c91-f485-4eab-9ddf-2c56249393ca" is csv name, "success" is extra name
# export_csv_image(img_dir, csv_dir, "ea1a2c91-f485-4eab-9ddf-2c56249393ca", "success")