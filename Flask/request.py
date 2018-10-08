import requests
import cv2
import json

FASTAI_REST_API_URL = "http://127.0.0.1:5000/predict"
IMAGE_PATH = 'test2.jpg'

content_type = 'image/jpeg'
headers = {'content_type' : content_type}

img = cv2.imread(IMAGE_PATH)

_,img_encoded = cv2.imencode('.jpg', img)
response = requests.post(FASTAI_REST_API_URL, data=img_encoded.tostring(), headers=headers)

print(json.loads(response.text))
