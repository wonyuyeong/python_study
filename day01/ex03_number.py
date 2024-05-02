# 숫자형  : 정수, 실수, 8진수, 16진수

# 1. 정수 : 소수점이 없는 숫자
age = 28
print(age, type(age))

# 2. 실수 : 소수점이 있는 숫자
weight = 92.4
print(weight, type(weight))

# 3. 실수형지수(컴퓨터식 지수 표현)
height = 1.812E2    # 1.812e2 => 1.812 * 10^2 (10의2승)
print(height, type(height))

# 4. 복소수 : 실수부와 허수부
num = 412 + 34j
print(num, type(num))

# 4-1. 실수부만 추출
print(num.real, type(num.real))

# 4-2. 허수부만 추출
print(num.imag, type(num.imag))

# 0-9 a, b, c, d, e, f, 10, 11-19, 1a, 1b, 1c, 1d, 1e, 1f, 20.... (8진수와 16진수의 원리)

# 8진수 : 0o 시작
num = 0o10              # 8 (int)
print(num, type(num))

# 16진수 : 0x 시작
num = 0x10              # 16 (int)
print(num, type(num))

print('-' * 30) # 줄긋기

# 정수를 실수로 변환
num = 27
res = float(num)
print(res, type(float(res)))

# 실수를 정수로 변환
num = 28.124
res = int(num)
print(res, type(res))

# 소숫점 둘째자리 까지 구하기
num1 = 27.444
num2 = 27.445

# 반올림 안된다.
res1 = int(num1 * 100) / 100    # 27.44
res2 = int(num2 * 100) / 100    # 27.44
print(res1)
print(res2)

# 반올림 됨.
print('%.2f' %num1)     # 27.44
print('%.2f' %num2)     # 27.45

# 일의 자리 버림
res1 = int(num1 / 10) * 10
res2 = int(num2 / 10) * 10
print(res1)
print(res2)

