class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, titre, auteur):
        livre = {"titre": titre, "auteur": auteur, "emprunté": False}
        self.livres.append(livre)

    def rechercher_livre(self, titre):
        for livre in self.livres:
            if livre["titre"].lower() == titre.lower():
                return livre
        return None

    def emprunter_livre(self, titre):
        livre = self.rechercher_livre(titre)
        if livre is None:
            raise ValueError("Le livre n'existe pas.")
        if livre["emprunté"]:
            raise ValueError("Le livre est déjà emprunté.")
        livre["emprunté"] = True

    def retourner_livre(self, titre):
        livre = self.rechercher_livre(titre)
        if livre is None:
            raise ValueError("Le livre n'existe pas.")
        if not livre["emprunté"]:
            raise ValueError("Le livre n'est pas emprunté.")
        livre["emprunté"] = False
