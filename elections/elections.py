import pandas as pd

# Charger le fichier Excel
df2 = pd.read_excel("elections/resultats-par-niveau-subcom-t1-france-entiere.xlsx")

# Trier par nombre d'inscrits (ordre croissant) sur tout le dataframe
df_sorted = df2.sort_values(by="Inscrits", ascending=True)

# Sélectionner les 10 communes avec le moins d'inscrits
df_top10 = df_sorted.head(10)

# Colonnes à afficher dans la console
colonnes_afficher = [
    "Code du département",
    "Libellé du département",
    "Code de la commune",
    "Libellé de la commune",
    "Inscrits"
]

# Affichage console
print(df_top10[colonnes_afficher])

# Sauvegarder dans un fichier Excel
df_top10.to_excel("elections/10_communes_moins_inscrits.xlsx", index=False)