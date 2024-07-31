from tkinter import *
import random
import pandas
from pandas import DataFrame

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/danish.csv")
    to_learn = original_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_title, text="Danish")
    canvas.itemconfig(canvas_word, text=current_card["Danish"])
    canvas.itemconfig(card_background, image=my_image_front)
    flip_timer = window.after(2000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_title, text="English")
    canvas.itemconfig(canvas_word, text=current_card["English"])
    canvas.itemconfig(card_background, image=my_image_back)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)

    next_card()


# Creating a new window and configurations
window = Tk()
window.title("Flashy")

flip_timer = window.after(1000, func=flip_card)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, highlightthickness=0)

my_image_front = PhotoImage(file="images/card_front.png")
my_image_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=my_image_front, )
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="", font=("Ariel", 40, "bold"))

my_image_right = PhotoImage(file="images/right.png")
my_image_wrong = PhotoImage(file="images/wrong.png")
button_right = Button(image=my_image_right, highlightthickness=0, command=is_known)
button_wrong = Button(image=my_image_wrong, highlightthickness=0, command=next_card)

button_wrong.grid(column=0, row=1)
button_right.grid(column=1, row=1)

next_card()

window.mainloop()
