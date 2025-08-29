"""
light = input("Enter the color of light : ")

if("red" == light):
    print("stop")

elif("yellow" == light):
    print("Ready")
elif ("green" == light):
    print("Go")
else :
    print("Jai Baba ki")

print("USING TERNARY OPERATOR!")
food = input("Food : ")
eat = "I like it!" if (food == "Sarso da saag") else "I don't like it!"
print(eat)
food = input("Food : ")
eat = "Sweet" if food == "jalebi" or food == "rasogulla" else "Not sweet"
print(eat)
"""

print("DAM CLEVER IF")
"""syntax : <var>  = (false_val,true_val)[<condition>])"""

age = int(input("Enter the age: "))
vote = ("no","yes")[age >= 18]
print(vote,"voteing")

