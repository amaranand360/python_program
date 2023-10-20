myDIct ={
    "name":"AMAR KUMAR",
    "usn": "ENG21CS0030",
    "CGPA":[7.09,8.32,9.01],
    "branch":"CSE",
    "info":('bihar',"pin",813105),
    "anotherdist":{'pin':560068,"country":"INDIA"}
}
print(myDIct.keys())        #print the key of dictionary.
print(myDIct.values())      #print the key-value of dictionary.
print(myDIct.items())       #print the (key,value )for all contents.

# print(list(myDIct.keys()))
# print(list(myDIct.values()))

updatedict ={
    "friend":('ris','md','ashraf'),
    "hometown":"BGP",
    "current-location":"bangulue"
}
myDIct.update(updatedict)       #print updated dictionary!
print(myDIct)
print(myDIct.keys())

print(myDIct.get("usn"))        #~prints value associated with key and return 'none' if key not present!
print(myDIct["name"])           #~prints value associated with key and throws a 'error' if key not present!
print(myDIct.pop("CGPA"))       #remove the key.
print(myDIct.popitem())         #remove the random key.

print(myDIct)