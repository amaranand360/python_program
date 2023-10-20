# my_set={1,9,6,2,7,1,3,8}   # define set.
# print(my_set)
# print(type(my_set))
# my_set.add("ashraf")
# print(len(my_set))

# s = set()           #creating empty set!
# print(type(s))
# s.add(9)            #adding value to empty set!
# s.add(5)
# s.add(2)
# s.add('anand')
# print(s)
# s.add((8,5,'amar',5.23))
# print(s)                  #adding tupple in a set!but we can't add list.
# print(len(s))             #finding the lenght of set.
# s.remove(2)               #removeing pacticular eement.
# print(s)
# s.pop()                   #pop any element.
# print(s)
# s.clear()
# print(s)

# li=[1,5,3,'go']         #We can convert a list to set using set function
# set_with_list = set(li)
# print(set_with_list)
# print(set([1,2,3,'go']))


#python set opreaction!
A={1,2,3,4,5}
B={4,5,6,7,8}

print("Union = ", A | B)
print("Intersection =", A & B)
print("Diffrence = ", A-B)
print("Symmetric Diff = ", A ^ B)