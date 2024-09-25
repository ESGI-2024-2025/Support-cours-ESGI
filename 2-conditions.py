
# On demande à l'utilisateur son âge
age = input("Quel est ton âge ? ")

# Or, age est un str (string), on le convertit en int (integer)
age = int(age)

# Maintenant, verifions son status...
if age < 11:
    print("Vous êtes un enfant.")
elif age < 18:
    print("Vous êtes un ado.")
elif age == 27:
    print("Vous êtes un vieux croulant (désolé Dylan, fallait une égalité pour tester...)")
else:
    print("Vous êtes un adulte.")

# On specifie un sexe
homme = input("Etes vous un homme ? ")

if homme == "oui":
    homme = True
elif homme == "non":
    homme = False
else:
    print("J'ai pas compris ta réponse")

# Verifions les stats attribuées au sexe à la naissance...
if homme:
    print("Vous êtes plus fort !")
else:
    print("Vous êtes plus intelligente !")
