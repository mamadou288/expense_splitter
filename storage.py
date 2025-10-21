import json

def save_data(group):
    data = {
        "group": group.name,
        "users": [{"name": u.name, "balance": u.balance} for u in group.members],
        "expenses": [
            {
                "payer": e.payer.name,
                "amount": e.amount,
                "participants": [p.name for p in e.participants]
            }
            for e in group.expenses
        ]
    }
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(" Données sauvegardées avec succès !")


def load_data(group):
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("⚠️ Aucune donnée trouvée, démarrage d’un nouveau groupe.")
        return group

    print(f"{data['group']}")
    from models.user import User
    from models.expense import Expense

    # Recréer les utilisateurs
    users = {u["name"]: User(u["name"]) for u in data["users"]}
    for u_data in data["users"]:
        users[u_data["name"]].balance = u_data["balance"]

    # Recréer les dépenses
    for e in data["expenses"]:
        payer = users[e["payer"]]
        participants = [users[name] for name in e["participants"]]
        expense = Expense(payer, e["amount"], participants)
        group.add_expense(expense)

    # Ajouter les utilisateurs recréés
    for u in users.values():
        group.add_user(u)

    return group
