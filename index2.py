import tkinter as tk
import json

class CalorieCounterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calorie Counter App")
        self.geometry("400x400")
        self.logged_in = False
        self.username = ""
        
        # Create login screen
        self.login_frame = tk.Frame(self)
        self.username_label = tk.Label(self.login_frame, text="Username:")
        self.username_entry = tk.Entry(self.login_frame)
        self.password_label = tk.Label(self.login_frame, text="Password:")
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        
        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.login_button.pack()
        self.login_frame.pack()
        
        # Create calorie counter screen
        self.calorie_counter_frame = tk.Frame(self)
        self.food_label = tk.Label(self.calorie_counter_frame, text="Food:")
        self.food_entry = tk.Entry(self.calorie_counter_frame)
        self.calories_label = tk.Label(self.calorie_counter_frame, text="Calories:")
        self.calories_entry = tk.Entry(self.calorie_counter_frame)
        self.log_button = tk.Button(self.calorie_counter_frame, text="Log", command=self.log_calories)
        self.progress_bar = tk.Canvas(self.calorie_counter_frame, width=300, height=20)
        self.logout_button = tk.Button(self.calorie_counter_frame, text="Logout", command=self.logout)
        
        self.food_label.pack()
        self.food_entry.pack()
        self.calories_label.pack()
        self.calories_entry.pack()
        self.log_button.pack()
        self.progress_bar.pack()
        self.logout_button.pack()
        
    def login(self):
        # Check if the username and password are correct
        # Set self.logged_in to True if successful
        # Store the username in self.username
        # If login is successful, switch to the calorie counter screen
        pass
    
    def logout(self):
        # Set self.logged_in to False
        # Clear the username
        # Switch to the login screen
        pass
        
    def log_calories(self):
        # Get the food and calorie inputs from the user
        # Store them in a dictionary
        # Add the dictionary to a list of logs
        # Write the list of logs to a JSON file
        # Update the progress bar based on the total calories logged so far
        pass
    
    def update_progress_bar(self):
        # Get the total calories logged so far from the JSON file
        # Calculate the percentage of the daily goal reached
        # Update the progress bar with the percentage
        pass
    
if __name__ == "__main__":
    app = CalorieCounterApp()
    app.mainloop()


# This is just a basic framework for the app, and you'll need to fill in the details for each of the methods. For example, the login method would need to validate the user's login credentials and set the self.logged_in flag accordingly. The log_calories method would need to read and write to a JSON file to store the logs, and then call the update_progress_bar method to update the progress bar. 