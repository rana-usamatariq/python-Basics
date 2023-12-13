class item:
   def __int__(self ,name,price,quantity):
       self.name = name
       self.price = price
       self.quantity = quantity

   ''' creating other method'''
def  calculate_total_price(self ,x , y):
         return x * y
item1 = item()
item1.name = " phone"
item1.price = 5666
item1.quantity = 6
'''print(item1.calculate_total_price(item1.price, item1.quantity))'''
print("the name of mobile is{}".format(item1.name))
print(item1.name)
print(item1.price)
print(item1.quantity)
item2 = item()
item2.name = "laptop"
item2.quantity = 899
item2.price = 100
total =  item2.price * item2.quantity
'''print(" the total prices of items y multiplications {}".format(calculate_total_price))'''
'''print(" the total prices of item2 is :{}".format(total))'''
print(" the complete information of item1 is  : {} ".format(item1.name),(item1.price),(item1.quantity))
print("the complete information of item2 is   : {}  ".format(item2.price),(item2.quantity),(item2.name))