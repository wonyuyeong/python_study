# ictedu 홈페이지 정보 가져오기(크롤링)
# https://comic.naver.com/webtoon?tab=wed
# https://comic.naver.com/webtoon?tab=wed

from urllib.request import urlopen
from bs4 import BeautifulSoup

myurl = "https://ictedu.co.kr/index.php?main_page=home"
response = urlopen(myurl)

print(response)

soup = BeautifulSoup(response, "html.parser")
# print(soup)

# 각각 별도로
# c_title = soup.find_all("h3", {"class" : "title"})
# for i in c_title :
#     print(i.find("a").string)
    
# c_lt = soup.find_all("li", {"class" : "lt"})
# for i in c_lt:
#     print(i.find("div").string)

# 두개를 포함하고 있는 요소를 찾기

# # c_info = soup.find_all("div", {"class" : "info"})
# # for i in c_info :
# #   c_title = i.find("h3", {"class" : "title"})
# #    print(c_title.find("a").string.strip(), end=" // ")
    
#     c_lt = i.find("li", {"class" : "lt"})
#     print(c_lt.find("div").string.strip(), end="  ") """
c_info = soup.find_all("div",{"class":"info"})
for i in c_info:
    c_title = i.find("h3",{"class":"title"}).find("a").get_text().strip()
    print(c_title, end="  /  ")
    
    c_lt = i.find("li",{"class":"lt"}).find("div").get_text().strip()
    print(c_lt, end="  /  ")
    
    print()
    print("-"*50)



