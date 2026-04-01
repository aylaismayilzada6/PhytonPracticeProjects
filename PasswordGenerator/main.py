from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_symbols + password_numbers


    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def search():

    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found :(")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No data for {website} exist.")



def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password" : password
        }
    }
    if len(website) == 0 or len(password) == 0:
        empty_check = messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                    #reading old data
                    data = json.load(data_file)

                    #updateing old data with new data
                    data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=3)
        else:
            data.update(new_data)


            with open("data.json", "w") as data_file:
                # saving the updated data
                json.dump(data, data_file, indent=3)
        finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)







# ---------------------------- UI SETUP ------------------------------- #




from numpy.f2py.cfuncs import commonhooks


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

window.grid_columnconfigure(1, minsize=250)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0, pady=(0, 20))

# Labels
Label(text="Website:").grid(column=0, row=1, sticky="e", pady=5)
Label(text="Email/Username:").grid(column=0, row=2, sticky="e", pady=5)
Label(text="Password:").grid(column=0, row=3, sticky="e", pady=5)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, sticky="w")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_entry.insert(0, "ayla@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3, sticky="w")

# Buttons
Button(text="Search", command=search).grid(column=2, row=1, padx=5)
Button(text="Generate Password", command=generate_password)\
    .grid(column=2, row=3, padx=5)
Button(text="Add", width=36, command=save)\
    .grid(column=1, row=4, columnspan=2, pady=10)
window.mainloop()






