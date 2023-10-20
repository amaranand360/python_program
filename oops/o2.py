class programmer:
    compeny = 'microsoft'
    
    def __init__(self,name,salery,id,product) :
        self.Name = name
        self.Salery = salery
        self.Id = id
        self.Product = product

    def getinfo(self):
        print(f"The name of {self.compeny} programmer is{self.Name} his salery is {self.Salery}, his id is {self.Id} and product is {self.Product}.\n")

        

def inputinfo(ob_NAME) :
    name =input("Enter your name:")
    salery=input("Enter your salery:")
    ids = input("Enter your id:")
    product=input("Enter your product!:")

    ob_NAME = programmer(name,salery,ids,product)   #object creaction .
    ob_NAME.getinfo()                               #printing info using object.
    return 

# main part ----------------------------------------------------------------------------------
print("Wellcome TO OBJECT Oraintaited programming in python!")
n = int(input("Enter your no of empoley!"))
for i in range (0,n) :
    ob_NAME =input("Enter your empoley object name : ")
    inputinfo(ob_NAME)

