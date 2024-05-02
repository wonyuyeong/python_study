# def 함수명(매개변수) :
#           수행할 문장1
#           수행할 문장2
#           수행할 문장3
#           [return 데이터]

def add(a,b) :
    return a+b

def sub(a,b):
    print(a-b)
    
# 함수 호출
res = add(10,5)
print(res)

sub(7,5)

# 같은 함수명이 여러개 존재할 수 없다.(오버로딩이 안됨)
# 같은 함수를 다시 선언하면 위에 함수가 없어진다.
def sub(a):
    print(10-a)

sub(10)     # 오류 안 남
# sub(3,3)    # 오류 남

# 받는 매개변수의 값을 모를 때
def add_many(*args):
    print(args)
    
add_many(1,2,3)
add_many(2,4,6,8,10,12)

def add_mul(choice, *args) :
    if choice == 'add' :
        result = 0
        for i in args :
            result = result + i
    elif choice == 'mul' :
        result = 1
        for i in args :
            result = result * i
    else :
        result = "잘 선택해 주세요"
    return result

res = add_mul("add", 1,2,3,4,5)
print(res)

res = add_mul("mul", 1,2,3,4,5)
print(res)

res = add_mul("sub", 1,2,3,4,5)
print(res)


