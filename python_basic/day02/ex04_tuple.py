# 튜플 : 몇가지를 제외하고 리스트와 거의 같음
#        불변, 수정 안됨, (항목, 항목, 항목)

# 튜플 생성
t1 = (1,2,3)
print(t1, type(t1))

t2 = ()
print(t2, type(t2))

# 하나의 데이터만 들어있는 튜플을 만들기 위해서는 반드시 요소 뒤에 쉼표를 붙여야 한다.
# t3 = (3)    # int
t3 = (3,)
print(t3, type(t3))

# 여러개 일때는 () 생략 가능
t4 = 1,2,3,4,5
print(t4, type(t4))

# 튜플의 항목을 삭제, 수정 하려면
# 인덱싱하기
t1 = (1,2,'a','b')
print(t1[0], type(t1[0]))

# 슬라이싱하기 (2~~)
print(t1[1:], type(t1[1:]))

# 더하기 (+)
t1 = (1,2,'a','b')
t2 = (3,4)
t1 = t1+t2
print(t1)   # (1, 2, 'a', 'b', 3, 4)

# 곱하기(반복)
print(t2 * 3)    # (3, 4, 3, 4, 3, 4)

# 길이 : len()
print(len(t1))

# 튜플 항목의 삭제, 수정 안됨
# 삭제 : del
t1 = (1,2,'a','b')
# del t1[1]
# print(t1)

# 수정 : 'a' 를 'A'
# t1[2] = 'A'
# print(t1)

# 튜플을 리스트로 변경하자
t1_list = list(t1)
print(t1_list, type(t1_list))

del t1_list[2]
print(t1_list)

t1_list[2] = 'B'
print(t1_list)





