#3.Multilevel inheritance
class Coder :
    collage ="DSU"
    name ="AMAR"

    # def __init__(self,n,i,s) :     
    #     self.name=n
    #     self.idee=i
    #     self.salery=s

    # def printdetails(self) :
    #     print(self.name,self.idee,self.salery)  

    def info(self):
        print("This is codeaing-class.||main parent-class!")

    def intro(self):
        print("This is a proggmer-class.||main parent-class!")    

class person(Coder) :
    name ="CTPY"
    course_code ="23CS205"
    creadit = 3
    # def __init__(self,n,i,s):
    #     super().__init__(n,i,s)
    def info(self):
        super().info()
        print("This is a person-class.||main parent-child-class!")


class amar(person) :

    def info(self):
        super().info()
        print("This is a amar-class.|| It is multilevel-type-class!")


c= Coder()
c.info()

#p = person("AMAR","eng21cs0030",1800000)
p= person()
p.info()

a = amar()
a.info()
