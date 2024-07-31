import json
from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, random, choice
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)  # Join method

    password_inpute.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_inpute.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="ops", message="make sure you have fill all form")
    else:
        try:
            with open("data.json", mode="r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            with open("data.json", mode="w") as file:
                # saving updated data
                json.dump(data, file, indent=4)
                messagebox.showinfo(title="Data Saved", message="Sucessfully saved")
        finally:
            website_input.delete(0, END)
            password_inpute.delete(0, END)

# ---------------------------- Find PassWord ------------------------------- #
def find_password():

    website = website_input.get().title()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message= f"Email: {email}\nPassword:{password}")
        else:
            messagebox.showinfo(title=website,message=f"{website} is not found in the data base")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, )
canvas = Canvas(width=200, height=200, highlightthickness=0)

logo_img = PhotoImage(file="../Day29-Password/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
# labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_lable = Label(text="Password:")
password_lable.grid(column=0, row=3)

# inputs
website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()
email_input = Entry(width=43)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "nati@gmail.com")
password_inpute = Entry(width=21)
password_inpute.grid(column=1, row=3)
# button
gennerate_passButton = Button(text="Generate Password", command=generate_password)
gennerate_passButton.grid(row=3, column=2)
search_button = Button(text="Search",width=13, command=find_password)
search_button.grid(column=2, row=1)
add_button = Button(text="Add", width=35, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
