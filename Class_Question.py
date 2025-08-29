"""
Q-1: Create Account class with two attributes - balance and account number and create methods to debit ,credit & printing the balance.
Q-2: Creating a Student class that takes name and marks of subjects and print total marks, average marks.
Q-3: Define a Circle class to create a circle with radius rusing the contructor.Define Area method for calculating the area and a prameter method 
     too.
Q-4: Create a class Employee which contains attributes role,department ,salary.Their is a method showdetails to show details of particular employee
     Create a engineer class tha inherits properties of class Employee and also have new attributes name and age.
Q-5: Create a class called Order which include price and items.
     Use a dunder function __gt__() to convey that:
        order1>order2 if price of order1> price of order2
"""
"""
#Qestion -1
class Account:
    def __init__(self,account_no,account_balance):
        self.account_no = account_no
        self.account_balance = account_balance
    
    def get_balance(self):
        return self.account_balance
        
    
    def credit(self,ammount):
        self.account_balance += ammount
        print("Rs.",ammount,"Was credited.")
        print("Current Balance :",self.get_balance())
    
    def debit(self,ammount):
        self.account_balance -= ammount
        print("Rs.",ammount,"Was debited.")
        print("Current Balance :",self.get_balance())

Person1 = Account(10010101,100001223)
print("Your Account No. is",Person1.account_no,"and your balance is",Person1.get_balance())
Person1.credit(9000)
Person1.debit(100000)

#Question - 2
class Student_marks:
    @staticmethod
    def hello():
        print("Hello!")
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def result(self):
        self.total = sum(self.marks)
        self.average = self.total/len(self.marks)
        print("Your total marks is = ",self.total," and your average is = ",self.average)
    
studemt1 = Student_marks("Harsh",[67,89,76,99,86])
studemt1.hello()
studemt1.result()

#Question - 3
class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius)**2
    def parameter(self):
        return 2* 3.14 * self.radius

cr1 = Circle(6)
print("Area of circle =",cr1.area(),"and parameter =",cr1.parameter())
        
#Question - 4
class Employee:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary

    def show_details(self):
        print("Role -",self.role)
        print("Department -",self.department)
        print("Salary -",self.salary)

class Engineer(Employee):
    def __init__(self,name,age ):
        self.name = name
        self.age = age
        super().__init__("Engineer","Aerospace",400000)
        

# emp = Employee("Manager","Research & Development",5000000)
# emp.show_details()

eng = Engineer("Ravan",20)
eng.show_details()

"""
#Question - 5
class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
    def __gt__(self,obj):
        if self.price > obj.price:
            return self.item
        else:
            return obj.item

odr = Order("Chips",20)
odr2 = Order("Biscuits",10)
odr3 = Order("Cold drink",90)
print(odr3 < odr)
print(odr > odr2)
