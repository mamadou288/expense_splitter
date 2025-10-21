class User:
    """
    Représente un participant dans le groupe de dépenses.
    Chaque utilisateur a :
    - un nom
    - un solde (positif = on lui doit, négatif = il doit)
    """
    def __init__(self, name):
        """
        Initialise un nouvel utilisateur avec un nom
        et un solde initial de 0.
        """
        self.name = name
        self.balance = 0.0

    def update_balance(self, amount):
        """
        Met à jour le solde de l'utilisateur.
        amount > 0  -> on lui doit de l'argent
        amount < 0  -> il doit de l'argent
        """
        self.balance += amount

    def __str__(self):
        """
        Retourne une représentation lisible de l'utilisateur.
        Exemple : "Alice : +20.00€"
        """
        sign = "+" if self.balance >= 0 else ""
        return f"{self.name} : {sign}{self.balance:.2f}€"