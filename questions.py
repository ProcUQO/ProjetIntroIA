# Contient nos questions
# par Camilien
import random

TYPES=["Addition","Soustraction","Division"]
lastTypes = [] # Je vais garder en mémoire la 1 ou 2ème dernière question pour pas qu'elle se répète trop

def choisirType():
    global lastTypes

    available = [t for t in TYPES if t not in lastTypes]
    if not available:
        lastTypes.pop(0)
        return choisirType() #récursif!!
    
    chosen = random.choice(available)
    lastTypes.append(chosen) # équivalent java de .add(chosen)
    if len(lastTypes) > 2: # Peut être 1, 3, à nous de juger le random-ness
        lastTypes.pop(0)

    return chosen

def generateQuestion():
    questionType = choisirType() # on prend le type de plus tôt
    # On s'attend à avoir (question, answer), exemple (1+1 = 2)
    if questionType == "Addition":
        return generateAddition()
    if questionType == "Soustraction":
        return generateSoustraction()
    if questionType == "Multiplication":
        return "Revoir (Multiplication)", "0"
    if questionType == "Division":
        return generateDivision()
    
# J'y vais un peu avec la logique inverse. Je génère la réponse en premier, et ensuite je fait les deux chiffres soustrait pour l'addition.
def generateAddition():
    answer = random.randint(0,9) # entre 0 et 9 pour un seul caractère
    a = random.randint(0, answer)
    b = answer - a

    return f"{a} + {b}", str(answer)

def generateSoustraction():
    answer = random.randint(0,9) # entre 0 et 9 pour un seul caractère
    b = random.randint(0, 9)
    a = answer + b

    return f"{a} - {b}", str(answer)

def generateDivision():
    answer = random.randint(0,9)
    b = random.randint(1,9)
    a = answer * b

    # Je reroll simplement si la réponse est zéro, parce que c'est impossible, simplement!
    if answer == 0:
        return generateDivision()
    
    return f"{a} ÷ {b}", str(answer)