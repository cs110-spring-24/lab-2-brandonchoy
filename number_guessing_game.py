
import random

while True: 
    user = 0
    guess = 0
    num = random.randint(1, 100)

    while user != num:
        user = input("enter your guess: ")
        user = int(user)
        guess = guess + 1 
        if user > num: 
            print("Too high")
        elif user < num:
            print("Too low")
        else:
            print("You got it!")
            print(f"tt took you {guess} guesses")       

    again = input("qould you like to play again?: ")
    if again == "no":
        print("goodbye")
        break 