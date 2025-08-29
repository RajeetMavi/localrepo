# #list question-1
# movies = []
# print("Enter your three favourite movie!")
# for i in range(0,3,1):
#     movies.append(input("Enter name of movie :"))

# print(movies)

#list question-2
"""
checking do list contain palindrome element
l = [1,'abc','pop',1]
for i in l:
    if(type(i) == str):
        if (i[::-1] == i):
            print(i)
            print("Yes it contain palindrome")
        
"""
list1 = ["a",1,2,1,"a"]
copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("Yes it is a palindrome")
