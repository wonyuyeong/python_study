from urllib.request import urlopen
import json

# HTML 인 경우 BeautifulSoup 을 이용해서 파싱하고, JSON 데이터는 바로 읽어온다.
myurl = "http://localhost:8090/test07.do"
response = urlopen(myurl)
data = json.load(response)

for i in data:
    print(i["시·도별(1)"], end=" ")
    print(i["총인구 (명)"], end=" ")
    print(i["1차 접종 누계"], end=" ")
    print(i["2차 접종 누계"], end=" ")
    # print(i["1차 접종 퍼센트"], end=" ")
    # print(i["2차 접종 퍼센트"])
    # 소수점 첫째자리 퍼센트
    print('{:.1f}%' .format(i["1차 접종 퍼센트"]), end=" ")
    print('{:.1f}%' .format(i["2차 접종 퍼센트"]))


