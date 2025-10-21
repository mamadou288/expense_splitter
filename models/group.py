# group.py

from models.user import User
from models.expense import Expense

class Group:
    """
    Représente un groupe de participants et leurs dépenses partagées.
    Un groupe contient :
    - des utilisateurs (members)
    - des dépenses (expenses)
    """

    def __init__(self, name: str):
        """
        Initialise un nouveau groupe avec un nom.
        """
        self.name = name
        self.members: list[User] = []
        self.expenses: list[Expense] = []


    def add_user(self, user: User):
        """
        Ajoute un utilisateur au groupe (si non déjà présent).
        """
        if user not in self.members:
            self.members.append(user)
            print(f" {user.name} a été ajouté au groupe '{self.name}'.")
        else:
            print(f"ℹ {user.name} est déjà membre du groupe '{self.name}'.")


    def add_expense(self, expense: Expense):
        """
        Ajoute une dépense au groupe et met à jour les soldes automatiquement.
        """
        self.expenses.append(expense)
        expense.split()  # Mise à jour des balances des utilisateurs


    def show_summary(self):
        """
        Affiche toutes les dépenses enregistrées dans le groupe.
        """
        print(f"\n --- Dépenses du groupe '{self.name}' ---")
        if not self.expenses:
            print("Aucune dépense enregistrée pour le moment.")
        else:
            for expense in self.expenses:
                print(expense)

    def show_balances(self):
        """
        Affiche le solde de chaque membre du groupe.
        """
        print(f"\n --- Soldes actuels pour '{self.name}' ---")
        if not self.members:
            print("Aucun membre dans le groupe.")
        else:
            for user in self.members:
                print(user)
