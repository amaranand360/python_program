class Rectangle:
    
    
    def __init__(self,l,b):
        self.length = l
        self.width = b

    def Perimeter(self,l,b):
        self.perimeter = 2*(l+b)
        self.area = l*b

    def display(self):
        print("Length = ",self.length)
        print("Width = ",self.width)
        print("Perimeter = ",2*((self.length)+(self.width)))
        print("Area = ",(self.length)*(self.width))

class parallelpired(Rectangle):
    height = 10
    def __init__(self,l,b):
        self.length = l
        self.width = b
    def Display(self):
        print("Volume = ",(self.length)*(self.width)*(self.height))

obj = Rectangle(5,8)
obj.display()
obj2 = parallelpired(5,8)
obj2.Display()
