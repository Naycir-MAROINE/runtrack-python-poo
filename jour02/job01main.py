class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur
    def get_longueur(self):
        return self._longueur
    
    def set_longueur(self, nouvelle_longueur):
        self._longueur = nouvelle_longueur

    def get_largeur(self):
        return self._largeur

    def set_largeur(self, nouvelle_largeur):
        self._largeur = nouvelle_largeur   

mon_rectangle =Rectangle(10,5)         

print("longueur du rectangle:" , mon_rectangle.get_longueur)
print("largeur du rectangle:", mon_rectangle.get_largeur)

mon_rectangle.set_longueur(15)
mon_rectangle.set_largeur(8)

print("Nouvelle longueur du rectangle :", mon_rectangle.get_longueur())
print("Nouvelle largeur du rectangle :", mon_rectangle.get_largeur())