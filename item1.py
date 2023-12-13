
class item:
    def __int__(self, name: str, price : float , quantity = 0):


      # Run validations to the recieved arguments
       assert price >= 0
       assert quantity >= 0
     #ASSign the values  to self object
       self.name = name
       self.price = price
       self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity

item5 = item("PHONE" , 100, -1)

item5.price = -1
item5.quantity = -1
print(item5.calculate_total_price())



