# 시계열 데이터(시리즈=Series=numpy의 1차원) 나 데이터프레임(DataFrame = numpy의 2차원 = 행렬)

import pandas as pd

# 시리즈 생성
# 2017년 도시별 인구 데이터
lie = [9857426,1502227, 2475231, 3470653]
city = pd.Series(lie)
# city = pd.Series(lie)
print(city, type([9857426,1502227, 2475231, 3470653]))
print("-" * 50)                 

# index = 인덱스 레이블(라벨)
city2 = pd.Series([9857426,1502227, 2475231, 3470653], index=["서울", "대전", "대구","부산"])
print(city2, type(city2))  
print("-" * 50)   

print(city2.index)    # 인텍스 출력        
print(city2.values)   # value 출력

city2.name = "도시별 인구수"
print(city2)
