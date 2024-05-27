import numpy as np

# 벡터의 내적 : 두 벡터의 차원이 같아야 한다. 
#              각 요소의 곱을 모두 더한 것이다.
#              dot 함수 사용 = > 결과는 스칼라 ( a = 28)

a = np.array([2,5,1])
print(a, type(a))

b = np.array([4,3,5])
print(b, type(b))

print(np.dot(a,b.T))
print("-" * 50)

# matrix 곱셈 : 행렬 곱셈 (matmul())
c = np.array([[2,1],[1,4]])
d = np.array([[1,2,3],[0,1,2]])
print(np.matmul(c,d))  