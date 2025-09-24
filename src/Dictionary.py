# 1. Write python program:
# a) Convert two lists into a dictionary
key=["Ten","ID"]
value=["TraMy","345"]
my_dict={
    key[0]:value[0],
    key[1]:value[1]
}
print(my_dict)
#Cách 2:
my_dict = {}
for i in range(len(key)):
    my_dict[key[i]]=value[i]
print(my_dict)
#VIdu
my_dict={}
my_dict['a']=1
my_dict['b']=2
print(my_dict)
# b) Merge two Python dictionaries into one
dict1={'a':1,'b':2}
dict2={'c':3,'d':4,'a':7}
dict1.update(dict2)
print(dict1)
# c) Print the value of key ‘history’ from the below dict
# {‘id’:4, ’history’:’sample’, ’price’:73}
x = {'id':4, 'history':'sample','price':73}
print(x['history'])

# a) Initialize dictionary with default values
keys=['a','b','c']
default_value=0
my_dict={}
for key in keys:
    my_dict[key]=default_value
print(my_dict)
# b) Create a dictionary by extracting the keys from a given dictionary
dict={
    'a':1,
    'b':2,
    'c':3,
    'd':4
}
new_dict={}
for key in dict:
    new_dict[key]=None

print(new_dict)
# c) Delete a list of keys from a dictionary
my_dict={
    'a':1,
    'b':2,
    'c':3
}
key_remove=['a','b']
for key in key_remove:
    my_dict.pop(key,None)
print(my_dict)
# d) Check if a value exists in a dictionary
my_dict={
    'a':1,
    'b':2,
    'c':3,
    'd':4
}
value_check =[2,4]
if value_check in my_dict.values():
    print(f"{value_check} exist in my_dict")
else:
    print(f"{value_check} not in my_dict")


# e) Rename key of a dictionary
my_dict={'a':1,'b':2,'c':3,'d':4}
my_dict['tramy']=my_dict.pop('a')
print(my_dict)

# f) Get the key of a minimum value from the following dictionary
# {‘a’:4, ’b’:18, ’c’:73}
x= {'a':4,'b':18,'c':73}
min_value=min(x.values())
print(min_value)
#cách 2
min_value=min(x, key=x.get)
print(x[min_value])

# a) Change value of a key in a nested dictionary
student={
    'name':'Anna',
    'marks':{
        'math':80,
        'english': 75
    }
}
student['marks']['math']=90
# 2. Write a Python program that counts the number of times characters appear in
# a text paragraph and its appearing positions.
text = '''Hello world!
Python is fun'''
char_info = {}
for i in range(len(text)):
    ch=text[i]
    if ch not in char_info:
        char_info[ch]=[1,[i]]
    else:
        char_info[ch][0]+=1 #tăng số lần xuất hiện lên 1
        char_info[ch][1].append(i) #danh sách vị trí tăng thêm
for ch, info in char_info.items():
    print(f'{ch} xuất hiện {info[0]} lần, vị trí {info[1]}')
# 3. Write a program using a dictionary containing keys starting from 1 and
# values ​​containing prime numbers less than a value N.
def is_prime(num):
    if num<2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True

number=int(input("NHập số N: "))
prime_number={}
key=1

for i in range(2,number+1):
    if is_prime(i):
        prime_number[key]=i
        key+=1
print("Dictionary các số nguyên tố nhỏ hơn N: ", prime_number)
