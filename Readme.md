# Gestionnaire de Dépenses Partagées

Une application Python simple pour **partager les dépenses entre amis** (voyage, colocation, sortie, etc.).  
Chaque dépense est enregistrée, partagée équitablement, et les soldes sont calculés automatiquement.

---

## Fonctionnalités

- Ajouter des participants  
- Enregistrer des dépenses  
- Calculer automatiquement qui doit combien  
- Sauvegarde automatique des données (fichier `data.json`)  
- Chargement automatique au redémarrage

---

## Structure du projet

expense_splitter/
│
├── app.py # Interface principale (menu interactif)
├── user.py # Classe User : nom et solde
├── expense.py # Classe Expense : partage des paiements
├── group.py # Classe Group : gestion du groupe et des dépenses
└── utils/
└── storage.py # Sauvegarde et chargement des données (JSON)

---

## Utilisation

1. Lance le programme :
   python app.py
2. Crée un groupe et ajoute des utilisateurs.
3. Ajoute des dépenses et consulte les soldes.


