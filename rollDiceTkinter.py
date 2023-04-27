from tkinter import *
import tkinter as tk
from random import *
import random as rd

fen_principale = Tk()

# Paramètrage fenêtre principale
fen_principale.geometry('300x500')
fen_principale.configure(background = '#617B8D')

def lancer4(): #fonction permettant le lancer aléatoire du dé
    variable = [rd.randint(1, 4)]
    # variable = choice(nombre)
    numero['text'] = "Résultat : %s" % variable

de = Button(fen_principale, text="lancer le dé 4", width=15, command=lancer4, background='#B4B5B5', activebackground='#333577', activeforeground='white')
de.pack(padx=20, pady=20)

def lancer6(): #fonction permettant le lancer aléatoire du dé
    variable = [rd.randint(1, 6)]
    # variable = choice(nombre)
    numero['text'] = "Résultat : %s" % variable

de = Button(fen_principale, text="lancer le dé 6", width=15, command=lancer6, background='#B4B5B5', activebackground='#333577', activeforeground='white')
de.pack(padx=20, pady=20)


def lancer10(): #fonction permettant le lancer aléatoire du dé
    variable = [rd.randint(1, 10)]
    # variable = choice(nombre)
    numero['text'] = "Résultat : %s" % variable

de = Button(fen_principale, text="lancer le dé 10", width=15, command=lancer10, background='#B4B5B5', activebackground='#333577', activeforeground='white')
de.pack(padx=20, pady=20)

def lancer12(): #fonction permettant le lancer aléatoire du dé
    variable = [rd.randint(1, 12)]
    # variable = choice(nombre)
    numero['text'] = "Résultat : %s" % variable

de = Button(fen_principale, text="lancer le dé 12", width=15, command=lancer12, background='#B4B5B5', activebackground='#333577', activeforeground='white')
de.pack(padx=20, pady=20)

def lancer20(): #fonction permettant le lancer aléatoire du dé
    variable = [rd.randint(1, 20)]
    # variable = choice(nombre)
    numero['text'] = "Résultat : %s" % variable

de = Button(fen_principale, text="lancer le dé 20", width=15, command=lancer20, background='#B4B5B5', activebackground='#333577', activeforeground='white')
de.pack(padx=20, pady=20)

def lancer100(): #fonction permettant le lancer aléatoire du dé
    variable = [rd.randint(1, 100)]
    # variable = choice(nombre)
    numero['text'] = "Résultat : %s" % variable

de = Button(fen_principale, text="lancer le dé 100", width=15, command=lancer100, background='#B4B5B5', activebackground='#333577', activeforeground='white')
de.pack(padx=20, pady=20)

# #ce que le dé affiche

# numero100 = Label(fen_principale, text="Résultat : ", width = 14, background='#DCCA93', font = 'bold', foreground='#000130' )

numero = Label(fen_principale, text="Résultat : ", width = 14, background='#DCCA93', font = 'bold', foreground='#000130' )
res = str(numero)[1:-1]
numero.pack(padx=20, pady=20, side="right")



fen_principale.mainloop()