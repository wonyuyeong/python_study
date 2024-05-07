# import 현재 파일이 가지고 있지 않은 함수, 모듈을 사용하기 위해서
# 호출할때 사용하는 예약어

# 함수, 함수, 함수 => 모듈(하나의 파일)
# 모듈이란 함수나 변수 또는 클래스를 모아놓은 파이썬 파일이다.

# 패키지는 모듈의 집합
# 패키지는 파이썬 모듈을 계층적(디렉토리구조)으로 관리할 수 있게 해줌

# 현재 위치가 python_basic 이므로 같은 폴더안에 있어서 day06 안붙여도된다.
import Ex09_Main01 as calc
# 이건 이건 day03 붙여줘야함
import day03.ex12_function as c
print(calc.add(5,3))
print(calc.sub(5,3))

print(c.add(10,13))