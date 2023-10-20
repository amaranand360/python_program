# x = int(input("Enter your age= "))
# if x<0 :
#     print("invalide input ! please try with valide input!")
# elif  x>=0 and x<=12 :
#     print("You are a kid!")
#     print("You are not able to give vote")
# elif x>12 and x<18 :
#     print("You are Boy/girl!")
#     print("You are not able to give vote")
# else :
#     print("You are an adult!")
#     print("You are able to give vote")
   

from ast import Or
c = input("Enter the color of light: ")
c = str(c)

if c == 'GREEN' or 'green' :
    print(" Car is allowed to go") 
elif c== 'YELLOW' or 'yellow' :
    print(" Car has to wait") 
elif c== 'purple' or 'PURPLE' :
    print(" Car has to wait")     

else :   
    print("Car has to stop") 



# import calendar
# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# print(calendar.month(y, m))