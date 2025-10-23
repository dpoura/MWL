class DailyWeightChange:

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