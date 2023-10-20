f = open("demo.txt","r")             #It is use to open file. 
# content =f.read(3)                #It is use to read file. 
# print(content)
for line in f:
    print(line,end="")
# print(f.readlines())
f.close()                        #It is use to close file. 

# f = open("Amar.txt","r")         #It is use to open file. 
# content =f.read()                #It is use to read file. 
# print(content)
# f.close()      


# f = open("Amar.txt","rb")    #It is use to open file for reading in binary mode. 
# content =f.read()            #It is use to read file. 
# print(content)
# f.close()                          #It is use to close file. 
# # b'Hii bro \r\nI am amar \r\n    How are you?'     #output

# f = open("Amar.txt",'r+')  #it is use to open file for reading and writting mode. 
# content = f.read()
# print(content)

# f.write('Welcome to DSU\n')
# f.write('This is our Python class 3\n')
# print("File written successfully!")
# f.close()

# f = open("Amar.txt",'r')
# data = f.read()
# print(data)
# f.close()

# f = open("Amar.txt",'rb+')  #it is use to open file for reading and writting mode in binary formate. 
# content = f.read()
# print(content)
#f.close()

# f = open("Amar.txt",'w')  #it is use to open file for only writting mode. 
# f.write('Welcome to DSU\n')
# f.write('This is our Python class 3\n')
# print("File written successfully!")
# f.close()

# f = open("Amar.txt",'w+')  #it is use to open file for writting  and reading mode. 
# f.write('Welcome to DSU\n')
# f.write('This is our Python class 3\n')
# print("File written successfully!")
# content = f.read()
# print(content)
# f.close()

# f = open("Amar.txt",'a')  #it is use to open a file for appeand. 
# f.write('Welcome to DSU\n')
# f.write('This is our Python class 3\n')
# print("File updated successfully!")
#f.close()


# f = open("Amar.txt",'a+')  #it is use to open file for updating and reading mode. 
# f.write('Welcome to DSU\n')
# f.write('This is our Python class!\n')
# print("File updated successfully!")
# content = f.read()
# print(content)
# # print(f.seek(2))
# f.close()
# # file property of python
# print(f.closed)
# print(f.name)
# print(f.mode)

# import os
# if os.path.exists("Demo_file.txt"):
#    os.rename("Demo_file.txt","anandraj.txt")
#    print("File renamed successfully!")

# else:
#   print("The file does not exist")


# import os
# if os.path.exists("Amar.txt"):
#    os.remove("Amar.txt")
#   print("File deleted successfully!")
# else:
#   print("The file does not exist!")




