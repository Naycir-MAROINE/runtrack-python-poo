class CompteBancaire:
    def __init__(self, numero_compte,nom,prenom, solde, decouvert=False):
        self._numero_compte = numero_compte
        self._nom = nom
        self._prenom = prenom
        self._solde = solde
        self._decouvert = decouvert

    def afficher(self):
        print(f"Compte {self._numero_compte}- {self._nom} {self._prenom}")

    def afficher_solde(self):
      print(f"Solde du compte : {self._solde} euros")


    
    def versement(self, montant):
        self._solde += montant
        print(f"Versement de {montant} euros effectué. Nouveau solde : {self._solde} euros")    

    def retrait(self, montant):
        if self._solde - montant >= 0 or self._decouvert:
            self._solde -= montant
            print(f"Retrait de {montant} euros effectue. Nouveau solde : {self._solde} euros")
        else:
            print("solde insuffisant. Operation impossible.") 

    def agios(self , taux):
        if self._solde < 0:
            agios = abs(self._solde) * taux
            self._solde -=agios
            print(f"Agios de { agios} euros appliques. Nouveau solde : {self._solde} euros")
        else:
            print("Pas d'agios necessaires. Solde positif.")

    def virement(self, compte_destinataire, montant):
        if self._solde - montant >= 0 or self._decouvert:
            self.retrait(montant)
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} euros effectue vers le compte { compte_destinataire._numero_compte}")
        else:
            print("Solde insuffisant. Virement impossible.")  

compte1 = CompteBancaire(1,"Dupont", "Jean", 1000)
compte2 = CompteBancaire(2,"Durand","Alice", -500, decouvert=True)

compte1.afficher()
compte2.afficher()

compte1.afficher_solde()   
compte2.afficher_solde()  

compte1.versement(500)
compte1.retrait(200)

compte2.agios(0.05)

compte1.versement(300)
compte2.afficher()

compte1.afficher_solde()
compte2.afficher_solde()
