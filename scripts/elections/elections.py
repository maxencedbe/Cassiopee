import pandas as pd

df2 = pd.read_excel("data/elections/resultats-par-niveau-subcom-t1-france-entiere.xlsx")

df_sorted = df2.sort_values(by="Inscrits", ascending=True)

df_top10 = df_sorted.head(10)

colonnes_afficher = [
    "Code du département",
    "Libellé du département",
    "Code de la commune",
    "Libellé de la commune",
    "Inscrits"
]

print(df_top10[colonnes_afficher])

df_top10.to_excel("results/elections/10_communes_moins_inscrits.xlsx", index=False)