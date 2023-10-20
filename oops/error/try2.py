try:
    a = int(input("Enter a number!"))
    b = int(input("Enter a number!"))
    x = a/b

except TypeError as t:
    print("type err")
except ValueError as e:    
    print("Entered value is wrong",e)
except ZeroDivisionError as e:    
    print("Can't divide by zero",e)

else:
    print("The answer of division  %f"  %x)

# except TypeError:
#     print("Error!")
finally:   
    print("Exiting the program!...........")