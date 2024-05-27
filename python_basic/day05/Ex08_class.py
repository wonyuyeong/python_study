class Calc : 
    def add(self, s1, s2) :
        return s1 + s2
    def sub(self, s1, s2) :
        return s1 - s2
    def mul(self, s1, s2) :
        return s1 * s2
    def div(self, s1, s2) :
        return s1 / s2

calc = Calc()

while True : 
    su1 = int(input("수1 : "))
    su2 = int(input("수2 : "))
    op = input("연산자 : ")
    result = 0
    
    if op=="+" :
        result = calc.add(su1,su2)
    elif op == "-" :
        result = calc.sub(su1,su2)
    elif op == "*" :
        result = calc.mul(su1,su2)
    elif op == "/" :
        try :
            result = calc.div(su1,su2)
        except Exception as e :
            print("0으로는 나눌 수 없습니다.")
    
    if(op=="+" or op=="-" or op=="*" or op=="/") :
        print("{0} {1} {2} = {3}".format(su1,op,su2,result))
    else:
        print("제대로 입력하세요")
    
    msg = input("계속할까요 ?(y/n)")
    if(msg == "n"): break
    