from urllib.request import urlopen
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import requests

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
params ={
    'serviceKey' : 'AdhJIKfmfCt3wG7aECgUVo9bYfrRRb4R+ZyZONBU3haxqk+jzV74PlV4eniVcj135tYPm0ab/FenVor163ShlA==',
    'returnType' : 'xml',
    'numOfRows' : '100',
    'pageNo' : '1',
    'sidoName' : '서울',
    'ver' : '1.0' 
    }
response = requests.get(url, params=params)
# print(response.content)

root=ET.fromstring(response.content)
data_list=[]
# 현재 노드부터 모든 하위 요소를 검색하여 태그이름이 item인 요소를 찾는다.
for i in root.findall(".//item"):
        data ={
                "sidoName": i.findtext("sidoName"),
                "stationName": i.findtext("stationName"),
                "pm10Value":i.findtext("pm10Value"),
                "pm25Value":i.findtext("pm25Value")
        }
        data_list.append(data)
        
# print(data_list)

for i in data_list:
    print(i["sidoName"], end=" ")
    print(i["stationName"], end=" ")
    print(i["pm10Value"], end=" ")
    print(i["pm25Value"] )
 