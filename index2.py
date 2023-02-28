from tkinter import *
import tkinter as tk
from tkinter import ttk
import json
import tkinter.messagebox
import collections
from PIL import ImageTk, Image




class CalorieCounterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Munch!")
        self.geometry("350x500")
        self.config(bg="beige")
        self.logged_in = False
        self.username = ""

        self.iconbitmap('foodicon.ico')
        
        # Define the user database filename
        self.user_db_filename = "users.json"

        # Load the user database
        with open(self.user_db_filename, "r") as f:
            self.users = json.load(f)

        with open('recentFoods.json', 'r') as p:
           self.food = json.load(p)

        #with open(self.food_db_filename, "r") as p:
            #self.food = json.load(p)


        # Define the current user variable
        self.current_user = ""
        self.username = None
        self.calorie_goal = 2000
        self.logged_calories = 0
        #self.food= {}
        self.createUsername= StringVar()
        self.createPassword= StringVar()
        self.createMail= StringVar()
        self.createHeight=IntVar()
        self.createWeight=IntVar()
        self.createSex=StringVar()
        self.createAge = IntVar()
        self.foodName = StringVar()
        self.food_calorie = IntVar()
        self.foods= list()
        self.foodList = list()




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
        
        # logo = Image.open('munchlogo2.png')
        # new_width = 200
        # new_height = 150
        # img = logo.resize((new_width, new_height))
        # logo = ImageTk.PhotoImage(img)
        # logo_label = Label(self.login_frame, image=logo)
        # logo_label.grid(padx=5, pady=5)

        self.welcome_label.grid(row=0, column=2)
        self.welcome_label2.grid(row=2, column=2)
        self.username_label.grid(row=4, column=2)
        self.username_entry.grid(row=5, column=2)
        self.password_label.grid(row=6, column=2)
        self.password_entry.grid(row=7, column=2)
        self.login_button.grid(row=8, column=2, pady=10)
        self.Createaccount_button.grid(row=10, column=2, pady=5)
        self.login_frame.grid(padx=100, pady=20)

        #Create change preferences screen
        self.changeprefs_frame = tk.Frame(self, background="beige")
        self.Updatemail_label = tk.Label(self.changeprefs_frame, text="Email: ", background="beige")
        self.Updatemail_entry = tk.Entry(self.changeprefs_frame,textvariable=self.createMail, justify=CENTER)
        self.UpdateSex_label = tk.Label(self.changeprefs_frame, text="Sex: ", background="beige")
        self.UpdateSex_entry = tk.Entry(self.changeprefs_frame, textvariable=self.createSex, justify=CENTER)
        self.UpdateAge_label = tk.Label(self.changeprefs_frame, text="Age: ", background="beige")
        self.UpdateAge_entry = tk.Entry(self.changeprefs_frame, textvariable=self.createAge, justify=CENTER)
        self.Updateheight_label = tk.Label(self.changeprefs_frame, text="Height", background="beige")
        self.Updateheight_entry = tk.Entry(self.changeprefs_frame, textvariable=self.createHeight, justify=CENTER)
        self.Updateweight_label = tk.Label(self.changeprefs_frame, text="Weight:", background="beige")
        self.Updateweight_entry = tk.Entry(self.changeprefs_frame, textvariable=self.createWeight, justify=CENTER)
        self.Updatecaloriegoal_label = tk.Label(self.changeprefs_frame, text="New Calorie Goal:", background="beige")
        self.Updatecaloriegoal_entry = tk.Entry(self.changeprefs_frame, textvariable=self.calorie_goal, justify=CENTER)
        self.Savechanges_button = tk.Button(self.changeprefs_frame, text="Save Changes", command=self.SaveChanges, background="white", activebackground="beige", fg="darkgreen")  

        self.Updatemail_label.grid(row=0, column=1, padx=100)
        self.Updatemail_entry.grid(row=1, column=1, padx=100)
        self.UpdateSex_label.grid(row=2, column=1, padx=100)
        self.UpdateSex_entry.grid(row=3, column=1, padx=100)
        self.UpdateAge_label.grid(row=4, column=1, padx=100)
        self.UpdateAge_entry.grid(row=5, column=1, padx=100)
        self.Updateheight_label.grid(row=6, column=1, padx=100)
        self.Updateheight_entry.grid(row=7, column=1, padx=100)
        self.Updateweight_label.grid(row=8, column=1, padx=100)
        self.Updateweight_entry.grid(row=9, column=1, padx=100)
        self.Updatecaloriegoal_label.grid(row=10, column=1, padx=100)
        self.Updatecaloriegoal_entry.grid(row=11, column=1, padx=100)
        self.Savechanges_button.grid(row=12, column=1, padx=100, pady=5)   
        # self.changeprefs_frame.grid(padx=100, pady=100)         

        #Create create account screen
        self.createAccount_frame = tk.Frame(self, background="beige")
        self.CreateUsername_label = tk.Label(self.createAccount_frame, text="Username:", background="beige")
        self.CreateUsername_entry = tk.Entry(self.createAccount_frame, textvariable=self.createUsername, justify=CENTER)
        self.CreatePassword_label = tk.Label(self.createAccount_frame, text="Password:", background="beige")
        self.CreatePassword_entry = tk.Entry(self.createAccount_frame, show="*", textvariable=self.createPassword, justify=CENTER)
        self.Createmail_label = tk.Label(self.createAccount_frame, text="Email: ", background="beige")
        self.Createmail_entry = tk.Entry(self.createAccount_frame,textvariable=self.createMail, justify=CENTER)
        self.CreateSex_label = tk.Label(self.createAccount_frame, text="Sex: ", background="beige")
        self.CreateSex_entry = tk.Entry(self.createAccount_frame, textvariable=self.createSex, justify=CENTER)
        self.CreateAge_label = tk.Label(self.createAccount_frame, text="Age: ", background="beige")
        self.CreateAge_entry = tk.Entry(self.createAccount_frame, textvariable=self.createAge, justify=CENTER)
        self.Createheight_label = tk.Label(self.createAccount_frame, text="Height in Cm:", background="beige")
        self.Createheight_entry = tk.Entry(self.createAccount_frame, textvariable=self.createHeight, justify=CENTER)
        self.Createweight_label = tk.Label(self.createAccount_frame, text="Weight in Kg:", background="beige")
        self.Createweight_entry = tk.Entry(self.createAccount_frame, textvariable=self.createWeight, justify=CENTER)
        self.CreateAccount_button = tk.Button(self.createAccount_frame, text="Create Account", command=self.CreateAccount, background="white", activebackground="beige", fg="darkgreen")
        self.GoBack_button = tk.Button(self.createAccount_frame, text="Go Back", command=self.tologinpage, background="white", activebackground="beige", fg="darkgreen")


        self.CreateUsername_label.grid(row=0, column=0, padx=100, pady=5)
        self.CreateUsername_entry.grid(row=1, column=0, padx=100, pady=5)
        self.CreatePassword_label.grid(row=2, column=0, padx=100, pady=5)
        self.CreatePassword_entry.grid(row=3, column=0, padx=100, pady=5)
        self.Createmail_label.grid(row=4, column=0, padx=100, pady=5)
        self.Createmail_entry.grid(row=5, column=0, padx=100, pady=5)
        self.CreateSex_label.grid(row=6, column=0, padx=100, pady=5)
        self.CreateSex_entry.grid(row=7, column=0, padx=100, pady=5)
        self.CreateAge_label.grid(row=8, column=0, padx=100, pady=5)
        self.CreateAge_entry.grid(row=9, column=0, padx=100, pady=5)
        self.Createheight_label.grid(row=10, column=0, padx=100, pady=5)
        self.Createheight_entry.grid(row=11, column=0, padx=100, pady=5)
        self.Createweight_label.grid(row=12, column=0, padx=100, pady=5)
        self.Createweight_entry.grid(row=13, column=0,padx=100, pady=5)
        self.CreateAccount_button.grid(row=14, column=0, padx=100, pady=5)
        self.GoBack_button.grid(row=15, column=0, padx=100, pady=5)
        
        # Create calorie counter screen
        self.calorie_counter_frame = tk.Frame(self, bg="beige")
        # self.food_label = tk.Label(self.calorie_counter_frame, text="Food:")
        # self.food_entry = tk.Entry(self.calorie_counter_frame)
        self.calories_label = tk.Label(self.calorie_counter_frame, text="Enter Calories:", bg="beige")
        self.foodName_label = tk.Label(self.calorie_counter_frame, text = "Enter Food Name", bg="beige")
        self.calories_progress_label = tk.Label(self.calorie_counter_frame, text="Make an entry!", bg="beige")
        self.calories_entry = tk.Entry(self.calorie_counter_frame, textvariable=self.food_calorie)
        self.foodEntry = tk.Entry(self.calorie_counter_frame, textvariable=self.foodName)
        self.log_button = tk.Button(self.calorie_counter_frame, text="Log", command=self.log_calories, fg="darkgreen", background="white", activebackground="beige")
        self.recent_foods_label = tk.Label(self.calorie_counter_frame, text="Recently Used Foods:", bg="beige")
        self.food_list = Listbox(self.calorie_counter_frame, width = 30, height = 6)
        self.food_list.bind('<Double-Button-1>', addCaloriesfromList)
        self.progress_bar = ttk.Progressbar(self.calorie_counter_frame, orient="horizontal", length=200, mode="determinate")
        self.change_preferences_button = Button(self.calorie_counter_frame, text="Change Preferences", command=self.tochangeprefs, fg="darkgreen", background="white", activebackground="beige")
        self.logout_button = tk.Button(self.calorie_counter_frame, text="Logout", command=self.logout, fg="darkgreen", background="white", activebackground="beige")
        self.clear_calories_button = tk.Button(self.calorie_counter_frame, text="Clear Calories", command=self.clear_calories, fg="darkgreen", background="white", activebackground="beige")
        # self.food_label.grid()
        # self.food_entry.grid()
        self.calories_progress_label.grid(row=0, column=0, padx=75, pady=5)
        self.progress_bar.grid(row=1, column=0, padx=75, pady=5)
        self.calories_label.grid(row=4, column=0, padx=75)
        self.foodName_label.grid(row=2, column=0, padx=75)
        self.calories_entry.grid(row=5, column=0, padx=75, pady=5)
        self.foodEntry.grid(row=3, column=0, padx=75, pady=5)
        self.log_button.grid(row=6, column=0, padx=75, pady=5)
        self.recent_foods_label.grid(row=7, column=0, padx=75, pady=5)
        self.food_list.grid(row=8, column=0, padx=75, pady=5)
        self.change_preferences_button.grid(row=9, column=0, padx=75, pady=5)
        self.clear_calories_button.grid(row=10, column=0, padx=75, pady=5)
        self.logout_button.grid(row=11, column=0, padx=75, pady=5)


        # self.food_listbox = tk.Listbox(self.calorie_counter_frame, height=10)
        # self.food_listbox.grid()

        # self.food_scrollbar = tk.Scrollbar(self.calorie_counter_frame)
        # self.food_scrollbar.grid(side=tk.RIGHT, fill=tk.Y)

        # self.food_listbox.config(yscrollcommand=self.food_scrollbar.set)
        # self.food_scrollbar.config(command=self.food_listbox.yview)
        
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
            self.login_frame.grid_forget() # hide the login screen
            self.calorie_counter_frame.grid() # show the calorie counter screen
            self.update_progress_bar() # initialize the progress bar
            self.foods = self.food[self.current_user]




        else:
            # Display an error message if the username or password is incorrect
            error_label = tkinter.messagebox.showerror(title="Error", message="Incorrect username or password.")
    
    def logout(self):
        self.logged_in = False
        self.username = ""
        self.calorie_counter_frame.grid_forget() # hide the calorie counter screen
        self.login_frame.grid(padx=100, pady=100) # show the login screen
        self.foods=list()
        
    def log_calories(self):
        # Get the current calorie count for the current user
        current_calories = self.users[self.current_user]["total_calories"]

        # Add the new calories to the current count
        new_calories = int(self.food_calorie.get())
        total_calories = current_calories + new_calories

        # Update the user's calorie count in the user database
        self.users[self.current_user]["total_calories"] = total_calories



        # Save the updated user database to the file
        with open(self.user_db_filename, "w") as f:
            json.dump(self.users, f)

        # Update the progress bar and calories label
        self.update_progress_bar()
        self.addFoodtoList()
        
    def clear_calories(self):
        self.users[self.current_user]["total_calories"] = 0
        self.update_progress_bar()
    
    def update_progress_bar(self):
        # Calculate the percentage of the user's calorie goal that has been reached
        self.calorie_goal = int(self.users[self.current_user]["calorie_goal"])
        self.total_calories = int(self.users[self.current_user]["total_calories"])
        progress = int(self.total_calories / self.calorie_goal * 100)

        # Update the progress bar value and label
        self.progress_bar["value"] = progress
        self.calories_progress_label["text"] = f"{self.total_calories}/{self.calorie_goal} calories"

        # Update the progress bar style based on the percentage of the goal reached
        if progress <= 50:
            self.progress_bar["style"] = "green.Horizontal.TProgressbar"
        elif progress > 50 and progress <= 100:
            self.progress_bar["style"] = "yellow.Horizontal.TProgressbar"
        else:
            self.progress_bar["style"] = "red.Horizontal.TProgressbar"


    def tochangeprefs(self):
        self.calorie_counter_frame.grid_forget()
        self.changeprefs_frame.grid(padx=10, pady=100)
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
        self.Updateheight_entry.insert(0, self.users[self.current_user]["Height in Cm"])
        self.Updateweight_entry.insert(0, self.users[self.current_user]["Weight in Kg"])
        self.Updatecaloriegoal_entry.insert(0, self.users[self.current_user]["calorie_goal"])

    def SaveChanges(self):
        self.users[self.current_user]["Email"] = self.Updatemail_entry.get()
        self.users[self.current_user]["Sex"] = self.UpdateSex_entry.get()
        self.users[self.current_user]["Age"] = self.UpdateAge_entry.get()
        self.users[self.current_user]["Height in Cm"] = self.Updateheight_entry.get()
        self.users[self.current_user]["Weight in Kg"] = self.Updateweight_entry.get()
        self.users[self.current_user]["calorie_goal"] = self.Updatecaloriegoal_entry.get()

        with open('users.json', 'w') as file:
                json.dump(self.users, file)
        
        self.changeprefs_frame.grid_forget()
        self.calorie_counter_frame.grid()

    def tocreateaccount(self):
        #shows the create account page
        self.login_frame.grid_forget()
        self.createAccount_frame.grid()

    def tologinpage(self):
        self.createAccount_frame.grid_forget()
        self.login_frame.grid(padx=100, pady=100)

    def CreateAccount(self):
        #saves users credentials and information in the json file
        if self.createUsername.get() == "" or self.createPassword.get() == "" or self.createMail.get()=="" or self.createHeight.get()=="" or self.createWeight.get()=="" or self.createSex.get()=="" or self.createAge.get()=="":
            tkinter.messagebox.showerror(title="Empty Fields", message="Some fields in the form are empty, please complete and try again.")
        else:

            self.users[self.createUsername.get()] = {}
            self.users[self.createUsername.get()]['Password'] = self.createPassword.get()
            self.users[self.createUsername.get()]['Email'] = self.createMail.get()
            self.users[self.createUsername.get()]['Height'] = self.createHeight.get()
            self.users[self.createUsername.get()]['Weight'] = self.createWeight.get()
            self.users[self.createUsername.get()]['Sex'] = self.createSex.get()
            self.users[self.createUsername.get()]['Age'] = self.createAge.get()
            self.users[self.createUsername.get()]["total_calories"] = 0
            self.food[self.createUsername.get()] = []


            if self.createSex == "male" or self.createSex == "Male":
               self.users[self.createUsername.get()]['calorie_goal'] = int(round(88.362 + (13.397*self.createWeight.get()) + (4.799*self.createHeight.get()) - (5.677*self.createAge.get())))
            else:
                self.users[self.createUsername.get()]['calorie_goal'] = int(round(447.593 + (9.247*self.createWeight.get()) + (3.098*self.createHeight.get()) - (4.330*self.createAge.get())))


            with open('users.json', 'w') as file:
                json.dump(self.users, file)

            self.createAccount_frame.grid_forget()
            self.login_frame.grid(padx=100, pady=100)


    def addFoodtoList(self):
        if self.foodName.get() == "" or self.food_calorie.get() == "":
            tkinter.messagebox.showerror(title="Empty Fields", message="Some fields in the form are empty, please complete and try again.")     
        else:
            self.food[self.current_user] = self.foods
            #self.foods.append((self.foodName.get(),self.food_calorie.get()))
            self.food[self.current_user].insert(0,{self.foodName.get(): self.food_calorie.get()})
            #self.food[self.current_user]['Foods'].append(self.foods)
            self.food_list.insert(0,f'{self.foodName.get()} - {self.food_calorie.get()}')
            self.foodList.insert(0,self.foodName.get())

            with open('recentFoods.json','w') as file:
                json.dump(self.food, file)

def addCaloriesfromList(event):
    foodIndex = self.food_list.curselection()
    calorieAmount = self.food[self.current_user][foodIndex][self.foodList[foodIndex]]

    current_calories = self.users[self.current_user]["total_calories"]

    # Add the new calories to the current count
    new_ListCalories = int(calorieAmount)
    total_calories = current_calories + new_ListCalories

    # Update the user's calorie count in the user database
    self.users[self.current_user]["total_calories"] = total_calories



    # Save the updated user database to the file
    with open(self.user_db_filename, "w") as f:
        json.dump(self.users, f)

    # Update the progress bar and calories label
    self.update_progress_bar()







if __name__ == "__main__":
    app = CalorieCounterApp()
    app.mainloop()
