from tkinter import Button, Entry

from buy_page import display_products
from canvas import root, frame
from helpers import clean_screen, get_password_hash
from json import loads, dump


def render_entry():
    register_button = Button(
        root,
        text='Register',
        bg='green',
        fg='white',
        borderwidth=0,
        width=20,
        height=3,
        command=register  # pass by reference because we need the command to call the function when we click

    )

    login_button = Button(
        root,
        text='Login',
        bg='blue',
        fg='white',
        borderwidth=0,
        width=20,
        height=3,
        command=login
    )

    frame.create_window(350, 260, window=register_button)
    frame.create_window(350, 320, window=login_button)


def register():
    clean_screen()

    frame.create_text(100, 50, text='First name: ')
    frame.create_text(100, 100, text='Last name: ')
    frame.create_text(100, 150, text=' Username: ')
    frame.create_text(100, 200, text='Password: ')
    # could make a password repeat authentication

    frame.create_window(200, 50, window=first_name_box)
    frame.create_window(200, 100, window=last_name_box)
    frame.create_window(200, 150, window=username_box)
    frame.create_window(200, 200, window=password_box)

    register_button = Button(
        root,
        text='Register',
        bg='green',
        fg='white',
        borderwidth=0,
        width=10,
        height=2,
        command=registration
    )
    frame.create_window(300, 250, window=register_button)


def get_users_data():
    info_data = []
    with open('db/users_info.txt', 'r') as users_file:
        for line in users_file:
            info_data.append(loads(line))

    return info_data


def login():
    clean_screen()

    frame.create_text(100, 50, text='Username: ')
    frame.create_text(100, 100, text='Password: ')

    frame.create_window(200, 50, window=username_box)
    frame.create_window(200, 100, window=password_box)



    frame.create_window(250, 150, window=login_button)


def logging():
    if validate_login():
        display_products()

    else:
        frame.create_text(160, 200, text='Invalid username or password!', fill='red')


def validate_login():
    info_data = get_users_data()

    current_username = username_box.get()
    current_password = get_password_hash(password_box.get())

    for record in info_data:
        record_username = record['Username']
        record_password = record['Password']

        if current_username == record_username and current_password == record_password:
            return True
    return False


def registration():
    info_dict = {
        'First name': first_name_box.get(),
        'Last name': last_name_box.get(),
        'Username': username_box.get(),
        'Password': password_box.get(),
    }
    print(info_dict)
    if validate_registration(info_dict):
        with open('db/users_info.txt', 'a') as users_file:
            info_dict['Password'] = get_password_hash(info_dict['Password'])
            dump(info_dict, users_file)
            users_file.write('\n')
            display_products()


def validate_registration(info):
    frame.delete('error')  # deletes the current error if it's not an error anymore
    for key, value in info.items():
        if not value.strip():
            frame.create_text(
                300,
                300,
                text=f'{key} cannot be empty!',
                fill='red',
                tags='error',

            )

            return False

    info_data = get_users_data()

    for record in info_data:
        if record['Username'] == info['Username']:
            frame.create_text(
                300,
                300,
                text=f"{info['Username']} is already existing username!",
                fill='red',
                tags='error',

            )

            return False
    return True


def print_event(event):
    # print(event)
    info = {
        username_box.get(),
        password_box.get()
    }

    for el in info:
        if not el.strip():
            login_button['state'] = 'disabled'
            break
    else:
        login_button['state'] = 'normal'


first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
username_box = Entry(root, bd=0)
password_box = Entry(root, bd=0, show='*')

login_button = Button(
        root, text='Login',
        bg='blue',
        fg='white',
        borderwidth=0,
        command=logging
    )

login_button['state'] = 'disabled'

root.bind('<KeyRelease>', print_event)  # listener
