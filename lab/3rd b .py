# 1 + x/1! + x3/2! + x5/3! + x7/4! +.......+ x2n-1/n!

x = int(input("Enter the value of X : "))

# n = lenght of the series
n = int(input("\nEnter the series length : "))

# i am declaring sum=1 because there 1 in starting of the series
sum = 1
number = 1
for i in range(1, n+1):
    fact = 1
    j = 1
    while j <= i:
        fact = fact*j
        j = j+1
    sum = sum + (x*number)/fact
    number = number + 2

print(f"The sum of the series up to {n} terms if {sum}")
