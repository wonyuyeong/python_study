# 숫자형을 활용한 연산자
# 사칙연산(+, -, *, /, //(몫), %(나머지))
# 복합연산(+=, -=, *=, /=, //=, %=, **=)

su1 = 7
su2 = 3

res = su1 + su2
print(res)

res = su1 - su2
print(res)

res = su1 * su2
print(res)

res = su1 / su2
print('%.2f' %res)

res = su1 // su2
print(res)

res = su1 % su2
print(res)

print('-' * 50)

su1 = su1 + 10
print(su1)  # 17

su1 += 10
print(su1)  # 27
