class noeud:
    def __init__(self, valeur, enfants):
        
        self.valeur = valeur 
        self.enfants = []
        self.enfants.append(enfants)

    def ajouter_enfant(self, enfants):
        
        self.enfants.append(enfants)

    def affichage(self):
       # if isinstance (str, self.valeur):
        #    if isinstance (int, self.enfants):
         #       print(self.valeur,"(",self.enfants,")")
        print (self.valeur,end="")
        print (self.enfants)

    
n_1 = noeud("exp",0)

print("\n")
n_1.ajouter_enfant(3)
n_1.affichage()
print("\n")
