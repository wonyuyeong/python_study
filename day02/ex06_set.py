# 집합 : 중복을 허용하지 않는다, 순서가 없다. 인덱싱으로 값을 얻을 수 없다.
s1 = set([1,2,3,4,5])
print(s1, type(s1))

s2 = {100,200,300,400,500}
print(s2, type(s2))

# 중복안됨
s3 = set([1,2,3,4,5, 1,5,7,5,2,10,9])   # {1, 2, 3, 4, 5, 7, 9, 10} <class 'set'>
print(s3, type(s3))

# 인덱싱으로 값을 얻을 수 없다.
# print(s3[4])    # 오류

# 리스트나 튜플로 전환해서 인덱싱 해야한다.
lis = list(s3)
print(lis[4])   # 5

tu = tuple(s3)
print(tu[4])    # 5
print('-' * 50)

# 교집합(&), 합집합(|), 차집합(-) 가능
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

print(s1 & s2)
print(s1 | s2)
print(s1 - s2)
print(s1.difference(s2))

# 추가, 삭제, 전체 삭제
# s3 = s1 + s2      # 오류발생

# 추가 : add , update
s1.add(10)
print(s1)

# s1 = s1 + s2 대신
s1.update(s2)
print(s1)

# 삭제 : remove(데이터)
s1.remove(10)
print(s1)

# 인덱싱으로 값을 얻을 수 없다.
# del s1[2]
# print(s1)

# s1.remove(100)      # 없는 요소 삭제 하려면 오류

# discard() 삭제하고자 하는 요소가 없어도 오류 발생 안함
s1.discard(6)
print(s1)

s1.discard(100)
print(s1)

# 딕셔너리에서 사용하는 것 처럼 in을 사용해서 데이터가 있는지 없는지 판단 가능
print(5 in s1)      # True
print(100 in s1)    # False

# 전체 삭제 : clear()
s1.clear()
print(s1)