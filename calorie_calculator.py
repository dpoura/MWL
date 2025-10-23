class CalorieCalculator:

    def calculate_calories(self):

        """
        Calculate calories based on user input.

        parameters:
        none

        returns:
        float: Total calories for the given food item
        """
        
        calories_per_100g = int(input("Enter calories per 100g: "))
        weight_in_grams = int(input("Enter weight in grams: "))
        calories = calories_per_100g * (weight_in_grams / 100)

        return calories
