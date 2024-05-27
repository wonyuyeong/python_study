# list :  대괄호 사이에 쉼표로 구분된 값(항목)의 목록, (다른언어의 배열과 비슷하다.)
#         자바와 다르게 서로 다른 유형의 항목을 포함 할 수 있다.
odd = [1,3,5,7]
str = ["hi", "bye", "good"]
person = ["홍길동", 24, 180.1, 'A', True]

# 리스트도 인덱싱과 슬라이싱이 가능하다.
print(odd[2], type(odd[2])) # 5

print(odd[0:2], type(odd[0:2])) # [1,3]
print(str[-1], type(str[-1]))   # "good"

# 리스트 안에 리스트가 존재 할 수 있다.
even = [2,4,6,odd,8,10]
print(even)
print(even[0], type(even[0]))
print(even[3], type(even[3]))
print(even[3][2], type(even[3][2]))

# string 가능
print(person[0][1])     # 홍길동의 길 추출하자