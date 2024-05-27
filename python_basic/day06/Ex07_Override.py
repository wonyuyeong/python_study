# 메서드 오버라이딩 : 부모클래스의 메서드와 같은 이름으로 자식 메서드를 만들지만 내용이 다른 것

class Animal():
    name = "휴먼"
    def sound(self):
        print("Hi~~~~")
    def eat(self):
        print("먹는다")
        
class Cat(Animal):
    name = "삼색이"
    def sound(self):
        print("냐옹~~")
    def prn(self):
        print(self.name)
                
class Dog(Animal):
    def sound(self):
        print("먕먕~~")
    def prn(self):
        print(self.name)    # 따로 선언을 안했기때문에 휴먼
        print(super().name) # 휴먼

if __name__ == "__main__":
    cat = Cat()
    cat.sound()
    cat.prn()
    print("-" * 50)
    
    dog = Dog()
    dog.sound()
    dog.prn()

