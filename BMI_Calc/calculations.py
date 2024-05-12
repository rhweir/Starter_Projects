class Calculator:
    """A class to perform the calculation functions of the BMI tool"""

    # calculate the users BMI
    def calc_bmi(self, x, y):
        return round(x / (y * y), None)

    def stn_to_lbs(self, x, y):
        return (x * 14) + y

    # convert user weight in lbs to kg
    def lbs_to_kg(self, x):
        return round(x * 0.453592, 2)

    # convert user height in inches to m
    def inch_to_m(self, x):
        return round((x * 2.54) / 100, 2)

    def cm_to_m(self, x):
        return x / 100
