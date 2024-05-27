# 최대값 구하기
# 입력 : 숫자가 n개 들어있는 리스트
# 출력 : 숫자가 no 중 가장 큰 값

def find_max(lis) :
    n = len(lis)        # 매개변수 길이 구하자.
    max_v = lis[0]      # 첫번째 값을 최대값으로 기억시킨다.
    for i in range(1,n):
        if(lis[i] > max_v) :
            max_v = lis[i]
    return max_v

lis = [17,92,18,323,55,45,90]
print(find_max(lis))

# 두번이상 나온 이름 찾기
# 입력 : 이름이 n개 들어있는 리스트
# 출력 : 중복되는 이름의 집합(set)

def find_same_name(lis2) :
    n = len(lis2)
    result = set()  # 결과를 set에 저장하기 위해서 빈 set
    for i in range(0, n-1) :
        for j in range(i+1, n) :
            if(lis2[i] == lis2[j]) :
                result.add(lis2[i])     # 추가할 때 : list=>append,  set=>add
    return result
    
name = ["Tom", "Jerry", "Mike", "Tom", "hong", "Mike"]
print(find_same_name(name))