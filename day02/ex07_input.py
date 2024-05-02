# input 키보드로 정보를 입력 받아서 처리할 수 있다.
# input 으로 들어온 정보는 문자열이다.

name = input("이름을 입력하세요 >>")

kor = int(input("국어점수 : "))
eng = int(input("영어점수 : "))
math = int(input("수학점수 : "))

sum = kor+eng+math
avg = sum / 3
avg2 = int(avg*100)/100

print("이름 : ", name)
print("총점 : ", sum)
print("평균 : ", avg)
print("평균 : ", avg2)