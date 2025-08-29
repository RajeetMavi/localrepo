"""
SET :-
-> Collection of unordered data or items
-> Each element of set must be "unique" and "unmutable"
-> Set is mutable nut set_elements are not mutable
-> Can store any type of data
-> Syntax : set_name = {elements}

"""
"""
c
collection = {1,2,3,4,5,"H","I","J",2,2,2}# ignores duplicate elements

# print(type(collection))
# print(len(collection))
# print(collection)

#Set methods

collection.add(23)#add an element
collection.add("crimson")
collection.add((1,2,3,45,6))
# collection.add([1,2,3,5,6,7]) #lead to error as list is mutable ERROE :- TypeError: unhashable type: 'list'
"""
"""
-> As set elements are immutable therfore we can not add a list or dict to a set
"""

"""ollection.remove(2)#removes the elments
collection.pop()#remov any random element

set2 = {1232,456,67,76543,56365}
set1 = {"H","I","K","K","L","D"}

print(collection.union(set2))
set3 = collection.intersection(set1)
print(set3)
print(collection)
collection.clear()#leads to empty set 
print(len(collection))
"""

"""
Question - 1

subjects = {"python","python","python","c++","c","java","c++","Javascript","java"}
number_of_classes = len(subjects)
"""

"""
Question - 2
"""
values = {9,9.0}
print(values)
values = {9,"9.0"}
print(values)
values = {9,(9.0,)}
print(values)
values = {(9,9.0)}
print(values)