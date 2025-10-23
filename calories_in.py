class CaloriesIn:

    def calculate_calories_in(self):
        """
        Calculate total calorie intake from meals.
        
        Parameters:
        breakfast (float): Calories consumed at breakfast
        lunch (float): Calories consumed at lunch
        dinner (float): Calories consumed at dinner
        other (float): Calories consumed from other sources/snacks
        
        Returns:
        float: Total calorie intake
        """

        breakfast = float(input("Enter calories consumed at breakfast: "))
        lunch = float(input("Enter calories consumed at lunch: "))
        dinner = float(input("Enter calories consumed at dinner: "))
        other = float(input("Enter calories consumed from other sources/snacks: "))

        calories_in = breakfast + lunch + dinner + other

        return calories_in