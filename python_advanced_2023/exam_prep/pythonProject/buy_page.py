from tkinter import Button

from canvas import frame, root
from helpers import clean_screen
from json import load, dump
from Pillow import Image, ImageTk


def display_products():
    clean_screen()


def display_stock():
    global info
    with open('db/products_data.json', 'r') as stock:
        info = load(stock)

    x, y = 150, 50

    for product_name, product_info in info.items():
        product_image = ImageTk.PhotoImage(Image.open(product_info["image"]))
        images.append(product_image)

        frame.create_text(x, y, text=product_name, font=("Comic Sans MS", 15))
        frame.create_image(x, y + 100, image=product_image)

        if product_info['quantity'] > 0:
            color = 'green'
            text = f"In stock: {product_info['quantity']}"

            product_button = Button(
                root,
                text='Buy',
                bg='green',
                fg='white',
                font=('Comic Sans MS', 12),
                width=5,
                command= lambda x=product_name, y=info: buy_product(x, y)
            )

            frame.create_window(x, y + 230, window=product_button)
        else:
            color = 'red'
            text = 'Out of stock'

        frame.create_text(x, y + 180, text=text, fill=color, font=('Comic Sans MS', 12))


        x += 200

        if x > 550:
            y += 230
            x = 150


def buy_product(product_name, info):
    info[product_name]['quantity'] -= 1

    with open("db/products_data.json", "w") as stock:
        dump(info, stock)

    display_products()


images = []