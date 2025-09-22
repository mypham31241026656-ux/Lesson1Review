# 1. write a program that prints numbers from 1 to 10
import random

for i in range(1,11):
    print(i)
# 2. Write a program to calculate the sum of numbers in a range from 1 to n (n is
# entered from the keyboard)
n=int(input("Enter a number: "))
total=0
for i in range(1,n):
    total +=i
print(total)
# 3. Write a program to calculate the sum of even (/odd) numbers in a range from
# 1 to n (n is entered from the keyboard)
n=int(input("Enter a number: "))
even_total=0
odd_total=0
for i in range(1,n):
    if i%2==0:
        even_total +=i
    else:
        odd_total +=i
print("Sum of even numbers: ",even_total)
print("Sum of odd numbers: ",odd_total)
# 4. Write a program to check how many vowels are in a string entered from the
# keyboard.
string=str(input("Enter a string: "))
vowels = "euoaiEUOAI"
count=0
for i in string:
    if i in vowels:
        count += 1
print(count)

# 5. Write a program to count the number of words in a sentence the user enters.
sentence=input("Enter a sentence: ")
count=0
for word in sentence.split():
    count+=1
print(count)
# 6. Write a program that implements a game as the following description:
# 7. 1. The computer generates a random number from 1 to 100
# 8. 2. The user was asked to guess
# 9. 3. match the user-guessing number to the generated number
random_number = random.randint(1,100)
guess=int(input("Enter a guess: "))

if guess == random_number:
    print("Correct!")
else:
    print("Incorrect!")
print("THe computer generated random number is: ",random_number)
print("Thank you for playing!")

# 10. The user can only guess five times
random_number = random.randint(1,100)
attempts = 5
for i in range(1, attempts+1):
    guess=int(input(f"Attempts {i}.Enter a guess only five times: "))
    if guess > random_number:
        print("Too high! Again")
    elif guess < random_number:
        print("Too low! Again!")
    else:
        print("Correct!")
else:
    print("Sorry you used all attempts!")
print("The computer generated random number is: ",random_number)
print("Thank you for playing!")


