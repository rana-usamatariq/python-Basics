class car:
   name : str
   speed : int
   model : int
def __int__(self , name  , speed , model):
     self.name = name
     self.speed = speed
     self.model = model

class audi(car):
    enginetype: str
def __int__(self, name = "BMW" ,speed = 9000,model = 9900 , enginetype ="diesel"):
     super().__int__(name , speed , model )
     self.enginetype = enginetype





car1=audi()
print(car1.name)
print(car1.speed)
print(car1.model)
print(car1.enginetype)

