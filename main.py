from tkinter import *
import random
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list += [random.choice(letters) for x in range(nr_letters)]
    password_list += [random.choice(numbers) for x in range(nr_numbers)]
    password_list += [random.choice(symbols) for x in range(nr_symbols)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_set.set(password)
    pyperclip.copy(password)
    #password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    saved_pw = website_entry.get() + " | " + username_entry.get() + " | " + password_entry.get() + "\n"

    if website_entry.get() == "" or username_entry.get() == "" or password_entry.get() == "":
        messagebox.showwarning(title="Empty field", message="Please don't leave any fields empty")
        return

    confirm_dialog = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered:"
                                                                               f" \n Email: {username_entry.get()} "
                                                                               f" \n Password: {password_entry.get()}\n"
                                            )
    if confirm_dialog:
        file = "data.txt"
        with open(file, mode="a") as data:
            data.write(saved_pw)
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

my_pass_image = PhotoImage(file="logo.png")
image_canvas = Canvas(width=200, height=200)
image_canvas.create_image(100, 100, image=my_pass_image)
image_canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", anchor="e", width=13)
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:", anchor="e", width=13)
username_label.grid(column=0, row=2)
password_label = Label(text="Password:", anchor="e", width=13)
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()
username_entry = Entry()
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
#edit to add your own default email
username_entry.insert(END, "")
password_set = StringVar()
password_entry = Entry(textvariable=password_set)
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()

