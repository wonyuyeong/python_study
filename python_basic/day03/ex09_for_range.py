# for문과 함께 자주 사용하는 range 함수

su = range(10)
print(su, len(su))      # range(0,10) : 0 부터 10 미만

for i in su :
    print("i=", i)

# 5단 출력
for i in range(1, 10):
    print("5 * {0} = {1}" .format(i, i*5))

print("-" * 50)

# 구구단
for i in range(2,10):
    for j in range(1,10):
        print("{0} * {1} = {2}" .format(i,j,i*j), end = "    ")    # 줄바꿈 안함
        print()     # 줄바꿈
        

