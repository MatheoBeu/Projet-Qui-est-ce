from tkinter import *
import tkinter as ttk

win = Tk()
win.title("Qui est-ce ?")
win.geometry("750x550")
win.minsize(700, 500)

win.config(background='grey')

label_title = Label(win, text="Generateur de Theme", font=("Courrier", 40), bg='grey')
label_title.pack()

nbcolonnes = Label(win, text="Nombres de colonnes", font=("Courrier", 20), bg='grey')
nbcolonnes.place(x=20, y=150)
entrycolonnes = Entry(win)
entrycolonnes.place(x=300, y=150)

nblignes = Label(win, text="Nombres de lignes", font=("Courrier", 20), bg='grey')
nblignes.place(x=20, y=200)
entrylignes = Entry(win)
entrylignes.place(x=300, y=200)

def creer_attribut():
    win2=Tk()
    win2.title("new attribut")
    win2.geometry("550x250")
    win2.config(background='grey')

    new_attribut = Label(win2, text="Nouvelle Attribut : ", font=("Courrier", 20), bg='grey')
    new_attribut.place(x=10, y=30)
    entryattribut = Entry(win2)
    entryattribut.place(x=200, y=30)
    ajoute = Button(win2, text="+",)
    ajoute.place(x= 430, y=30)

    exist_attribut = Label(win2, text="Attribut deja existants: ", font=("Courrier", 20), bg='grey')
    exist_attribut.place(x=10, y=80)



valider = Button(win, text="Creer attribut", command=creer_attribut)
valider.place(x=75, y=250)

valider = Button(win, text="Ajouter Perso")
valider.place(x=75, y=300)

valider = Button(win, text="Modifier Perso")
valider.place(x=300, y=300)

valider = Button(win, text="Generer le Theme")
valider.place(x=300, y=350)

win.mainloop()
