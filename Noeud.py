
class Noeud:
    """Représente un nœud dans un arbre de calcul.

    Un nœud contient une valeur (opérateur, variable ou constante)
    ainsi qu'une liste de nœuds enfants.
    """

    def __init__(self, valeur, enfants):
        self.valeur = valeur
        self.enfants = []
        self.enfants.append(enfants)

    def ajouter_enfant(self, enfants):
        """Ajoute un enfant à la liste des enfants du nœud.

        Args:
            enfants: Le nœud enfant à ajouter.
        """
        self.enfants.append(enfants)

    def affichage(self):
        """Affiche la valeur du nœud et ses enfants."""
        print(self.valeur, end="")
        print(self.enfants)

    def evaluer(self):
        """Évalue l'expression représentée par le nœud.

        Returns:
            La valeur calculée de l'expression.
        """
        pass


dictionnaire = {}

n_1 = Noeud("exp", 0)

print("\n")
n_1.ajouter_enfant(3)
n_1.affichage()
print("\n")

'''SHARUKKKKK SALUT HIII'''