import random

i=0
a="University of Economicss HCMC"
while i<len(a): # chạy từ 0 đến 4, không vượt quá độ dài chuỗi, tránh lỗi "index out of range".
    if a[i]=='s'or a[i]=='e':
        i+=1
        continue
    print(a[i])
    i+=1

# 1. Guess The Number Game:
# - we will generate a random number with the help of randint() function from 1 to 100
# and ask the user to guess it.
# - After every guess, the user will be told if the number is above or below the
# randomly generated number.
# - The user will win if they guess the number maximum five attempts.
# - Ask the user to stop or continue playing again.
random_number=random.randint(1,100)
attempts=5
while True:
    for i in range(1, attempts+1):
        guess=int(input("Guess a number between 1 and 100: "))
        if guess>random_number:
            print("Too high!")
        elif guess<random_number:
            print("Too low!")
        else:
            print("Correct!")
    print("You used all attempts!")
    print("The computer generated random number is: ",random_number)
    play_again= input("Do you want play continue? (yes/no):").strip().lower()
    if play_again != 'yes':
        print("Thank you for playing!")
        break


# 2. Write a game that simulate rolling a pair of dice.
# - If the sum of two faces is greater than 5 → “Tài”
# - Otherwise → “Xỉu”
# - User ask for guessing “Tài” or “Xỉu”
# - Match the results
# - After one turn, ask user for continue playing game.
# - **** Extend the game by asking the user to enter an amount of money, then
# continue playing until the user runs out of money or the user stops playing. Statistics
# of results.
face_1=random.randint(1,6)
face_2=random.randint(1,6)
total=face_1+face_2
win=0
loss=0
money=int(input("How much money do you have? "))

while money>0:
    print("Current money: ",money)
    bet=int(input("Your bet: "))
    if bet>money:
        print("Run out of money!")
        break
    if total>5:
        result="Tài"
    else:
        result="Xỉu"
    guess=input("Guess Tài or Xỉu: ").strip().lower()
    if guess == result:
        money+=bet
        win+=1
        print(f"You win!The total is: {total}->{result.capitalize()}")
    else:
        money-=bet
        loss-=1
        print(f"You lose!The total is: {total}->{result.capitalize()}")
    play_again=input("Do you want play continue? (yes/no):").strip().lower()
    if play_again != 'yes':
        print("Thank you for playing!")
        break
print("The statatics: ")
print("Wins: ",win)
print("Losses: ",loss)
print("Ending money: ",money)


