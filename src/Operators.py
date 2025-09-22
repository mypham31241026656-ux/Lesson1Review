# 1. Write a program that prompts the user to enter base and height of the
# triangle and calculate an area of this triangle (area = 0.5 x b x h).
import math

base=float(input("Enter the base: "))
height=float(input("Enter the height: "))
area=base*height*1/2
print("The area of this triangle is ",area)
# 2. Write a script that prompts the user to enter side a, side b, and side c of the
# triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a=float(input("Enter the side a: "))
b=float(input("Enter the side b: "))
c=float(input("Enter the side c: "))
perimeter=a+b+c
print("The perimeter of the triangle is ",perimeter)

# 3. Get length and width of a rectangle using prompt. Calculate its area (area =
# length x width) and perimeter (perimeter = 2 x (length + width))
l=float(input("Enter the length: "))
w=float(input("Enter the width: "))
area_rectangle=l*w
perimeter_rectangle=2*(l+w)
print("The perimeter of the rectangle is ",perimeter_rectangle)
print("The area of the rectangle is ",area_rectangle)

# 4. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and
# circumference (c = 2 x pi x r) where pi = 3.14.
radius=float(input("Enter the radius: "))
area_circle = math.pi*radius**2
print("The area of the circle is ",area_circle)

# 10. Use and operator to check if 'on' is found in both 'python' and 'dragon’


# 11. “I hope this course is not full of jargon.” Use in operator to check if
# jargon is in the sentence.
# 12. _
# 13. Find the length of the text python and convert the value to float and
# convert it to string
# 14. Even numbers are divisible by 2 and the remainder is zero. How do you
# check if a number is even or not using python?
# 15. Writs a script that prompts the user to enter hours and rate per hour.
# Calculate pay of the person?
# 16. Write a script that prompts the user to enter number of years.
# Calculate the number of seconds a person can live. Assume a person
# can live hundred years
