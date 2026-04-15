import tkinter as gui
from questions import generateQuestion

# Pas de question encore sur le wake
current_answer = None;
# Pour les transitions, pas besoin de dessiner quand on nous donne le résultat
drawing_enabled = True;

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
    # On passe en mode révision de réponse
    global drawing_enabled
    drawing_enabled = False
    
    # Désactive et masque les boutons Clear et Valider (réapparaît ensuite, no worries)
    clearButton.grid_remove()
    validerButton.grid_remove()

    # Activer et afficher le bouton OK
    okButton.grid(row=2, column=0)  # Place le bouton OK à la place de Valider
    okButton.config(state="normal")

    # encore une fois, temporaire à mort
    prediction = predictionTEMPORAIRE()
    if prediction == current_answer:
        feedback = f"Bonne réponse! ({prediction})"
    else:
        feedback = f"Faux! Réponse lue: ({prediction}), la bonne réponse est {current_answer}"
    # Debug
    print("La réponse attendue:", current_answer)
    feedbackLabel.config(text=feedback)

    # rajouter réseau neurones
    nouvelleQuestion()

def prochaine():
    global drawing_enabled
    drawing_enabled = True

    # Réactiver et réafficher les boutons Clear et Valider
    clearButton.grid(row=1, column=0)
    validerButton.grid(row=2, column=0)

    # Désactiver et masquer le bouton OK
    okButton.grid_remove()

    # Effacer le feedback
    feedbackLabel.config(text="")

    # Nouvelle question
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
frameDessin = gui.Canvas(conteneurDessin, width=300, height= 440)
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

# Va être notre feedback!
feedbackLabel = gui.Label(frameQuestion, text="", font=('Arial', 10))
feedbackLabel.configure(background='pink', anchor="center") # va changer
feedbackLabel.grid(row=1, column=0, padx=5, pady=5, sticky="ew")  # ew pour stretch le width
frameQuestion.columnconfigure(0, weight=1) 

okButton = gui.Button(conteneurDessin, text='OK', width=42, command=prochaine)
okButton.configure(background='orange')
okButton.grid(row=3, column=0)
# Pas visible au démarrage
okButton.grid_remove()
okButton.config(state="disabled")

#permet d'organiser l'interface avec les colonne et ranger des grilles
frameGeneral.pack()
frameQuestion.grid(row=0, column=0)
conteneurDessin.grid(row=0, column=1)
frameDessin.grid(row=0, column=0)
clearButton.grid(row=1, column=0)


#permet d'instancier des rectangles de grosseur défini quand on maintien le click.
def Drawing(event):
    if not drawing_enabled:
        return
    posX = event.x
    posY = event.y
    
    frameDessin.create_rectangle((posX,posY),(posX+2,posY+2), fill='black')

frameDessin.bind("<B1-Motion>", Drawing)

# À NE PAS GARDER!! Va être remplacé par le chiffre trouvé par le réseau de neurone, donne toujours 4 en attendant
# Peut être pour le debugging, mais Yannick a peut-être sa propre méthode pour débogger le chiffre
def predictionTEMPORAIRE():
    return str(4)

# question du startup
nouvelleQuestion() 
app.mainloop()