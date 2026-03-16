import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

flashcards = pd.read_csv("data/french_words.csv")
to_learn = flashcards.to_dict(orient="records")


def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(language_text, text="French")
    canvas.itemconfig(word_text, text=current_card["French"])

window = Tk()
window.configure(background=BACKGROUND_COLOR)
window.title("Flashcards")
window.configure(padx=50, pady=50)

canvas = Canvas(width=800, height=528, bg=BACKGROUND_COLOR)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 264, image=front_image)
# canvas.create_image(400, 264, image=back_image)
language_label = Label(text="English")
word_label = Label(text="Some word")
language_label.grid(row=1, column=0)
language_text = canvas.create_text(400, 150, text="Language", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 60))
canvas.grid(row=0, column=0, columnspan=2, sticky=W+E)


correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=next_card)

correct_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

next_card()



mainloop()




