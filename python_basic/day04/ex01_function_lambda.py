# 람다식 : 보통 함수로 간결하게 만들 때 사용
# 함수이름 = lambda 매개변수1, 매개변수2, ... : 매개변수를 활용한 표현식
# return 예약어가 없어도 표현식의 결과값을 리턴한다.

str = lambda : "Hello"
print(str())

str2 = lambda a,b : a+b
res = str2(7,10)
print(res)

def str3(a,b) :
    return a+b

res = str3(7,10)
print(res)

