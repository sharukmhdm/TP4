class Noeud:
    """Représente un nœud dans un arbre de calcul."""

    def __init__(self, valeur, enfants):
        self.valeur = valeur 
        self.enfants = []
        self.enfants.append(enfants)

    def ajouter_enfant(self, enfants):
        """Ajoute un enfant à la liste des enfants du nœud."""
        self.enfants.append(enfants)

    def affichage(self):
        """Affiche la valeur du nœud et la liste de ses enfants."""
        print(self.valeur, end="")
        print(self.enfants)

    def evaluer(self):
        """Évalue la valeur du nœud."""
        pass


dictionnaire = {}

n_1 = Noeud("exp", 0)

print("\n")
n_1.ajouter_enfant(3)
n_1.affichage()
print("\n")