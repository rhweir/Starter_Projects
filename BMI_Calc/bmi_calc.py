from calculations import Calculator

calculator = Calculator()


def main():
    print(
        "Welcome to the BMI Calculator\nWould you prefer to work in imperial or metric units?"
    )
    choice = None
    while choice != 1 or 2:
        choice = int(input("Enter (1) for imperial or (2) for metric "))
        if choice == 1:
            weight = int(input("Please enter your weight in lbs. "))
            weight = calculator.lbs_to_kg(weight)
            height = int(input("Please enter your height in inches. "))
            height = calculator.inch_to_m(height)
            result = calculator.calc_bmi(weight, height)
            print(f"Your BMI is {result}")
            break
        elif choice == 2:
            weight = int(input("Please enter your weight in kg. "))
            height = int(input("Please enter your height in cm. "))
            height = calculator.cm_to_m(height)
            result = calculator.calc_bmi(weight, height)
            print(f"Your BMI is {result}")
            break


main()
