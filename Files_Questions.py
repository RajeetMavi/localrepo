"""
# Question 1 and Question 2
def file_input(file):
    choice = 1
    while True:
        file.write(input("Enter data : "))
        file.write("\n")
        choice = int(input("Enter 0 for exiting data entry: "))
        if choice == 0:
            break


    
def file_output(file):
    file.seek(0)
    data = file.read()
    print(data)
    return data


with open("sample.txt",'w+') as file:
    file_input(file)
    file.seek(0)
    data = file_output(file)
    file.seek(0)
    data = data.replace("java","python")
    file.seek(0)
    file.truncate()
    file.write(data)
    file.close()# Not necessary while using with

with open("sample.txt","r") as file:
    data = file.read()
    file.seek(0)
    if(data.find("python") != -1):
        print("Data found!")
    else:
        print("Data Not found!")

def check_for_line():
    with open("sample.txt",'r') as file:
        word = "learning"
        data = True
        count = 1
        while data:
            data = file.readline()
            if(data.find(word) != -1):# we can also use (word in data) for same condition
                print("Word found at line :")
                return count
            count = count + 1
    return -1

print(check_for_line())

"""

def count_even():
    """
    # Method 1
    with open("numbers.txt",'r') as file:
        data = file.read()
        num_str = ""
        for i in range(0,len(data)):
            
            if (data[i] == ',' or data[i] == '\0'):
                print(int(num_str))
                num_str = ""
            else:
                num_str += data[i]
    """
    # Method 2
    with open("numbers.txt","r") as file:
        data = file.read()
        nums = data.split(",")

        for i in nums:
            if(int(i)%2 == 0):
                print(int(i))


count_even()