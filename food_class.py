class food:
    def __init__(self, foodName, numberOfCalories):
        self.foodName = foodName
        self.calories = numberOfCalories


    def __str__(self):
        return f'{self.foodName} - {self.calories} Calories'