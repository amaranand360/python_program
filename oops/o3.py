class calculator :
    def __init__(self,number) :
        self.num=number

    def squre(self) :
        print(f"The squre value of {self.num} = {self.num **2}")

    def squreroot(self):
        print(f"The squre root value of {self.num} = {self.num **0.5}")

    def qube(self) :
        print(f"The qube value of {self.num} = {self.num **3}")

    def fact(self) :  
        fact=1
        #x = self.num
        for i in range (1,self.num+1) :
            fact = fact*i
        print(f"The factroial of {self.num} = {fact}")

    @staticmethod       #without using self keyword.
    def greet():
        print("***********************Wellcome to calucaltion world*********************")

            
n = int(input("Enter a number "))
a = calculator(n) 
a.greet()
a.squre()
a.qube()
a.fact()
a.squreroot()
