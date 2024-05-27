# 매개변수에 초기값 미리 지정하기
def say(name, age, gender = True) :
    print("나의 이름은 {}입니다." .format(name))
    print("나의 나이는 {}입니다." .format(age))
    if gender : 
        print("남성입니다.")
    else :
        print("여성입니다.")
        
say("hong", 24, True)
print("-" * 50)

say("kim", 18, False)
print("-" * 50)

say("park", 21)
print("-" * 50)

# 매개변수에 초기값 미리 지정할때 반드시 뒤에는 없거나, 초기값이 미리 지정되어있는 매개변수가 있어야 한다.
# 초기값이 없는 매개 변수는 초기값이 있는 매개변수 뒤에 사용할 수없다.
# def say(name,  gender = True, age) :
#    print("나의 이름은 {}입니다." .format(name))
#    print("나의 나이는 {}입니다." .format(age))
#    if gender : 
#        print("남성입니다.")
#    else :
#        print("여성입니다.")