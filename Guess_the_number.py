import random


target = random.randint(1,10)
while True:
    user_choice = input("Guess the number or Enter Quit(Q): ")
    if user_choice == 'Q':
        print("---Game Over---")
        break

    user_choice = int(user_choice)
    if (user_choice == target):
        print("You guessed it correct!")
        print("---Game Over---")
        break
    elif (user_choice > target):
        print("You guessed a greater number!")
    else :
        print("You guessed a smaller number")


        