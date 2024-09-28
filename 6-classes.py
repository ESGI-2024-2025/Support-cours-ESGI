
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

# créons notre première classe
# par exemple, un système pour gérer une promotion


# on va vouloir créer des promos...
class Promotion:

    def __init__(self, ecole, annee) -> None: # cette fonction sera appelée lors de la création d'une nouvelle instance de la classe
        self.ecole = ecole # ceci sont des attributs, des variables liées à une instance
        self.annee = annee

# ainsi que des eleves...
class Eleve:

    def __init__(self,nom, age, promotion) -> None:
        self.nom = nom
        self.age = age
        self.promotion = promotion

    def get_promotion_name(self): # ceci est une méthode (fonction dans une classe), elle est accessible en faisant <instance>.get_promotion_name()
        return self.promotion.ecole + " " + str(self.promotion.annee) # self fait reference a l'instance en cours, pour acceder à ses attributs ou methodes
    

esgi_1er_annee = Promotion("ESGI",1) # on créé une instance de Promotion, celle de la première année de l'ESGI
mael = Eleve("Maël",17,esgi_1er_annee) # ici, on créé un élève, Mael, 17 ans, qui fait parti de la promotion créée précédemment

print(mael.get_promotion_name()) # on affiche le nom de la promotion de Maël grâce à la méthode qui fait parti de la classe Eleve