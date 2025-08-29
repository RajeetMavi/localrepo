"""
STRING :-
-> string is an array of characters
-> string is immutable
-> indexing of string is possible

"""
# str1 = "The wisdom tooth does'nt provide wisdom just a biological thing!"
#indexing
# print(str1[1])

#slicing
# print(str1[1:32])
# print(str1[0:])#till len(str1)
#Negative indexing
# print(str1[-100:1])#it prints one place before 1

string = "hello"
# string[0] = 'H' --> not allowed (immutable type)
#string methods
#string methods retuns updated string
"""
print(string[::-1])
print(string.capitalize())
print(string.count("l"))
print(string.endswith('0'))
print(string.find('o'))
"""

# print("H'kjgdsjg")
# print("Hello "'to his wonderful.....'"world")
# print(string.upper())
# tup1 = (5,1,5)
# tup2 = (5,2,5)
# print(tup1 > tup2)

tup = tuple("sajfkjdshajdghl")
print(tup.count("s"))