from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)
    password = ''.join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data ={
        website:{
            'email': email,
            'password': password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message='Plz make sure you have not left any fields empty!!!')
    else:
            try:
                with open('data.json', 'r') as data_file:
                    # reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # updating old data with new data
                data.update(new_data)

                with open('data.json', 'w') as data_file:
                    # saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

def find_password():
    website = website_entry.get()
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Data File Found!!!')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title='Error', message=f"No details for {website} exists")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

website_label = Label(text='Website')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username: ')
email_label.grid(column=0, row=2)

password_lable = Label(text='Password: ')
password_lable.grid(column=0, row=3)

website_entry = Entry(width=23)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=40)
email_entry.grid(column=1,row=2, columnspan=2)
email_entry.insert(0, 'lnl5609@126.com')

password_entry = Entry(width=23)
password_entry.grid(column=1, row=3)


generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text='Add', width=40, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text='Search', width=16, command=find_password)
search_button.grid(column=2, row=1)


window.mainloop()

# add a SEARCH Button
# adjust the layout and other widgets as needed to get the desired look
# create a function called find_password
# check if the users' text entry matches an item in the data.json
# if yes, show a messagebox with the websites' name and password
# catch an exception that might occur tryingt to access the data.json showing a messagebox with the text 'no data file found'
# if it does not exist, show a messagebox that reads 'no details for the website exists'