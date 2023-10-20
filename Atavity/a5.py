# def difference(n):
#     if n <= 17:                #function exeample
#         return 17 - n
#     else:
#         return (n - 17) * 2
# n = int(input("ENter a number: "))        
# print(difference(n))    
#-----------------------------------------------------------------------------------------------------------------------

# for i in range(10):            # it take range by defalut 0to10 and print and break the loop when reached at 7
#     if i == 7:
#         break
#     print(i)

# for i in range(10):            # it take range by defalut 0to10 and print and skip 6 and continue the program
#     if i == 6:
#         continue
#     print(i)    

# for i in range(10):            # it take range by defalut 0to10 and print and pass is alow print
#     pass    
#     print(i)

while True:
    print("I am a programmer")
    break
while False:
    print("Not printed because while the condition is already flase") 
    break


n = int(input("Enter number= "))
x=1                       # inctionalization    
pro =1
sum = 0        
while x <=n :              # condition
    print (x)
    sum = sum+x             #opreactions
    pro=pro*x  
    x=x+1             # increament or decreament 
print ("I like Python.")
print("sum = ",sum)
print("%d ! = %d" %(n,pro)) 


