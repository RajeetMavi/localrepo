"""
FOR LOOP :-
-> For loop works over a range
-> Useful when number of iterations are known
-------- Some specail keywords ----------
1) pass
    -pass is a null statement that does nothing
    -Used as placeholder for future code
2) continue
    -continue is used for skipping current iteration
3) break
    -It is used for stoping the loop 
    -It ends the loop and get out of the loop
"""
# USING for else
vegies = ["Toamto","Brinjal","Sarso","Kidney bean"]
for item in vegies:
    print(item)
else:
    print("DONE")
print()

number = [1,23,3,4456,432,2435,43,46,567,546,435,3243465,432,45]
x = int(input("Enter the number: "))
for val in number:
    if (val == x):
        print("Number found!")
        break
else :
    print("Not found!")