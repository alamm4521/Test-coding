#!/bin/python3.10


from asyncio.windows_events import NULL
from multiprocessing.connection import answer_challenge
import random
from pickle import TRUE
import this
import requests
print("Hello, World!")

if 5 > 2:
    print("Five is greater than two!")

if 5 > 2:
    print("5  2")
if 5 > 2:
    print("Five is greater than two!")
if 5 > 2:
    print("Five is greater than two!")


#this is coment
print("hello world")

# print("hello world") #this is comment

print("hello hp")

#thius is comment
# in multiuline
# more then one line

print("hello world")

"""
#thius is comment
# in multiuline
#more then one line
"""

print("hello world")

x = 5
y = float(1212)

print(type(x), x)
print(type(y), y)

# A will not overwrite a
a = "sally"
A = "SALLY"

print(a, " ", A)

# Legal variable names:

myvar = "jhon"
my_var = "jhon"
_my_var = "jhon"
My_var = "jhon"
MYVAR = "jhon"
myvar2 = "jhon"

print("Ligal variable ", myvar, my_var, _my_var, My_var, MYVAR, myvar2)

# This example will produce an error in the result
"""
2myvar = "John"
my-var = "John"
my var = "John"
"""
print("Remember that variable names are case-sensitive")

myVariableName = "jhon"

print("Camel Case Each word, except the first, starts with a capital letter:", myVariableName)

MyVariableName = "jhon"

print("Pascal Case Each word starts with a capital letter:", MyVariableName)

my_variable_name = "jhon"

print("Snake Case Each word is separated by an underscore character:", my_variable_name)

x, y, z = "Orange", "Banana", "Cherry"

print("Many Values to Multiple Variables Python allows you to assign values to multiple variables in one line: ")
print(x)
print(y)
print(z)

x = y = z = "Orange"
print("One Value to Multiple Variables And you can assign the same value to multiple variables in one line: ")
print(x)
print(y)
print(z)

fruts = ["apple", "banana", "orange"]
x, y, z = fruts

print("Unpack a Collection If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.")
print(x)
print(y)
print(z)

# Python - Output Variables
# Output Variables

x = "hello its good programing"
print(x)
#In the print() function, you output multiple variables, separated by a comma:
x = "hello"
y = " its good"
z = " programing"
print(x, y, z)

#You can also use the + operator to output multiple variables:
x = "hello"
y = "its good"
z = "programing"
print(x + y + z)
#For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x+y)
#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
"""
x = 5
y = "John"
print(x + y)
"""
#The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
x = 5
y = "John"
print(x, y)
#Python - Global Variables
#Global Variables
x = "East bread"


def myfunc():
    print("east not working " + x)


myfunc()

x = "East bread"


def myfunc():
    x = "timing is perfect"
    print("bread " + x)


#local
myfunc()
#global
print("bread co2  " + x)


def myfunc():
  global x
  x = "fantastic"


myfunc()

print("Python is " + x)


#

x = "awesome"


def myfunc():
  global x
  x = "fantastic"


myfunc()

print("Python is " + x)

#Python Data Types

#Built-in Data Types

x = 5

print(x, type(x))

x = "Hello World"  # str
print(x, type(x))
x = 20  # int
print(x, type(x))
x = 20.5  # float
print(x, type(x))
x = 1j  # complex
print(x, type(x))
x = ["apple", "banana", "cherry"]  # list
print(x, type(x))
x = ("apple", "banana", "cherry")  # tuple
print(x, type(x))
x = range(6)  # range
print(x, type(x))
x = {"name": "John", "age": 36}  # dict
print(x, type(x))
x = {"apple", "banana", "cherry"}  # set
print(x, type(x))
x = frozenset({"apple", "banana", "cherry"})  # frozenset
print(x, type(x))
x = True  # bool
print(x, type(x))
x = b"Hello"  # bytes
print(x, type(x))
x = bytearray(5)  # bytearray
print(x, type(x))
x = memoryview(bytes(5))  # memoryview
print(x, type(x))
x = None  # NoneType
print(x, type(x))

x = str("Hello World")  # str
print(x, type(x))
x = int(20)  # int
print(x, type(x))
x = float(20.5)  # float
print(x, type(x))
x = complex(1j)  # complex
print(x, type(x))
x = list(("apple", "banana", "cherry"))  # list
print(x, type(x))
x = tuple(("apple", "banana", "cherry"))  # tuple
print(x, type(x))
x = range(6)  # range
print(x, type(x))
x = dict(name="John", age=36)  # dict
print(x, type(x))
x = set(("apple", "banana", "cherry"))  # set
print(x, type(x))
x = frozenset(("apple", "banana", "cherry"))  # frozenset
print(x, type(x))
x = bool(5)  # bool
print(x, type(x))
x = bytes(5)  # bytes
print(x, type(x))
x = bytearray(5)  # bytearray
print(x, type(x))
x = memoryview(bytes(4))  # memoryview
print(x, type(x))

#Python Numbers
#Python Numbers

x = 2
y = 3.1
z = 1j

print(x, type(x))
print(y, type(y))
print(z, type(z))

x = 1
y = 7878787878787883787878
z = -255554645654656

print(x, type(x))
print(y, type(y))
print(z, type(z))

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))


x = 1    # int
y = 2.8  # float
z = 1j   # complex


#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


print(random.randrange(1, 100))

#Python Requests Module

#Python Requests Module


#the required first parameter of the 'get' method is the 'url':
x = requests.get('https://w3schools.com/python/demopage.htm')

#print the response text (the content of the requested file):
print(x.text)

#Python Casting

#Specify a Variable Type

x = int(1)
y = int(2.6)
z = int(3)

print(x)
print(y)
print(z)

x = float(1)
y = float(2.0)
z = float(3)
w = float(4.0)

print(x)
print(y)
print(z)
print(w)

x = str(1)
y = str(444)
z = str(2.00)

print(x)
print(y)
print(z)

print("hello")
print('hello')
hello = "hello "
print(hello)

a = "hello"

print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Strings are Arrays
a = "Hello, World!"
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])

print(a[6])
print(a[7])
print(a[8])
print(a[9])

print("Looping Through a String Since strings are arrays, we can loop through the characters in a string, with a for loop.")
for x in "banana":
 print(x)

print()

a = "Hello, World!"
print("Sring lenth", len(a))

#Check String To check if a certain phrase or character is present in a string, we can use the keyword in.

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


#Python Strings
#Check String
#Check String
#To check if a certain phrase or character is present in a string, we can use the keyword in .

txt = "the best tea in life is green tea with lemon and honney"
print("tea" in txt)
print("coffee" in txt)
if "lemon" in txt:
  print("yes, 'lemon' is present")
print("sugar" not in txt)
if "sugar" not in txt:
  print("No, 'expensive' is NOT present")

#Python - Slicing Strings
#https: // www.w3schools.com/python/python_strings_slicing.asp
#Slicing
txt = "hello world"
print(txt[2:5])

#Slice From the Start
print(txt[:5])
#Slice To the End
print(txt[2:])
#Slice To the End
print(txt)
print(txt[-5:-2])
#Python - Modify Strings
#Upper Case
a = "Hello, World!"
print(a.upper())
#Lower Case
print(a.lower())
a = "   Hello, World!  "
print(a.strip())
#Replace String
a = "Hello, World!"
print(a.replace("World", "Germany"))
print(a.replace("e", "a"))
#Split String
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']
#Python - String Concatenation
#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)
c = a + " " + b
print(c)
#Python - Format - Strings
#String Format
#Use the format() method to insert numbers into strings:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

age = 55
txt = "my name is jhone, and i am {}"
print(txt.format(age))

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

txt_qty = 5
txt_item = 200
txt_price = 90
txt_my_order = "I want {} pieces of item {} for {} dollars."
print(txt_my_order.format(txt_qty, txt_item, txt_price))

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

txt_my_order = "I want {1} pieces of item {2} for {0} dollars."
print(txt_my_order.format(txt_qty, txt_item, txt_price))
txt_my_order = "I want {2} pieces of item {0} for {1} dollars."
print(txt_my_order.format(txt_qty, txt_item, txt_price))
txt_my_order = "I want {0} pieces of item {1} for {2} dollars."
print(txt_my_order.format(txt_qty, txt_item, txt_price))

#Python - Escape Characters
#Escape Character

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#\'	Single Quote
txt = 'It\'s alright.'
print(txt)
#\\	Backslash
txt = "This will insert one \\ (backslash)."
print(txt)

#\n	New Line
txt = "Hello\nWorld!"
print(txt)
#\r	Carriage Return
txt = "Hello\rWorld!"
print(txt)
#\t	Tab
txt = "Hello\tWorld!"
print(txt)

#\b	Backspace
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)
#\f	Form Feed
txt = "Hello \fWorld!"
print(txt)
#\ooo	Octal value
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)
#\xhh	Hex value
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

#Python - String Methods
#String Methods

#capitalize()	Converts the first character to upper case
txt = "hello, and welcome to my world."

x = txt.capitalize()

print(x)
#casefold()	Converts string into lower case
txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)
#center()	Returns a centered string
txt = "banana"

x = txt.center(20)

print(x)
#count()	Returns the number of times a specified value occurs in a string
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)
#encode()	Returns an encoded version of the string
txt = "My name is Ståle"

x = txt.encode()

print(x)
#endswith()	Returns true if the string ends with the specified value
txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)
#expandtabs()	Sets the tab size of the string
txt = "H\te\tl\tl\to"

x = txt.expandtabs(2)

print(x)
#find()	Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)
#format()	Formats specified values in a string
txt = "For only {price:.2f} dollars!"
print(txt.format(price=49))
#format_map()	Formats specified values in a string
point = {'x': 4, 'y': -5}
print('{x} {y}'.format_map(point))

point = {'x': 4, 'y': -5, 'z': 0}
print('{x} {y} {z}'.format_map(point))
#index()	Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)
#isalnum()	Returns True if all characters in the string are alphanumeric
txt = "Company12"

x = txt.isalnum()

print(x)
#isalpha()	Returns True if all characters in the string are in the alphabet
txt = "CompanyX"

x = txt.isalpha()

print(x)
#isdecimal()	Returns True if all characters in the string are decimals
txt = "\u0033"  # unicode for 3

x = txt.isdecimal()

print(x)
#isdigit()	Returns True if all characters in the string are digits
txt = "50800"

x = txt.isdigit()

print(x)
#isidentifier()	Returns True if the string is an identifier
txt = "Demo"

x = txt.isidentifier()

print(x)
#islower()	Returns True if all characters in the string are lower case
txt = "hello world!"

x = txt.islower()

print(x)
#isnumeric()	Returns True if all characters in the string are numeric
txt = "565543"

x = txt.isnumeric()

print(x)
#isprintable()	Returns True if all characters in the string are printable
txt = "Hello! Are you #1?"

x = txt.isprintable()

print(x)
#isspace()	Returns True if all characters in the string are whitespaces
txt = "   "

x = txt.isspace()

print(x)
#istitle()	Returns True if the string follows the rules of a title
txt = "Hello, And Welcome To My World!"

x = txt.istitle()

print(x)
#isupper()	Returns True if all characters in the string are upper case
txt = "THIS IS NOW!"

x = txt.isupper()

print(x)
#join()	Joins the elements of an iterable to the end of the string
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)
#ljust()	Returns a left justified version of the string
txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.")
#lower()	Converts a string into lower case
txt = "Hello my FRIENDS"

x = txt.lower()

print(x)
#lstrip()	Returns a left trim version of the string
txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")
#maketrans()	Returns a translation table to be used in translations
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))
#partition()	Returns a tuple where the string is parted into three parts
txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)
#replace()	Returns a string where a specified value is replaced with a specified value
txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)
#rfind()	Searches the string for a specified value and returns the last position of where it was found
txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)
#rindex()	Searches the string for a specified value and returns the last position of where it was found
txt = "Mi casa, su casa."

x = txt.rindex("casa")

print(x)
#rjust()	Returns a right justified version of the string
txt = "banana"

x = txt.rjust(20)

print(x, "is my favorite fruit.")
#rpartition()	Returns a tuple where the string is parted into three parts
txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("bananas")

print(x)
#rsplit()	Splits the string at the specified separator, and returns a list
txt = "apple, banana, cherry"

x = txt.rsplit(", ")

print(x)
#rstrip()	Returns a right trim version of the string
txt = "apple, banana, cherry"

x = txt.rsplit(", ")

print(x)
#split()	Splits the string at the specified separator, and returns a list
txt = "welcome to the jungle"

x = txt.split()

print(x)
#splitlines()	Splits the string at line breaks and returns a list
txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)
#startswith()	Returns true if the string starts with the specified value
txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)
#strip()	Returns a trimmed version of the string
txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")
#swapcase()	Swaps cases, lower case becomes upper case and vice versa
txt = "Hello My Name Is PETER"

x = txt.swapcase()

print(x)
#title()	Converts the first character of each word to upper case
txt = "Welcome to my world"

x = txt.title()

print(x)
#translate()	Returns a translated string
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))
#upper()	Converts a string into upper case
txt = "Hello my friends"

x = txt.upper()

print(x)
#zfill()	Fills the string with a specified number of 0 values at the beginning
txt = "50"

x = txt.zfill(10)

print(x)

#https://www.w3schools.com/python/python_booleans.asp
#Python Booleans
#Boolean Values
print(10 > 9)
print(10 == 9)
print(10 < 9)

#When you run a condition in an if statement, Python returns True or False:

#Example
#Print a message based on whether the condition is True or False:

a = 200
b = 5

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Evaluate Values and Variables
#The bool() function allows you to evaluate any value, and give you True or False in return ,

#Example
#Evaluate a string and a number:

print("hello loadsheding")
print(bool(1))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#Most Values are True
print(bool("abc"))
print(bool(123))
print(["apple", "orange", "banana"])

#Some Values are False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


class myclass():
  def __len__(self):
    return 0


myobj = myclass()
print(bool(myobj))


class hirokclass():
  def __len__(self):
    return 0

  def __hirok__(self):
    return 0


myobj = myclass()
print(bool(myobj))

hirokobj = hirokclass()
print(bool(hirokobj))

#https://www.w3schools.com/python/python_booleans.asp
#Functions can Return a Boolean
#You can create functions that returns a Boolean Value:


def myFunction():
  return True


print(myFunction())
a = ""


def hirokfunction():
  qwe = "helllo"
  return qwe


print(hirokfunction())

#Print "YES!" if the function returns True, otherwise print "NO!":


def my_function():
  a = "hello"

  return a


print(a)
if my_function():
  print("YES! ", my_function())
else:
  print("NO!")

#Check if an object is an integer or not:

  x = 500
  print(isinstance(x, int))

#https://www.w3schools.com/python/python_operators.asp

#Python Operators
#Python Operators
print(10 + 500)
print("a"+"b")
a = 40
b = 5
#+	Addition	x + y
print(a+b)
#-	Subtraction	x - y
print(a-b)
#*	Multiplication	x * y
print(a*b)
#/	Division	x / y
print(a/b)
#%	Modulus	x % y
print(a % b)
#** Exponentiation x ** y
print(a**b)
#// Floor division x // y
x = 40
y = 5

print(x // y)

#Python Assignment Operators

#=	x = 5	x = 5
x = 5
print(x)
#+= x += 3 x = x + 3
x = 5
x += 5
print(x)
x = x + 5
print(x)
#-= x -= 3 x = x - 3
x = 5
x -= 5
print(x)
x = x - 5
print(x)
#*= x *= 3 x = x * 3
x = 5
x *= 10
print(x)
x = x * 5
print(x)
#/= x /= 3 x = x / 3
x = 5
x /= 10
print(x)
x = x / 5
print(x)
#%= x %= 3 x = x % 3
x = 10
x %= 5
print(x)
x = x % 5
print(x)
#//= x //= 3 x = x // 3
x = 10
x //= 5
print(x)
x = 10
x = x // 5
#**= x **= 3 x = x ** 3
x = 2
x **= 5
print(x)
x = x ** 5
print(x)
#&= x &= 3 x = x & 3
x = 5
x &= 5
print(x)
x = 10
x = x & 5
print(x)
#|= x |= 3 x = x | 3
x = 10
x |= 5
print(x)
#^= x ^= 3 x = x ^ 3
x = 10
x ^= 2
print(x)
x = x ^ 2
print(x)
#>>= x >>= 3 x = x >> 3
x = 10
x >>= 2
print(x)
x = 10
x = x >> 2
print(x)
#<<= x <<= 3 x = x << 3
x = 10
x <<= 2
print(x)
x = x << 2
print(x)

#Python Comparison Operators

#==	Equal	x == y
x = 5
y = 1
print(x == y)
#!=	Not equal	x != y
print(x != y)
#>	Greater than	x > y
print(x > y)
#<	Less than	x < y
print(x < y)
#>=	Greater than or equal to	x >= y
print(x >= y)
#<=	Less than or equal to	x <= y
print(x <= y)

#Python Logical Operators

#and Returns True if both statements are true	x < 5 and x < 10
x = 9
print(x > 4 and x < 10)
print(x < 5 and x > 10)
#or Returns True if one of the statements is true	x < 5 or x < 4
print(x > 5 or x < 10)
print(x < 5 or x > 10)
#not Reverse the result, returns False if the result is true not (x < 5 and x < 10)
print(not (x > 5 and x < 10))
print(not (x < 5 and x > 10))

#Python Membership Operators

#in Returns True if a sequence with the specified value is present in the object	x in y
x = ["apple", "banana"]
print("banana" in x)
#not in Returns True if a sequence with the specified value is not present in the object	x not in y
x = ["apple", "banana"]
print("mango" not in x)
print("mango" in x)

#Python Bitwise Operators

#https://www.w3schools.com/python/python_lists.asp
#Python Lists
#List
thislist = ["apple", "banana", "cherry"]
print(thislist)

list_frute = ["mango", "orange", "apple"]
print(list_frute)

#Allow Duplicates
#Lists allow duplicate values:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]

print(thislist)

list_frute = ["orange", "apple", "cherry", "orange", "apple", "cherry"]

print(list_frute)

#List Length
#To determine how many items a list has, use the len() function:

list_frute = ["orange", "apple", "cherry", "orange", "apple", "cherry"]

print(len(list_frute))

#List Items - Data Types

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

list_frute = ["orange", "apple", "banana"]
list_numbers = [3, 4, 4, 5, 6, 7, 8]
list_bool = [True, False, True]

print(list_frute)
print(list_numbers)
print(list_bool)

print(list_frute, list_numbers, list_bool)

list_type = ["abc", "55", "True", "89", "sexy"]

print(type(list_type))

#The list() Constructor
#It is also possible to use the list() constructor when creating a new list.

list_const = list(("apple", "banana", "manago"))
print(list_const)

#Python - Access List Items
#Access Items

print("Python - Access List Items")
print("Access Items")

list_access = ["apple", "orange", "banana"]
print(list_access[1])

#https: // www.w3schools.com/python/python_lists_access.asp
#Negative Indexing

#Print the last item of the list:
print("Negative Indexing")
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

list_neg_index = ["apple", "banana", "cherry"]
print(list_neg_index[-2])

#Range of Indexes

this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:5])
print(this_list[:4])
print(this_list[2:])
#Range of Negative Indexes
print(this_list[-4:-1])
#Check if Item Exists
if "banana" in this_list:
  print("Yes, 'banana' is in the fruits List'")
if "sony" in this_list:
  print("Yes, 'banana' is in the fruits List")
else:
  print("No, 'this list not contain sony'")

#https://www.w3schools.com/python/python_lists_change.asp
#Python - Change List Items

#Change Item Value
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
this_list[1] = "blackcurrant"
print(this_list)

#Change a Range of Item Values
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
this_list[1:3] = ["detol", "president"]
print(this_list)

list_this = ["apple", "banana", "mango"]
list_this[1:3] = ["air purifier", "watermelon"]
print(list_this)
list_this[1:2] = ["air purifier", "watermelon"]
print(list_this)

#Insert Items

list_this = ["apple", "banana", "mango"]
list_this.insert(2, "watermelon")
print(list_this)

#Python - Add List Items
#Append Items

list_this = ["apple", "banana", "mango"]
list_this.append("detol")
print(list_this)

#Insert Items
list_this = ["apple", "banana", "mango"]
list_this.insert(1, "orange")
print(list_this)

#Extend List
#list_this = ["apple", "banana", "mango"]
list_tropical_fruts = ["mango", "pineapple", "papaya"]
list_this.extend(list_tropical_fruts)
#this also work
#list_this = list_this + list_tropical_fruts
print(list_this)

#Add Any Iterable
list_this = ["apple", "banana", "mango"]

_list_tuple1 = ("kiwi", "detol")

print(list_this)

#Python - Remove List Items

#Remove Specified Item

_list_this = ["apple", "banana", "cherry"]
_list_this.remove("banana")
print(_list_this)

#Remove Specified Index

_list_this = ["apple", "banana", "cherry"]

_list_this.pop(2)
print(_list_this)
#If you do not specify the index, the pop() method removes the last item.
_list_this = ["apple", "banana", "cherry"]
_list_this.pop()
print(_list_this)
#The del keyword also removes the specified index:
_list_this = ["apple", "banana", "cherry"]
del _list_this[0]
print(_list_this)
#The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist
#Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#https://www.w3schools.com/python/python_lists_loop.asp

#Python - Loop Lists
#Loop Through a List

this_list = ["apple", "banana", "cherry"]
for x in this_list:
  print(x)

#Loop Through the Index Numbers
print("Loop Through the Index Numbers")
this_list = ["apple", "banana", "cherry"]
for i in range(len(this_list)):
  print(this_list[i])

#Using a While Loop
print("Looping Using List Comprehension")
this_list = ["i need apple wine",
             "i need banana",
             "its cherry, bikini is good for you"]
i = 0
while i < len(this_list):
    print(this_list[i])
    i = i + 1

#Python - List Comprehension
print("Python - List Comprehension")
print("")
#List Comprehension
print("List Comprehension")

list_wine = ["apple", "banana", "cherry", "mango", "lemmon", "sugar"]
new_list = []

for x in list_wine:
  if "ch" in x:
    new_list.append(x)

#With list comprehension you can do all that with only one line of code:

print(new_list)
print("The condition is like a filter that only accepts the items that valuate to True.")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "qqqqq"]

print(newlist)

#https://www.w3schools.com/python/trypython.asp?filename=demo_list_comprehension_noif
#https://www.w3schools.com/python/python_lists_comprehension.asp

#The Syntax
#newlist = [expression for item in iterable if condition == True]

#Condition

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x > "apple"]

print(newlist)

#The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".
#The condition is optional and can be omitted:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits]

print(newlist)

#Iterable

newlist = [x for x in range(10)]

print(newlist)

#Same example, but with a condition:

newlist = [x for x in range(10) if x < 5]

print(newlist)

#Expression

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)

#You can set the outcome to whatever you like:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist)

#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)

#The expression in the example above says:

#"Return the item if it is not banana, if it is banana return orange".

#Python - Sort Lists

#https://www.w3schools.com/python/python_lists_sort.asp

#Sort List Alphanumerically

#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort()

print(thislist)

#Sort the list numerically:

thislist = [100, 50, 65, 82, 23]

thislist.sort()

print(thislist)

#Sort Descending
#To sort descending, use the keyword argument reverse = True:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort(reverse=True)

print(thislist)

#Sort the list descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)

#Customize Sort Function


def myfunc(n):
  return abs(n - 60)


thislist = [100, 50, 65, 82, 23]

thislist.sort(key=myfunc)

print(thislist)

#Case Insensitive Sort

thislist = ["banana", "Orange", "kiwi", "Cherry", "pepsi"]

thislist.sort()

print(thislist)\

thislist = ["banana", "Orange", "kiwi", "Cherry", "pepsi"]

thislist.sort(key=str.lower)

print(thislist)

thislist = ["banana", "Orange", "kiwi", "Cherry", "pepsi"]

thislist.reverse()

print(thislist)

#Python - Copy Lists

#Copy a List

#https://www.w3schools.com/python/python_lists_copy.asp


#Copy a List

mylist = ["apple", "banana", "cherry"]

thislist = mylist.copy()
#thislist = mylist
print(thislist)

#Another way to make a copy is to use the built-in method list().

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Python - Join Lists

#Join Two Lists

list1 = ["1", "2", "4", "6", "8"]
list2 = ["2", "4", "6", "7", "7", "5", "5"]

list3 = list1 + list2

print(list3)

#Another way to join two lists is by appending all the items from list2 into list1, one by one:

for x in list2:
  list1.append(x)

print(list1)

#Or you can use the extend() method, which purpose is to add elements from one list to another list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#Python - List Methods

#List Methods

#Python List append() Method

fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)

#Python List clear() Method

#Remove all elements from the fruits list:

fruits = ['apple', 'banana', 'cherry', 'orange']

fruits.clear()

print(fruits)

#Python List copy() Method

#Copy the fruits list:
fruits = ['apple', 'banana', 'cherry', 'orange']

x = fruits.copy()

print(x)

#Python List count() Method

#Return the number of times the value "cherry" appears in the fruits list:

fruits = ["apple", "banana", "cherry"]

x = fruits.count("cherry")

print(x)

fruits = [1, 4, 2, 9, 7, 8, 9, 3, 1]

x = fruits.count(9)

print(x)

#Python List extend() Method

#Add the elements of cars to the fruits list:

fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits)

fruits = ['apple', 'banana', 'cherry']

points = (1, 5, 8, 9)

fruits.extend(points)

print(fruits)

#Python List index() Method

#What is the position of the value "cherry":

fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

#What is the position of the value "cherry":

fruits = [55, 7, 88, 2, 4, 5, 7, 98, 3]

x = fruits.index(88)

print(x)

#Python List insert() Method

#Insert the value "orange" as the second element of the fruit list:

fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")

print(fruits)

#Python List pop() Method
#Remove the second element of the fruit list:

fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)

print(fruits)

fruits = ["apple", "banana", "cherry"]

x = fruits.pop(1)

print(x)

#Python List remove() Method

fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")

print(fruits)

#Python List reverse() Method

fruits = ['apple', 'banana', 'cherry']

fruits.reverse()

print(fruits)

#Python List reverse() Method

fruits = ['apple', 'banana', 'cherry']

fruits.reverse()

print(fruits)


#Python List sort() Method

cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(cars)

#Python List Exercises
#https://www.w3schools.com/python/python_lists_exercises.asp

#Python Tuples

mytuple = ("apple", "banana", "cherry")

print(mytuple)

#Tuple

thistuple = ("apple", "banana", "cherry")
#thistuple = thistuple + ("dettol",)
print(thistuple)

#https://www.w3schools.com/python/python_tuples.asp


print("hello world")
#Python Tuples
#A tuple is a collection which is ordered and unchangeable.
mytuple = ("apple","banana","cherry")

print(mytuple)

thistuple = ("apple","banana","cherry","apple","cherry","decorta")
print(thistuple)

#Tuple Length

print(len(thistuple))

#Create Tuple With One Item

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Tuple Items - Data Types

tuple1 = ("appple","banana","cherry")
tuple2 = (1,65,6,7,7,78,8,98)
tuple3 = (True, False, True, False)

print(tuple1)
print(tuple2)
print(tuple3)


#A tuple can contain different data types:
tuple1 = ("anb", 444, True, 89, 'male')

print(tuple1)

#What is the data type of a tuple?

mytuple = ("apple","banana","cherry")
print(type(mytuple))

#The tuple() Constructor

thistuple = tuple(("apple","banana","cherry"))
#thistuple = tuple({"apple", "banana"})
#thistuple = tuple(["apple", "banana"])
print(thistuple)

#Python - Access Tuple Items
#https://www.w3schools.com/python/python_tuples_access.asp

#Access Tuple Items

thistuple = ("apple","banana","cherry")
print(thistuple[1])

#Negative Indexing
print(thistuple[-2])

#Range of Indexes

thistuple = ("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistuple[2:5])

#By leaving out the start value, the range will start at the first item:

thistuple = thistuple
print(thistuple[:4])

#By leaving out the end value, the range will go on to the end of the list:

thistuple = thistuple
print(thistuple[2:])

#Specify negative indexes if you want to start the search from the end of the tuple:

#This example returns the items from index -4 (included) to index -1 (excluded)

thistuple = thistuple

print(thistuple[-4:-1])

#Check if Item Exists

thistuple = thistuple

if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
  
#Python - Update Tuples
#https://www.w3schools.com/python/python_tuples_update.asp

#Change Tuple Values

x = ("apple","banana","cherry")
y = list(x)

y[1] = "kiwi"
x = tuple(y)

print(x)

#Add Items
thistuple = thistuple
print(thistuple)
y = list(thistuple)
y.append("Charlie Puth - Attention ")
thistuple = tuple(y)

print(thistuple)

#Add tuple to a tuple

thistuple = ("apple","banana","cherry")
y = ("Charlie Puth - Left And Right (feat. Jung Kook of BTS) [Official Video]",)
thistuple += y 
print(thistuple)

#Note: You cannot remove items in a tuple

thistuple = thistuple
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

#Or you can delete the tuple completely:

thistuple = thistuple
del thistuple

 #print(thistuple)  
#https://www.w3schools.com/python/python_tuples_unpack.asp
#Python - Unpack Tuples
