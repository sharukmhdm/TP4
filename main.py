import matplotlib.pyplot as plt
import networkx as nx
from Noeud import Noeud


def main():
    # Test de la classe Noeud
    racine = Noeud("A", 1)
    racine.ajouter_enfant(2)
    print("Test du nœud :")
    racine.affichage()

    # Test de networkx et matplotlib
    graphe = nx.Graph()
    graphe.add_edge("A", "B")
    graphe.add_edge("B", "C")

    print("\nGraphe networkx créé avec succès !")
    print(f"Noeuds du graphe : {list(graphe.nodes)}")


if __name__ == "__main__":
    main()