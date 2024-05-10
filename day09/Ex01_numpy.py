# numpy 모듈 : 대규모, 다차원배열을 다루기 위한 모듈
#              기본적으로 array라는 자료형을 사용함(행렬의 개념과 비슷함)
#              아나콘다 설치시 함께 설치됨, (개인적으로 설치 시 터미널에 pip install numpy)
#              import numpy as np 호출
#              리스트 자료형과 아주 유사함(인덱싱과 슬라이싱)

import numpy as np

# 1차원 배열 다루기 : numpy array([한가지 종류가 저장된 리스트])
#                     리스트를 배열로 바꾸어서 사용함
# 배열변수 = np.array([list])
# 배열변수 : 할당된 배열공간의 주소를 참조하는 레퍼런스 변수임 (주소저장변수)
# 배열로 만들 리스트는 반드시 정수 | 실수 값들로만 구성되어 있어야 한다.
'''
    리스트 : -, / 연산 불가능
             + 연결 , * 반복연산
    
    배열 : 사칙연산 모두 가능
'''

# 정수
ar = np.array([0,1,2,3,4,5])
# numpy.ndarray 는 다차원배열구조 => 선형대수 계산에 이용
print(ar, type(ar))
print("-" * 60)

# 실수
ar = np.array([0.1, 1.1, 2.1, 3.1, 4.1, 5.1])
# numpy.ndarray 는 다차원배열구조 => 선형대수 계산에 이용
print(ar, type(ar))
print("-" * 60)

# 정수+실수 => 다 실수로바뀜
ar = np.array([0.1, 1, 2.1, 3, 4.1, 5])
# numpy.ndarray 는 다차원배열구조 => 선형대수 계산에 이용
print(ar, type(ar))
print("-" * 60)

# str+정수+실수  => str (자료형을 하나로 통일 시킨다.)
ar = np.array(['a', 'r', 1, 3.4])
# numpy.ndarray 는 다차원배열구조 => 선형대수 계산에 이용
print(ar, type(ar))
print("-" * 60)

# 스칼라 : 크기만 가지고 방향은 가지고 있지 않은 양, a= 24
# 벡터 : 크기와 방향을 가지고 있는 양, 
# 리스트일때 벡터와 연산 처리의 예
dataList = [0,1,2,3,4,5,6,7,8,9]

# 리스트 요소를 2배로 증가 하자
for i in dataList:
    dataList[i] = i * 2

print(dataList)

# 리스트를 배열로 만들어서 각 요소를 2배로 증가하자.
dataList2 = [0,1,2,3,4,5,6,7,8,9]
ar = np.array(dataList2)
print(ar * 2)

# 만약에 리스트를 배열처럼 사용하면 각 요소가 2배로 증가하지 않는다
print(dataList2 *2)
print("-" * 60)

a = [1,2,3,4,5]
b = np.array(a)

print(a+a)  # 반복
print(b+b)  # 실제 계산됨

print(a*2)  # 반복
print(b*2)  # 실제 계산됨

# 배열은 비교연산, 논리연산, 산술연산이 가능
ar1 = np.array([1,2,3])
br1 = np.array([10,20,30])

print(2 * ar1 + br1)        # 2*ar[0]+br[0] = 12
print(ar1 == 2)             # [False True False]
print(br1 == 2)             # [False False False]
print(ar1 >= 2)             # [False True True]
print((ar1 ==2) & (br1 >10)) # ar1[0] == 2(F) & br1[0]>10(F) => False       [False True False]