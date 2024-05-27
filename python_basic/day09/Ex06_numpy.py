# 전치 연산 : 행렬 교환
#            T 속성 사용함 => 2차원배열변수.T
# 2차원배열의 행과 열을 바꿀때 사용 : 2행 3열.T => 3행 2열
import numpy as np

ar = np.array([[1,2,3],[4,5,6]]) # 2행 3열
print(ar)
print(ar.shape)  #(2,3)
print(ar.T)
print(ar.T.shape)  #(3,2)
print("-" * 50)

# 1차원 배열을 다차원배열로 변경할 때 reshape 함수 사용( 전체 크기(갯수)는 변경되지 않는다.)
ar = np.arange(12) # 0-11
print(ar, len(ar))
print("-" * 50)

bar = ar.reshape(3,4)
print(bar)
print(len(bar))
print("-" * 50)

bar2 = ar.reshape(2,3,2)
print(bar2)
print(len(bar2))
print("-" * 50)

bar3 = ar.reshape(4,-1)  # 전체 갯수와 첫번째 값을 가지고 계산에 의해서 결정됨(-1 일 경우)
print(bar3)
print("-" * 50)

# 다차원배열을 1차원배열롤 변경 :  flatten 함수, ravel 함수
bar4 =  np.arange(12).reshape(3,4)
print(bar4)
print(bar4.flatten())
print(bar4.ravel())
print("-" * 50)


bar5 = np.arange(12).reshape(2,3,2)
print(bar5)
print(bar5.flatten())
print(bar5.ravel())
print("-" * 50)

# flatten함수와 reavel 함수 차이점
ori_arr = np.array([[1,2,3],[4,5,6]])
f_arr = ori_arr.flatten()
r_arr = ori_arr.ravel()

# 차이를 보기 위해서 원본을 변경하자.
ori_arr[0,0] = 100     # 맨 처음
ori_arr[-1,-1] = 600   # 맨 끝

print(ori_arr)
print(f_arr)    # 원본이 변경되어도 변경되지 않는다. (복사해서 사용)
print(r_arr)    # 원본이 변경되면 같이 변경된다.