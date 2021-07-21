from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import random


# password generator section that triggers on clicking generate button---------------------------------------------------------------------------------
def generate():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(5, 10)
    nr_symbols = random.randint(2, 5)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for text in range(nr_letters):
        password_list.append(random.choice(letters))

    for text in range(nr_symbols):
        password_list.append(random.choice(symbols))

    for text in range(nr_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)

    password = ""
    for text in password_list:
        password += text
    password_entry.insert(0, password)


# Triggers when bbutton is clicked----------------------------------------------------------------------------


def clicked():
    w_name = website.get()
    e_name = email.get()
    p = password_entry.get()
    if w_name == 'Enter your website name here..' or e_name == "Enter your email here" or p == 'Enter your own password or click generate password':
        messagebox.showerror("OOPS!", "Please enter valid credentials")
        root.quit()
    else:
        with open("data.txt", "a") as secured_file:
            secured_file.write(f"Website : {w_name} --> Email : {e_name} --> Password : {p} \n")
            website.delete(0, END)
            email.delete(0, END)
            password_entry.delete(0, END)

#GUI part------------------------------------------------------------------------------
root = Tk()
root.title('AD Locker')
root.geometry('450x700')
root.iconbitmap('lock_icon.ico')
root.resizable(False, False)
my_canvas = Canvas(root, height=800, width=450)
my_img = ImageTk.PhotoImage(Image.open('lock.jpg'))
my_canvas.create_image(0, 0, image=my_img, anchor='nw')
my_canvas.pack(fill='both', expand=True)
website = Entry(root, font=('Helvetica', 10), width=30, borderwidth=2)
website.insert(-1, 'Enter your website name here..')
email = Entry(root, font=('Helvetica italic', 10), width=30, borderwidth=2)
email.insert(-1, "Enter your email here")
password_entry = Entry(root, font=('Helvetica', 10), width=30, borderwidth=2)
password_entry.insert(-1, 'Enter your own password or click generate password')
gen_pass_button = Button(root, text='Generate password', command=lambda: generate())
save_button = Button(root, text="Save password!", command=lambda: clicked())
my_canvas.create_text(220, 70, text="Welcome to AD Locker!.", font=("Helvetica", 25), fill="white")
website_window = my_canvas.create_window(50, 110, anchor="nw", window=website)
email_window = my_canvas.create_window(50, 150, anchor="nw", window=email)
password_entry_window = my_canvas.create_window(50, 190, anchor="nw", window=password_entry)
gen_pass_button_window = my_canvas.create_window(280, 188, anchor="nw", window=gen_pass_button)
save_button = my_canvas.create_window(119, 230, anchor="nw", window=save_button)

root.mainloop()
