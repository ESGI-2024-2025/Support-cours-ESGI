
import random

def generateDice():
    return random.randint(1,6)

# ...mais comment vérifier si l'utilisateur rentre bien un chiffre, avant de le convertir en entier...
# ...sinon... !
int("chocolat")
# Erreur !

# ...donc tant que l'utilisateur ne rentre pas une valeur autorisée, on redemande...

age = input("Entrez votre age: ")

# Si age n'est pas un chiffre, on refait un tour de boucle
while not age.isdigit():
    age = input("Entrez votre age: ")

# Si on se retrouve ici, la condition de la boucle n'est plus respectée, donc... age isdigit !
# On peut convertir l'âge sans souci
int(age)

# On peut aussi utiliser for : ça permet de faire un nombre précis d'iteration
# Par exemple, lire toutes les valeurs d'une liste de dés
dices = [generateDice(), generateDice(), generateDice(), generateDice(), generateDice(), generateDice(), generateDice(), generateDice()]

# On declare i, qui va de 0 et 7 dans le contexte de la boucle
for i in range(0,8):
    print("position",i,":",dices[i])

# ...ou alors, on peut déclarer une variable qui va "interer" sur la liste, donc prendre tour après tour les valeurs de la liste
for de in dices:
    print(de)
