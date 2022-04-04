import os
import tkinter.filedialog
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

left = 0
W = 0
H = 475

screen = tk.Tk()
screen.title('MuralTools')
screen.geometry('768x500')

mnBar = tk.Menu(screen)

frButtons = tk.Frame(screen, bg='#ff0000')
frImage = tk.Frame(screen, bg='#00ff00')
frProps = tk.Frame(screen, bg='#0000ff')

lbButtons = tk.Label(frButtons, text='Herramientas', anchor='w')
lbImage = tk.Label(frImage, text='Vista previa', anchor='w')
lbBack = tk.Label(frImage, text='', bg="#000000")
lbImg = tk.Label(frImage, text='', image='')
lbProps = tk.Label(frProps, text='Propiedades', anchor='w')

def encoder():
    os.system('python3 Encoder/newencoder.py')

btEncoder = tk.Button(frButtons, text='Codificador', command=encoder)

def phScreen():
    phscreen = Toplevel()

    lbInPath = Label(phscreen, text='Entrada', anchor='w')
    lbOuPath = Label(phscreen, text='Salida', anchor='w')
    lbImPath = Label(phscreen, text='Imagen', anchor='w')

    flInPath = filedialog.askdirectory()
    flInPath = filedialog.askdirectory()
    flImage = filedialog.askopenfilename()

    btApply = Button(phscreen, text='Aplicar')

    lbInPath.grid(row=0, column=0)
    lbOuPath.grid(row=0, column=2)
    lbImPath.grid(row=0, column=4)

    flInPath.grid(row=0, column=1)
    flOuPath.grid(row=0, column=3)
    flImage.grid(row=0, column=4)

    btApply.grid(row=1, column=4)

def clScreen():
    clscreen = Toplevel()

""" 
files = os.listdir('Palette/Output')
f = files[0]
iml = Image.open('Palette/Output/' + f)

AR = iml.size[0] / iml.size[1]
W = H * AR

imr = iml.resize((int(W),H))
img = ImageTk.PhotoImage(imr)
lbImg.config(image=img) 

left = (700 - W) / 2
"""

opMenu = tk.Menu(mnBar)
opMenu.add_command(label='Rutas', command=phScreen)
opMenu.add_command(label='Colores', command=clScreen)

mnBar.add_cascade(label='Opciones', menu=opMenu)

frButtons.place(x=0, y=0, width=156, height=500)
frImage.place(x=156, y=0, width=706, height=500)
frProps.place(x=862, y=0, width=156, height=500)

lbButtons.place(x=3, y=3, width=150, height=15)
lbImage.place(x=3, y=3, width=150, height=15)
lbBack.place(x=3, y=20, width=700, height=475)
lbImg.place(x=3 + left, y=20, width=W, height=H)
lbProps.place(x=3, y=3, width=150, height=15)

btEncoder.place(x=3, y=20, width=150, height=30)

screen.config(menu=mnBar)
screen.mainloop()
