class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur

    def longueur(self):
        return self._longueur

    def longueur(self, value):
        self._longueur = value

    def largeur(self):
        return self._largeur

    def largeur(self, value):
        self._largeur = value

    def perimetre(self):
        return 2 * (self._longueur + self._largeur)
    
    def surface(self):
        return self._longueur * self._largeur
    

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)    
        self._hauteur = hauteur

    def hauteur(self):
        return self._hauteur
    
    def hauteur(self, value):
        self._hauteur =value

    def volume(self):
        return self._longueur * self._largeur * self._hauteur

rectangle = Rectangle(6,9)
print(f"Perimetre du rectangle : {rectangle.perimetre()}")
print(f"Surface du rectangle : {rectangle.surface()}")

parallelepipede = Parallelepipede(4,5,6)
print(f"Volume du parallelepipede : {parallelepipede.volume()}")
