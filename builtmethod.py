class Car:
    '''constructor'''
    def __init__(self, windows,tyres, engine):
        self.windows = windows
        self.tyres = tyres
        self.engine = engine

        ''' call constructor'''
car1=Car(3,  3  , "petrol")
print(dir(car1))
print(car1.windows)
print(" the total tyres of car are{}".format(car1.tyres))
print(" the total windows of car are {}".format(car1.windows))
def self_driving(self):
    print("the car type is {}".format(self.engine))



