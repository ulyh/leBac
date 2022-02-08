#-------------------------------------------------------------------------------
# Name:        bac
# Author:      h
# Created:     20/05/2021
#-------------------------------------------------------------------------------
# -*- coding: UTF-8 -*-
from easygui import *
from tkinter import *
from PIL import Image, ImageTk

def average():
    """ donne la moyenne obtenue au Bac
        prend une liste en argument """
    # définir les variables pour les notes matières
    global math,fran,pc,hg,bio,res

    # dictionnaire des matières du Bac avec leurs coefficients associés

    dico = {"Mathématiques":7, "Français":4, "Physique-Chimie":8, \
    "Histoire-Géographie":5, "Biologie":6}

    # vide la case résultat
    res.delete(0, END)

    # récupère la saisie des matières en str
    note_m = math.get()
    note_fran = fran.get()
    note_pc = pc.get()
    note_hg = hg.get()
    note_bio = bio.get()


    # liste des notes en str
    notes = [note_m, note_fran, note_pc, note_hg, note_bio]

    # calcul de la moyenne
    somme = 0
    total = 0
    for i, key in enumerate(dico):
        total += dico[key] # somme les coefficents
        dico[key] = dico[key] * float(notes[i]) # value => coef * note
        somme += dico[key] # somme les notes avec leurs coefs
    moyenne = somme/total
    moyenne = round(moyenne, 2) # moyenne de l'etudiant
    res.insert(0, moyenne)
    return moyenne

""""
def resultat():
    # donne le résultat au Bac
    moyenne = average()
    if moyenne >= 10:
        message = "Admis"
    elif moyenne >= 8:
        message = "Rattrapage"
    else:
        message = "Ajourné"
    return message
"""

def admis():
    """ crée une fenêtre de résultats: admis/rattrapage/ajourné """

    moyenne = average()

    if moyenne >= 10:

        # création d'une fenêtre
        fen1 = Tk()
        fen1.title("Baccalauréat 2021")
        fen1.geometry("400x400")
        fen1.config(bg="white")

        # construis un tableau
        tab = Canvas(fen1, width=300, height=300, bg="white", \
        highlightbackground="white") # la bordure du canvas
        tab.grid(row=1, column=0)

        # affiche un message
        texte = Message(fen1, \
        text="Félicitations !\n\nVous êtes l'heureux propriétaire du Baccalauréat.",
        bg="white", fg="black", font=("Arial", 15), aspect=350)
        texte.grid(row=0, column=0, columnspan=50)

        # récupère l'image dans le dossier
        pic = PhotoImage(file="bac.png", master=fen1)

        # redimensionne l'image
        picz = pic.subsample(2,2)

        tab.create_image(130, 90, anchor=NW, image=picz)

        pic.show()

    elif moyenne >=8:

        # création d'une fenêtre
        fen1 = Tk()
        fen1.title("Baccalauréat 2021")
        fen1.geometry("400x400")
        fen1.config(bg="white")

        # construire un tableau
        tab = Canvas(fen1, width=300, height=300, bg="white", \
        highlightbackground="white") # la bordure du canvas
        tab.grid(row=1, column=0)

        # affiche un message
        texte = Message(fen1, \
        text="Courage !\n\nVous êtes admis au rattrapage.",\
        bg="white", fg="grey", font=("", 15), aspect=350)
        texte.grid(row=0, column=0, columnspan=50)

        # récupère l'image dans le dossier
        pic = PhotoImage(file="main.png", master=fen1)

        # redimensionne l'image
        picz = pic.subsample(2,2)

        tab.create_image(90, 50, anchor=NW, image=picz)
        pic.show()
    else:

        # création d'une fenêtre
        fen1 = Tk()
        fen1.title("Baccalauréat 2021")
        fen1.geometry("400x400")
        fen1.config(bg="#fbf0f5")

        # construis un tableau
        tab = Canvas(fen1, width=300, height=300, bg="#fbf0f5",
        highlightbackground="#fbf0f5") # la bordure du canvas
        tab.grid(row=1, column=0)

        # affiche un message
        texte = Message(fen1,text="Ajourné\n\n\
        Si aux exams tu t'es planté\nViens faire un tour à Lambé!",bg="#fbf0f5",
        fg="grey", font=("", 15), aspect=700)
        texte.grid(row=0, column=0, columnspan=50)

        # récupère l'image dans le dossier
        pic = PhotoImage(file="lambezellec.png", master=fen1)

        # redimensionne l'image
        picz = pic.subsample(1,2)

        tab.create_image(50, 50, anchor=NW, image=picz)
        pic.show()



def dellabel():
    """ Vide les cases """
    # definir les variables
    global math, fran, pc, hg, bio, res

    # vide les cases
    res.delete(0, END)
    math.delete(0, END)
    fran.delete(0, END)
    pc.delete(0, END)
    hg.delete(0, END)
    bio.delete(0, END)

def menu():
    # définir les variables
    global math,fran,pc,hg,bio,res

    # création d'une fenêtre avec le résultat et moyenne du Bac
    fenetre = Tk()
    fenetre.title("Vos résultats")
    fenetre.geometry("400x300")
    fenetre.config(bg="grey")


    # création des labels
    titre = Label(fenetre, text="Résultats du Baccalauréat 2021", bg="grey",\
    fg="black", font=("Arial", 17), pady=15)
    stitre = Label(fenetre, text="Entrez vos notes", fg="#307D7E", bg="#fbf0f5",\
    font=("Arial", 11))
    math_label = Label(fenetre, text="Mathématiques",font=("", 10, "bold"),\
    justify="right",bg="grey",fg="#d0f2e9")
    fran_label = Label(fenetre, text="Français",font=("", 10, "bold"),\
    bg="grey",fg="#d0f2e9")
    Label()
    pc_label = Label(fenetre, text="Physique-Chimie",font=("", 10, "bold"),\
    bg="grey",fg="#d0f2e9")
    hg_label = Label(fenetre, text="Histoire-Géographie",font=("", 10, "bold"),\
    bg="grey",fg="#d0f2e9")
    bio_label = Label(fenetre, text="Biologie",font=("", 10, "bold"),\
    justify="left",bg="grey",fg="#d0f2e9")

    # saisie des notes
    math = Entry(fenetre, width=15, bg="#d0f2e9", justify="center")
    fran = Entry(fenetre, width=15, bg="#d0f2e9", justify="center")
    pc = Entry(fenetre, width=15, bg="#d0f2e9", justify="center")
    hg = Entry(fenetre, width=15, bg="#d0f2e9", justify="center")
    bio = Entry(fenetre, width=15, bg="#d0f2e9", justify="center")
    res = Entry(fenetre, width=15, bg="#fbf0f5", justify="center")

    #label résultat
    #texte_res = resultat()
    #res_label = Label(fenetre, text=texte_res)

    # construit un bouton résultat
    bt_res = Button(fenetre, text="Résultats", bg="#fbf0f5", fg="#307D7E",\
    font=("Arial", 10), command= admis)

    # construit un bouton close
    close = Button(fenetre, text="Close", bg="grey", fg="#d0f2e9", \
    font=("Arial", 11), command= fenetre.destroy)

    # construit bouton réinitialiser
    dell = Button(fenetre, text="réinitialiser", bg="#fbf0f5", fg="#307D7E",\
    font=("Arial", 11), command= dellabel)


    # position des labels
    titre.grid(row=0, column=0, columnspan=4)
    stitre.grid(row=1, column=0, sticky=EW, columnspan=4)
    math_label.grid(row=2, column=0); math.grid(row=2, column=1)
    fran_label.grid(row=3, column=0); fran.grid(row=3, column=1)
    pc_label.grid(row=4, column=0); pc.grid(row=4, column=1)
    hg_label.grid(row=5, column=0); hg.grid(row=5, column=1)
    bio_label.grid(row=6, column=0); bio.grid(row=6, column=1)
    res.grid(row=7, column=1)

    bt_res.grid(row=7, column=0)
    close.grid(row=8, column=3)
    dell.grid(row=8, column=2)

    fenetre.mainloop()



if __name__ == '__main__':
    menu()

#--- Programme principal -------------------------------------------------------
