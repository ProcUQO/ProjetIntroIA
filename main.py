import tkinter as gui
from questions import generateQuestion

# Pas de question encore sur le wake
current_answer = None;

# Utilise questions.py pour faire une question
def nouvelleQuestion():
    global current_answer

    q, a = generateQuestion()
    current_answer = a
    textQuestion.config(text=q)
    # Je nettoie la zone à dessin à chaque nouvelle question, comme sur le jeu original
    ClearDessin() 

# Temporaire, Yannick va pouvoir plugger la prédiction ici
def valider():
    print("La réponse attendue:", current_answer)
    # rajouter réseau neurones
    nouvelleQuestion()

#voilà les info et dimension de l'écran de l'application
app = gui.Tk()
app.geometry("1000x600")
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
frameQuestion.rowconfigure(0, minsize= 465)

#Conteneur où on va pouvoir dessiner pour répondre aux questions.
conteneurDessin = gui.Frame(frameGeneral)
conteneurDessin.configure(background='lightgrey')
conteneurDessin.columnconfigure(0, minsize=300)
conteneurDessin.rowconfigure(0, minsize=275)
conteneurDessin.rowconfigure(1, minsize= 25)
conteneurDessin.rowconfigure(2, minsize=25)

#créé un canevas pour qu'on puisse répondre au question en dessinant
frameDessin = gui.Canvas(conteneurDessin, width=300, height= 410)
frameDessin.configure(background='lightBlue')

#Permet d'effacer notre réponse si on c'est tromper
#Ou on peut l'utiliser quand on change de question
def ClearDessin():
    print('Je delete')
    frameDessin.delete('all')

#crée un bouton pour effacer notre réponse si on s'est tromper
clearButton = gui.Button(conteneurDessin, text='Clear', width=42, command=ClearDessin)
clearButton.configure(background='lightgreen')

# Bouton pour valider la question, sinon c'est dur de jouer hahaha
validerButton = gui.Button(conteneurDessin, text='Valider', width=42, command=valider)
validerButton.configure(background='lightblue')
validerButton.grid(row=2, column=0)

#Affiche un texte dans la grid de nos question
textQuestion = gui.Label(frameQuestion, text="Zone de questions", font=('Arial', 16))
textQuestion.configure(background='pink')
textQuestion.grid(row=0, column=0, padx=5, pady=5)

#permet d'organiser l'interface avec les colonne et ranger des grilles
frameGeneral.pack()
frameQuestion.grid(row=0, column=0)
conteneurDessin.grid(row=0, column=1)
frameDessin.grid(row=0, column=0)
clearButton.grid(row=1, column=0)


#permet d'instancier des rectangles de grosseur défini quand on maintien le click.
def Drawing(event):
    posX = event.x
    posY = event.y
    
    frameDessin.create_rectangle((posX,posY),(posX+2,posY+2), fill='black')

frameDessin.bind("<B1-Motion>", Drawing)

app.mainloop()