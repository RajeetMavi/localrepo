"""
DECORATOR :-
    -> A decorator in Python is a function that modifies the behavior of another function or method without changing its code.
    -> They are used to wrap functions dynamically and add additional functionality.
    -> A decorator is a function that takes another function as input.
    -> Decorators help in logging, authentication, and code reusability.
    -> It is used with @decorator_name syntax.
    --------Types of Decorators
        1. Function Decorators
            -- Function decorators modify the behavior of functions.
        2. Class Method Decorators
            -- Python provides built-in decorators for class methods.
            -- Example :- 
                ~ @staticmethod
                    - Used for defining static methods inside a class.
                ~ @classmethod
                    - Used for modifying class attributes.
                ~ @property
                    - We can use property decorator to make any method in a class to use the method as property
        3. Built-in Decorators
             ____________________________________________________________________________________________
             | Decorator	    :                       Purpose                                         |
             |__________________________________________________________________________________________|
             | @staticmethod	: Defines a method that doesn't need access to self or cls.             |
             | @classmethod	    : Defines a method that operates on the class instead of an instance.   |
             | @property	    : Defines a getter method for an attribute.                             |
             |__________________________________________________________________________________________|
"""