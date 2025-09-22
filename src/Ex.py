# The radius of a circle is 30 meters.
# a) Calculate the area of a circle and assign the value to a variable name of
# area_of_circle
import math

r=30
area_of_circle=math.pi*pow(r,2)
print(area_of_circle)
# b) Calculate the circumference of a circle and assign the value to a variable name of
# circum_of_circle
circum_of_circle = 2 * math.pi * r
print(circum_of_circle)
# c) Take radius as user input and calculate the area.
r=int(input("Enter the radius: "))
area_of_circle=math.pi*pow(r,2)
print(area_of_circle)