import calc_functions

while True:

    print("Hello, welcome to the calculator. What would you like to do?")
    options = ["Addition", "Subtraction", "Multiplication", "Division", "Average", "Slope"]
    print(options)
    action = input("What do you want to do?").lower()

    if action == "end":
        break
    else:
        calc_functions.run(action)

print("Good bye.")
