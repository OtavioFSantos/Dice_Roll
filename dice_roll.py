import tkinter as tk
from PIL import Image, ImageTk
from random import choice

window = tk.Tk()
window.geometry('300x300')
window.title('Dice')

dices = ['dice1.png', 'dice2.png', 'dice3.png', 'dice4.png', 'dice5.png', 'dice6.png']
dice = ImageTk.PhotoImage(Image.open(choice(dices)))

label = tk.Label(window, image = dice)
label.pack(side = tk.BOTTOM)

def roll_dice():
    dice = ImageTk.PhotoImage(Image.open(choice(dices)))
    label.configure(image = dice)
    label.image = dice

button = tk.Button(window, text = 'Roll Dice', foreground = 'black', command = roll_dice)
button.pack()

window.mainloop()