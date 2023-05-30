import time
from words import words
from tkinter import *
import random


def get_random_word():
    return random.choice(words)


def word_to_(word):
    list_of_ = []
    for i in word:
        list_of_.append("_ ")

    return "".join(list_of_)[:-1]


def check_letter(letter, list_of):
    letter = letter.lower()
    if not letter.isalpha() or len(letter) != 1 or letter in list_of:
        return False
    list_of.append(letter)
    return True


def check_letter_in_word(word, letter):
    return letter in word


def add_letter(letter, sit, word):
    sit = list(sit.replace(" ", ""))
    for i, let in enumerate(list(word)):
        if let == letter:
            sit[i] = letter

    return " ".join(sit)


def check_for_win(word, sit):
    return word == sit.replace(" ", "")


def restart(ca):
    global title, inputs, secret_word, situation, count_lose, list_of_used
    c.delete('all')
    time.sleep(2)

    count_lose = 0
    list_of_used = []
    title = Label(win, text="Hangman", fg="black", bg="white", font=('Arial', 30))
    c.create_window(300, 30, window=title)

    inputs = Entry(win, bg="blue")
    c.create_window(320, 280, window=inputs)

    secret_word = get_random_word()
    situation = Label(win, text=word_to_(secret_word), fg="black", bg="white", font=('David', 20))
    c.create_window(200, 170, window=situation)

    c.create_image(0, 0, image=pic0, anchor=NW)
    ca.delete()


def get_input(event=None):
    global situation, secret_word, count_lose
    inp = inputs.get()
    inputs.delete(0, END)
    if check_letter(inp, list_of_used):
        if check_letter_in_word(secret_word, inp):
            sit = add_letter(inp, situation.cget("text"), secret_word)
            c.delete("situation")
            situation = Label(win, text=sit, fg="black", bg="white", font=('David', 20))
            c.create_window(200, 170, window=situation)
            if check_for_win(secret_word, sit):
                ca = Canvas(win, background="white", width=400, height=300)
                c.create_window(200, 150, window=ca)
                label = Label(win, text="YOU'VE WON", background="white", font=('David', 40))
                w = Label(win, text=f"the word was: {secret_word}", background="white", font=('David', 20))
                ca.create_window(200, 200, window=w)
                ca.create_window(200, 150, window=label)
                win.update()
                restart(ca)
        else:
            count_lose += 1
            c.create_image(0, 0, image=pics[count_lose], anchor=NW)
            if count_lose == 6:
                ca = Canvas(win, background="white", width=400, height=300)
                c.create_window(200, 150, window=ca)
                label = Label(win, text="YOU'VE LOST", background="white", font=('David', 40))
                w = Label(win, text=f"the word was: {secret_word}", background="white", font=('David', 20))
                ca.create_window(200, 200, window=w)
                ca.create_window(200, 150, window=label)
                win.update()
                restart(ca)


win = Tk()
win.resizable(False, False)
win.geometry("400x300")
win.title("Hangman")
list_of_used = []
count_lose = 0
c = Canvas(win, background="white", width=400, height=300)
c.pack()

title = Label(win, text="Hangman", fg="black", bg="white", font=('Arial', 30, 'underline'))
c.create_window(300, 30, window=title)

inputs = Entry(win, bg="blue")
c.create_window(320, 280, window=inputs)

secret_word = get_random_word()
situation = Label(win, text=word_to_(secret_word), fg="black", bg="white", font=('David', 20))
c.create_window(200, 170, window=situation)

pic0 = PhotoImage(file="img.png")
pic1 = PhotoImage(file="img_1.png")
pic2 = PhotoImage(file="img_2.png")
pic3 = PhotoImage(file="img_3.png")
pic4 = PhotoImage(file="img_4.png")
pic5 = PhotoImage(file="img_5.png")
pic6 = PhotoImage(file="img_6.png")
pics = [pic0, pic1, pic2, pic3, pic4, pic5, pic6]

c.create_image(0, 0, image=pic0, anchor=NW)

win.bind('<Return>', get_input)

win.mainloop()
