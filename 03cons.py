class car:
    def __int__(self , windows, doors, enginetype ) :
        self.windows = windows
        self.doors = doors
        self.enginetype = enginetype



def driving(self):
       print("car is used for driving")
# audi car inheritence
class audi(car):
 def __int__(self ,windows, doors, enginetype ,speed):
     super(). __int__(windows,doors,enginetype)
     self.speed = speed

def self_driving(self):
    return " it is self driving car"

audi7 = audi ()
audi7.windows = 90
audi7.doors = 555
audi7.enginetype = "diesel"
audi7.speed = 900

print("the complete information  of car {}".format(audi7.windows),(audi7.windows),(audi7.speed))
print(audi7.self_driving())

