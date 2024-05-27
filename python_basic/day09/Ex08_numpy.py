import numpy as np

# # 브로드캐스팅
# # 백터(행렬)끼리 덧셈 또는 뺄셈을 하려면, 행과 열의 갯수가 같아야 함 (원칙)
# # numpy 에서 행과 열이 다른 백터 끼리도 연산이 가능하도록 지원 => 이 기능을 브로드캐스팅이라고 한다.
# # 크기가 작은 백터가 자동으로 크기가 큰 백터의 행과 열 개숫와 맞춰짐(확장)

# x = np.arange(5)
# print(x)

# y = np.ones_like(x)
# print(y)
# print("-" * 50)

# print(x + y)
# print(x + 5)
# print("-" * 50)

# # 배열 연결 : 두 개이상의 배열들을 연결해서 하나의 큰 배열을 만듦
# #            hstack, vstack, dstack ,statck

# # hstack(horizental stack) : 행의 갯수가 같은 2차원배열을 좌우으로(가로) 합칠때 사용 => 열 갯수가 늘어나게 됨
# ar1 = np.ones((2,3))
# print(ar1)

# ar2 = np.zeros((2,2))
# print(ar2)

# print(np.hstack([ar1, ar2]))
# print("-" * 50)

# # vstack(vertital stack) : 열의 개숫가 같은 2차원 배열들을 위아래로 (세로) 합칠때 사용 => 행 갯수가 늘어나게 됨
# ar3 = np.ones((2,3))
# print(ar3)

# ar4 = np.zeros((3,3))
# print(ar4)

# print(np.vstack([ar3, ar4]))
# print("-" * 50)

# # dstack(depth statck) : depth = 면 (차원)
# #                        2차원배열 여러 개를 깊이(depth) 방향으로 합칠때 사용
# #                        a행 X b열 배열의 갯수가 n개 합치면 , 결과는 a면 x b행 x n 열이 된다.
# ar5 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12] ])
# print(ar5)

# ar6 = np.array([[5,6,7,8],[9,10,11,12],[1,2,3,4]])
# print(ar6)
# print("-" * 50)

# ar7 = np.dstack([ar5, ar6])
# print(ar7)
# print(ar7.shape)  # (면, 행, 열)
# print("-" * 50)

# # stack : a행 x b열 x n개  = n면 a행 b열
# # axis : 0=> 면, 1=>행 , 2 => 열

# ar8 = np.stack([ar5, ar6])
# print(ar8)
# print(ar8.shape)  # (면, 행, 열)
# print("-" * 50)  

# 난수 발생 : 하나의 프로그램에서 여러사람이 난수를 발생하면 그때 마다 다른 값이 나온다.
#            이렇게 다른 값이 나온 것을 방지하기 위해서 사용  
# np.random.seed(인수=정수 = 시작값지정)
np.random.seed(5)

print(np.random.rand(5))

# 난수 7개 생성 ( 0.0 <= 난수 < 1.0 )
print(np.random.rand(6))

# 데이터 섞기 (shuffle)
x = np.arange(10)
print(x)

np.random.shuffle(x)
print(x)
