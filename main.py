import os
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

os.system('python3 Palette/palette.py')

screen = tk.Tk()
screen.title('MuralTools')
screen.geometry('768x300')

frButtons = tk.Frame(screen)
frImage = tk.Frame(screen)
frProps = tk.Frame(screen)

lbButtons = tk.Label(frButtons, text='Herramientas')
lbImage = tk.Label(frImage, text='Vista previa')
lbBack = tk.Label(frImage, text='', bg="black")
lbImg = tk.Label(frImage, text='', image='')
lbProps = tk.Label(frProps, text='Propiedades')

def encoder():
    os.system('python3 Encoder/newencoder.py')

btEncoder = tk.Button(frButtons, text='Codificador', command=encoder)

W = 0
H = 275
 
files = os.listdir('Palette/Output')
f = files[0]
iml = Image.open('Palette/Output/' + f)

AR = iml.size[0] / iml.size[1]
W = H * AR

imr = iml.resize((int(W),H))
img = ImageTk.PhotoImage(imr)
lbImg.config(image=img) 

left = (500 - W) / 2

frButtons.place(x=0, y=0, width=106, height=300)
frImage.place(x=106, y=0, width=506, height=300)
frProps.place(x=612, y=0, width=156, height=300)

lbButtons.place(x=3, y=3, width=100, height=15)
lbImage.place(x=0, y=3, width=100, height=15)
lbBack.place(x=3, y=20, width=500, height=275)
lbImg.place(x=3 + left, y=20, width=W, height=H)
lbProps.place(x=0, y=3, width=100, height=15)

btEncoder.place(x=3, y=20, width=100, height=30)

screen.mainloop()
