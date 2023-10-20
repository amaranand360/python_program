name = input("What is  your name: ")
a = input("Enter Your age = ")
h = input("Enter Your height")
a = int(a)
h = float(h)
print("Your name is ",name)
print(name ,"You are", a, "Years old")     #Manual string formattin

print( f"You are {a} year old")
print( f"Your height is {h} feet tall")       #Formatted string literals or f-strings
print( f"{name} you are {a} years old")

print("{} you are {} years old".format(name,a)) # the string format() method
PI = 3.14159265
print("The value of PI is {:.2f}".format(PI))

print('%s you are %d years old' %(name,a))
print( 'Your height is %.2f feet tall' %(h))       #Old string formatting or printf() style in C




name = input("What is  your name: ")
a = input("Enter Your age = ")
h = input("Enter Your height = ")
print("Hello everyone!")
print("My name is {} and I am {} years old".format(name,a))       # the string format() method
