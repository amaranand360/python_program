# using of arithmetic operation input by user

a = input("Enter 1st oprand = ")
op= input("Enter oprater[+,-,*,/,^]= ")
b = input("Enter 2nd oprand of b = ")
a = float(a)
b = float(b)
op=str(op)
if op =='+':
    Result=a+b
elif op =='-':
    Result=a-b
    
elif op =='*':
    Result=a*b
    
elif op =='/':
    Result=a/b
    
elif op == '^':
    Result=int(pow(a,b))

print(" %.2f %s %.2f = %.2f" %(a,op,b,Result))



# print("Tne squre  =",a*a)
# print("Tne squre of b =",b*b)
# print("Tne squre of c =",c*c)
# print("Tne cube of c =",c*c*c)
# print("the cube of a=",a*a*a)
# print("the cube of b =",b*b*b)
# print("a>b? =",a>b)
# print("a<b?",a<b)
# print("a>c?",a>c)
# print("b>c/",b>c)




