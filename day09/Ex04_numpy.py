import numpy as np
# 확률분포
import scipy.stats as sp

x = np.array([18, 5, 10, 23, 19, -8, 10, 0, 0, 5, 2, 15, 8,
2, 5, 4, 15, -1, 4, -7, -24, 7, 9, -6, 23, -13,
1, 0, 16, 15, 2, 4, -7, -18, -2, 2, 13, 13, -2,
-2, -9, -13, -16, 20, -4, -3, -11, 8, -15, -1, -7, 4,
-4, -10, 0, 5, 1, 4, -5, -2, -5, -2, -7, -16, 2,
-3, -15, 5, -8, 1, 8, 2, 12, -11, 5, -5, -7, -4], dtype='f') # dtype='i' => 정수, dtype='f' 실수로 형변환

print(x)
print("요소의 개수 : ", len(x))
print("산술평균 : ", np.mean(x))
# 데이터가 평균에서 얼마나 퍼져있는지 측정
print("분산 : ", np.var(x))
# 데이터의 변이 정도 (분산의 제곱근을 이용)
print("표준편차 : ", np.std(x))
print("최대값 : ", np.max(x))
print("최소값 : ", np.min(x))
print("중앙값 : ", np.median(x))    # 2사분위 수 와 같다
print("1사분위 수 : ", np.percentile(x, 25))    # 25%
print("2사분위 수 : ", np.percentile(x, 50))    # 50%
print("3사분위 수 : ", np.percentile(x, 75))    # 75%
print("4사분위 수 : ", np.percentile(x, 100))    # 100%