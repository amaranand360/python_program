class student :                                      # class defanation 
    def getdetails(self):                            #function 
        print(self.name,self.age,self.usn)
    
amar = student()                                     #object creaction.
amar.name="AMAR"
amar.age=18
amar.usn='Eng21cs0030'
amar.getdetails()                                   #function calling using the object.
    



#*********************************constructor*****************************************************
class Employe :
    def __init__(self,n,id,s) :     
           self.name=n
           self.idee=id
           self.salery=s

    def printdetails(self) :
        print(self.name,self.idee,self.salery)                 

md = Employe('RIS',56,10.5)                           #object creaction with parameater.
md.printdetails()                                     #consterctoer calling using the object.
