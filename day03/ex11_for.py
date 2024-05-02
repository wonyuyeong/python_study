# 데이터를 이용해서 합격자, 불합격자를 별도로 저장하자. (60 이상이면 합격)

# 리스트
t_list = [90,25,67,45,80]
success = []
fail =[]
for i in t_list:
    if(i>=60):
        success.append(i)
    else :
        fail.append(i)
print(success)
print(fail)

# 튜플 : 요소가 한번 정해지면 변경, 추가, 삭제 할 수 없다.
# t_tuple = (90,25,67,45,80)
# success = ()
# fail =()
# for i in t_list:
#     if(i>=60):
#         success.append(i)
#     else :
#         fail.append(i)
# print(success)
# print(fail)

# set
t_set = {90,95,67,45,80}
success = set()
fail = set()
for i in t_list:
    if(i>=60):
        success.add(i)
    else:
        fail.add(i)
print(success)
print(fail)   

# 딕셔너리
t_dic = {"홍길동" : 90, "일지매" : 25, "장길산" : 67, "임꺽정" : 45, "홍범도" : 80 }
success = dict()
fail = dict()
for i,j in t_dic.items():
    if(j>=60):
        success[i]= j
    else:
        fail[i] = j
print(success)
print(fail) 