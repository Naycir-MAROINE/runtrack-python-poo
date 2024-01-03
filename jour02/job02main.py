class Livre:
    def __init__(self , titre , auteur , nombre_pages):
        self._titre = titre 
        self._auteur = auteur
        self._nombre_pages = nombre_pages

    def get_titre(self):
        return self._titre

    def set_titre(self, nouveau_titre):
        self._titre = nouveau_titre

    def get_auteur(self):
        return self._auteur

    def set_auteur(self, nouveau_auteur):
        self._auteur = nouveau_auteur   

    def get_nombre_pages(self):
        return self._nombre_pages

    def get_nombre_pages(self):
        return self._nombre_pages

    def set_nombre_pages(self, nouveau_nombre_pages):
        if isinstance(nouveau_nombre_pages, int) and nouveau_nombre_pages > 0:
            self._nombre_pages = nouveau_nombre_pages
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")



mon_livre = Livre("Harry Potter", "J.K" "Rowling", 500)

print("titre :", mon_livre.get_titre())
print("auteur :",mon_livre.get_auteur())
print("Nouveau nombre de pages :", mon_livre.get_nombre_pages())

mon_livre.set_nombre_pages(600)
print("Nouveau nombre de pages :", mon_livre.get_nombre_pages())

mon_livre.set_nombre_pages(-100)
