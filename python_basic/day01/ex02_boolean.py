# 파이썬의 자료형 : 숫자(int, float), 문자열(str), 불린, 리스트, 튜플, 딕셔너리, 집합
# boolean : 참/거짓
# 참 : True, 거짓 : False   ** 주의 : 첫글자는 대문자!

con = True
print(con)
print(type(con))

# 변수는 하나의 정보만 가진다.
con = False
print(con)
print(type(con))

con = 'Hi~~~'
print(con)
print(type(con))

print('*' * 10)

# 숫자를 불린형으로 변경하자 : bool(숫자)
# 0이면 False, 0을 제외한 숫자는 True로 만든다.
su1 = 0
su2 = 1
su3 = 135

print(bool(su1))
print(bool(su2))
print(bool(su3))

# 문자열을 불린형으로 : bool(문자열)
# 데이터 있으면 True, 데이터 없으면 False
# 나머지 자료형도 같다.

str1 = 'ictedu'
str2 = ''
str3 = ' '
print(bool(str1))
print(bool(str2))
print(bool(str3))