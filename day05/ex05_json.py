import json
from collections import OrderedDict

with open("day05/data/gfriend.json", encoding="utf-8") as f1 :
    # object_pairs_hook=OrderedDict => json 객체를 collections:OrdereDict 객체로 변환 시킴
    # json 객체의 키와 값의 쌍이 유지되면서 순서가 보존된다.
    data = json.load(f1, object_pairs_hook=OrderedDict)
    
print(data, type(data))
print("-" * 50)

# key, value 처리 for문
# enumerate() 함수는 반복 가능한 객체의 각 항목에 대해서 인덱스와 값을 차례대로 접근한다.
for k,v in enumerate():
    print(k, end=" ")
print("*" * 50)

for k,v in data["albums"].item():
    print(k, "\t", v)