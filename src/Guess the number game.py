# 1. Guess The Number Game:
# -we will generate a random number with the help of randint() function from 1 to 100 and ask the user to guess it.
# -After every guess, the user will be told if the number is above or below the randomly generated number.
# -The user will win if they guess the number maximum five attempts.
# -Ask the user to stop or continue playing again.
# ***
# Add another situations like:
# level of game (hard (guess 3 times), medium (6 times), easy (10 times)
# assume that you have 100$, each game you spent 5$. Play game until you choose stop, report the game you win/lost and amount you have.
import random

money=100
win=loss=0

while money>=5:
    level=input("Choose a level (hard/medium/easy): ").strip().lower()
    if level == "hard":
        max_attempts=3
    elif level == "medium":
        max_attempts=6
    elif level == "easy":
        max_attempts=10
    else:
        print("Invalid level! Please choose a level (hard/medium/easy).")
        continue

    money -= 5
    random_number = random.randint(1,100)
    print(f"I have picked a number between 1 and 100. You have {max_attempts} attempts.")

    for i in range(1, max_attempts+1):
        guess=int(input("Guess a number between 1 and 100: "))
        if guess==random_number:
            win+=1
            print(f"Correct! The number is {random_number}")
            break
        elif guess>random_number:
            print(f"Too high! ")
        elif guess<random_number:
            print(f"Too low! ")
    else:
        print(f"Sorry, you ran out of attempts!The number is {random_number}")
        loss+=1
    print("Money left: ",money)
    if money<5:
        print("Not enough money to continue")
        break

    play_again = input("Would you like to play again? (y/n): ").strip().lower()
    if play_again != "y":
        print("Thank you for playing!")
        break
print("GAME OVER! THE STATATICS: ")
print("Total games played: ",win+loss)
print("Wins: ",win)
print("Losses: ",loss)
print("Money left: ",money)
