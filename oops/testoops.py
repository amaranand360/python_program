class info :
    branch = 'cse'
    collage = 'DSU'
    def __init__(self,n,a,l,c):
        self.name = n
        self.age = a
        self.location =l
        self.collage =c
    def getdetails(self):
        print(f"name = {self.name},age={self.age},location={self.location},clg ={self.collage},branch ={self.branch}")
        # print(self.collage)
        # print(self.branch)


amar = info('AMAR',18,'BIHAR',"LPU")
# amar.name = 'AMAR'
# amar.NUM = 34
# amar.age = 20
# amar.location = 'bihar'
amar.getdetails()

savar = info("savhar verma",20,'ranchi',"VTU")
# savar.name = 'savar'
# savar.NUM = 30
# savar.age = 21
# savar.location = 'ranchi'
savar.getdetails()

# print(person.NAME)
# print(person.NUM)
# print(person.age)
# print(person.location)
