# json 은 json 데이터를 쉽게 처리하고자 사용하는 모듈

import json
with open("day07/myinfo.json", "r", encoding="utf-8") as f :
    data = json.load(f)

print(data, type(data))

d = {"name" : "둘리", "birth" : "0101", "age" : 24}
j_data = json.dumps(d)
print("-"* 50)

# 한글 깨진것 처럼 보이지만 다시 json.loads를 하면 제대로 나온다.
print(j_data)           # 한글깨짐
print(json.loads(j_data))

# dumps 에 옵션을 주면 깨지지 않는다.
d2 = {"name" : "춘식이", "birth" : "0313", "age" : 3}
j_data2 = json.dumps(d2, ensure_ascii=False)
print(j_data2)