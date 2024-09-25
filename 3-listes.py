
from random import randint

def generateDice():
    return randint(1,6)

# On veut PAR PUR HASARD génerer plusieurs dés, genre 8
# Au lieu de faire...

de1 = generateDice()
de2 = generateDice()
de3 = generateDice()
de4 = generateDice()
de5 = generateDice()
de6 = generateDice()
de7 = generateDice()
de8 = generateDice()

# ...on peut tout mettre sur une seule variable, avec des listes
des = [generateDice(), generateDice(), generateDice(), generateDice(), generateDice(), generateDice(), generateDice(), generateDice()]

# On peut accéder aux valeurs de la liste avec leur indice, donc leur position dans la liste
print(des[0])       # Affiche l'element d'indice 0, donc le 1er element
print(des[1])       # Affiche l'element d'indice 1, donc le 2eme element
print(des[2])       # Affiche l'element d'indice 2, donc le 3eme element
# ...
print(des[7])       # Affiche l'element d'indice 7, donc le 7+1eme element

# ... mais on ne va pas faire ça comme ça pour afficher les valeurs, avec une liste de 1000 elements, ça serait bonbon, donc...