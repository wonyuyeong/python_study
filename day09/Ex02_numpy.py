# numpy는 ndarray 클래스를 사용한다.(다차원배열 = N차원 배열)

import numpy as np

# 2차원 배열
# 1차원 배열 여러개(행별의 열의 개수가 같아야한다.)를 하나로 묶은 것
# 행과 열로 구성된 행렬(matrix) 형태
# [[...], [...], [...]] : 리스트 안 리스트

two_ar = np.array([[0,1,2], [3,4,5]]) # 2행 3열
# 열의 개수가 다르면 오류
# two_ar = np.array([[0,1,2], [3,4,5,6,7]])
print(two_ar, type(two_ar), two_ar.shape)
print("행의 갯수 : {0}" .format(len(two_ar)))
print("각 행별 열의 갯수 : {0}" .format(len(two_ar[0])))

# 2차원 배열의 각 값에 접근하기 : 배열변수[행 index][열 index]
# print(two_ar[0][0])
for i in range(0, len(two_ar)) : 
    for j in range(0, len(two_ar[i])):
        print('two_ar[{0}{1}] : {2}' .format(i,j,two_ar[i][j]))

# 3차원 배열 만들기
# 값의 종류가 같고, 행과 열 갯수가 동일한 2차원 배열들의 묶음
# 행, 열, 면
three_ar = np.array([[[1,2,3,4], [5,6,7,8], [9,10,11,12]],                      # 0면
                        [[10,20,30,40], [50,60,70,80], [90,100,110,120]],])     # 1면
print(three_ar)
print(three_ar.shape)   # 2행 3열 4면(2,3,4)
print("depth : ", len(three_ar))        # 면의 개수
print("row : ", len(three_ar[0]))       # 행의 개수
print("col : ", len(three_ar[0][0]))    # 열의 개수

# 3차원 배열의 각 값에 접근하기 : 배열변수[면 index][행 index][열 index]
for i in range(0, len(three_ar)):
    for j in range(0, len(three_ar[i])):
        for k in range(0, len(three_ar[i][j])):
            print('three_ar[{}{}{}] : {}' .format(i,j,k,three_ar[i][j][k]), end=" ")
        print()
    print("================================================================================================")
    
# 크기가 다른 두 행렬의 연산 지원
a1 = [[1,1,1], [2,2,2], [3,3,3]]
a2 = [1,2,3]
b1 = np.array(a1)
b2 = np.array(a2)
print(b1+b2) # [[2 3 4], [3 4 5], [4 5 6]]

# 배열의 차원(ndim)과 크기(shape) 알아내기
c1 = np.array([1,2,3,4,5])
c2 = np.array([[0,1,2], [3,4,5]])
c3 = np.array([[[1,2,3,4], [5,6,7,8], [9,10,11,12]],                     
                        [[10,20,30,40], [50,60,70,80], [90,100,110,120]],]) 

print(c1.ndim)
print(c1.shape)

print(c2.ndim)
print(c2.shape)

print(c3.ndim)
print(c3.shape)

