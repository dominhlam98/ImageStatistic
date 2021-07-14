import requests
import json
import os
import base64
import pandas as pd

token_file = open("token.txt","r+")
token = token_file.read()
# print(token)

def request(url, headers, data):
  response = requests.post(url, data=json.dumps(data), headers=headers)
  return response

def delete_request(url):
  my_headers = {
    'content-type': 'application/json',
    'X-Auth-Token': token
    }
  data = {
    "appData": {
      "username": "dominhlam98+stgfpguest@gmail.com",
      "password": "123456",
      "organizationId": 1
    }
  }
  
  response = request(url, data, my_headers)

  print(response)

def authenticate_request(url, base64):
  my_headers = {
    'content-type': 'application/json',
    'X-Auth-Token': token
    }
  data = {
    "appData": {
      "images": [
        base64
      ],
      "possibleSubs": [],
      "tagId": "",
      "hostelId": 32,
      "appActionTS": "OPEN_DOOR",
      "deviceInfo": None,
      "appAction": ""
    }
  }
  
  return request(url, my_headers, data)

bnbUrl = 'https://bnbplus.work'
# bnbUrl = 'http://192.168.1.5:8080'
api = '/api/faceid/delete-face-id/face'
face_auth_api = '/api/v3/bnb-face-login'

column = ['No.', 'File Name', 'Customer Id', 'Sub']

img_dir = 'D:\\Data\\Learning\\ImageStatistic\\Predict Image'

# img_dir = 'D:\\Data\\Learning\\ImageStatistic\\ScaleImage140Success'


csv_dir = 'D:\\Data\\Learning\\ImageStatistic\\CSV_Bright_Dark'
cnt = 0
row_array = []

success = 0
fail = 0
for file_name in os.listdir(img_dir):
  cnt += 1
  file_path = img_dir + '\\' + file_name
  base64_img = ''
  with open(file_path, "rb") as img_file:
    base64_img = base64.b64encode(img_file.read())
  base64_img = base64_img.decode('utf-8')
  
  # base64_text = open("base64_lam.txt","r+")
  # base64_img = base64_text.read()
  url = bnbUrl + face_auth_api
  res = authenticate_request(url, base64_img)
  
  my_json = res.content.decode('utf8').replace("'", '"')
  data = json.loads(my_json)
  
  appData = data['appData']
  
  row = ['', '', '', '']
  if appData == None:
    fail += 1
    row = [cnt, file_name, '', '']
  else:
    sub = appData['sub']
    customer = appData['customer'] 
    if sub == None:
      fail += 1
      row = [cnt, file_name, '', '']
    else:
      success += 1
      row = [cnt, file_name, customer['customerId'], sub]
      
  print(row)
  row_array.append(row)

row_array.append(['Success', success, 'Fail', fail])

os.chdir(csv_dir)
excel = pd.DataFrame(row_array, columns= column)
excel.to_csv('face_success.csv', index=False, na_rep='')
  




