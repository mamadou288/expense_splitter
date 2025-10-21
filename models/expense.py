from models.user import User

class Expense:
    """
    Représente une dépense effectuée dans un groupe.
    Un Expense est composé de :
    - un payeur (payer)
    - un montant total (amount)
    - une liste de participants (participants)
    """

    def __init__(self, payer: User, amount: float, participants: list[User]):
        """
        Initialise la dépense.
        Composition : l'Expense contient des objets User.
        """
        self.payer = payer
        self.amount = amount
        self.participants = participants

    def split(self):
        """
        Calcule la part de chaque participant et met à jour les soldes.
        """
        share = self.amount / len(self.participants)

        # Chaque participant doit payer sa part
        for user in self.participants:
            user.update_balance(-share)

        # Le payeur récupère la totalité qu’il a avancée
        self.payer.update_balance(self.amount)

        print(f" Dépense enregistrée : {self.payer.name} a payé {self.amount}€ pour {len(self.participants)} personnes.")
        print(f"Chaque participant doit {share:.2f}€")

    def __str__(self):
        """
        Retourne une représentation lisible de la dépense.
        Exemple : "Alice a payé 60.0€ pour Alice, Bob, Charlie"
        """
        participant_names = ", ".join([p.name for p in self.participants])
        return f"{self.payer.name} a payé {self.amount:.2f}€ pour {participant_names}"
