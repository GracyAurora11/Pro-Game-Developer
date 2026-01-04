class Cars():
    def __init__(self,size,color,brand,nodoors,fuel):
        self.size=size
        self.color=color
        self.brand=brand
        self.nodoors=nodoors
        self.fuel=fuel

    def driving(self):
        print('lets drive.')
    def petrol(self):
        print('lets fuel the car')
    def display(self):

        print('The size of the object is',self.size)
        print('The color of the object is',self.color)
        print('The brand of the object is',self.brand)
        print('The nodoors of the object is',self.nodoors)
        print('The fuel of the object is',self.fuel)

object1=Cars('Small','Dark Blue','Nissan','2','Petrol')
object2=Cars('Medium','Red','Toyota','4','Petrol')
object3=Cars('Large','Dark Grey,','BMW','4','Diesel')

print(object1.size)
print(object2.color)
print(object3.brand)
print(object2.nodoors)
print(object3.fuel)

object3.display()