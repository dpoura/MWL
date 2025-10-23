class DailyCalorieNeedsCalculator:

    def calculate_daily_calorie_needs(self):
        """
        Calculate daily calorie needs using the Mifflin-St Jeor Equation.
        Mifflin-St Jeor Equation for Basal Metabolic Rate (BMR) = (10 * weight) + (6.25 * height) - (5 * age) + s where s is +5 for men and -161 for women
        Multiplying BMR by an activity factor of 1.2 for little or no exercise. E.g. basic walking, light housework, etc.
        
        Parameters:
        none

        Returns:
        float: Estimated daily calorie needs
        """

        sex = input("Enter your sex (male/female): ")
        age = int(input("Enter your age in years: "))
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in centimeters: "))

        if sex.lower() == 'male':
            s = 5
        else:
            s = -161
        
        daily_calorie_needs = 1.2 * ((10 * weight) + (6.25 * height) - (5 * age) + s)

        return daily_calorie_needs