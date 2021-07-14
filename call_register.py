import requests
import json
import os
import base64
import pandas as pd
from datetime import datetime

bnbUrl = 'https://bnbplus.work'
# bnbUrl = 'http://192.168.1.5:8080'

token_file = open("token.txt","r+")
token = token_file.read()
# print(token)

def request(url, headers, data):
  response = requests.post(url, data=json.dumps(data), headers=headers)
  return response

def uploadFacepasssImage(bookId, personId, base64):
  upload_face = "/api/facepass-upload-base64"
  url = bnbUrl + upload_face
  
  my_headers = {
    'content-type': 'application/json',
    'X-Auth-Token': token
    }
  now = datetime.now()
  date_time = now.strftime("%m-%d-%YT%H:%M:%S")
  
  data = {
    "appData": {
      "bookId": bookId,
      "personType": "GUEST",
      "personId": personId,
      "imgBase64": base64,
      "imgName": "/" + date_time + ".jpeg",
      "imgMimeType": "image/jpeg"
    }
  }
  return request(url, my_headers, data)


def registerBnbAccount(email, hostelId, password):
  register_bnb_account = "/api/face-pass/register-bnb-account"
  url = bnbUrl + register_bnb_account
  
  my_headers = {
    'content-type': 'application/json',
    'X-Auth-Token': token
    }
  data = {
    "appData": {
      "username": email,
      "lang": "ja",
      "hostelId": hostelId,
      "password": password
    }
  }
  return request(url, my_headers, data)


def faceRegisterUpdateS3(bookId, personId, email, sub, tag):
  face_register_update_s3 = "/api/bnb-face-register-update-s3"
  url = bnbUrl + face_register_update_s3
  
  my_headers = {
    'content-type': 'application/json',
    'X-Auth-Token': token
    }

  data = {
    "appData": {
      "bookId": bookId,
      "personType": "GUEST",
      "personId": personId,
      "email": email,
      "sub": sub,
      "tag": tag
    }
  }
  return request(url, my_headers, data)


img_file_path = 'D:\\Data\\Learning\\ImageStatistic\\Predict Image\\2021-07-13T10_07_07.533Z_1_1.jpg'
csv_dir = 'D:\\Data\\Learning\\ImageStatistic\\CSV_Bright_Dark'


# with open(img_file_path, "rb") as img_file:
#   base64_img = base64.b64encode(img_file.read())
# base64_img = base64_img.decode('utf-8')
# bookId = 3142
# personId = 3139

# res = uploadFacepasssImage(bookId, personId, base64_img)
# my_json = res.content.decode('utf8').replace("'", '"')
# data = json.loads(my_json)
# appData = data['appData']


# email = "dominhlam98+stgfpguest@gmail.com"
# hostelId = 16
# password = "123456"

# res = registerBnbAccount(email, hostelId, password)
# my_json = res.content.decode('utf8').replace("'", '"')
# data = json.loads(my_json)
# appData = data['appData']



bookId = 3142
personId = 3139
email = "dominhlam98+stgfpguest@gmail.com"
sub = "20e56eba-d7f6-431f-947a-163ab5d418a1"
tag = "dominhlam98+stgfpguest-test-reg-python"

res = faceRegisterUpdateS3(bookId, personId, email, sub, tag)
my_json = res.content.decode('utf8').replace("'", '"')
data = json.loads(my_json)
appData = data['appData']


    

  




