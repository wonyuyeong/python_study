# 네이버 웹툰 정보 가져오기(크롤링)
# https://comic.naver.com/webtoon?tab=wed
# https://comic.naver.com/webtoon?tab=wed

from urllib.request import urlopen
from bs4 import BeautifulSoup

myurl = "https://comic.naver.com/webtoon?tab=wed"
response = urlopen(myurl)

soup = BeautifulSoup(response, "html.parser")

s1 = soup.find_all("div", {"class" : "DailyList__info_area--f4sN6"})

print(s1)
