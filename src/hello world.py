# from bdb import test

print("This line will be printed.")

y = -75545547
if y/3 >= 1:
    # this prints the value of y/3
    print(y/3)

x = "Hello"
y = "World!"

print(x + " " + y)

myInt = 8

myFloat = 3.0

print(myInt)
print(myFloat)

m = float(7)
n = int(myFloat)

# string(n) means changing the form of n int to str
c = str(n)
print("The value is: " + c)

# backslashes ignore things right behind them
myString = "Okay\"s"
print(myString)

a, b = 1, 2
print(a, b)

# it calculates from what is behind =(and left to right)
# a,b = b * 2, a * 2 => a, b = 2, 2 ... a = 2, b = 2
a, b = b, a

# this doesn't calculate them at the same time
# a = b => a=2, a= b => b=1 (X) ,   a = b => a=2, b = a (a=2) => b=2 (O)
a = b
b = a


# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)


myList = []
# list.append : add something into a list
myList.append(1)
myList.append(2)
myList.append(3)
# if you want to access an index, the index should be created
for x in myList:
    print(x)

numbers = [1, 2, 3]
strings = ["hello", "world"]
names = ["John", "Erica", "Jessica"]
# every index starts with 0 in python
#John = 0, Erica = 1

# write your code here
# names[] refers the process of accessing a specific element in a sequence, such as a string or list
second_name = names[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

number = (1 + 3 * 3) / 5
number = int(number)
print(number)

remainder = 1937 % 3
print(remainder == 0)
print(True == 1)
print(False == 0)

squared = (7 ** 2)
cubed = (7 ** 3)
print(squared, cubed)

helloworld = "Hello" + " " + "World" + "!"
print(helloworld)

lotsOfKyle = "Kyle" * 13
print(lotsOfKyle)

odd_numbers = [1, 3, 5, 7, 9, 11, 13]
even_numbers = [2, 4, 6, 8, 10, 12, 14]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1,2,3] * 2)

x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

floatA = 10.0
# %s = string, #f = float, %d = integer
# %s find thing to put behind % (same way %f go.)
# % means find
print("the %s is %f" % ("float",floatA))

# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)

name = "Kyle"
age = 21
print("His name is %s, and he is %d years old" % (name, age))

print("the %s is %.2f" % ("float",floatA))

# list -> order is important. so it print in order
data = ("John", "Doe", 53.44)
format_string = "Hello"

print(format_string + " %s %s. Your current balance is $%d." % (data))

astring = "Hello world!"
astring2 = 'Hello world!'

print(len(astring))
print(astring.index("H"))
print(astring[3:7])
print(astring.count("o"))
print(astring[3:-3])

print(astring[6:10])
print(astring[6:10:2])
print(astring[::-1])
print(astring.upper())
print(astring.lower())
print(astring.startswith("world!"))
print(astring.endswith("world!"))

astring = "Hello world!"
afewwords = astring.split(" ")
print(astring, afewwords)



s = "hiiiiiiiaaiiiiiiiiis"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

x = 13
print(x == 13)
print(x == 12)
print(x > 12)

name = "Kyle"
two_names = ("Kyle", "Elin")
age = 21
if name == "Kyle" and age == 21:
    print("Your name is %s and you are %d years old." % (name, age))
if name == "Kyle" or name == "Elin":
    print("Your name is %s or %s." % (two_names))

print("Hello")

name = "Kyle"
if name in ["Kyle", "Elin"]:
    print("your name is either %s or %s." % ("Kyle", "Elin"))

x = [1, 2, 3]
y = [1, 2, 3]
print(x==y)
print(x is y)

print(not False)
print((not False) == (False))

print("Hello world")
# change this code
number = 10
second_number = 10
first_array = [1,2,3]
second_array = [1,2]

if number < 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number > 10:
    print("6")

print("Hello Worlds")
primes = [1, 2, 3, 4, 5]
for prime in primes:
    print (prime)

print("assertv")

for x in range(4):
    print(x)
for y in range(3, 7):
    print(y)
for z in range(3, 7, 4):
    print(z)


count = 0
while count < 3:
    print(count)
    count += 1  # This is the same as count = count + 1

print("hihi")

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

print("HI")

for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

print("keke")


count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

    for i in range(1, 10):
        if (i % 5 == 0):
            break
        print(i)
    else:
        print("this is not printed because for loop is terminated because of break but not due to fail in condition")


numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
print("")
for number in numbers:
    if (number < 237) and (number % 2 == 0):
        print(number)

def myfunction(x):
    print(x)

myfunction("hi")

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s" % (username, greeting))
my_function_with_args("Kyle", "enjoy")

def sum_two_numbers(a, b):
    return a + b
k = sum_two_numbers(4, 5)
print(k)

# Define our 3 functions
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)

# Modify this function to return a list of strings as defined above
def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]
# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence():
    for x in list_benefits():
        print(x + " is a benefit of functions!")

build_sentence()

class MyClass:
    variable = "blah"

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)

menu = {}
#menu is pizza, chicken. 10.00 is under PIZZA.
menu["pizza"] = 10.00
menu["chicken"] = 20.00

#this is how to find the menu which has 10.00 value
for item in menu:
    if menu[item] == 10.00:
        print(item)
print(menu)

second_menu = {
    "pizza": 10.00,
    "chicken": 20.00
}
print(second_menu)
#[] = list/index, () = tuple(size 정해짐), {} = dictionary
third_menu = {"pizza" : 10.00, "chicken" : 20.00}

#items() -function임 -> name and number 함께 불러오기 ㄱㄴ
for name, number in menu.items():
    print("%d is menu of %s" % (number, name))

#item = pizza, chicken -> menu[item] = 10.00, 20.00
for item in menu:
    print("%d is menu of %s" % (menu[item], item))

new_menu = {
    "pizza": 10.00,
    "chicken": 20.00
}
del new_menu["chicken"]
#it still has value but
#new_menu.pop("pizza")
#it returns value
a = new_menu.pop("pizza")
print(a)

print("HelloWorlds!")

christmas_menu = {
    "turkey": 10.00,
    "cookie": 20.00,
    "coke": 30.00,
    "burger": 40.00
}

del christmas_menu["turkey"]
christmas_menu["cake"] = 50.00

if "cake" in christmas_menu:
    print("cake is listed in the christmas.")

if "turkey" not in christmas_menu:
    print("turkey is not listed in the christmas_menu.")

import practice
practice.helloTest()

from practice import helloTest
helloTest()


from random import randint

import random
x = []
for _ in range(500):
    new_number = random.randint (0,5)
    x.append(new_number)

y = 7123471277924902987420
z = 824138421243124109874918732
y = y + z
print(y)

y = 0
for number in x:
    y = y + number
print(y / 500)

x = 0
for _ in range(500):
    x = x + randint(0,5)
print(x/500)

x = 0
count = 0
while count < 500:
    x = x + random.randint(0,5)
    count += 1  # This is the same as count = count + 1
print(x/500)


a = [1,2,3,4,5,6]
print([x + 1 for x in a if x % 2 == 0])

