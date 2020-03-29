# self-variable-python    

## See the below Video

https://drive.google.com/file/d/1f-4jCLd48k26UcyNlUCjrsIdJZX3vi4Q/view?usp=sharing


## Why Self in Python
Self is a variable which is the first argument of method which is created inside the class in python. It is a temporary placeholder of objects of the class and is very useful when you are working with different objects inside the same class and accessing the same methods of the class. In this code I have created three objects of the class such as Apple, Gauva and Mango. Please look at the below screenshot to understand the case in more precise way. **This refers to same class_method**. *Self helped in distinguishing between each of them.*

![self](https://user-images.githubusercontent.com/3431730/42982784-91ecf9fc-8c00-11e8-8660-17a8ea6e1c70.png)

---

### Please look at the below code to understand it better
```
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
```

---

Self is temporary holding these three objects which are Mango, Apple and Gauva.
