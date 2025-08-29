"""
DICTIONARY :-
-> Dictionary store value in Key:value pair
-> They are unordered ,mutable and dont allow duplicate keys
-> Can store any type of data
-> key and values can be of any type
-> Syntax : dict_name = {key:value}
"""

student = {
    "name" : "Sohit",
    "class" : 10,
    "section": 'A',
    "age" : 14,
    12 : "gaming",
    "is boy" : True,
    "subjects" : ["Maths","Scinece","Hindi","Social science","Computer Science",]
}

# # print(student)

# #changing data
# student["name"] = 'Arya'
# student["surname"] = "Bhatt"

# #over writing
# student["surname"] = 45

# #Accessing elements
# print(student["subjects"])
# print(student["name"])
# print(student)

# #creating NULL dictionary
# null_dict = {}
# print(null_dict)

#creating nested list

# student["marks"] = {
#     "Maths":78,
#     "Hidni" : 80,
#     "science": 74,
#     "Computer science" : 94,
#     "SST" : 90,
#     "English" : 89
#     }

# print(student)

# #Dicionary Methods
# print(student.keys(),"\n")
# print(student.values(),"\n")
# print(student.items(),"\n")

# print(student.get('name'))
# """Why get if we can use student["name]"""
# # student["name2"]# ---> error:KeyError: 'name2' stop execution of program
# print(student.get('name2')) #---> return: none , let program to run 

student.update({"city" : "Mumbai"})
# print(student.get("city"))

# print(list(student.items()))
# print(len(student)) --> mumber of elements

"""
Question - 1
dictionary = {1:"One",2:"Two",3:"Three"}
dict_list = list(dictionary.items())
print(dict_list)
n = len(dict_list)
for i in range(0,n):
    print(dict_list[i])

print("\n\n")
for key,value in dictionary.items():
    print(f"{key},{value}")
"""

"""Question - 2"""

word_meanings = {
    "table":["a piece of furniture","list of facts and figure"],
    "cat":"a small animal"
    }

marks = {}

x = int(input("Enetr the marks of Physics: "))
marks.update({"physics" : x})

x = int(input("Enetr the marks of Maths: "))
marks.update({"Maths" : x})

x = int(input("Enetr the marks of Science: "))
marks.update({"Science" : x})

print(marks)