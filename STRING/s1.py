# #count length of string wihout using built function!
# def string_length(string1):
#     count = 0
#     for char in string1:
#         count += 1
#     return count
# string1=str(input("Enter string without using space: "))    
# print("Lenght of string= ",string_length(string1))

#printint every char in string!
# fruit=str(input("Enter string without using space: "))    
# index = 0
# while index < len(fruit) :
#     letter = fruit[index]
#     print(letter,":",index)
#     index = index + 1



# #inseting another string in between string !
# name=input("Enter your string: ")
# str1=name[0:len(name)//2]
# newstr=input("Enter new string: ")
# str2=name[len(name)//2:]
# print(str1+newstr+str2)    


name="amaRKUmar"
upper1=[]
lower2=[]
for latter in name :
    if latter.isupper():
        upper1.append(latter)
    else :
        lower2.append(latter)
li=lower2+upper1
print(li)

for element in li:
    str = str + element
str3=''.join(li)    
print(str)
print(str3)

#str1="I am amar ! and amar is a smart boy amar anand is the nick name and amar kumar is the full name"

