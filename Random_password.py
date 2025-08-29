import random
import string

pass_source = string.ascii_letters + string.digits + string.punctuation
pass_length = int(input("Enter the length of password:"))
password = ""
# for i in range(0,pass_length):
#     password = password + random.choice(pass_source)

# print("Your random password is = ",password)

#using list comprehension

List = "".join([random.choice(pass_source) for i in range(0,pass_length)])
print(List)