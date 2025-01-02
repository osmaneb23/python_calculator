from tkinter import *

def clear_entry():
	entry.delete(0, END)

def ajouter_nombre(num):
    entry.insert(END, str(num))

def ajouter_virgule():
    if (entry.get().find(",") == -1):
        entry.insert(END, ",")

def delete():
    entry.delete(len(entry.get()) - 1, END)

def clear():
	clear_entry()

# Crée la fenêtre parent
window = Tk()
# Titre à la fenêtre
window.title("Calculatrice") 
# Fond de couleur blanc
window.configure(bg="white")
window.minsize(400,620)
window.maxsize(600, 820)
# Position et taille au lancement
window.geometry("400x620+1250+100")

# Create main frame
main_frame = Frame(window, bg="white")
main_frame.pack(expand=True, fill='both', padx=20, pady=20)

# Create and configure entry
entry = Entry(main_frame, bg="white", fg="black", font=('Aileron', 20))
entry.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)

# First row buttons
Button(main_frame, text="%", width=8, height=2, bg="black", fg="white").grid(row=1, column=0, padx=2, pady=2)
Button(main_frame, text="CE", width=8, height=2, bg="black", fg="white", command=clear_entry).grid(row=1, column=1, padx=2, pady=2)
Button(main_frame, text="C", width=8, height=2, bg="black", fg="white", command=clear).grid(row=1, column=2, padx=2, pady=2)
Button(main_frame, text="⌫", width=8, height=2, bg="black", fg="white", command=delete).grid(row=1, column=3, padx=2, pady=2)

# Number pad and operations
buttons = [
    '7', '8', '9', '÷',
    '4', '5', '6', 'x',
    '1', '2', '3', '-',
    '0', ',', '=', '+'
]

row = 2
col = 0
for button in buttons:
    if button.isdigit():
        btn = Button(main_frame, text=button, width=8, height=2, bg="grey", fg="white", 
                    font='Aileron', command=lambda x=button: ajouter_nombre(x))
    elif button == ',':
        btn = Button(main_frame, text=button, width=8, height=2, bg="black", fg="white",
                    command=ajouter_virgule)
    else:
        btn = Button(main_frame, text=button, width=8, height=2, bg="black", fg="white")
    
    btn.grid(row=row, column=col, padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Configure grid weights
for i in range(6):
    main_frame.grid_rowconfigure(i, weight=1)
for i in range(4):
    main_frame.grid_columnconfigure(i, weight=1)

window.mainloop()