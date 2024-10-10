class Morpion:

    def __init__(self):
        self.__plateau = [["","",""],["","",""],["","",""]]
        self.__joueur = "X"

    def afficher(self):
        """Afficher le plateau."""
        for ligne in self.__plateau:
            print(f" {ligne[0]} | {ligne[1]} | {ligne[2]}")

    def jouer_coup(self):
        pass

    def verifie_victoire(self):
        pass

    def plateau_plein(self):
        pass

    def chager_joueur(self):
        pass

    def jouer(self):
        self.afficher()

if __name__ == "__main__":
    m = Morpion
    m.jouer()