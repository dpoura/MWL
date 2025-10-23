class CaloriesAllowed:

    def calculate_calories_allowed(self, calories_in, calories_out, daily_calorie_deficit):
        """
        Calculate remaining calories allowed for the day.
        
        Parameters:
        calories_in (float): Total calorie intake
        calories_out (float): Total calorie expenditure
        daily_calorie_deficit (float): Daily calorie deficit goal
        
        Returns:
        float: Remaining calories allowed
        """
        remaining = calories_out + daily_calorie_deficit - calories_in
        calories_allowed = max(0, remaining)

        return calories_allowed