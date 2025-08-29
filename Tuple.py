"""
TUPLE :-
-> Tuple stores any type of data
-> Tuples are immutable
-> Indexing is possible in tuple
-> Syntax : tuple_name = ()
"""
tup = ()
print(type(tup))# <class 'tuple'>
tup = (1)
print(type(tup))# <class 'int'>
tup = (1,)
print(type(tup))# <class 'tuple'>

#Methods
tup = (34,23,2,34,546,4,45,234,45)

print(tup.index(4))
print(tup.count(45))
