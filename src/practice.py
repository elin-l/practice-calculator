class Vehicle:
    name = ""
    kind = ""
    color = ""
    value = 0.0

    def __init__(self, a, b, c, d):
        self.name = a
        self.kind = b
        self.color = c
        self.value = d


    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


car1 = Vehicle("fer", "cra", "red", 600000.00)
car2 = Vehicle("van", "car", "blue", 10000.00)



print(car1.description())
print(car2.description())



import re

find_members = []
x= []

def helloTest():
    print("hihihi")

for x in range(6):
    print(x)


def Average():
    number1, number2 = ask_two_numbers()

    answer = (float(number1) + float(number2)) / 2
    print(answer)

    number_list = []
    number_ = number_list.extend(input("insult numbers"))
    number_list = number_
    number_of_number = len(number_list)
    answer = sum(number_) / number_of_number


def ask_two_numbers():
    number1 = input("first number?")
    number2 = input("second number?")
    return number1, number2


number = input("insult numbers")
number_list = number


def Average():
    number_of_number = input("How many numbers would you like to use?")
    num_of_num = input("first number?")

    answer = sum(num_of_num) / number_of_number

def slope2():
    p1 = input("coordinate(x1, y1): ").split()
    for x1 in p1:
        x1 = float(x1)
    for y1 in p1:
        y1 = float(y1)
    p2 = input("coordinate(x2, y2): ").split()
    for x2 in p2:
        x2 = float(x2)
    for y2 in p2:
        y2 = float(y2)

    m = (y2 - y1) / (x2 - x1)
    print(m)


    ans = input("What do you want to know? There are three options : time, velocity, displacement")
    if ans == "time":
        velocity = float(input("enter velocity"))
        displacement = float(input("enter displacement"))
        answer = displacement / velocity
    print(answer)

#    elif ans == "velocity":
#        time = float(input("Enter time"))
#        displacement = float(input("enter displacement"))
#        answer = displacement / time
#    print(answer)

#    elif ans == "displacement":
#        time = float(input("Enter time"))
#        velocity = float(input("enter velocity"))
#        answer = time * velocity
#    print(answer)

#    else:
#    print("You stupid.")