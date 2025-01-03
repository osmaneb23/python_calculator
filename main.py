from tkinter import *
from PIL import Image, ImageTk
import os

def apply_entry_style():
    # Fonction utilitaire pour maintenir le style cohérent
    entry.config(
        bg="#f0f0f0",
        fg="black",
        relief='solid',
        borderwidth=1
    )

# Fonctions pour gérer les entrées de la calculatrice
def clear_entry():
    entry.config(state='normal')
    entry.delete(0, END)
    entry.config(state='readonly')
    apply_entry_style()

def ajouter_nombre(num):
    entry.config(state='normal')
    entry.insert(END, str(num))
    entry.config(state='readonly')
    apply_entry_style()

def ajouter_virgule():
    entry.config(state='normal')
    if (entry.get().find(",") == -1):
        entry.insert(END, ",")
    entry.config(state='readonly')
    apply_entry_style()

def delete():
    entry.config(state='normal')
    entry.delete(len(entry.get()) - 1, END)
    entry.config(state='readonly')
    apply_entry_style()

def clear():
    # Alias pour clear_entry()
    clear_entry()

def handle_keypress(event):
    # Empêcher la saisie directe dans l'Entry
    return "break"

# Configuration de la fenêtre principale
window = Tk()
window.title("Calculatrice") 
window.configure(bg="white")
image = Image.open('ico/calculator.png')
photo = ImageTk.PhotoImage(image)
window.wm_iconphoto(True, photo)
# window.wm_iconbitmap('ico/calculator.png')

# Définition des tailles minimale et maximale de la fenêtre
window.minsize(400,620)
window.maxsize(600, 820)
# Position initiale de la fenêtre sur l'écran (x=1250, y=100)
window.geometry("400x620+1250+100")

# Création du cadre principal qui contiendra tous les éléments
main_frame = Frame(window, bg="white")
main_frame.pack(expand=True, fill='both', padx=20, pady=20)

# Création du champ de saisie
entry = Entry(main_frame, 
             bg="#f0f0f0",  # Fond gris clair
             fg="black", 
             font=('Aileron', 20), 
             justify='right',
             relief='solid',  # Bordure solide
             borderwidth=1)   # Épaisseur de la bordure
entry.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)

# Liaison pour empêcher la saisie directe
entry.bind('<Key>', handle_keypress)

# Boutons de la première rangée (fonctions spéciales) avec police cohérente
Button(main_frame, text="%", width=8, height=2, bg="black", fg="white").grid(row=1, column=0, padx=2, pady=2)
Button(main_frame, text="CE", width=8, height=2, bg="black", fg="white", command=clear_entry,).grid(row=1, column=1, padx=2, pady=2)
Button(main_frame, text="C", width=8, height=2, bg="black", fg="white", command=clear,).grid(row=1, column=2, padx=2, pady=2)
Button(main_frame, text="⌫", width=8, height=2, bg="black", fg="white", command=delete,).grid(row=1, column=3, padx=2, pady=2)

# Configuration du pavé numérique et des opérations
buttons = [
    '7', '8', '9', '÷',
    '4', '5', '6', 'x',
    '1', '2', '3', '-',
    '0', ',', '=', '+'
]

# Création dynamique des boutons
row = 2
col = 0
for button in buttons:
    if button.isdigit():
        # Boutons numériques en gris
        btn = Button(main_frame, text=button, width=8, height=2, bg="grey", fg="white", 
                    command=lambda x=button: ajouter_nombre(x))
    elif button == ',':
        # Bouton virgule
        btn = Button(main_frame, text=button, width=8, height=2, bg="black", fg="white",
                    command=ajouter_virgule)
    elif button == '=':
        # Bouton égale
        btn = Button(main_frame, text=button, width=8, height=2, bg="red", fg="white",
                    command=ajouter_virgule)
    else:
        # Boutons d'opération en noir
        btn = Button(main_frame, text=button, width=8, height=2, bg="black", fg="white")
    
    btn.grid(row=row, column=col, padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Configuration pour que les éléments s'adaptent à la taille de la fenêtre
for i in range(6):
    main_frame.grid_rowconfigure(i, weight=1)
for i in range(4):
    main_frame.grid_columnconfigure(i, weight=1)

# Ajout de la liaison des touches
window.bind('<Key>', handle_keypress)

# Lancement de la boucle principale
window.mainloop()