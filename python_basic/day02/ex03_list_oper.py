# 리스트 연산하기

# 리스트 더하기 (+)

su1 = [1,2,3]
su2 = [4,5,6,"홍길동",8]
res = su1+su2
print(res)

# 리스트 반복하기 (*)
res = su1 *3
print(res)

# 오류발생 (인트와 스트링은 합칠 수 없다)
# res = su1[1] + "hi"
# print(res)

# 형변환 : 자료형(대상) , int(), float(), str()
res = str(su1[1]) + "hi"
print(res)

# 리스트 항목 추가, 삭제, 수정 기능 (가변)
odd = [1,7,5,3,9]

# 항목 추가 : append(항목)
odd.append(11)
print(odd)

# 항목 수정 : 리스트[위치] = 데이터
odd[2] = 13
print(odd)

# 항목 삭제 : del 함수 사용 : del 리스트[위치]
del odd[2]
print(odd)

# 항목 삭제 : remove 함수 사용 : 리스트.remove(데이터)
odd.remove(7)
print(odd)

# 중간 삽입 : insert(위치, 데이터)
odd.insert(2,13)
print(odd)

# 리스트 정렬 : sort()
odd.sort()
print(odd)

str = ['a', 'c', 'A', 'e', 'b', 'B', '가', 't', '1']
str.sort()
print(str)

# 리스트 뒤집기 : reverse
str = ['a', 'c', 'A', 'e', 'b', 'B', '가', 't', '1']
str.reverse()
print(str)

# 리스트 요소 끄집어 내기 : pop() => 맨 끝에 있는 항목 삭제하기
odd = [1,2,3,4,5]
odd.pop()
print(odd, res)

# 리스트 확장 - extend(리스트)
su1 = [1,2,3,4,5]
su1.extend([7,8,9])
print(su1)

# 중복 가능
su1.extend([1,3,5,7])
print(su1)