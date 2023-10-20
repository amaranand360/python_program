#loop and range
#1. print neatural number upto n and find sum pro ava !

n=int(input("Enter a number wtich sum & fact u want ! ="))
sum =0
pro =1
print("The neatural number\n")
for i in range(1,n+1,1):
    sum=sum+i
    pro = pro*i
    print(i)
    # print("sum=",sum)
    # print("product=",pro)
print("Tne sum of neatural num till %d  = " %(n),sum)    
print(' %d! = %d ' %(n,pro))    
print("avarage = ",sum/n)

for i in range(1, 2):
    print("SUCCESSFUL!")
