# 3. print even and odd by user given range and cal sum and product !

x=int(input("Enter intical range(num): "))
y=int(input("Enter final range(num): "))
sum=0
pro=1

print("The even numbers[%d-%d] are" %(x,y))
for i in range(x,y+1):
    if i%2==0 :
        print(i)
        sum=sum+i
        pro=pro*i
print("Tne sum of even num  [%d-%d]  = " %(x,y),sum)
print("Tne pro of even num  [%d-%d]  = " %(x,y),pro)  

sum=0
pro=1
print("\n")
print("The odd numbers[%d-%d] are" %(x,y))
for i in range(x,y+1):
    if i%2!=0 :
        print(i)
        sum=sum+i
        pro=pro*i
print("Tne sum of odd num  [%d-%d]  = " %(x,y),sum) 
print("Tne product of odd num  [%d-%d]  = " %(x,y),pro)  


# if x%2==0 :
#     print("The even numbers[%d-%d] are" %(x,y))
#     for i in range(x,y+1,2):
#         print(i)
#         sum=sum+i
#         pro=pro*i
#     print("Tne sum of even num  [%d-%d]  = " %(x,y),sum)
#     print("Tne pro of even num  [%d-%d]  = " %(x,y),pro)    
    

# else :
#     print("The odd numbers[%d-%d] are" %(x,y))
#     for i in range(x,y+1,2):
#         print(i)
#         sum=sum+i
#         pro=pro*i
#     print("Tne sum of odd num  [%d-%d]  = " %(x,y),sum) 
#     print("Tne product of odd num  [%d-%d]  = " %(x,y),pro)    
   
    
        



