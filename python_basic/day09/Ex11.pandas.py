import pandas as pd

city = pd.Series([9857426,1502227,2475231,3470653], index=["서울", "대전", "대구", "부산"])

# in : 주로 검색 용도로 사용
print("서울" in city) # True
print("수원" in city)   # False
print("-" * 50)

for k, v in city.items():
    print("{0} = {1}" . format(k,v))
    