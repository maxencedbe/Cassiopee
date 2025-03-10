import pandas as pd

df1 = pd.read_csv("table-adresses-reu.csv", sep=",")
df2 = pd.DataFrame(pd.read_excel("resultats-par-niveau-subcom-t1-france-entiere.xlsx")) 

# Trier les communes par le nombre d'inscrits (ordre croissant)
df2_sorted = df2.sort_values(by="Inscrits", ascending=True)

# Filtrer pour ne garder que les départements entre 1 et 11
departements_selectionnes = [str(i) for i in range(1, 12)]
df_filtre = df2[df2["Code du département"].isin(departements_selectionnes)]

# Trier par nombre d'inscrits (ordre croissant)
df_filtre_sorted = df_filtre.sort_values(by="Inscrits", ascending=True)

# Afficher les 10 communes avec le moins d'inscrits
colonnes_afficher = ["Code du département", "Libellé du département", "Code de la commune", "Libellé de la commune", "Inscrits"]
print(df_filtre_sorted[colonnes_afficher].head(10))


