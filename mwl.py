from daily_calorie_needs import DailyCalorieNeedsCalculator

class MWL:

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
    
    def calculate_daily_calorie_deficit(self):
        """
        Calculate daily calorie deficit needed to achieve target weight loss.
        
        Parameters:
        none
        
        Returns:
        float: Daily calorie deficit
        """

        target_weight_loss_per_week = float(input("Enter your target weight loss per week in kilograms: "))

        calories_per_kg = 7700  # Approximate calories in 1 kg of body weight
        days_in_week = 7
        daily_calorie_deficit = (target_weight_loss_per_week * calories_per_kg) / days_in_week

        return daily_calorie_deficit
    
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
    
    def calculate_net_calories(self, calories_in, calories_out):
        """
        Calculate net calories (calories in - calories out).
        
        Parameters:
        calories_in (float): Total calorie intake
        calories_out (float): Total calorie expenditure
        
        Returns:
        float: Net calories
        """
        net = calories_in - calories_out

        return net
    
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
    
    def calculate_daily_weight_change(self, net_calories):
        """
        Calculate estimated daily weight change based on net calories.
        
        Parameters:
        net_calories (float): Net calories (calories in - calories out)
        
        Returns:
        float: Estimated daily weight change in kilograms
        """
        calories_per_kg = 7700  # Approximate calories in 1 kg of body weight
        daily_weight_change = net_calories / calories_per_kg
        return daily_weight_change