# write a program to find the sum of the series

N = int(input("Enter the length of the series : "))

sum = 0
i = 1
while i <= N:
    sum = sum + 1/i
    i = i+2
print(f"The sum of the series is {sum}")
