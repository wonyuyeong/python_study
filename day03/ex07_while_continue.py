# 맨 처음(while문에서는 조건식)으로 되돌아가는 예약어 : continue

# 1~10 홀수 출력
su = 1
while su <= 11:
    if su%2 == 0:
        su += 1
        continue
    print(su)
    su += 1
print('-' * 50)
    
su = 0
while su < 10:
    su += 1
    if su%2 == 0:
        continue
    print(su)


    