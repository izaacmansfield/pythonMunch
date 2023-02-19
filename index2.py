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

        #Create change preferences screen
        self.changeprefs_frame = tk.Frame(self)
        self.Updatemail_label = tk.Label(self.changeprefs_frame, text="Email: ")
        self.Updatemail_entry = tk.Entry(self.changeprefs_frame,textvariable=self.createMail)
        self.UpdateSex_label = tk.Label(self.changeprefs_frame, text="Sex: ")
        self.UpdateSex_entry = tk.Entry(self.changeprefs_frame, textvariable=self.createSex)
        self.UpdateAge_label = tk.Label(self.changeprefs_frame, text="Age: ")
        self.UpdateAge_entry = tk.Entry(self.changeprefs_frame, textvariable=self.createAge)
        self.Updateheight_label = tk.Label(self.changeprefs_frame, text="Height")
        self.Updateheight_entry = tk.Entry(self.changeprefs_frame, textvariable=self.createHeight)
        self.Updateweight_label = tk.Label(self.changeprefs_frame, text="Weight:")
        self.Updateweight_entry = tk.Entry(self.changeprefs_frame, textvariable=self.createWeight)
        self.Updatecaloriegoal_label = tk.Label(self.changeprefs_frame, text="New Calorie Goal:")
        self.Updatecaloriegoal_entry = tk.Entry(self.changeprefs_frame, textvariable=self.calorie_goal)
        self.Savechanges_button = tk.Button(self.changeprefs_frame, text="Save Changes", command=self.SaveChanges)  

        self.Updatemail_label.pack()
        self.Updatemail_entry.pack()
        self.UpdateSex_label.pack()
        self.UpdateSex_entry.pack()
        self.UpdateAge_label.pack()
        self.UpdateAge_entry.pack()
        self.Updateheight_label.pack()
        self.Updateheight_entry.pack()
        self.Updateweight_label.pack()
        self.Updateweight_entry.pack()
        self.Updatecaloriegoal_label.pack()
        self.Updatecaloriegoal_entry.pack()
        self.Savechanges_button.pack()            

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
        self.change_preferences_button = Button(self.calorie_counter_frame, text="Change Preferences", command=self.tochangeprefs)
        self.logout_button = tk.Button(self.calorie_counter_frame, text="Logout", command=self.logout)
        
        self.food_label.pack()
        self.food_entry.pack()
        self.calories_label.pack()
        self.calories_entry.pack()
        self.log_button.pack()
        self.progress_bar.pack()
        self.logout_button.pack()
        self.change_preferences_button.pack()
        
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
            self.current_user = username
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
        # Get the current calorie count for the current user
        current_calories = self.users[self.current_user]["total_calories"]

        # Add the new calories to the current count
        new_calories = int(self.calories_entry.get())
        total_calories = current_calories + new_calories

        # Update the user's calorie count in the user database
        self.users[self.current_user]["total_calories"] = total_calories

        self.calories_entry.delete(0, tk.END)

        # Save the updated user database to the file
        with open(self.user_db_filename, "w") as f:
            json.dump(self.users, f)

        # Update the progress bar and calories label
        self.update_progress_bar()
        

    
    def update_progress_bar(self):
        # Calculate the percentage of the user's calorie goal that has been reached
        self.calorie_goal = self.users[self.current_user]["calorie_goal"]
        self.total_calories = self.users[self.current_user]["total_calories"]
        progress = int(self.total_calories / self.calorie_goal * 100)

        # Update the progress bar value and label
        self.progress_bar["value"] = progress
        self.calories_label["text"] = f"{self.total_calories}/{self.calorie_goal} calories"

        # Update the progress bar style based on the percentage of the goal reached
        if progress <= 50:
            self.progress_bar["style"] = "green.Horizontal.TProgressbar"
        elif progress > 50 and progress <= 100:
            self.progress_bar["style"] = "yellow.Horizontal.TProgressbar"
        else:
            self.progress_bar["style"] = "red.Horizontal.TProgressbar"


    def tochangeprefs(self):
        self.calorie_counter_frame.pack_forget()
        self.changeprefs_frame.pack()
        self.ChangePrefs()
    
    def ChangePrefs(self):
        with open("users.json") as f:
            users = json.load(f)

        self.Updatemail_entry.delete(0, tk.END)
        self.UpdateSex_entry.delete(0,tk.END)
        self.UpdateAge_entry.delete(0,tk.END)
        self.Updateheight_entry.delete(0, tk.END)
        self.Updateweight_entry.delete(0, tk.END)
        self.Updatecaloriegoal_entry.delete(0, tk.END)

        self.Updatemail_entry.insert(0, self.users[self.current_user]["Email"])
        self.UpdateSex_entry.insert(0, self.users[self.current_user]["Sex"])
        self.UpdateAge_entry.insert(0, self.users[self.current_user]["Age"])
        self.Updateheight_entry.insert(0, self.users[self.current_user]["Height"])
        self.Updateweight_entry.insert(0, self.users[self.current_user]["Weight"])
        self.Updatecaloriegoal_entry.insert(0, self.users[self.current_user]["calorie_goal"])

    def SaveChanges(self):
        self.users[self.current_user]["Email"] = self.Updatemail_entry.get()
        self.users[self.current_user]["Sex"] = self.UpdateSex_entry.get()
        self.users[self.current_user]["Age"] = self.UpdateAge_entry.get()
        self.users[self.current_user]["Height"] = self.Updateheight_entry.get()
        self.users[self.current_user]["Weight"] = self.Updateweight_entry.get()
        self.users[self.current_user]["calorie_goal"] = self.Updatecaloriegoal_entry.get()

        with open('users.json', 'w') as file:
                json.dump(self.users, file)
        
        self.changeprefs_frame.pack_forget()
        self.calorie_counter_frame.pack()

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
            self.users[self.createUsername.get()]['Sex'] = self.createSex.get()
            self.users[self.createUsername.get()]['Age'] = self.createAge.get()
            self.users[self.createUsername.get()]["total_calories"] = 0

            if self.createSex == "male" or self.createSex == "Male":
               self.users[self.createUsername.get()]['calorie_goal'] = 88.362 + (13.397*self.createWeight.get()) + (4.799*self.createHeight.get()) - (5.677*self.createAge.get())
            else:
                self.users[self.createUsername.get()]['calorie_goal'] = 447.593 + (9.247*self.createWeight.get()) + (3.098*self.createHeight.get()) - (4.330*self.createAge.get())


            with open('users.json', 'w') as file:
                json.dump(self.users, file)

            self.createAccount_frame.pack_forget()
            self.login_frame.pack()


if __name__ == "__main__":
    app = CalorieCounterApp()
    app.mainloop()
