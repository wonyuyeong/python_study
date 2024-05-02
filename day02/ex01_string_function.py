# 문자열 관련 함수들 : 문자열 뒤에 .(점)를 붙인 후 함수 이름을 써 주면 된다.
# 문자 개수 세기 = count
str = "hobby"
print(str.count('b')) #

# 위치 알려주기 - find, index
print(str.find('b'))    # 2
print(str.find('k'))    # -1 (없으면 -1 반환)

print(str.index('b'))   # 2
# print(str.index('k'))   # -1 (없으면 오류)

# 문자열 삽입 : join (문자열 뿐만 아니라 리스트나 튜플에 사용가능)
print("," .join(str))    #str이 가지고 있는 문자열의 각각의 문자 사이에 ',' 를 삽입한다.

# 소문자를 대문자로 바꾸기 - upper
print(str.upper())

# 대문자를 소문자로 바꾸기 - lower
print((str.upper()).lower())

# 첫글자 대문자 나머지 소문자 - capitalize()
print(str.capitalize())

str = "  hello   "
# 왼쪽 공백 지우기 - lstrip
print(str.lstrip(), len(str.lstrip()), len(str))       # 'hello   '  8 10

# 오른쪽 공백 지우기 - rstrip
print(str.rstrip(), len(str.rstrip()), len(str))       # '   hello'  7 10

# 양쪽 공백 지우기 - strip
print(str.strip(), len(str.strip()), len(str))         # 'hello'  5 10

# 문자열 바꾸기 - replace
str = "Life is too short"
print(str.replace("Life", "Your leg"))  # Your leg is too short

# 문자열 나누기 - split("구분자") : 구분자를 생략하면 스페이스, 탭, 엔터를 기준으로 나눈다. => 결과가 리스트로 나온다.
print(str.split())

