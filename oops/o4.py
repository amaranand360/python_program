class train :
    NAME = 'INTERCITYEXPRESS'
    NUM =  32741
    FARE = 90
    SEAT = 100
    def __init__(self,name,type,age,ts) :
        self.name = name
        self.age=   age
        self.type = type
        self.Totalseat = ts
    

    def getdetails(self) :
        print("The train name is :",self.NAME)
        print("The train number :",self.NUM) 
        print("The train in avaiable seat is : ",self.SEAT)

    def fareinfo(self) :
        print("The fare of per seat = Rs ",self.FARE)
        print("your taken seat : ",self.Totalseat)
        print(f"your total payable fare = Rs {(self.Totalseat * self.FARE)*(1+0.18)}")

    def Ticketstatus(self) :
        if self.SEAT > 0 :
            print(f"Your Ticket is booked!\n  you alloact {self.type} class seat.\nyour seat number is:{self.SEAT} ",)
            print(f"{self.name} has alloat {self.Totalseat} seat")
            self.SEAT=self.SEAT- self.Totalseat
        else :
            print("Sorry!  Train is full / chaek for tatkal tickets.")

amar = train('AMAR','SLEPER',19,2)
amar.getdetails()
amar.Ticketstatus()
amar.fareinfo()

