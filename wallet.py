class PorteFeuille:
    def __init__(self, couleur, marque,porteCearte,poids):
        self.couleur = couleur
        self.marque = marque
        self.poids = poids
        self.argent = 0
        self.porteCartes = []

    def getMoney(self):
        return self.argent

    def addMoney(self, montant):
        if montant > 0:
            self.argent += montant
        else:
            raise ValueError("Le montant doit être positif.")

    def checkMoney(self):
        return f"Il y a {self.argent} € dans le portefeuille."

    def addCard(self, porteCarte):
        self.portesCartes.append(porteCarte)

    def lost(self):
        self.argent = 0
        self.porteCartes = []
