"""
WHILE LOOP :-
-> While loop works over a iterator
-> an iterator is a variable used for controlling number of iterations in a loop
-> Useful when number of iterations are not known
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

"""
Question - 1
1 to 100
i = 1
while (i<=100):
    print(i,end=" ")
    i = i+1
"""
"""
Question - 2
"""
l = (34,345,13,456,2345,3554)
i = 0
x = int(input("Enetr a number: "))
while(i<len(l)):
    if (x == l[i]):
        print("Element found at index ",i)
        break
    i = i+1
