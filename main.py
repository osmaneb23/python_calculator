from tkinter import *

def clear_entry():
	entry.delete(0, END)

def ajouter_nombre(num):
    entry.insert(END, str(num))

def clear():
	clear_entry()

# Crée la fenêtre parent
window = Tk()

window.title("Calculatrice") 
window.configure(bg="white")
window.minsize(400,620)
window.maxsize(600, 820)
window.geometry("400x620+1250+100")
entry = Entry(window, bg="white", fg="blue", width=200)
entry.pack()
button = Button(window, text="%", width=1, height=1, bg="black", fg="white")
button.pack()
button = Button(window, text="CE", width=1, height=1, bg="black", fg="white", command=clear_entry)
button.pack()
button = Button(window, text="C", width=1, height=1, bg="black", fg="white", command=clear)
button.pack()
button = Button(window, text="⌫", width=1, height=1, bg="black", fg="white")
button.pack()
button = Button(window, text="÷", width=1, height=1, bg="black", fg="white")
button.pack()
for i in range(9):
    button = Button(window, text=str(i+1), width=1, height=1, bg="grey", fg="white", 
                   font='Aileron', command=lambda x=i+1: ajouter_nombre(x))
    button.pack()

window.mainloop()