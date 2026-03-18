import os
import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

if not os.path.exists("data/words_to_learn.csv"):
    flashcards = pd.read_csv("data/french_words.csv")
else:
    flashcards = pd.read_csv("data/words_to_learn.csv")
to_learn = flashcards.to_dict(orient="records")

current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_image)

def card_learned():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.configure(background=BACKGROUND_COLOR)
window.title("Flashcards")
window.configure(padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=528, bg=BACKGROUND_COLOR)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 264, image=front_image)
language_label = Label(text="English")
word_label = Label(text="Some word")
language_label.grid(row=1, column=0)
language_text = canvas.create_text(400, 150, text="Language", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 60))
canvas.grid(row=0, column=0, columnspan=2, sticky=W+E)


correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=card_learned)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
correct_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

next_card()

mainloop()




