"""
FUNCTIONS :-
-> Functions are block of reusable code
-> Used for performing a specific task
-> Helps in organising code
-> defined using 'def' keyword
-> syntax - def function_name(parameters):
                #statements
                return val

--------CHARACTERISTICS-------
    - Encapsulation: Functions group a set of related statements into one block.
    - Reusability: They allow you to reuse the same code multiple times without rewriting it.
    - Abstraction: Functions simplify complex tasks by hiding the details behind a function call

--------TYPES OF FUNCTIOONS------
    - Built-in Functions: Functions provided by Python (e.g., print(), len(), max()).
    - User-Defined Functions: Functions created by the user for specific tasks.
    - Lambda Functions: Anonymous, single-expression functions using the lambda keyword

-> Parameters: Variables listed in the function definition.
-> Arguments: Values passed to the function when calling it.

-----variable length arguments-----
    - *args and **kwargs in Python
    -  *args and **kwargs are special syntax used in function definitions to handle variable-length arguments.
        They allow you to write functions that accept any number of arguments.
-> RECURSION - When a function call itself
"""
# #User defined functions
# def prod(a,b):
#     #we can provide default values to prod --> def prod(a = 1,b = 0)
#     #Good choice to write default values at end
#     return a*b
# print("product of 4 and 5 is =",prod(4,5))

# def process_data(my_list, my_tuple, my_dict, my_string, my_set):
#     print("List:", my_list)
#     print("Tuple:", my_tuple)
#     print("Dictionary:", my_dict)
#     print("String:", my_string)
#     print("Set:", my_set)

# process_data(
#     [1, 2, 3],
#     (10, 20),
#     {"key": "value"},
#     "example",
#     {100, 200}
# )

# #Built in Functions 
# print("Ram","ji",sep=" Ram ",end = " bhaiyo")
# print()

#recursive functions
"""
def sum_natural(n = 1):
    if(n == 0):
        return 0
    return sum_natural(n-1) + n
n = int(input("Enter the number of terms: "))
print("sum of ",n,"numbers is = ",sum_natural(n))

def print_list(l,i = 0):
    if(i == len(l)):
        return
    print(l[i])
    print_list(l,i+1)

l = [1, 2, 3]
print_list(l)
"""
