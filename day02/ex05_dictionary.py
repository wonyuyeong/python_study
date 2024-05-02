# 딕셔너리 => 키, 값 으로 이루어져있음
#             {key1 : value1, key2 : value2, ....}

dic = {'name' : 'hong', 'phone' : '010-9999-7979', 'age' : 24, 'gender' : True}
print(dic,type(dic))

# 추가
dic = {1: 'a', "2" : "b"}
print(dic,type(dic))

# dic[5] 에서 5는 인덱스가 아니라 name 임
dic[5] = 'c'
dic[4] = 'k'
print(dic,type(dic))

# 리스트 추가
dic[3] = [1,2,3,4]
print(dic,type(dic))

# 튜플
dic[6] = (1,2,3,4)
print(dic,type(dic))

# 딕셔너리
dic[10] ={'name' : 'hong', 'phone' : '010-9999-7979'}
print(dic,type(dic))

# 삭제 : del 이름[key]
del dic[6]
print(dic,type(dic))

del dic[10]['phone']
print(dic,type(dic))

# 수정 : key 가 같으면 덮어쓰기 된다.
dic[5] = 'K'
print(dic, type(dic))

dic[10]['name'] = 'goh'
print(dic,type(dic))


# 딕셔너리 관련 함수
dic = {'name' : 'hong', 'phone' : '010-9999-7979', 'age' : 24, 'gender' : True}
print(dic.keys(), type(dic.keys()))
print(dic.values(), type(dic.values()))
print('-' * 50)

# 리스트가 필요한 경우 : 리스트로 변경하면 append, insert, pop, remove, sort 등을 사용할 수 있다.
print(list(dic.keys()), type(list(dic.keys())))

# 쌍으로 얻기 - item()
print(dic.items(),type(dic.items()))

# key : value 쌍 모두 지우기 - clear
dic.clear()
print(dic)

# 얻기 : get(키)
dic = {'name' : 'hong', 'phone' : '010-9999-7979', 'age' : 24, 'gender' : True}
print(dic.get('name'))
print(dic['name'])

# 없는 key를 호출 했을 때
#print(dic.get('hobby')) # none
#print(dic['hobby'])

print(dic.get('hobby','movie')) # 키가 없으면 None이 아니라 movie가 나온다.
# print(dic['hobby'])

# key값조사하기 -in
print('name' in dic) # T
print('email' in dic) # F
