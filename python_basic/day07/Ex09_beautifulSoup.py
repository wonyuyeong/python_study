from urllib.request import urlopen
from bs4 import BeautifulSoup

# 날씨 xml 읽기
target = urlopen("http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
soup = BeautifulSoup(target, "html.parser")
# print(soup)

# location 태그 찾기
for i in soup.select("location"):
    # .get_text() 대신 .string 가능 
    # .get_text() -> 태그 빼고 글자만
    print("도시 : ", i.select_one("city").get_text())
    print("날씨 : ", i.select_one("wf").get_text())
    print("최저기온 : ", i.select_one("tmn").get_text())
    print("최고기온 : ", i.select_one("tmx").get_text())
    print("--------------------------")