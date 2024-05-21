from functions import Calculator

calculator = Calculator()


def main():
    choice = None
    while choice != range(1, 5):
        choice = int(
            input("Select Add[1], Subtract[2], Divide[3], Multiply[4], Quit[5] ")
        )
        if choice == 1:
            y_input = float(input("Input y value? "))
            x_input = float(input("Input x value? "))
            result = calculator.add(x_input, y_input)
            print(result)
        elif choice == 2:
            x_input = float(input("Input x value? "))
            y_input = float(input("Input y value? "))
            result = calculator.subtract(x_input, y_input)
            print(result)
        elif choice == 3:
            x_input = float(input("Input x value? "))
            y_input = float(input("Input y value? "))
            result = calculator.divide(x_input, y_input)
            print(result)
        elif choice == 4:
            x_input = float(input("Input x value? "))
            y_input = float(input("Input y value? "))
            result = calculator.multiply(x_input, y_input)
            print(result)
        elif choice == 5:
            print("Thank you")
            break


main()
