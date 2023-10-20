# list1=[4,5,6,8,2,0,7]                   # list creation with same datatype example
# list2=["amar",5,8,7.70,True,'a',"raj"]  # list creaction with MULTI datatypes !
# print(list1)
# print(list1[2])         # index accseceing
# print(list1[-4:])     
# print(list2)  
# print(list2[6])           #list sliceing
# print(list2[1:3])

#****************LIST OPREACTION******************************************************************
LI = [4,8,6,3,9,7,3,5,30,13]  
print(LI)
# LI.sort()              # sorting in Assinding order !
# print(LI)
LI.reverse()           #  printing LIST element in reverse order !
print(LI)

# LI.append(45)
# print(LI)              #adds that element at the end of string! 
# LI.append("END")
# print(LI)

# LI.insert(5,90)       # inserting element at paticuler index append(index,value)!
# print(LI)               
# print(len(LI))         # finding length of list !
                  
# LI.pop(1)              # delete the value of paticuler index pop(index)!
# print(LI)
# LI.remove(30)          # remove the vlaue from list remove(value)
# print(LI)


LI1=['a','m','a','r']
print("Occrence of a = ",LI1.count('a') ) #it returns occurence of element in list!
LI2=['k','u','m','a','r']
LI1.extend(LI2)                          # oldlist.extande(anotherlist)=updatedlist
print("NEW extended list: ",LI1) 
li=[1,"AMAR",(3,5,7),[4,7.5,0.9],('s','f',5,9)]
print(li.index("AMAR"))                  # index returns of list 
print(li[4][0])                          # assceing nessted list element

new_list = li.copy()                         # list copy with = oprater!
#new_list = li
print(new_list)