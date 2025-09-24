# Write a Python program
# - to create a tuple of numbers and print one item.
x=(1,2,5,7,9)
print(x[3])
# - to unpack a tuple into several variables.
x=("My","Chuẩn","Me")
(girl,boy,fruit)=x
print(girl)
print(boy)
print(fruit)
# - to add an item to a tuple.
x=("Xoai","Cam","Quyt")
a=list(x)
a.append("Oi")
b=tuple(a)
print(b)
# - to find the index of an item in a tuple.
x=(1,4,6,3)
print(x.index(4))
# - to find the repeated items of a tuple
x=(1,4,6,3,4,5,3)
duplicate=[]
for i in x:
    if x.count(i)>1:
        if i not in duplicate:
            duplicate.append(i)
print(duplicate)
