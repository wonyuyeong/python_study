from urllib.request import urlopen
from bs4 import BeautifulSoup

myurl = "http://www.kma.go.kr/XML/weather/sfc_web_map.xml"
response = urlopen(myurl)

soup = BeautifulSoup(response, "html.parser")
# print(soup)

c_local = soup.find_all("local")
for i in c_local :
    print("도시 : ", i.string, end=" ")
    print("상태 : ", i["desc"], end= " ")
    print("온도 : ", i["ta"])
    print("-"* 50)