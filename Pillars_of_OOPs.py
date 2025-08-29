"""
FOUR PILLARS OF OPPs :-
1. Encapsulation
    - It is the concept of binding data (variables) and methods (functions) together within a class.
    - It helps in hiding the internal details and only exposing necessary functionalities.
2. Abstraction
    - Hides the complex implementation details and only shows the relevant features to the user.
    - Achieved using abstract classes and methods.
3. Inheritance
    - Allows a child class to inherit properties and methods from a parent class.
    - Types of Inheritance in Python:
        ~ Single Inheritance
        ~ Multiple Inheritance
        ~ Multilevel Inheritance
        ~ Hierarchical Inheritance
        ~ Hybrid Inheritance
4. Polymorphism
    - The ability to use the same function name for different types (method overloading & overriding).
    - When the same operator is allowed to have different meaning according to the context.
    - Example :- 
        - print(2 + 3)#addition
          print("Solo Leveling"+" Arise")#concatenate
          print([1,2,3]+[4,5,6])#merger
        -Here we are using same operator + as addtion and concatenation operator. This is called polymorphism.
    - We know python do have inbuilt classes, considering above example - <class 'int'>,<class 'str'>,<class 'list'> and therefore in each class
      ther is different meaning of operator + (this is called implicit operator overloading)
"""

# # Performing Inheritance
# # An examaple of Single Inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("Car starting..")
#     @staticmethod
#     def stop():
#         print("Car stopped.")

# class Toyota_car(Car):# all methods of class Car can be used by instance of Toyota_car
#     def __init__(self,type):
#         self.type = type

# # car1 = Toyota_car("Fortuner")
# # car2 = Toyota_car("Land Cruser")
# # car1.start()# if no method with name start present in Toyota_car then it foes to inherited class Car search for start()
# # print(car1.name)

# # Multi_level Inheritance
# class Fortuner(Toyota_car):# class Fortuner Inherit properties of Toyota_car as well as Car
#     def __init__(self,fuel_type):
#         self.fuel_type = fuel_type

# #Understanding Multiple Inheritance
# class Mother:
#     M_personality = "Soft"
# class Father:
#     F_personality = "Strict"
# class Child(Mother,Father):
#     C_personality = "Charming"

# shaurya = Child()# This class can inherit personlity of both base classes here Mother and Father
# print("My personality is",shaurya.C_personality,"but i am",shaurya.M_personality,"and",shaurya.F_personality,"too")
    
    
#using super() method

# class Books:
#     def __init__(self,subject):
#         self.subject = subject
#     def type(self,cover):
#         self.cover = cover
#         return cover
#     @staticmethod
#     def code():
#         print("Books are the best thing in this world!")
# class Maths(Books):
#     def __init__(self,name,std,subject):
#         self.standard = std
#         self.name = name
#         #self.subject = subject -> this will create an attribute for Mathss but we want to change type of parent class i.e. Books
#         super().__init__(subject)# we use super method for above problem
#         super().code()


# Math1 = Maths("Foundational Math",6,"Mathematics")
# #print(Math1.subject)#AttributeError: 'Maths' object has no attribute 'subject'
# #to resolve above problem we usse super() method
# print("This is a book of subject",Math1.subject,"for standard",Math1.standard,"and name of book is",Math1.name,",comes in",
# Math1.type("Hard Binding"))

# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         # self.percentage = str((self.phy + self.chem + self.math)/3) + "%"
    
#     # def calc_percentage(self):
#     #     self.percentage = str((self.phy + self.chem + self.math)/3) + "%"
#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math)/3) + "%"

# student1 = Student(99,98,89)
# print(student1.percentage)
# # But lets take a scenerio where teacher by mistake give him 89 rather of 98
# student1.math = 98
# print(student1.math)# the value of math is changed but not that of percentage
# # print(student1.percentage)# no changes occours in percentage as percentage is aleready fixed during passing of old arguments

# #now to change percentage we can create a function and call it here - calc_percentage
# # student1.calc_percentage()
# # print(student1.percentage)#cahnges can be seen now but do we have to call it again for changes

# #here we can @property decorator
# # no need to change the percentage value or call a method to change attribtue of an object just call it as usual

# print(student1.percentage)#Now we can call property just like attributes 

#polymorphism
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,obj2):#we changed meaning of + for our class this is called operation overloading
        newReal = self.real + obj2.real
        newImg = self.img + obj2.img
        return Complex(newReal,newImg)
    
    def __sub__(self,obj):
        newReal = self.real - obj.real
        newImg = self.img - obj.img
        return Complex(newReal,newImg)

num1 = Complex(4,8)
num2 = Complex(6,4)
# result = num1.add(num2) #but can we write it like this - result = num1 + num2 ,here comes polymorphism
# result.showNumber()
# we can create a Dunder functio to do - result = num1 + num2 just write def __add__() instead of def add()
result = num2 + num1
result.showNumber()
sub = num2 - num1
sub.showNumber()


