class One :
    def func01(self):
        print(1)
        
        
    def play(self):
        print("놀다")

class Two(One):
    def func02(self):
        print(2)

class Three(One):
    def func03(self):
        print(3)
        
        # 부모메서드 호출 : super()
        super().func01()
        super().play()

if __name__ == "__main__":
    two = Two()
    two.func02()   
    two.func01()
    two.play()
    print("-" * 50)
    
    three = Three()
    three.play()