"""
LIST :-
-> List is an ordered collection of data or items
-> List is mutable
-> List can store any type of data
-> Indexing is possible in list
-> Syntax : list_name = [data]



name = ["Karan","Dev","shivam"]
name[0] = "Arya"
print(name,"length = ",len(name))
# print(name[10]) --> index out of range


l = [1,23,34,23,453,3435,234]
#slicing list

# print(l[::-1])
# print(l[:4])
# print(l[0:])

strl = ["A","c","L","A","a","z"]

#LIST METHODS
# l.append(9999)
# print(l)
# l.reverse()
# print(l)
# l.append(9999)
# print(l)
# l.sort()
# strl.sort()
# print(strl)
# print(l)
# l.sort(reverse=True)
# print(l)
# l.insert(3,00000.1)
# print(l)
# print()

# l.reverse(),strl.reverse()
# print(l,strl)
print(l.count(23))
print(sum())
"""
l = [132,325,43634,65734,2347,4643,2345,546,6423,436,756,876879,54]
strl = ["A","c","L","A","a","z"]
strl.remove(strl[0])
print(strl)
#list comprehension
# cubes = [i*3 for i in range(0,11)]
# print(cubes)

comp = [(x,y) for x in [10,20,30] for y in [20,34,23] if x != y]
print(comp)