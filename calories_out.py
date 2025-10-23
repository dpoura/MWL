class CaloriesOut:

    def calculate_calories_out(self, daily_calorie_needs):
        """
        Calculate total calorie expenditure.
        
        Parameters:
        daily_calorie_needs (float): Basal Metabolic Rate * 1.2
        exercise_calories (float): Calories burned through exercise
        
        Returns:
        float: Total calorie expenditure
        """
        exercise_calories_1 = 0
        exercise_calories_2 = 0
        exercise_calories_3 = 0
        exercise_calories_1 = float(input("Enter calories burned through exercise: "))
        exercise_calories_2 = float(input("Enter calories burned through exercise: "))
        exercise_calories_3 = float(input("Enter calories burned through exercise: "))

        calories_out = daily_calorie_needs + exercise_calories_1 + exercise_calories_2 + exercise_calories_3

        return calories_out