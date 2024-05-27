from urllib.request import urlopen
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import requests
import json

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
params ={
    'serviceKey' : 'AdhJIKfmfCt3wG7aECgUVo9bYfrRRb4R+ZyZONBU3haxqk+jzV74PlV4eniVcj135tYPm0ab/FenVor163ShlA==',
    'returnType' : 'json',
    'numOfRows' : '100',
    'pageNo' : '1',
    'sidoName' : '서울',
    'ver' : '1.0' 
    }

# json.load() : 파일 객체에서 json 데이터를 읽어서 파이썬 객체로 변환 (주로 파일)
# json.loads() : json 형식의 문자열을 파이썬 객체로 변환("주로 네트워크를 통해 수신된 json")
response = requests.get(url, params=params)
data = json.loads(response.content)

# 딕셔너리 하나
# print(type(data), len(data))
list = data["response"]["body"]["items"]
for i in list:
    print(i["sidoName"], end=" ")
    print(i["stationName"], end=" ")
    print(i["pm10Value"], end=" ")
    print(i["pm25Value"])

 