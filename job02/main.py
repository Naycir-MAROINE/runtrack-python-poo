class Operation:
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Instanciation de la classe Operation avec des valeurs par défaut pour nombre1 et nombre2
operation_instance = Operation()

# Impression des valeurs des attributs nombre1 et nombre2
print("Valeur de nombre1:", operation_instance.nombre1)
print("Valeur de nombre2:", operation_instance.nombre2)
