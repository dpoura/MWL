class DailyCalorieDeficitCalculator:

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