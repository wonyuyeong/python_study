from urllib.request import urlopen
from bs4 import BeautifulSoup

myurl = "http://localhost:8090/test05.do"
response = urlopen(myurl)

soup = BeautifulSoup(response, "html.parser")
# print(soup)

c_local = soup.find_all("local")
for i in c_local :
    print("도시 : ", i.string)
    print("상태 : ", i["desc"])
    print("온도 : ", i["ta"])
    print("-"* 50)