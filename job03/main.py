class Operation:
    def __init__(self, nombre1=12, nombre2=6):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(f"Résultat de l'addition : {resultat}")

# Instanciation de la classe Operation avec des valeurs par défaut pour nombre1 et nombre2
operation_instance = Operation()


operation_instance.addition()
