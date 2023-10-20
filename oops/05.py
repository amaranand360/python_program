#inheritance
#1.Single inheritance:
# class Coder :
#     collage = "DSU"

#     def intro(self):
#         print("This is a proggmer class.||main parent-class!")

# class ctpy(Coder) :
#     name ="CTPY"
#     course_code ="23CS205"
#     creadit = 3

#     def intro(self):
#         print("THIS is a python class || child class!")


# p = Coder()
# c= ctpy()
# p.intro()
# c.intro()     
# print(c.collage)        

#2.Multiple Inheritance:
# class Coder :
#     collage = "DSU"
#     name ="AMAR"

#     def __init__(self,m,r) :     
#            self.nam=m
#            self.sal=r
#     def printdata(self) :
#         print(self.nam,self.sal)         

#     def info(self):
#         print("This is a codeaing-class.||main parent-class!")

#     def intro(self):
#         print("This is a proggmer class.||main parent-class!")    

# class ctpy :
#     name ="CTPY"
#     course_code ="23CS205"
#     creadit = 3
#     def __init__(self,n,id,s) :     
#            self.name=n
#            self.idee=id
#            self.salery=s

#     def printdetails(self) :
#         print(self.name,self.idee,self.salery)                 

#     def info(self):
#         print("This is a ctpy-class.||main parent-class!")

#     def intro(self):
#         print("THIS is a compucation-thinging-in-python class || child class!")

# class python(ctpy,Coder) :

#     def __init__(self,i,n,id,s,m,r) : 
#         Coder.__init__(self,m,r)  
#         ctpy.__init__(self,n,id,s)
#         self.age=i

#     def introduction(self):
#         print("This is a python class.|| It is multiple-type-class!")



# ris = python(18,"amar","eeeng32","18000","ANAND",800000)
# print(ris.age)
# ris.printdetails()
# ris.printdata()

# print(ris.collage)
# print(ris.name)
# print(ris.course_code)
# print(ris.creadit)
# ris.info()
# ris.intro()

#3.Multilevel inheritance
# class Coder :
#     collage = "DSU"
#     name ="AMAR"

#     def info(self):
#         print("This is AMAR codeaing-class.||main parent-class!")

#     def intro(self):
#         print("This is a proggmer class.||main parent-class!")    

# class person(Coder) :
#     name ="CTPY"
#     course_code ="23CS205"
#     creadit = 3
#     def info(self):
#         print("This is a python-class.||main parent-child-class!")


# class amar(person) :

#     def introduction(self):
#         print("This is a python class.|| It is multilevel-type-class!")

# anand = amar()
# print(amar.collage)
# print(amar.name)
# print(amar.course_code)
# anand.introduction()
# anand.info()
# anand.intro()

#4.Hierarchical inheritance.
# class empoley:
#     compeny = "Microsoft"
#     salery = 90000
#     def introduction(self):
#         print("This is a empoley class.|| It is a parent-class!")

# class amar(empoley):
#     idee = "micr132348"
#     wp = "softwere-eng" 
#     salery = 100000
#     def introduction(self):
#         print("This is a empoley-child class.|| It is a parent-child-class!")    

# class md(empoley):
#     idee = "micro484623" 
#     wp = "developer"  
#     salery = 20000000
#     def introduction(self):
#         print("This is a another child- class.|| It is a parent-child-class!")

# class ris(empoley):
#     idee = "micro454563" 
#     wp = "test-eng"  
#     salery = 1800000
#     def introduction(self):
#         print("This is a ris class child of empoley class.|| It is a parent-child-class!")

# am = amar()
# print(am.compeny)
# print(am.idee)
# print(am.salery)
# print(am.wp)
# am.introduction()

# amd = md()
# print(amd.compeny)
# print(amd.idee)
# print(amd.salery)
# print(amd.wp)
# amd.introduction()


# mr = ris()
# print(mr.compeny)
# print(mr.idee)
# print(mr.salery)
# print(mr.wp)
# mr.introduction()

#5.Hybrid Inheritance
class empoley:
    compeny = "Microsoft"
    salery = 90000
    def introduction(self):
        print("This is a empoley class.|| It is a parent-class!")

class amar(empoley):
    idee = "micr132348"
    wp = "softwere-eng" 
    salery = 100000
    def introduction(self):
        print("This is a empoley-child class.|| It is a parent-child-class!")    

class md(empoley):
    idee = "micro484623" 
    wp = "developer"  
    salery = 20000000
    def introduction(self):
        print("This is a another child- class.|| It is a parent-child-class!")

class ris(amar,md):
    # idee = "micro454563" 
    # wp = "test-eng"  
    # salery = 1800000
    def introduction(self):
        print("This is a ris class child of empoley class.|| It is a parent-child-class!")

print(issubclass(ris,amar))     #Return whether 'cls' is derived from another class or is the same class.
print(issubclass(ris,empoley))

# am = amar()
# print(am.compeny)
# print(am.idee)
# print(am.salery)
# print(am.wp)
# am.introduction()

# amd = md()
# print(amd.compeny)
# print(amd.idee)
# print(amd.salery)
# print(amd.wp)
# amd.introduction()


mr = ris()
print(mr.compeny)
print(mr.idee)
print(mr.salery)
print(mr.wp)
mr.introduction()

