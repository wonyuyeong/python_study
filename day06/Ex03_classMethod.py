# 클래스메서드
# 객체를 생성하지 않아도 static 처럼 바로 사용 가능
# static 과 다른 점은 cls 라는 인자가 더 추가된다.
# cls 는 클래스를 가리킨다.
# @classmethod 라는 데코레이터를 사용

class Calc : 
    count = 0
    
    @staticmethod
    def plus(a,b):
        return a+b

    def minus(self, a,b) :
        return a-b
    
    @classmethod
    def mul(cls, a,b):
        return a*b
    
    @classmethod
    def countUp(cls):
        cls.count += 1
    @classmethod
    def countUp(cls):
        cls.count += 1
    
if __name__ == "__main__":
    # static은 객체 생성 없이 호출 가능
    print("{0} + {1} = {2}" .format(3,5,Calc.plus(3,5)))
    
    # instance 객체 생성 후 호출 가능
    c = Calc()
    print("{0} - {1} = {2}" .format(3,5,c.minus(3,5)))
    
    # classmethod
    print("{0} * {1} = {2}" .format(3,5,Calc.mul(3,5)))
    
    # classmethod
    Calc.countUp()
    print(Calc.count)
    
    
    
    
    