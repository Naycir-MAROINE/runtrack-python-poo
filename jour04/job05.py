import math

class Forme:
    def aire(self):
        return 0
    

class Rectangle(Forme):
    def __init__(self, largeur , hauteur):
        self._largeur = largeur
        self._hauteur = hauteur

    def aire(self):
        return self._largeur * self._hauteur
    
class Cercle(Forme):
    def __init__(self,radius):
        self._radius = radius

    def aire(self):
        return math.pi * self._radius ** 2

mon_rectangle  = Rectangle(6,7)
print("Aire du rectangle :", mon_rectangle.aire())

mon_cercle = Cercle(3)
print("Aire du cercle:", mon_cercle.aire())