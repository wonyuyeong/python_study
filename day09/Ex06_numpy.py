# 전치 연산 : 행렬 교환
#             T 속성 사용함 => 2차원배열변수.T
# 2차원배열의 행과 열을 바꿀 때 사용 : 2행 3열.T => 3행 2열
import numpy as np

ar = np.array([[1,2,3], [4,5,6]]) # 2행 3열
print(ar)           # [[1 2 3] [4 5 6]]     => 2행 3열
print(ar.shape)     #(2,3)
print(ar.T)         # [[1 4] [2 5] [3 6]]   => 3행 2열
print(ar.T.shape)   #(3,2)

#