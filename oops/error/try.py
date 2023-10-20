#Guess the number
while(True):
    print("\npress 'e' for EXIT the program!")
    a=input("Guess the number[1-100] :\n")
    if a == 'e':
        print("You are sucessfully Exit the program!")
        break
    try:
        a = int(a)
        
        if a < 0:
            raise ValueError()

        elif a > 100:
            raise ValueError() 
    
        elif(a<83):
            print("Your number is too LOW!")

        elif(a>83):
            print("Your number is too HIGH!")

        elif(a == 83):
            print(f"Your Guess is right! your number was {a}!")
            break
    except ValueError:
        print("please try with valid input!")  
    except Exception as e: 
        print(f"YOUR input result is may have type-ERROR!{e}") 
    
print("Thanku for playing...!")


# #Guess the number
# while(True):
#     print("\npress 'e' for EXIT the program!")
#     a=input("Guess the number[1-100] :\n")
#     if a == 'e':
#         print("You are sucessfully Exit the program!")
#         break
#     try:
#         a = int(a)
#         if(a<83 and a>0):
#             print("Your number is too LOW!")

#         elif(a>83 and a<101):
#             print("Your number is too HIGH!")

#         elif(a == 83):
#             print(f"Your Guess is right! your number was {a}!")
#             break
#         elif(a<0 and a>101):
#             print(f"Your number is out of range..!\n{a}")
#     except ValueError as e: 
#             print(f"YOUR input result is may have type-ERROR!{e}")
    
# print("Thanku for playing...!")