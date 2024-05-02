# csv 에 with 사용하기

import csv

with open("day04/data/csv02.csv", "w", encoding="utf-8", newline='') as f1 :
    wr = csv.writer(f1)
    wr.writerow(["1", "hong", "270", "90"])
    wr.writerow(["2", "won", "240", "80"])
    wr.writerow(["3", "lee", "255", "85"])
    wr.writerow(["4", "kim", "285", "95"])
    wr.writerow(["5", "park", "210", "70"])

with open("day04/data/csv02.csv", "r", encoding="utf-8") as f2 :
    rd = csv.reader(f2)
    for i in rd :
        print(i)
print('-' * 50)

lines = []
with open("day04/data/csv02.csv", "r", encoding="utf-8") as f3 :
    rd = csv.reader(f3)
    for i in rd :
        if(int(i[3])>=90) :
            i.append("A학점")
            i.append("우수자")
        elif(int(i[3])>=80) :
            i.append("B학점")
        elif(int(i[3])>=70) :
            i.append("C학점")
        else :
            i.append("F학점")
            
        lines.append(i)
print("-" * 50)

with open("day04/data/csv02_e.csv", "w", encoding="utf-8", newline='') as f4 :
    wr = csv.writer(f4)
    wr.writerows(lines)
            

