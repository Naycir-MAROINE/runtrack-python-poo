class Forme:
    def aire(self):
        return 0
    

class Rectangle(Forme):
    def __init__(self, largeur , hauteur):
        self._largeur = largeur
        self._hauteur = hauteur

    def aire(self):
        return self._largeur * self._hauteur


mon_rectangle = Rectangle(5,6)

print(mon_rectangle.aire())