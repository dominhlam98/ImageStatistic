from imageFunc import Image
import cv2
import os

img_dir = 'D:\\Data\\Learning\\ImageStatistic\\image'
separate_img_dir = 'D:\\Data\\Learning\\ImageStatistic\\separate_image'

if os.path.exists(separate_img_dir) == False:
    os.mkdir(separate_img_dir) 

char1 = 'Z_0'
char2 = 'Z_1'

file_type1 = '.jpg'
file_type2 = '.jpeg'

for subdir in os.listdir(img_dir):
  path = img_dir + '\\' + subdir
  separate_path = separate_img_dir + '\\' + subdir
  
  if os.path.exists(separate_path) == False:
    os.mkdir(separate_path) 

  success_path = separate_path + '\\success'
  if os.path.exists(success_path) == False:
    os.mkdir(success_path)

  fail_path = separate_path + '\\fail'
  if os.path.exists(fail_path) == False:
    os.mkdir(fail_path)

  reg_path = separate_path + '\\register'
  if os.path.exists(reg_path) == False:
    os.mkdir(reg_path)

  cnt_file = cnt_fail = cnt_success = cnt_reg = 0
  for filename in os.listdir(path):
    cnt_file += 1
    file_path = path + '\\' + filename
    img = cv2.imread(file_path)

    if file_type2 in filename:
      cnt_reg += 1
      os.chdir(reg_path)
      cv2.imwrite(filename, img)
      continue

    split = filename.split(char1)
    if len(split) == 1:
      split = filename.split(char2)

    if split[1] == file_type1:
      cnt_fail += 1
      os.chdir(fail_path)
      cv2.imwrite(filename, img)
      continue

    cnt_success += 1
    os.chdir(success_path)
    cv2.imwrite(filename, img)

  print(subdir + ' total: ' + str(cnt_file) + ' reg-face: ' + str(cnt_reg) + ' success-face: ' + str(cnt_success) + ' fail-face: ' + str(cnt_fail))


    

    

