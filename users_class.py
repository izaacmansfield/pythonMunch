class users:
    def __init__(self, username, password, height, weight, sex, age, calorie_goal=0, totalcalories=0):
        self.username= username
        self.password = password
        self.height = height
        self.weight = weight
        self.sex=sex
        self.age=age
        self.calorie_goal = calorie_goal
        self.totalcalories = totalcalories



    def Calculate_bmr(self):
        if self.sex=="Male":
            self.bmr= 88.362 + (13.397*self.weight) +(4.799*self.height)
        else:
            pass
        
        self.calorie_goal = self.bmr
        
