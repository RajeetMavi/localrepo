with open("input.txt","r") as file:
    count = 0
    line = file.readline()
    while (line != ""):
        count = count + 1
        line = file.readline()
    print(count)

            