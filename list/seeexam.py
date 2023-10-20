# n= int(input("Enter total numbers: "))
# li =[]
# for i in range(n):
#     num = int(input("Enter the element (number): "))
#     li.append(num)
# print(li)
# sum =0
# pro =1
# i=0

# for index in li:
#     if li[i]%2 == 0 :
#         sum += li[i]
#         i = i+1

#     else :
#         pro = pro*li[i]
#         i = i+1

# print("Tne sum of all even numbers = ",sum)
# print("Tne product of all odd numbers= ",pro)



# num = int(input("Enter the  (number): "))
# sum = 0
# while(num != 0):
#     sum = sum + num%10
#     num = num//10
# print("Tne sum of all digits of number = ",sum)

# def inputfun():
#     a=float(input("Enter the marks of sub1: "))
#     b=float(input("Enter the marks of sub2: "))
#     c=float(input("Enter the marks of sub3: "))
#     ava = (a+b+c)/3
#     return ava

# print("Enter the marks of Test-1")
# test1 = inputfun()
# print("Enter the marks of Test-2")
# test2 = inputfun()

# if (test1 >= test2):
    
#     print("The test-1 is your best test with ava marks ",test1)

# else:
    
#     print("The test-2 is your best test with ava marks ",test2)

# a = int(input("Enter the 1-side lenght of traingle: "))
# b = int(input("Enter the 2-side lenght of traingle: "))
# c = int(input("Enter the 3-side lenght of traingle: "))

# if ( a == b and a == c):
#     print("It is a euileateral trangile")

# elif(a== b or a == c or b == c):
#     print("It is a isolease trangile")

# else:
#     print("It is a scalence trangile")


# def fact(num):
#     pro=1
#     for i in range(1,num+1,1):
#         pro = pro*i
#     return pro

# n = int(input("Enter the number which fact U want: "))
# fac = fact(n)
# print("The facterioal of %d is: %d" %(n,fac))

# f = open('ANAR.txt','r')
# data = f.read()
# print(data)
# f.close()


# li=[]
# for i in range(10,101,1):
#     if(i%2==0 and i%3==0):
#         li.append(i)
# print("The numbers which is divisable by 6 are")
# print(li)


# def countfun(word): 
#     count=0
#     count2=0
#     for char in str:
#         if char == 'a' or 'e' or 'i' or 'o' or 'u':
#             count = count+1
#         else:
#             count2 = count2+1
#     return count , count2

# str = input("Enter a word: ")
# print("Total no of vovels and consonenets are: ",countfun(str))


# li=[1,2,3,4,5]
# tup = (1.3,li,'ee')
# print(tup)

# marksdict = {
#     'student1':78,
#     'student2':80,
#     'student3':90
# }
# print(marksdict)
# updatedict ={
#     'student2':95
# }
# marksdict.update(updatedict)
# print(marksdict)





# i=0
# li=[]
# while(i < 5):
#     n = int(input("Enter a number: "))
#     li.append(n)
#     i=i+1
# print(li)


# def isprime(num):
#     j=2
#     count=0
#     while(j<=num):
#         if(num%j== 0):
#             count=count+1
#         j=j+1
#     return count 

    
# i=0
# while(i<5):
#     count = isprime(li[i])
#     if(count == 1):
#         print("%d is a prime number"%li[i])

#     if li[i]%2==0:
#         print("%d is a even number"%li[i])

#     elif li[i]%2!=0 :
#         print("%d is a odd number"%li[i])
#     i=i+1


# str = "CompShmnElob"
# newstr=" "
# li=[]
# for letter in str:
#     if letter.isupper():
#         li.append(letter)
# print(li[0],li[1],li[2])

# li=[]
# while(True):
#     num = (input("Enter the number "))
#     if(num == 'done'):
#         break
#     num =int()
#     li.append(num)
# total = int(0)
# i=0
# while(i<len(li)):
#     total=total+li[i]
#     i=i+1
# print("sum = ",total)
# print(" count =",len(li))


# str = "amar"
# i=(len(str))
# while(i >0):
#     i=i-1
#     print(str[i])

