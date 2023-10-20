name = input("Enter your name: ")
a = float(input("Marks obtain in python: "))
b = float(input("Marks obtain in English: "))
c = float(input("Marks obtain in Math: "))
d = float(input("Marks obtain in deld: "))
e = float(input("Marks obtain in Ds: "))
ava =(a+b+c+d+e)/5
# print(" YOUR NAME IS = ",name)
# print("Marks obtain in python: ",a)
# print("Marks obtain in English: ",b)
# print("Marks obtain in Meth: ",c)
# print("Marks obtain in deld: ",d)
# print("Marks obtain in python: ",e)
# print("The total % marks obtain : ",ava)

if ava>0 and ava<45:
    print(" YOUR NAME IS = ",name)
    print("The total % marks obtain : ",ava)
    print("fail ! \n grade: 'F'")
elif ava>=45 and ava<60:
    print(" YOUR NAME IS = ",name)
    print("The total % marks obtain : ",ava)
    print("Pass!  \n Grade :'P'")
elif ava>=60 and ava<75:
    print(" YOUR NAME IS = ",name)
    print("The total % marks obtain : ",ava)
    print(" pass ! \nRemark: good \n grade :'B+'")  
elif ava>=75 and ava<85:
    print(" YOUR NAME IS = ",name)
    print("The total % marks obtain : ",ava)
    print(" Pass !\nRemark: very good\n grade :'A+'")
elif ava>=85 and ava <=100:
    print(" YOUR NAME IS = ",name)
    print("The total % marks obtain : ",ava)
    print(" Pass! \nRemark:  excellent\n grade: 'O'")
else  : 
    print(" it’s an error.")







