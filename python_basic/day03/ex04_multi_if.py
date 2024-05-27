# if 조건식1 :
#       조건식1이 참일 때 실행
# elif 조건식2 :
#       조건식2이 참일때 실행
# elif 조건식3 :
#       조건식3이 참일때 실행
# [else:
#       모두 거짓일때 즉 나머지]

# 이름, 국어, 영어, 수학 점수를 받아서 총점, 평균, 학점을 구하자
#받은 점수가 90점 이상이면 a, 80점 이상이면 b, 70점 이상이면 c, 나머지 f

name = str(input("이름을 입력하세요 >>"))

kor = int(input("국어점수 : "))
eng = int(input("영어점수 : "))
math = int(input("수학점수 : "))

sum = kor + eng + math
avg = sum/ 3
avg2 = int(avg*100)/100

if (avg2>=90) :
    hak = "A"
elif (avg2>=80) :
     hak = "B"
elif (avg2>=70) :
     hak = "C"
else :
    hak = "F"

print("이름 : " , name)
print("총점 : " , sum)
print("평균 : " , avg2)
print("학점 : " , hak)


