from random import randint
# ..mais pourquoi certains ont des parenthèses ? Comme print ? Ou input ? Ceux sont... des fonctions !

def helloWorld():
    print("Hello World!")

# Affiche hello world dans la console
helloWorld()

# Pourquoi les parenthèses ? Pour apporter des informations aux fonctions si nécessaire
# Par exemple, print prend une infinité d'arguments : toutes les valeurs à afficher dans la console
# Input prend un argument : le message à afficher pour demander quelque chose
# Penchons nous sur input:

a = input("Valeur: ")
print(a)

# Pourquoi a obtient une valeur ? Car il recupere la valeur sur input. Mais comment assigner une valeur sur l'appel d'une fonction ?
# Avec un return !
# Pour génerer un dé, revenons là dessus...
def generateDice():
    return randint(1,6)

# On voit que generate a un return : il prend la valeur qui est en face
# ...donc...
dice = generateDice()

# dice prend la valeur de la fonction, donc du return de la fonction !

def generate_certain_dice(nombre_de_des):

    des = []
    for i in range(0,nombre_de_des):
        generated_dice = generateDice()
        des.append(generated_dice)

    return des

liste_1 = generate_certain_dice(3)
liste_2 = generate_certain_dice(10)
liste_3 = generate_certain_dice(300)

print(liste_1, liste_2, liste_3)
