# Class and Methods
class Fruits:
    def fruit_name(self,name,describe):  #name of first method is fruit_name whose first argument is self
        self.name=name;                  #self is temporary placeholder for object
        self.describe=describe;
    def display(self):                   #another function which return some output
        return self.name,self.describe
object1= Fruits()                        #creating first object from class Fruits
object1.fruit_name("Apple:","Improving neurological health")
object1.display()
print(object1.name)
print(object1.describe)
#***********************************************************************************************************************#
# Going for second fruit
object2= Fruits()                        #creating second object from class Fruits
object2.fruit_name("Guava:","This Fruit helps in lowering risk of cancer")
object2.display()
print(object2.name)
print(object2.describe)
#**********************************************************************************************************************#
# Going for third fruit
object3= Fruits()                        #creating third object from class Fruits
object3.fruit_name("Mango:","Lowers Cholesterol")
object3.display()
print(object3.name)
print(object3.describe)

