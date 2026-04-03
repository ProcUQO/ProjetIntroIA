import tkinter as gui

#voilà les info et dimension de l'écran de l'application
app = gui.Tk()
app.geometry("800x500")
app.configure(background='lightgray')
app.title("Brain age project")

#Le titre principal de notre application
titre = gui.Label(app, text="Brain Age Test", font=('Arial', 18))
titre.configure(background='lightgray')
titre.pack()

#Conteneur principal qui va contenir les deux fenêtres
#(la zone des question et la zone pour dessiner)
frameGeneral = gui.Frame(app)
frameGeneral.configure(background='black')
frameGeneral.columnconfigure(0, weight=2)
frameGeneral.columnconfigure(1, weight=1)
frameGeneral.rowconfigure(0, minsize= 450)

#Conteneur pour les question qui vont être poser
frameQuestion = gui.Frame(frameGeneral)
frameQuestion.configure(background='pink')
frameQuestion.columnconfigure(0, minsize=300)
frameQuestion.rowconfigure(0, minsize= 440)

#Conteneur où on va pouvoir dessiner pour répondre aux questions.
frameDessin = gui.Frame(frameGeneral)
frameDessin.configure(background='lightblue')
frameDessin.columnconfigure(0, minsize=500)
frameDessin.rowconfigure(0, minsize= 440)

textQuestion = gui.Label(frameQuestion, text="Zone de questions", font=('Arial', 16))
textQuestion.configure(background='pink')
textQuestion.grid(row=0, column=0, padx=5, pady=5)

textDessin = gui.Label(frameDessin, text="Zone de dessin", font=('Arial', 16))
textDessin.configure(background='lightblue')
textDessin.grid(row=0, column=0, padx=5, pady=5)

frameGeneral.pack()
frameDessin.grid(row=0, column=1)
frameQuestion.grid(row=0, column=0)

drawSpace = gui.Canvas

app.mainloop()