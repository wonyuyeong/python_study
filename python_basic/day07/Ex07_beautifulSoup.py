from bs4 import BeautifulSoup
print("---------태그와 속성을 이용해서 가져오기 -------------")
# find_all('태그명', {'속성명' : '값', ...})
# find('태그명', {'속성명' : '값', ...})

# div 에서 id 속성값이 sample_id 인 것만 가져오기
with open("day07/sample.html", "r", encoding="utf-8") as f1:
    soup = BeautifulSoup(f1, "html.parser")
    s1 = soup.find("div", {"id" : "sample_id"})
print(s1)
print("-" * 50)

# div 에서 id 속성값이 sample_id 인 것중 p태그만 가져오기
with open("day07/sample.html", "r", encoding="utf-8") as f2:
    soup = BeautifulSoup(f2, "html.parser")
    s2 = soup.find("div", {"id" : "sample_id"})
    s3 = s2.find("p")
    s4 = s3.get_text()
print(s3)
print("-" * 50)
print(s4)
print("-" * 50)

# div 에서 id 속성값이 sample_id 인 것중 p태그 전체 가져오기
soup = BeautifulSoup(open("day07/sample.html", "r", encoding="utf-8"), "html.parser")
str1 = soup.find("div", {"id" : "sample_id"})
str2 = str1.find_all("p")
for i in str2 :
    print(i.get_text())