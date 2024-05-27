import pandas as pd

city = pd.Series([9857426, 1502227, 2475231, 3470653], index=["서울", "대전", "대구","부산"])

# in : 주로 검색 용도로 사용
print("서울" in city) # True
print("수원" in city) # False
print("-" * 50)

for k, v in city.items():
    print("{0} = {1}" .format(k,v))
    
print("-- 딕셔너리 객체에서 시리즈 생성 --")    
dic = {"서울":10022181 , "대전":1518775, "대구":2487829, "부산":3513777}
city2 = pd.Series(dic)
print(city2)

print("-- 인덱스 기반의 연산 (시리즈) ---")
res = city - city2 
print(res)

print("-- 인덱스 기반의 연산 (리스트) ---")
res2 = city.values - city2.values
print(res2)
print("-" * 50)

# 디셔너리는 순서가 없다. 순서를 주려면 index 사용 (NaN = Not a Number)
# dic2 = {"서울":10022181 , "대전":1518775, "대구":2487829, "부산":3513777, "인천" : 2925815}
city3 = pd.Series({"서울":10022181 , "대전":1518775, "대구":2487829, "부산":3513777, "인천" : 2925815}, 
                  index=["서울","대전","대구","부산","인천"])
res3 = city - city3 
print(res3)
print("-" * 50)

print(res3.notnull())  # 데이터가 있으면 True, 데이터가 없으면 False
print("-" * 50)

print(res3[res3.notnull()])  # 데이터가 없으면 출력하지 말아라


print("-- 인덱스 기반의 연산 데이터 개싱, 추가 , 삭제---")
city2["부산"] = 7773513
print(city2)

city2["광주"] = 2015513
print(city2)

del city2["서울"]
print(city2)






