def run(action):
    if action == "addition":
        Addition()

    elif action == "subtraction":
        Subtraction()

    elif action == "multiplication":
        Multiplication()

    elif action == "division":
        Division()

    elif action == "average":
        # Average()
        Average()

    elif action == "slope":
        #slope()
        slope()

    elif action == "velocity formula":
        velocity_formula()

    else:
        print("What do you mean," + action + "?")


def velocity_formula():
    answer = input("what do you want to know? \n>>>")
    if answer == "time":
        time()

    elif answer == "velocity":
        velocity()

    elif answer == "displacement":
        displacement()

    else:
        print("You stupid.")

def time():
    velocity = float(input("enter velocity \n>>>"))
    displacement = float(input("enter displacement \n>>>"))
    answer = displacement / velocity
    print(answer)


def velocity():
    time = float(input("Enter time \n>>>"))
    displacement = float(input("enter displacement \n>>>"))
    answer = displacement / time
    print(answer)

def displacement():
    time = float(input("Enter time \n>>>"))
    velocity = float(input("enter velocity \n>>>"))
    answer = time * velocity
    print(answer)


def Addition():
    number1, number2 = ask_two_numbers()

    answer = float(number1) + float(number2)
    print(answer)


def Subtraction():
    number1, number2 = ask_two_numbers()

    answer = float(number1) - float(number2)
    print(answer)


def Multiplication():
    number1, number2 = ask_two_numbers()

    answer = float(number1) * float(number2)
    print(answer)


def Division():
    number1, number2 = ask_two_numbers()

    answer = float(number1) / float(number2)
    print(answer)


def Average():
    num_list = []
    while True:
        num = input("Insert numbers. \nType no more to get an average. \n>>>")
        if num == "no more":
            break
        else:
            num_list.append(float(num))

    sum = 0
    for x in num_list:
        sum = sum + x

    total = len(num_list)

    answer = sum / total
    print(answer)


def Average2():
    num = 0
    length = 0
    while True:
        ip = input("Insert numbers. \nType no more to get an average. \n>>>")
        if ip == "no more":
            break
        else:
            num += float(ip)
            length += 1
    answer = num / length
    print(answer)

def slope():
    x1 = float(input("Enter an x1 coordinate: \n>>>"))
    y1 = float(input("Enter an y1 coordinate: \n>>>"))
    x2 = float(input("Enter an x2 coordinate: \n>>>"))
    y2 = float(input("Enter an y2 coordinate: \n>>>"))
    m = (y2 - y1) / (x2 - x1)
    print(m)

def slope2():
    p1 = input("coordinate(x1, y1): \n>>>").split()
    for i in range(2):
        p1[i] = float(p1[i])
        x1 = p1[0]
        y1 = p1[1]

    p2 = input("coordinate(x2, y2): \n>>>").split()
    for i in range(2):
        p2[i] = float(p2[i])
        x2 = p2[0]
        y2 = p2[1]
    m = (y2 - y1) / (x2 - x1)
    print(m)


def ask_two_numbers():
    number1 = input("first number? \n>>>")
    number2 = input("second number? \n>>>")
    return number1, number2

