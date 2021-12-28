# Essential Python String Methods

import re

# strip() with character
s = 'www.example.com'.strip('cmow.')
#print(s)

s1 = '###hello###'.strip('#')
#print(s1)

# remove prefix - will remove all characters, so t, h, and r 
s2 = 'Author: three!'.lstrip('Author: ')
#print(s2)

s3 = 'Author: three!'.removeprefix('Author: ')
#print(s3)

s4 = 'HelloPython'.removesuffix('Python')
#print(s4)

# replace 
s5 = 'string methods in python'.replace(' ', '-')
#print(s5)

# re.sub
s6 = 'string   methods in python'
s61 = re.sub('\s+', '-', s6)
#print(s61)

# split()
s7 = 'string methods in python'.split(' ') # you can use maxsplit=# as a parameter, with # being a number to choose how many splits occur. 
#print(s7)

# r.split()
s8 = 'string methods in python'.rsplit(' ', maxsplit=1) # maxsplit is optional
#print(s8)

# .join()
s9 = ['string', 'methods', 'in', 'python']
s91 = ' '.join(s9)    # instead of joining with a space, you can use another delimiter such as a hyphen or comma
#print(s91)

# upper()
s10 = 'python is awesome!'.upper()
#print(s10)

# lower()
s11 = 'PYTHON IS AWESOME!'.lower()
#print(s11)

# capitalize()
s12 = 'python is awesome!'.capitalize()
#print(s12)

# islower()
s13 = 'PYTHON IS AWESOME!'.islower()    # False
s13_2 = 'python is awesome!'.islower()  # True
#print(s13)
#print(s13_2)

# isupper()
s14 = 'PYTHON IS AWESOME!'.isupper()    # True
s14_2 = 'PYTHON is awesome!'.isupper()  # False
#print(s14)
#print(s14_2)

# count()
s15 = 'hello world'.count('o')
#print(s15)

# find() - will return first lowest index where it finds the substring
## Will return -1 if it does not find anything 
s16 = 'Machine Learning'
index = s16.find('a')
#print(index)
#print(s16[index:])

# rfind() - will start searching from the right side
s17 = 'Machine Learning'
index = s17.rfind('a')
#print(index)
#print(s17[index:])

# startswith()
#print('Patrick'.startswith('P'))   # True

# endswith()
#print('Patrick'.endswith('ck'))    # True

# partition() - splits the string at the first occurence of the substring
# Will return a tuple with 3 elements
# Given string is in the middle
# If it does not find the given string, then the whole string is the first item, and the other two items are two empty strings
s18 = 'Python is awesome!'
parts = s18.partition('is')
parts_2 = s18.partition('was')
#print(parts)
#print(parts_2)

# center()
s19 = 'Python is awesome!'
s19_2 = s19.center(30, '-')   # first parameter is the given length, and the 2nd parameter is the 'fill' character
#print(s19_2)

# ljust()
s20 = 'Python is awesome!'
s20_2 = s20.ljust(30, '-')  
#print(s20_2)

# rjust()
s21 = 'Python is awesome!'
s21_2 = s21.rjust(30, '-')  
#print(s21_2)

# f-strings
num = 1 
language = 'Python'
s22 = f'{language} is number {num} in programming!'
#print(s22)

# swapcase()
s23 = 'HELLO world'
s23_2 = s23.swapcase()
#print(s23_2)

# zfill()  -- returns a string with the length of the given number. Uses 0s to fill the string, starting from the left side
s24 = '42'.zfill(5)
print(s24)
s24_2 = '-42'.zfill(5)
print(s24_2)