# 리스트 컴프리헤션 : 표현식 for 항목 in 리스트 if 조건문

result = [i*10 for i in range(2,10)]
print(result, type(result))

result = [i*3 for i in range(1,11) if i%2 == 0]
print(result, type(result), len(result))