class Car :
    def __init__(self) :
        self.color = "red"
        self.wheel = 24
        self.cc = 2500
        
    def forward(self):
        print("앞으로 50km 전진")
    
    def backward(self):
        pass

# main 함수 => 시작위치,    
if __name__ == "__main__" :
    myCar = Car()
    print(myCar.color)
    print(myCar.wheel)
    print(myCar.cc)
    
    myCar.forward()
    myCar.backward()