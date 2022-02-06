import pandas
from tkinter import *
import random


BACKGROUND_COLOR = "#B1DDC6"


# read data
current_card = {}
to_learn 	 = {}

try:
	data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
	original_data = pandas.read_csv("data/french_words.csv")
	to_learn = original_data.to_dict(orient="records")

else:
	to_learn = data.to_dict(orient="records")


def is_known():
	global current_card, to_learn
	to_learn.remove(current_card)
	data = pandas.DataFrame(to_learn)
	data.to_csv("data/words_to_learn.csv", index=False)
	next_card()


def next_card():
	global current_card, flip_timer
	window.after_cancel(flip_timer)
	current_card = random.choice(to_learn)
	canvas.itemconfig(card_title, text="French", fill="black")
	canvas.itemconfig(card_word, text=current_card["French"], fill="black")
	canvas.itemconfig(card_background, image=card_front_img)
	flip_timer = window.after(3000, func=flip_cards)


def flip_cards():
	global current_card
	canvas.itemconfig(card_title, text="English", fill="white")
	canvas.itemconfig(card_word, text=current_card["English"], fill="white")
	canvas.itemconfig(card_background, image=card_back_img)


# window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_cards)


# load images
check_img = PhotoImage(file="./images/right.png")
cross_img = PhotoImage(file="./images/wrong.png")
card_back_img  = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")


# buttons
known_button   = Button(image=check_img, 
							highlightthickness=0, 
							command=is_known
						)

unknown_button = Button(image=cross_img, 
							highlightthickness=0, 
							command=next_card
						)

known_button.grid(column=1, row=1)
unknown_button.grid(column=0, row=1)


# canvas
canvas = Canvas(width=800, height=526, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, 
									text="", 
									font=("Arial", 40, "italic")
								)
card_word = canvas.create_text(400, 263, 
									text="", 
									font=("Arial", 60, "bold")
								)

canvas.grid(column=0, row=0, columnspan=2)

next_card()


window.mainloop()