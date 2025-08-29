"""
CLASS :-
-> A class is a blueprint for creating objects (instances).
-> A class defines a set of attributes (data) and methods (functions) that the created objects will have.
-> It allows you to bundle data and functionality together.

--------Key Concepts:
    - Class Definition: The class is defined using the class keyword.
    - Constructor (__init__): 
            --The constructor is a special method used to initialize the object's attributes when it is created.
            --The constructor if not deifned by programmer then it is defined automatically by python and hence called default constructor
                    #default constructor
                    def __init__ (self):
                        pass
            --The constructor created by the programmer with different parameters is called parameterized constructor
                    #parameterized constructor
                    def __init__(self,some_parameters):
                        self.some_parameter = "something"
            --We can create multiple constructors in a single class and one which mathces parameters passed is called
            --Generally we use a single constructor
                        
    - Attributes: 
            -- Attributes are variables that store information about an object. They define the state and properties of an object.
            ---- TYPES OF ATTRIBUTES---
                 (1) Instance Attribute :-
                     ~ Defined inside a class using (self)
                     ~ Unique to each object (instance
                     ~ Created in the __init__ method or elsewhere in the class
                     ~ Generally properties unique to instances are made instance attributes for eg - name,marks 
                 (2) Class Attributes :-
                     ~ Shared by all instances of the class
                     ~ Defined outside the __init__ method
                     ~ Accessed using ClassName.attribute or self.attribute
                     ~ Generally common properties are made class attributes for eg - College Name
            -- Precedence of instance(object) attribute is higher than class attribute
    - Methods: 
        -- A method in Python is a function that belongs to a class and operates on its objects.
        -- Methods define the behavior of objects and can manipulate their attributes.
        -- Generally in every method we had to pass self.
        ---- TYPES OF METHODSS---
            (1) Instance Methods
                ~ Operate on instance attributes.
                ~ Use self as the first parameter.
                ~ Can read or modify object attributes.
            (2) Class Methods
                ~ Operate on class attributes.
                ~ Use @classmethod decorator.
                ~ The first parameter is cls (reference to the class).
            (3) Static Methods
                ~ Don't operate on instance or class attributes.
                ~ Use @staticmethod decorator. 
                ~ No self or cls parameter.
            _________________________________________________________________________________________________________________
            |Method Type       | Uses self?  |Uses cls?    |Can Access Instance Attributes?	  |Can Access Class Attributes? |
            |Instance Method   | ✅ Yes	   | ❌ No	    |✅ Yes	                         |✅ Yes                       |
            |Class Method	   | ❌ No	   | ✅ Yes	    |❌ No	                         |✅ Yes                       |
            |Static Method	   | ❌ No	   | ❌ No	    |❌ No	                         |❌ No                        |
            |_______________________________________________________________________________________________________________|

    - Accessing Variables and Methods: You access instance attributes using self, which represents the current instance of the class.
"""

#creating a class
class Student:
    # name = "Himesh" we don't have to use same name for every student
    college_name = "ABCD college" #stored once in memory 
    name = "Anonymous"
    #parameterized constructor
    def __init__(self,fullname,marks):#invoked automatically , we can also use alias for self like - def __init__(object,fullname)
        self.name = fullname #by using alias we can write object.naem = fullname and if name is not present it creates one
        self.marks = marks #Instance attributes are stored as many times as number of instances created like here are 2
    def welcome(self):#we had to pass self as argument
        print("Welcome student ,",self.name)
    def get_marks(self):
        return self.marks
    

#creating an onject (instance)
# s1 = Student("Karan",89)# karan will be considered as second argument i.e fullname first is always self
# print(s1.college_name,s1.name,s1.marks)

# s2 = Student("Ram",99)#with every new object __init__ function is called
# print(s2.name,s2.marks,end=" ")
# print(Student.college_name)

# stu = Student("Karan",99)
# stu.welcome()
# print("Your marks = ",stu.get_marks())

""" USING del to delete a object(instance) or method and private and public concept """
class example:
    # prvate means object cannot access such methods or attributes
    # python specifically do not have such concept like java and c++
    # to do so just us __ (double undrscore) infront of method or attributes
    __conceptually_private = "conceptually_private" # an attribute that makes functions hypothetically private
    def __init__(self,name):
        self.name = name
    def __private(self):
        print("Top secret")
    def to_prove_is_private(self):
        self.__private()#As it is private therfore can be accesed with in class
Ex1 = example("Harish")
print(Ex1.name)# a public attribute
#del Ex1
#print(Ex1)# NameError: name 'Ex1' is not defined - as objected is deleted

#AttributeError: 'example' object has no attribute '__conceptually_private'. Did you mean: '_example__conceptually_private'?   
# print(Ex1.__conceptually_private)

#Ex1.__private()#AttributeError: 'example' object has no attribute '__private'

Ex1.to_prove_is_private()   
