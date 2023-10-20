#print reverse and find sum!
# x=int(input(print("Enter num!")))
# sum=0
# reversed_num=0
# while x!=0:
#     digit=x%10
#     sum = sum+digit
#     reversed_num = reversed_num*10+digit
#     x//=10

# print("Reverse num  and sum = ",reversed_num,sum)        

#using function cal sum !
# def sum(x,y):
#     return x+y

# def devide(x,y):
#     return x/y
# x=int(input(print("Enter num 1!")))
# y=int(input(print("Enter num! 2")))
# print(sum(x,y))
# print( devide(x,y))


#print even and odd num in paticuler range
# print("Even numbers !")
# for i in range (0,75,2):
#     print(i,end=" ") 


# print("\nodd numbers !")
# for i in range (1,75,2):
#     print(i,end=" ")     

#find the prime num!
# n=int(input(print("Enter num != ")))
# count=0
# for i in range (2,a) :
#     if n%i==0 :
#         count=count+1
#         print(i)

# if count ==0 :
#     print("%d is a prime number" %a)

# else :
#     print("It is not prime num")    

# for i in range(1,4,1):
#     for j in range(1,i+1,1):
#         print("*",end =" ")
#     print("\n")


a=int(input(print("Enter num != ")))
count =0
for i in range(1,a+1,1):
    count=0
    for j in range(1,i+1,1):
        if(i % j == 0):
            count=count+1
    if (count==2):
        print(j)       

