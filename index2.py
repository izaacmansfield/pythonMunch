from tkinter import *
import tkinter as tk
import json
import tkinter.messagebox


class CalorieCounterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Munch!")
        self.geometry("360x420")
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



        # Create login screen
        self.login_frame = tk.Frame(self, bg="beige")
        self.welcome_label = tk.Label(self.login_frame, text="Munch!", fg="darkgreen", height=2, font=("Open Sans", 18), bg="beige")
        self.welcome_label2 = tk.Label(self.login_frame, text="Track Your Daily Calories", height=2, bg="beige")

        self.username_label = tk.Label(self.login_frame, text="Username:", bg="beige")
        self.username_entry = tk.Entry(self.login_frame)
        self.password_label = tk.Label(self.login_frame, text="Password:", bg="beige")
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login, fg="darkgreen", height=2, width=5, bg="white", activebackground="beige")
        self.Createaccount_button = tk.Button(self.login_frame, text="Create Account", command=self.tocreateaccount, fg="darkgreen", height=2, bg="white", activebackground="beige")
        
        self.welcome_label.grid(row=0, column=2)
        self.welcome_label2.grid(row=2, column=2)
        self.username_label.grid(row=4, column=2)
        self.username_entry.grid(row=5, column=2)
        self.password_label.grid(row=6, column=2)
        self.password_entry.grid(row=7, column=2)
        self.login_button.grid(row=8, column=2, sticky=W)
        self.Createaccount_button.grid(row=8, column=2, sticky=E)
        self.login_frame.grid(padx=100, pady=100)


        #Create create account screen
        self.createAccount_frame = tk.Frame(self, background="beige")
        self.CreateUsername_label = tk.Label(self.createAccount_frame, text="Username:", background="beige")
        self.CreateUsername_entry = tk.Entry(self.createAccount_frame, textvariable=self.createUsername, justify=CENTER)
        self.CreatePassword_label = tk.Label(self.createAccount_frame, text="Password:", background="beige")
        self.CreatePassword_entry = tk.Entry(self.createAccount_frame, show="*", textvariable=self.createPassword, justify=CENTER)
        self.Createmail_label = tk.Label(self.createAccount_frame, text="Email: ", background="beige")
        self.Createmail_entry = tk.Entry(self.createAccount_frame,textvariable=self.createMail, justify=CENTER)
        self.Createheight_label = tk.Label(self.createAccount_frame, text="Height (In Cm)", background="beige")
        self.Createheight_entry = tk.Entry(self.createAccount_frame, textvariable=self.createHeight, justify=CENTER)
        self.Createweight_label = tk.Label(self.createAccount_frame, text="Weight (In Kg):", background="beige")
        self.Createweight_entry = tk.Entry(self.createAccount_frame, textvariable=self.createWeight, justify=CENTER)
        self.CreateAccount_button = tk.Button(self.createAccount_frame, text="Create Account", command=self.CreateAccount, background="white", activebackground="beige", fg="darkgreen")

        self.CreateUsername_label.grid(column=1)
        self.CreateUsername_entry.grid(column=1)
        self.CreatePassword_label.grid(column=1)
        self.CreatePassword_entry.grid(column=1)
        self.Createmail_label.grid(column=1)
        self.Createmail_entry.grid(column=1)
        self.Createheight_label.grid(column=1)
        self.Createheight_entry.grid(column=1)
        self.Createweight_label.grid(column=1)
        self.Createweight_entry.grid(column=1)
        self.CreateAccount_button.grid(column=1)
        self.createAccount_frame.grid(padx=100, pady=100)




        
        # Create calorie counter screen
        self.calorie_counter_frame = tk.Frame(self)
        self.food_label = tk.Label(self.calorie_counter_frame, text="Food:")
        self.food_entry = tk.Entry(self.calorie_counter_frame)
        self.calories_label = tk.Label(self.calorie_counter_frame, text="Calories:")
        self.calories_entry = tk.Entry(self.calorie_counter_frame)
        self.log_button = tk.Button(self.calorie_counter_frame, text="Log", command=self.log_calories)
        self.progress_bar = tk.Canvas(self.calorie_counter_frame, width=300, height=20)
        self.logout_button = tk.Button(self.calorie_counter_frame, text="Logout", command=self.logout)
        
        self.food_label.grid()
        self.food_entry.grid()
        self.calories_label.grid()
        self.calories_entry.grid()
        self.log_button.grid()
        self.progress_bar.grid()
        self.logout_button.grid()
        
    def login(self):
        with open("users.json") as f:
            users = json.load(f)
        # Get the entered username and password
        username = self.username_entry.get()
        password = self.password_entry.get()
    
        # Check if the username and password are correct
        if username in users and password == users[username]:
            self.logged_in = True
            self.username = username
            self.login_frame.grid_forget() # hide the login screen
            self.calorie_counter_frame.grid() # show the calorie counter screen
            self.update_progress_bar() # initialize the progress bar
        else:
            # Display an error message if the username or password is incorrect
            error_label = tk.Label(self.login_frame, text="Incorrect username or password", font=("Open Sans", 8), bg="beige")
            error_label.grid(row=10, column=1)
    
    def logout(self):
        self.logged_in = False
        self.username = ""
        self.calorie_counter_frame.grid_forget() # hide the calorie counter screen
        self.login_frame.grid() # show the login screen
        
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
        self.login_frame.grid_forget()
        self.createAccount_frame.grid()

    def CreateAccount(self):
        #saves users credentials and information in the json file
        if self.createUsername.get() == "" or self.createPassword.get == "" or self.createMail.get()=="" or self.createHeight.get()=="" or self.createWeight.get()=="":
            tkinter.messagebox.showinfo("Some fields in the form are empty please complete and try again")
        else:
            self.users[self.createUsername] = {}
            self.users[self.createUsername]['Password'] = self.createPassword
            self.users[self.createUsername]['Email'] = self.createMail
            self.users[self.createUsername]['Height'] = self.createHeight
            self.users[self.createUsername]['Weight'] = self.createWeight

            with open('users.json', 'w') as file:
                json.dump(self.users, file)






    
if __name__ == "__main__":
    app = CalorieCounterApp()
    app.mainloop()


# This is just a basic framework for the app, and you'll need to fill in the details for each of the methods. For example, the login method would need to validate the user's login credentials and set the self.logged_in flag accordingly. The log_calories method would need to read and write to a JSON file to store the logs, and then call the update_progress_bar method to update the progress bar. 