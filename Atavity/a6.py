
# while 1:
#     n = int(input("Enter number= "))
#     if n==101 :
#         print("Your guess is correct !")
#         break
#     else :
#         print("YOUR guess is incroccet number !")    


# x=1
# while x<=5:
#     if x<=3:
#         print(x*'*')
#         x =x+1
#     elif x==4:
#         print(2*'*')
#         x =x+1
#     elif x==5:
#         print("*") 
#         break   
      

# n = int(input("Enter number= "))
# x=1                                     # inctionalization            
# while x <=12 :                                 # condition
#     print ("%d * %d = %d" %(x,n,n*x))             #opreactions
#     x=x+1                                  # increament or decreament 
# print ("I like Python.")



for i in range(1,7,1):
    for j in range(1,7,1):
        print(i,",",j)
print("SUCCUSEFULLY DONE !")
    

fruit = 'PINEAPPLE'
index = 0
while index < len(fruit): 
    letter = fruit[index]
    print(index,",", letter)
    index = index + 1
