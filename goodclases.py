
# oops concept in PYTHON
class Car:
    # constructor
    def _init_(self,windows,tyres,engine):
        self.windows=windows
        self.tyres=tyres
        self.engine=engine


  def self_driving(self,engine):
    print(" the car types is {}".format(self.engine))



car1=Car(3,7,8)
#print(" the number of tyres in object car1 is{}".format(car1.tyres))
#print("the no of windows in object car1 is{}".format(car1.windows))
car1.self_driving(" electric")