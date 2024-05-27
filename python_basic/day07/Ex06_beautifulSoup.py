# BeautifulSoup : HTML 및 XML 파일에서 데이터를 추출하기 위해 사용되는 파이썬 라이브러리
# 설치하기 : pip install beautifulsoup4

from bs4 import BeautifulSoup
# html을 데려올 때 파일을 읽어도 되고
# urllib 또는 request 를 이용해서 웹에서 소스로 데려와도 됨

# 1. html 파일 읽기
with open("day07/sample.html", "r", encoding="utf-8") as f1 :
    # html.parser" 는 파이썬과 함께 제공되는 기본 파서 
    soup = BeautifulSoup(f1, "html.parser")

print(soup)
print("-" * 50)

# 2. 파서 이용하기
with open("day07/sample.html", "r", encoding="utf-8") as f2 :
    soup = BeautifulSoup(f2, "html.parser")
    # 해당 파일에 있는 모든 div
    all_div = soup.find_all("div")
print(all_div, type(all_div))
print("-" * 50)

with open("day07/sample.html", "r", encoding="utf-8") as f2 :
    soup = BeautifulSoup(f2, "html.parser")
    # 해당 파일에 있는 첫번째 div만 리턴
    one_div = soup.find("div")
print(one_div, type(one_div))
print("-" * 50)

# h1 만 가져오기
with open("day07/sample.html", "r", encoding="utf-8") as f2 :
    soup = BeautifulSoup(f2, "html.parser")
    # 해당 파일에 있는 첫번째 div만 리턴
    one_h1 = soup.find("h1")
print(one_h1)
print("-" * 50)