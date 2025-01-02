from tkinter import *

# Fonctions pour gérer les entrées de la calculatrice
def clear_entry():
    # Efface tout le contenu du champ de saisie
    entry.delete(0, END)

def ajouter_nombre(num):
    # Ajoute un nombre au champ de saisie
    entry.insert(END, str(num))

def ajouter_virgule():
    # Ajoute une virgule si elle n'existe pas déjà dans le nombre
    if (entry.get().find(",") == -1):
        entry.insert(END, ",")

def delete():
    # Supprime le dernier caractère du champ de saisie
    entry.delete(len(entry.get()) - 1, END)

def clear():
    # Alias pour clear_entry()
    clear_entry()

# Configuration de la fenêtre principale
window = Tk()
window.title("Calculatrice") 
window.configure(bg="white")
# Définition des tailles minimale et maximale de la fenêtre
window.minsize(400,620)
window.maxsize(600, 820)
# Position initiale de la fenêtre sur l'écran (x=1250, y=100)
window.geometry("400x620+1250+100")

# Création du cadre principal qui contiendra tous les éléments
main_frame = Frame(window, bg="white")
main_frame.pack(expand=True, fill='both', padx=20, pady=20)

# Création du champ de saisie
entry = Entry(main_frame, bg="white", fg="black", font=('Aileron', 20))
entry.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)

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

# Lancement de la boucle principale
window.mainloop()