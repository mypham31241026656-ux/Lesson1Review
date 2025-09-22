# Python if...else Statement
# 1. Write a program to check a person is eligible for voting or not (accept
# age from user)
import random

age = int(input("Enter the age: "))
if age >=18:
    print("A person is eligible for voting")
else:
    print("A person is not eligible for voting")

# 2. Write a program to check whether a number entered by user is even or
# odd.
number = int(input("Enter the number: "))
if number %2==0:
    print("The number is even")
else:
    print("The number is odd")

# 3. Write a program to check whether a number is divisible by 7 or not.
n = int(input("Enter the number: "))
if n%7==0:
    print("The number is divisible by 7")
else:
    print("The number is not divisible by 7")
# 4. Write a program to check the last digit od a number (entered by user)
# is divisible by 3 or not.
n=int(input("Enter the number: "))
a=n%10
if a%3==0:
    print("The number is divisible by 3")
else:
    print("The number is not divisible by 3")
# 5. Write a Python program to guess a number between 1 and 9.
guess=int(input("Guess a number between 1 and 9: "))
random_number = random.randint(1,9)
if random_number==guess:
    print("You guessed right!")
else:
    print("You guessed wrong!")

# 6. Write a program to accept a number from 1 to 7 and display the name
# of the day like 1 for Sunday, 2 for Monday and so on.
day=int(input("Enter the day: "))
if day==1:
    print("Sunday")
elif day==2:
    print("Monday")
elif day==3:
    print("Tuesday")
elif day==4:
    print("Wednesday")
elif day==5:
    print("Thursday")
elif day==6:
    print("Friday")
elif day==7:
    print("Saturday")
else:
    print("Invalid day. Enter the day from 1 to 7")

# a=3
# b=3
# print("A") if a>b else print("B")
# print("C") if a>b else (print("=") if a==b else print("D"))