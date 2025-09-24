# companies={'Las','Ralph'}
# tech_com=['apple','banana','apple']
# companies.update(tech_com) #thêm nhiều phần tử từ bất kì iterable(list,tuple,dictionary)
# print(companies)
#
# x={3,56,9}
# x.discard(56)
# print(x)

# 1. Write a Python program to find the maximum and minimum values in a
# set.
x={1,4,6,8,24,64,8}
max_value=max(x)
min_value=min(x)
print("Max: ",max_value)
print("Min: ",min_value)

# 2. Write a Python program to check if a given value is present in a set or
# not.
x={1,3,5,6,3,8}
value=5
if value in x:
    print(f"{value} is in the set")
else:
    print(f"{value} is not in the set")
# 3. Write a Python program to check if two given sets have no elements in
# common.
set1={1,2,3,4,5,6,7,8,9,10}
set2={2,6,3,7,9,10}
common=set1.intersection(set2)
if len(common)==0:
    print("Two set have no elements in common",common)
else:
    print("Two set have elements in common",common)
# 4. Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.
x=[1,2,3,4,5,6,7,8,9,10,4,6,3,6,8]
unique_word=set(x)
print(unique_word)

for i in unique_word:
    count_frequency=x.count(i)
    print(i,"occurs",count_frequency,"times" )


# 5. Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa. Use
# the Python set.
set1={3,6,2,9,14,8,9}
set2={2,6,3,9,45,24,76}
missing_set1=set2.difference(set1)
missing_set2=set1.difference(set2)
print(missing_set1)
print(missing_set2)
#Cách 2
set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 5, 6}

missing_in_set2 = set1 - set2
missing_in_set1 = set2 - set1

print("Missing in set2:", missing_in_set2)
print("Missing in set1:", missing_in_set1)