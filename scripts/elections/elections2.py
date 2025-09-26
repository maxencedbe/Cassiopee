import pandas as pd

df = pd.read_csv("data/elections/resultats-par-niveau-subcom-t1-france-entiere.csv", low_memory=False)

nom_idx = df.columns.get_loc('Nom')
gauche_candidats = {'MÉLENCHON', 'ARTHAUD', 'POUTOU', 'ROUSSEL'}

def top10_communes_candidats(candidats_cibles):
    voix_par_commune = {}
    noms_communes = {}

    for idx, row in df.iterrows():
        total_pourc = 0
        code_dep = row['Code du département']
        code_com = row['Code de la commune']
        nom_com = row["Libellé de la commune"]

        noms_communes[(code_dep, code_com)] = nom_com

        i = nom_idx
        while i < len(df.columns):
            cell = row.iloc[i]
            if isinstance(cell, str) and cell.upper() in candidats_cibles:
                pct_col_index = i + 3
                if pct_col_index < len(df.columns):
                    try:
                        pct_val = float(row.iloc[pct_col_index])
                        total_pourc += pct_val
                    except:
                        pass
                i += 4
            else:
                i += 1

        voix_par_commune.setdefault((code_dep, code_com), []).append(total_pourc)

    moyenne_par_commune = {commune: sum(vals)/len(vals) for commune, vals in voix_par_commune.items()}

    sorted_communes = sorted(moyenne_par_commune.items(), key=lambda x: x[1], reverse=True)
    top10 = sorted_communes[:10]

    return top10, noms_communes

def filtre_et_ajoute(df, top10, noms_communes, description_col):
    communes_top10 = [commune for commune, val in top10]
    communes_set = set(communes_top10)

    filtered_rows = []
    pourc_dict = dict(top10)

    for idx, row in df.iterrows():
        code_dep = row['Code du département']
        code_com = row['Code de la commune']
        if (code_dep, code_com) in communes_set:
            row[description_col] = pourc_dict[(code_dep, code_com)]
            filtered_rows.append(row)

    df_filtered = pd.DataFrame(filtered_rows)
    return df_filtered

top10_lpz, noms_communes = top10_communes_candidats({'LE PEN', 'ZEMMOUR'})
df_lepen_zemmour = filtre_et_ajoute(df, top10_lpz, noms_communes, '% Inference Le Pen + Zemmour')
df_lepen_zemmour.to_excel("results/elections/top10_communes_lepen_zemmour_lignes.xlsx", index=False)
print("Fichier Le Pen + Zemmour sauvegardé")

top10_macron, _ = top10_communes_candidats({'MACRON'})
df_macron = filtre_et_ajoute(df, top10_macron, noms_communes, '% Inference Macron')
df_macron.to_excel("results/elections/top10_communes_macron_lignes.xlsx", index=False)
print("Fichier Macron sauvegardé")

top10_gauche, _ = top10_communes_candidats(gauche_candidats)
df_gauche = filtre_et_ajoute(df, top10_gauche, noms_communes, '% Inference Gauche')
df_gauche.to_excel("results/elections/top10_communes_gauche_lignes.xlsx", index=False)
print("Fichier Gauche sauvegardé")