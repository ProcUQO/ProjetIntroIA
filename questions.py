# Contient nos questions
# par Camilien
import random

TYPES=["Addition","Soustraction","Division","RandomEmoji","Suite","NBLettre"]
lastTypes = [] # Je vais garder en mémoire la 1 ou 2ème dernière question pour pas qu'elle se répète trop
lastEmojiStories = [] # Même raison, à ajouter si je suis pas trop mort du cerveau
def choisirType():
    global lastTypes

    available = [t for t in TYPES if t not in lastTypes]
    if not available:
        lastTypes.pop(0)
        return choisirType() #récursif!!
    
    chosen = random.choice(available)
    lastTypes.append(chosen) # équivalent java de .add(chosen)
    if len(lastTypes) > 4: # Peut être 1, 3, à nous de juger le random-ness
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
    if questionType == "RandomEmoji":
        return generateEmoji()
    if questionType == "Suite":
        return generateSuite()
    if questionType == "NBLettre":
        return generateNB()
    
# J'y vais un peu avec la logique inverse. Je génère la réponse en premier, et ensuite je fait les deux chiffres soustrait pour l'addition.
def generateAddition():
    answer = random.randint(0,9) # entre 0 et 9 pour un seul caractère
    a = random.randint(0, answer)
    b = answer - a

    return f"{a} + {b}", answer

def generateSoustraction():
    answer = random.randint(0,9) # entre 0 et 9 pour un seul caractère
    b = random.randint(0, 9)
    a = answer + b

    return f"{a} - {b}", answer

def generateDivision():
    answer = random.randint(0,9)
    b = random.randint(1,9)
    a = answer * b

    # Je reroll simplement si la réponse est zéro, parce que c'est impossible, simplement!
    if answer == 0:
        return generateDivision()
    
    return f"{a} ÷ {b}", answer

# Question plus visuelle mais aléatoire. Pis non, y'aura pas de variante seahorse. Et oui, c'est cursed des emojis dans du code.
def generateEmoji():
    answer = random.randint(2,9)
    stories=[
        ("Oh non!\nJoe le fermier a perdu le contrôle de ses boeufs!\nPeux-tu lui dire combien il en a perdu?", "🐂"),
        ("La poissonière compte ses poissons,\nmais elle est pas très bonne en maths.\n Peux-tu l'aider?", "🐟"),
        ("Etienne est découragé, \ndes taouins sont arrivés en retard.\n Étant (naturellement) fatigué, \npeux-tu compter les présences pour lui?", "🧍"),
        ("Omer veut faire peur aux nouveaux étudiants.\nLa nouvelle stratégie à la mode?\nLes fantômes, bien sûr!\nPeux-tu lui faire un retour sur le \nnombre de participants? ", "👻")
    ]

    texte, emoji = random.choice(stories)
    return f"{texte}\n{emoji * answer}", answer

def generateSuite():
    answer=random.randint(0,9)
    saut=random.randint(1,3)
    start = answer-3*saut
    if start < 0:
        return generateSuite()
    # devrait pas dépasser 9, fight me, sinon jvous laisse me briser les os
    return f"{start},{start+saut},{start+2*saut}, ?", answer

# La preuve que notre IA est la best, c'est qu'elle sait compter des lettres. Vous êtes libres d'ajouter des mots.
# IMPORTANT, pas de majuscules!! J'veux pas faire de confusion sur si une majuscule ça compte ou non!!
def generateNB():
    mots=[
        "banana",
        "ananas",
        "avalanche",
        "anticonstitutionnellement",
        "tung tung tung sahur",
        "patate",
        "pâté chinois",
        "geronimo",
        "produit manmade",
        "kevin",
        "frappé aux ananas",
        "microsoft",
        "electro-encephalographie",
        "mississippi",
        "couscous",
        "abracadabra",
        "murmuration",
        "assassin",
        "cocorico",
        "coloscopie"
    ]
    motChoisi=random.choice(mots)
    lettres = [c for c in set(motChoisi) if c != " "] # je déteste les caractères vide, on filter ça dehors
    lettre=random.choice(lettres) # prend un caractère, parce que le random, c'est awesome
    answer=motChoisi.count(lettre)
    return f"Combien de '{lettre}' dans '{motChoisi}'?", answer