# 1. Write a Python program to calculate the length of a string
string ='Em là cây nến vàng'
a=len(string.replace(" ",""))
print(a)
# 2. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : 'google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

string ='google.com'
frequency= {}
for i in string:
    if i not in frequency:
        frequency[i] = 1
    else:
        frequency[i] += 1
print(frequency)
# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given
# string. If the string length is less than 2, return the empty string instead.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String
string=input('Nhập chuỗi vào đây: ')
if len(string)<2:
    print('Empty String')
else:
    new_string=string[0:2]+string[-2::]
    print(new_string)
# 4. Write a Python program to get a string from a given string where all occurrences of its first
# char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'
string='restart'
first_char=string[0]
result=first_char+string[1:].replace(first_char,'$')
print(result)
# 5. Write a Python program to get a single string from two given strings, separated by a space and
# swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz

def swap_first_two(a,b):
    new_a=b[0:2]+a[2:]
    new_b=a[0:2]+b[2:]
    return new_a+' '+new_b
print(swap_first_two('abc','xyz'))
# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If
# the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is
# less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'
string=input("Enter the string: ")
if len(string)>=3:
    if string[-3:]=='ing':
        string=string+'ly'
    else:
        string=string+'ing'
else:
    string=string
print(string)
# 7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given
# string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the
# resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'
def not_poor(text):
    not_pos=text.find('not')
    poor_pos=text.find('poor')
    if not_pos!=-1 and poor_pos!=-1 and poor_pos>not_pos:
        text=text[:not_pos]+'good'+text[poor_pos+4:]
    return text
print(not_poor('The lyrics is not that poor'))
# 8. Write a Python function that takes a list of words and return the longest word and the length
# of the longest one.
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9
def longest_word(words):
    longest=max(words,key=len)
    return longest, len(longest)
words_list=['ecd','Exercises','myne','milk']
longest, length= longest_word(words_list)
print('Longest word: ',longest)
print('Length of the longest word',length)
# 10. Write a Python program to change a given string to a newly string where the first and last
# chars have been exchanged.
def swap_first_last(s):
    if len(s)<=1:
        return s
    return s[-1]+s[1:-1]+s[0]
print(swap_first_last('python'))
# 11. Write a Python program to remove characters that have odd index values in a given string.
string=input('Enter the string: ')
result=''
for i in range(len(string)):
    if i %2==0:
        result+=string[i]
print(result)
# 12. Write a Python program to count the occurrences of each word in a given sentence
sentence=input("Enter the sentence: ")
words=sentence.split()
count={}
for word in words:
    if word not in count:
        count[word]=1
    else:
        count[word]+=1
print(count)
# 18. Write a Python function to get a string made of the first three characters of a specified string.
# If the length of the string is less than 3, return the original string.
# Sample function and result :
# first_three('ipy') -> ipy
# first_three(' python') -> pyt
string=input('Enter the string: ')
for i in string:
    if len(string)>=3:
        result=string[:3]
    else:
        result=string
print(result)