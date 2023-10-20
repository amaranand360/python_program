# str ="AMAR123anand86"
# mydict = {
#     'letter' : 0,
#     'digits' : 0,
#     'lower' : 0,
#     'upper' : 0,

# }

# for i in str:
#     if i.isalpha():
#         mydict['letter'] = mydisk['letter']+1
#     if i.isdigit():
#         mydict['digits'] = mydisk['digits']+1
#     if i.isupper():
#         mydict['upper'] = mydisk['upper']+1
#     if i.islower():
#         mydict['lower'] = mydisk['lower']+1
        
# print(mydict)

#************************************************

# text =input("Enter the sentence:")
# dict ={}

# for i in text:
#     if(i in dict):
#         dict[i] =dict[i]+1
#     else:
#         dict[i]=1

# print(dict)

#********************************************************
# text = "MY name is AMAR"
# li = (text.split( ))
# l2 =[]
# for i in li:
#     l2.append([li[i],i])
# print(l2)    

# str="Hello how are you"
# count = 0
# for i in str:
#     if i == 'o':
#         count=count+1
# print("Count of o:",count)

# a=input("enter the string:") 
# b={} 
# c=a.split()
# for i in c: 
#     if i not in b : 
#         b[i]=1 
#     else: 
#          b[i]=b[i]+1 
# print("frequency of the words in a string") 
# for k in b: 
#     print(k,':',b[k])

class student:
    # name ="AMAR KUMAR"
    # rollno=30
    def __init__(self,name,rollno):
        name = self.name
        roolno=self.rollno
    def getinfo(self):
        print(f"name:{self.name}\nRoll_no:{self.rollno}\nage={self.age}\nmarks={self.marks}.")

    def getage(self):
        self.age=input("Enter age:")
    
    def getmarks(self):
        self.marks=input("Enter marks: ")

s = student()
s.getage()
s.getmarks()
s.getinfo()

