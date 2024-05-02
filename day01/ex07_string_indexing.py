# 인덱싱 : 원하는 위치를 지정
# 슬라이싱 : 잘라내기

# 인덱싱 : 0부터 시작, 왼쪽에서 오른쪽, 음수인 경우에는 오른쪽에서 왼쪽으로

str = "Hello Python"
print(str[6])   # P

print(str[-1])  # n
print(str[-5])  # y

print('-' * 30)

# 슬라이싱 : 원하는 위치에서 원하는 갯수 만큼 추출
#  변수(데이터)[시작위치 : 끝위치(포함안됨)]
print(str[8:6])     # 안나온다.
print(str[6:8], type(str[6:8]))     # Py

print(str[-3: -5])  # 안나온다.
print(str[-5: -3])  # yt

print('-' * 30)

# Hello 추출하기 (처음부터 중간까지)
print(str[0:5])
print(str[:5])

# Python 추출하기 (중간부터 끝까지)
print(str[6:12])
print(str[6:])

# 전체
print(str)
print(str[:])

# 틀린글자 변경하기
# ** 가변형 자료형 : list(리스트), dict(딕셔너리), set(집합)    => 추가, 삭제, 수정 할 수 있음
# ** 불변형 자료형 : str, tuple(튜플)                           => 수정 불가능

str = "python"
# str[1] = 'y'  # 불변형 자료이므로 오류 발생
str2 = str[:1] + 'y' + str[2:]
print(str2)


