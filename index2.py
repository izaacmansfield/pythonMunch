from tkinter import *
import tkinter as tk
import json
import tkinter.messagebox


class CalorieCounterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calorie Counter App")
        self.geometry("400x400")
        self.logged_in = False
        self.username = ""


        
        # Define the user database filename
        self.user_db_filename = "users.json"

        # Load the user database
        with open(self.user_db_filename, "r") as f:
            self.users = json.load(f)

        # Define the current user variable
        self.current_user = ""
        self.username = None
        self.calorie_goal = 2000
        self.logged_calories = 0
        self.createUsername= StringVar()
        self.createPassword= StringVar()
        self.createMail= StringVar()
        self.createHeight=IntVar()
        self.createWeight=IntVar()
        self.createSex=StringVar()
        self.createAge= IntVar()



        # Create login screen
        self.login_frame = tk.Frame(self)
        self.username_label = tk.Label(self.login_frame, text="Username:")
        self.username_entry = tk.Entry(self.login_frame)
        self.password_label = tk.Label(self.login_frame, text="Password:")
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.Createaccount_button = tk.Button(self.login_frame, text="Create Account", command=self.tocreateaccount)
        
        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.login_button.pack()
        self.Createaccount_button.pack()
        self.login_frame.pack()


        #Create create account screen
        self.createAccount_frame = tk.Frame(self)
        self.CreateUsername_label = tk.Label(self.createAccount_frame, text="Username:")
        self.CreateUsername_entry = tk.Entry(self.createAccount_frame, textvariable=self.createUsername)
        self.CreatePassword_label = tk.Label(self.createAccount_frame, text="Password:")
        self.CreatePassword_entry = tk.Entry(self.createAccount_frame, show="*", textvariable=self.createPassword)
        self.Createmail_label = tk.Label(self.createAccount_frame, text="Email: ")
        self.Createmail_entry = tk.Entry(self.createAccount_frame,textvariable=self.createMail)
        self.CreateSex_label = tk.Label(self.createAccount_frame, text="Sex: ")
        self.CreateSex_entry = tk.Entry(self.createAccount_frame, textvariable=self.createSex)
        self.CreateAge_label = tk.Label(self.createAccount_frame, text="Age: ")
        self.CreateAge_entry = tk.Entry(self.createAccount_frame, textvariable=self.createAge)
        self.Createheight_label = tk.Label(self.createAccount_frame, text="Height")
        self.Createheight_entry = tk.Entry(self.createAccount_frame, textvariable=self.createHeight)
        self.Createweight_label = tk.Label(self.createAccount_frame, text="Weight:")
        self.Createweight_entry = tk.Entry(self.createAccount_frame, textvariable=self.createWeight)
        self.CreateAccount_button = tk.Button(self.createAccount_frame, text="Create Account", command=self.CreateAccount)

        self.CreateUsername_label.pack()
        self.CreateUsername_entry.pack()
        self.CreatePassword_label.pack()
        self.CreatePassword_entry.pack()
        self.Createmail_label.pack()
        self.Createmail_entry.pack()
        self.CreateSex_label.pack()
        self.CreateSex_entry.pack()
        self.CreateAge_label.pack()
        self.CreateAge_entry.pack()
        self.Createheight_label.pack()
        self.Createheight_entry.pack()
        self.Createweight_label.pack()
        self.Createweight_entry.pack()
        self.CreateAccount_button.pack()




        
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
        with open("users.json") as f:
            users = json.load(f)
        # Get the entered username and password
        username = self.username_entry.get()
        password = self.password_entry.get()
    
        # Check if the username and password are correct
        if username in users and password == users[username]["Password"]:
            self.logged_in = True
            self.username = username
            self.login_frame.pack_forget() # hide the login screen
            self.calorie_counter_frame.pack() # show the calorie counter screen
            self.update_progress_bar() # initialize the progress bar
        else:
            # Display an error message if the username or password is incorrect
            error_label = tk.Label(self.login_frame, text="Incorrect username or password")
            error_label.pack()
    
    def logout(self):
        self.logged_in = False
        self.username = ""
        self.calorie_counter_frame.pack_forget() # hide the calorie counter screen
        self.login_frame.pack() # show the login screen
        
    def log_calories(self):
        pass

    
    def update_progress_bar(self):
        # Calculate the percentage of the user's calorie goal that has been reached
        progress = int(self.logged_calories / self.calorie_goal * 100)

        # Update the progress bar value and label
        self.progress_bar["value"] = progress
        self.calories_label["text"] = f"{self.logged_calories}/{self.calorie_goal} calories"

        # Update the progress bar style based on the percentage of the goal reached
        if progress <= 50:
            self.progress_bar["style"] = "green.Horizontal.TProgressbar"
        elif progress > 50 and progress <= 100:
            self.progress_bar["style"] = "yellow.Horizontal.TProgressbar"
        else:
            self.progress_bar["style"] = "red.Horizontal.TProgressbar"

    def tocreateaccount(self):
        #shows the create account page
        self.login_frame.pack_forget()
        self.createAccount_frame.pack()

    def CreateAccount(self):
        #saves users credentials and information in the json file
        if self.createUsername.get() == "" or self.createPassword.get == "" or self.createMail.get()=="" or self.createHeight.get()=="" or self.createWeight.get()=="" or self.createSex=="" or self.createAge=="":
            tkinter.messagebox.showinfo("Some fields in the form are empty please complete and try again")
        else:

            self.users[self.createUsername.get()] = {}
            self.users[self.createUsername.get()]['Password'] = self.createPassword.get()
            self.users[self.createUsername.get()]['Email'] = self.createMail.get()
            self.users[self.createUsername.get()]['Height'] = self.createHeight.get()
            self.users[self.createUsername.get()]['Weight'] = self.createWeight.get()

            with open('users.json', 'w') as file:
                json.dump(self.users, file)

            self.createAccount_frame.pack_forget()
            self.login_frame.pack()







    
if __name__ == "__main__":
    app = CalorieCounterApp()
    app.mainloop()


# This is just a basic framework for the app, and you'll need to fill in the details for each of the methods. For example, the login method would need to validate the user's login credentials and set the self.logged_in flag accordingly. The log_calories method would need to read and write to a JSON file to store the logs, and then call the update_progress_bar method to update the progress bar. 