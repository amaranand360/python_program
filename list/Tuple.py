# t = (1,2,5,6,9,10)          # Tuple creation with same datatype example
# t1 = ()                     # Empty tuple
# t1 = (30,)                  #Tuple with single element
# t2 = (30,"amar",7.70,True)  # Tuple creaction with MULTI datatypes !
# my_tuple = ("AMAR",[7,6,5],(5,9,"MD")) #nested tuple
# print(my_tuple)
# print(my_tuple[1])            # index acceasing.
# print(my_tuple[2][1])         # inside index inside element accessing.
# print(my_tuple[:2])           # slicing.
# my_tuple[1][1] =8.32 
# print(my_tuple)              # changing list element inside the Tuple!


# t[2] = 9                    # cannot update the value of tuple it is inmuteable.
# print(t)  

# print(t[2])
# print(t)
# print(t2)                  # index accessing/ printing function
# print(t1[0])    
# print(t[0:4])              # slicing


#****************Tuple opreaction*************************************

ashraf = (1,1,"AMAR",5.24,True)
#T = (11,22,33,58)
#l1 =[1,"ris",5.23,5]
#print(type(ashraf))
print(ashraf)
#print(ashraf.count("AMAR"))       # T0 count the occurence of element is Tuple.

#print(ashraf.index(1))       #to finding the index of tuple element/ Tuple_name.index(ele_value)

# print(tuple+T)               # combine two tuple using + opreater.
# print(T*3)
# print((T,)*3)                #using repeat the tuple

#print(8 in ashraf)              #Tuple Membership Test.

# i=0
# for index in tuple :
#     print('Index [%d]= %d'%(i,index))
#     i=i+1
ashraf = (1,1,"AMAR",5.24,True)
amar = (1,5,9,7)
print(len(amar))              #Return lenght of tuple.

print(max(amar))              #Return the largest item in the Tuple.
# print(max(T))

print(min(amar))              
# print(min(T))                  #Return the smallest item in the Tuple.

print(sum(amar))              #Return sum of all item of tuple.

print(sorted(amar))          # takes element in the tuple and return a new sorted list.
# print(sorted(tuple))

print(type(ashraf))
print(ashraf)
print(ashraf.count("AMAR"))       # T0 count the occurence of element is Tuple.
print(8 in ashraf)                #false
print(ashraf.index(1))
