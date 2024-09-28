
# cependant, pourquoi certaines fonctions ressemblent à <fonction>(<element a manipuler>), et d'autres <element a manipuler>.<fonction>() ?
# exemple, concret, pourquoi pour ajouter une valeur à une liste, nous faisons liste.append(<element a ajouter>), au lieu de append(liste, <element a ajouter>) ?
# parce que append est en réalité une fonction qui appartient à une classe
# une classe est un element qui permet de créer différentes versions d'un même element, avec les mêmes fonctions associées, les mêmes informations de base, etc...
# int est une classe, str est une classe, list est une classe, dict est une classe, tuple est une classe, float est une classe... pour les plus évidents

# ici, on créé une "instance" de la classe "str"
text = str("Bonjour !") # bien evidemment, cela revient a faire text = "Bonjour !", car Python fait la conversion, mais on va utiliser le str pour la suite

# on peut acceder aux fonctions spécifiques d'une classe en utilisant l'instance qu'on souhaite traiter :
text = text.capitalize() # ici, capitalize, "méthode" (fonction d'une classe) de str, permet de transformer l'instance traitée en majuscules

is_a_number = text.isdigit() # ici, cela verifie si l'instance str text est un entier

# etc...

"""

CETTE SECTION SERA REMPLIE

"""
