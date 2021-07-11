from imageFunc import Image
from summaryFunc import SummaryImage
import cv2
import os
import pandas as pd

separate_img_dir = 'D:\\Data\\Learning\\ImageStatistic\\separate_image'
csv_dir = 'D:\\Data\\Learning\\ImageStatistic\\CSV'

if os.path.exists(csv_dir) == False:
  os.mkdir(csv_dir)

column = ['No.', 'File name', 'Image Status', 'Min H', 'Max H', 'Sum H', 'Average H',
                                      'Min S', 'Max S', 'Sum S', 'Average S',
                                      'Min V', 'Max V', 'Sum V', 'Average V',
                                      'Min R', 'Max R', 'Sum R', 'Average R',
                                      'Min G', 'Max G', 'Sum G', 'Average G',
                                      'Min B', 'Max B', 'Sum B', 'Average B' ]

summaryColumn = ['No.', 'File name', 'Type', 'Value']

for subdir in os.listdir(separate_img_dir):
  separate_path = separate_img_dir + '\\' + subdir
  sum_reg = sum_success = sum_fail = 0
  
  csv_path = csv_dir + '\\' + subdir
  if os.path.exists(csv_path) == False:
    os.mkdir(csv_path)

  array = []
  for subdir1 in os.listdir(separate_path):
    file_path = separate_path + '\\' + subdir1

    summaryArray = []
    cnt = 0
    summaryImage = SummaryImage()

    for filename in os.listdir(file_path):
      cnt += 1
      path = file_path + '\\' + filename
      image = cv2.imread(path)

      imageClass = Image(image)
      imageClass.setRgb()
      imageClass.setHsvImage()
      imageClass.setHsv()

      summaryImage.summary(imageClass, filename)

      row = imageClass.getRow(cnt, filename, subdir1)
      array.append(row)

    # array.append([''])
    
    csv_status_path = csv_path + '\\' + subdir1
    if os.path.exists(csv_status_path) == False:
      os.mkdir(csv_status_path)
    os.chdir(csv_status_path)
    
    summaryArray = summaryImage.getRowArray(cnt)
    excel = pd.DataFrame(summaryArray, columns= summaryColumn)
    excel.to_csv(subdir1, index=False, na_rep='')
    
  os.chdir(csv_path)

  excel = pd.DataFrame(array, columns= column)
  excel.to_csv(subdir, index=False, na_rep='')


