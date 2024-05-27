import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ax1.set_xlim([0., 8.])   # x축, 0-8 까지 표현
ax1.set_ylim([0., 40.])  

# 점찍기( # 마커는 제한적인 특수 문자 사용 가능 : ^, *, o, x)
# ax1.plot(4,20, 'o', c='red')
# ax1.plot(2,10, 'x', c='darkgreen')

x = np.array([1,3,5,7])
y = np.array([10,25,15,30])

# ax1.plot(x,y)   # 꺾은선 그래프

# 이때 'ob' 색과 마커를 한번에 지정
# ax1.plot(x,y,'ob')  # 점

# 분포도에서 만힝 사용
ax1.scatter(x,y,marker='*', color="red")


plt.show()