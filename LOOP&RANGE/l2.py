#2. print table of any number & calculate the sum of table element !
n=int(input("Enter a number wtich Table u want ! ="))
sum =0;
for i in range(1,11,1):
    print("%d * %d = %d" %(i,n,i*n))
    sum = sum+(i*n)
print("The sum of table element is %d !" %sum)    
print("Thank U")

