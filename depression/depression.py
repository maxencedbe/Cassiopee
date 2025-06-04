import pandas as pd
import webbrowser
import urllib.parse

file_path = "depression/Student Depression Dataset.csv"
df = pd.read_csv(file_path)

quasi_identifiants = ["Gender", "Age", "City", "Profession", "Degree"]

filtered_df = df[df["Have you ever had suicidal thoughts ?"] == "Yes"]

rare_combinations = filtered_df.groupby(quasi_identifiants).size().reset_index(name='count')
rare_combinations['risk_score'] = rare_combinations['count'].apply(lambda x: 1 / x)

unique_profiles = rare_combinations[rare_combinations['risk_score'] == 1.0]

# Création de la page HTML pour afficher les profils
html_content = """
<html>
<head>
    <meta charset="utf-8">
    <title>Profils à risque de ré-identification</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        tr:hover { background-color: #f5f5f5; }
        a { text-decoration: none; color: #337ab7; }
    </style>
</head>
<body>
    <h2>Profils uniques susceptibles d'être ré-identifiés</h2>
    <table>
        <tr>
            <th>Age</th>
            <th>City</th>
            <th>Profession</th>
            <th>Degree</th>
            <th>Gender</th>
            <th>Recherche Google</th>
        </tr>
"""

# Générer une ligne HTML pour chaque profil
for index, row in unique_profiles.iterrows():
    query = f"{row['Age']} ans {row['City']} {row['Profession']} {row['Degree']} {row['Gender']} LinkedIn"
    query_encoded = urllib.parse.quote(query)
    google_url = f"https://www.google.com/search?q={query_encoded}"
    
    html_content += f"""
        <tr>
            <td>{row['Age']}</td>
            <td>{row['City']}</td>
            <td>{row['Profession']}</td>
            <td>{row['Degree']}</td>
            <td>{row['Gender']}</td>
            <td><a href="{google_url}" target="_blank">Recherche</a></td>
        </tr>
    """

html_content += """
    </table>
</body>
</html>
"""

# Sauvegarder le fichier HTML
with open("depression/result.html", "w", encoding="utf-8") as f:
    f.write(html_content)

# Ouvrir la page HTML dans le navigateur
webbrowser.open("depression/result.html")

# Calculer la part des profils uniques dans la base filtrée
total_cases = len(filtered_df)
unique_cases = len(unique_profiles)

if total_cases > 0:
    proportion_unique = (unique_cases / total_cases) * 100
    print(f"Proportion de la base avec un score de risque de 1.0 : {proportion_unique:.2f}%")
