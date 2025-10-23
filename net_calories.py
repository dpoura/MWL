class NetCalories:

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