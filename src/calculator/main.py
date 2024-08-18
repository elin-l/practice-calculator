import calc_functions

options = ["Addition", "Subtraction", "Multiplication", "Division", "Average", "Slope", "Velocity formula"]

print("Hello. Welcome to the practice calculator.")

while True:

    print("What would you like to do?")
    print(options)
    action = input("What do you want to do? \nType end to close the app. \n>>>").lower()


    if action == "end":
        break
    else:
        calc_functions.run(action)

print("Good bye.")

