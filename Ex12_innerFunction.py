# 파이썬의 내장 함수는 외부 모듈과 달리 import가 필요없다.
# 바로 사용가능

# abs() : 절대값을 돌려주는 함수 (모두 양수가 된다)
print(abs(3))
print(abs(-3))
print(abs(3.2))
print(abs(-3.2))
print("-" * 50)

# all([리스트]) : 반복 가능한 자료형(리스트)를 입력 인수로 받아
#         해당 요소가 모두 참이면 결과는 참, 하나라도 거짓이면 거짓
# and 와 같은 개념
print(all([True, True, True, True]))        # True
print(all([True, True, False, True]))       # False
print(all([1,2,3,4,5,6,9]))                 # True  (숫자에서는 0초과이면 True)
print(all([1,2,3,4,0,5,6,9]))               # False (숫자에서는 0이면 False)
print(all(["apple banana mango"]))          # True
print(all([""]))                            # False (아무내용 없으면 False)
print(all([" "]))                           # True  (띄어쓰기도 내용으로 간주 True)
print(all(["apple  mango"]))                # True
print("-" * 50)

# any([리스트]) : 반복 가능한 자료형(리스트)를 입력 인수로 받아
#                 해당 요소가 모두 거짓이면 결과는 거짓, 하나라도 참이면 참
# or 과 같은 개념
print(any([True, True, True, True]))        # True
print(any([True, True, False, True]))       # True
print(any([1,2,3,4,5,6,9]))                 # True
print(any([1,2,3,4,0,5,6,9]))               # True
print(any(["apple banana mango"]))          # True
print(any([""]))                            # False (아무내용 없으면 False)
print(any([" "]))                           # True
print(any(["apple  mango"]))                # True
print("-" * 50) 

# chr(i) : 유니코드 숫자를 받아서 그 코드에 해당하는 문자를 리턴하는 함수
print(chr(97))      # a
print(chr(44032))   # 가
print("-" * 50) 

# ord("문자") : 해당 문자의 유니코드 숫자를 리턴하는 함수
print(ord("a"))     # 97
print(ord("가"))    # 44032
print("-" * 50) 

# divmod(a,b) : 몫과 나머지를 튜플 형태로 돌려줌
print((7//3), (7%3))
print(type(7//3), type(7%3))    # 자료형 int이다.
print(divmod(7,3), type(divmod(7,3)))   # 자료형 tuple
print("-" * 50) 

# ** 중요 ** enumerate : 순서가 있는 데이터(리스트, 튜플, 문자열)를 입력받아서 
#                        인덱스값을 포함하는 enumerate 객체(차례대로 접근하는 객체) 리턴
#                        보통 for문과 같이 사용
#                        데이터값을 이용해서 인텍스값을 추출할 때 유용하다.
for i, name in enumerate(["body", "food", "bar"]) :
    print(i, name)
print("-" * 50) 

# eval("문자열") : 실행가능한 문자열을 입력받아 문자열을 실행한 결과를 돌려주는 함수
print(1+2)                  # 3
print("1+2")                # 1+2
print(eval("1+2"))          # 3
print("-" * 50)

print(divmod(7,3))          # (2,1) 
print("divmod(7,3)")        # divmod(7,3) 
print(eval("divmod(7,3)"))  # (2,1) 

# filter(함수, 반복가능한 데이터) : 반복가능한 데이터를 요소 순서대로 함수를 호출했을 때 리턴값이 참인 것만 묶어서 리턴한다.
def positive(lis):   # 리스트를 받는다.
    result = []     # 결과를 저장하는 리스트
    for i in lis :
        if i > 0:      # 받은 리스트에서 0보다 큰자료만 별도로 저장하자
            result.append(i)
    return result

print(positive([1,2,-1,5,-4,0,9]))

print(list(filter(lambda x : x>0, [1,2,-1,5,-4,0,9])))

# 0-10 까지 짝수만
print(list(filter(lambda x : x%2==0, [0,1,2,3,4,5,6,7,8,9,10])))
print("-"* 50)
# int(x) : 문자열 형태의 숫자나 소수점이 있는 숫자를 정수로 리턴
print("3", type("3"))                   # 3, 자료형 str
print(int("3"), type(int("3")))         # 3, 자료형 int
print(int(3.53), type(int(3.53)))       # 오류발생, float로 처리해야한다.  

print(3.53, type(3.53))                 # 3.53, 자료형 float
print(float(3.53), type(float(3.53)))   # 3.53, 자료형 float

# list("문자열") : string 을 list 로 변경
print(list("python"))   # 한글자씩 리스트로 만듬

# len(s) 반복 가능한 자료형 s의 길이
print(len("python"))            # 6
print(len([1,2,3,4,5,6,7]))     # 7
print(len((1,2,3,4,5,6,7)))     # 7
print("-"* 50)

# ** map(함수, 반복 가능한 데이터)

# 가지고 있는 리스트 요소 *2 하기
def two_times(lis) :
    result = []
    for i in lis :
        result.append(i*2)
    return result

res = two_times([1,2,3,4,5])
print(res)

def two_times2(x):
    return x*2

lis2 = list(map(two_times2, [1,2,3,4,5]))
print(lis2)
print("-" * 50)

# max : 반복 가능한 자료형을 받아서 최대값을 리턴
# min : 반복 가능한 자료형을 받아서 최소값을 리턴
print("<max,min>")
print(max([2,3,1,8,4,9,4,6,7]))     # 9
print(min([2,3,1,8,4,9,4,6,7]))     # 1
print(max('pythonPYTHON'))          # y
print(min('pythonPYTHON'))          # H
print("-" * 50)

# ** range([start, ] stop, [step]) : for문과 함께 자주 사용하는 함수 (끝은 포함하지 않는다.)
print("<range>")
print(list(range(10,20,2)))     # [10,12,14,16,18]
print(list(range(5)))           # [0,1,2,3,4]
print("-" * 50)

# round : 반올림
# 파이썬은 기본적으로 '반올림 반짝' 방식을 사용하지 않고, 
# '짝수를 선호하는' 반올림을 해요. 
# 이를 round half to even 또는 bankers' rounding이라고 부르죠. 
# 이 방식은 반올림할 숫자가 정확히 중간값일 때, 
# 즉 1.5나 2.5처럼 0.5로 끝날 때, 가장 가까운 짝수로 반올림을 하게 되요. 
print("<round>")
print(round(4.2))       # 4
print(round(4.5))       # 4   짝수일때는 5가 반올림 안됨  
print(round(4.6))       # 5

print(round(5.2))       # 5
print(round(5.5))       # 6   홀수일때는 5가 반올림 됨
print(round(5.6))       # 6
print("-" * 50)

# sorted : 입력데이터를 정렬한 후 리스트로 리턴한다.
print("<sorted>")
lis3 = [3,1,2]
print(sorted(lis3))     # 1,2,3
print(sorted("zero"))   # e o r z
print(lis3)             # 3 1 2
print("-" * 50)

# str : 문자열 만들기
print("<str>")
print(str(3))
print(str(3.54))
print("-" * 50)

# tuple : 튜플 만들기
print("<tuple>")
print(tuple("abc"))
print(tuple([1,2,3]))
print("-" * 50)

# sum : 입력 데이터 합계 
print("<sum>")
print(sum([1,2,3]))     # 6
print(sum((1,2,3)))     # 6
print("-" * 50)