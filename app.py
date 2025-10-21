# app.py
from models.user import User
from models.expense import Expense
from models.group import Group

def main():
    print("--------------------Gestionnaire de dépenses partagé--------------------")
    print("Bienvenue dans votre application de partage de dépenses 💶\n")

    group_name = input("Entrez le nom du groupe : ")
    group = Group(group_name)

    print(f" Groupe '{group.name}' créé avec succès !\n")

    # Dictionnaire pour retrouver facilement les utilisateurs par nom
    users = {}

    while True:
        print("\n--- MENU ---")
        print("1️⃣ Ajouter un utilisateur")
        print("2️⃣ Ajouter une dépense")
        print("3️⃣ Afficher les dépenses")
        print("4️⃣ Afficher les soldes")
        print("5️⃣ Quitter")

        choice = input(" Votre choix : ").strip()

        # Ajouter un utilisateur
        if choice == "1":
            name = input("Nom du participant : ").strip().lower()
            if name in users:
                print(f" {name} existe déjà.")
            else:
                user = User(name)
                users[name] = user
                group.add_user(user)

        # Ajouter une dépense
        elif choice == "2":
            if not users:
                print("Aucun utilisateur. Ajoutez d'abord des participants.")
                continue

            payer_name = input("Qui a payé ? : ").strip().lower()
            if payer_name not in users:
                print(f" {payer_name} n'existe pas.")
                continue

            try:
                amount = float(input("Montant de la dépense (€) : "))
            except ValueError:
                print(" Montant invalide.")
                continue

            print("Participants (séparez les noms par des virgules) :")
            print(", ".join(users.keys()))
            participants_names = input(" Entrez les noms : ").split(",")
            participants = []

            for name in participants_names:
                name = name.strip().lower()
                if name in users:
                    participants.append(users[name])
                else:
                    print(f" {name} n'existe pas et sera ignoré.")

            if not participants:
                print(" Aucun participant valide.")
                continue

            expense = Expense(users[payer_name], amount, participants)
            group.add_expense(expense)

        # Afficher les dépenses
        elif choice == "3":
            group.show_summary()

        # Afficher les soldes
        elif choice == "4":
            group.show_balances()

        # Quitter
        elif choice == "5":
            print(" À bientôt !")
            break

        else:
            print(" Choix invalide. Essayez encore.")

if __name__ == "__main__":
    main()
