# CSV : 쉼표(,)로 구분한 텍스트 데이터 및 텍스트 파일
# 확장자는 .csv 이며 MIME 형식은 text/csv 이다.
# 첫번째 라인 컬러명이 나온다.
# csv 파일은 보통 list로 변환해서 처리한다.
# 또는 딕셔너리로 변환해서 처리한다.

# 모듈 이란 함수나 변수 또는 클래스를 모아놓은 파일
import csv

# newline=''  => 줄바꿈
f = open("day04/data/csv01.csv", "w", encoding="utf-8", newline='')
wr = csv.writer(f)

wr.writerow([1,"홍길동",24,"서울"])
wr.writerow([2,"둘리",39,"남극"])
wr.writerow([3,"마이콜",16,"제주도"])
f.close()

f = open("day04/data/csv01.csv", "r", encoding="utf-8")
rd = csv.reader(f)
print(rd, type(rd))
# 수정을  위해서 리스트에 넣어서 처리하자
lines = []
for i in rd :
    # 성년 미성년
    if(int(i[2]) <=18) :
      #  print("미성년자")
      i[2] = "미성년자"
    else:    
      #  print("미성년자")
      i[2] = "성년자"
      lines.append(i)
f.close()

# print(lines)
# 변경된 내용을 다시 쓰기
f = open("day04/data/csv01_e.csv", "w", encoding="utf-8", newline='')
wr = csv.writer(f)
wr.writerows(lines)
f.close()


f2 = open("day04/data/csv01.csv", "r", encoding="utf-8")
rd = csv.reader(f2)
print(rd, type(rd))
# 수정을  위해서 리스트에 넣어서 처리하자
lines2 = []
for i in rd :
    # 성년 미성년
    if(int(i[2]) <=18) :
      i.append("미성년자")
    else:    
      #  print("미성년자")
      i.append("성년자")
    lines2.append(i)
f2.close()

# print(lines)
# 변경된 내용을 다시 쓰기
f3 = open("day04/data/csv01_f.csv", "w", encoding="utf-8", newline='')
wr = csv.writer(f3)
wr.writerows(lines2)
f3.close()