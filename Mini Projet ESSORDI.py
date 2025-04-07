import pandas as pd
df = pd.read_csv("student_depression_dataset.csv")

print(df.head())

print(df.info())

print(df.describe(include='all'))

print(df.isnull().sum())

missing_values = df.isnull().sum()
print("Valeurs manquantes par colonne :\n", missing_values)

df = df.drop_duplicates()
df["Gender"] = df["Gender"].str.strip()
df["Profession"] = df["Profession"].str.strip()

def depression_level(x):
    return "Dépressif" if x == 1 else "Non-dépressif"

df["Depression_Level"] = df["Depression"].apply(depression_level)

df_selected = df[["Gender", "Age", "Academic Pressure", "Sleep Duration", "CGPA", "Depression_Level"]]
print(df_selected.head())

depressifs = df[df["Depression_Level"] == "Dépressif"]
print(depressifs.shape)  

def eval_sommeil(sleep):
    if "Less than 5 hours" in sleep or "5-6 hours" in sleep:
        return "Insuffisant"
    else:
        return "Normal"

df["Sleep_Quality"] = df["Sleep Duration"].apply(eval_sommeil)

cgpa_faible = df.sort_values("CGPA").head(10)
print(cgpa_faible[["CGPA", "Depression_Level"]])

cgpa_faible = df.sort_values("CGPA").head(10)
print(cgpa_faible[["CGPA", "Depression_Level"]])

print(df.groupby("Gender")["Depression_Level"].value_counts())

print(df.groupby("Depression_Level")["Academic Pressure"].mean())

stats = df[["Age", "Academic Pressure", "CGPA"]].describe()
print(stats)

correlation_matrix = df[["Academic Pressure", "CGPA", "Age", "Depression"]].corr()
print(correlation_matrix)

pressure_by_depression = df.groupby("Depression_Level")["Academic Pressure"].mean()
print(pressure_by_depression)

depression_by_gender = df.groupby("Gender")["Depression_Level"].value_counts()
print(depression_by_gender)

import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

df["Depression_Level"].value_counts().plot(kind="bar", color=["skyblue", "salmon"])
plt.title("Distribution des niveaux de dépression")
plt.xlabel("Niveau de dépression")
plt.ylabel("Nombre d'étudiants")
plt.show()

sns.boxplot(x="Depression_Level", y="Academic Pressure", data=df, palette="pastel")
plt.title("Pression académique selon la dépression")
plt.xlabel("Niveau de dépression")
plt.ylabel("Pression académique")
plt.show()

df["Sleep Duration"].value_counts().plot(kind="bar", color="lightgreen")
plt.title("Durée de sommeil des étudiants")
plt.xlabel("Durée de sommeil")
plt.ylabel("Nombre d'étudiants")
plt.xticks(rotation=45)
plt.show()

df["Gender"].value_counts().plot(kind="pie", autopct='%1.1f%%', startangle=90, colors=["#ff9999", "#66b3ff"])
plt.title("Répartition par genre")
plt.ylabel("")  
plt.show()

plt.figure(figsize=(8, 6))
sns.heatmap(df[["Depression", "Academic Pressure", "CGPA", "Age"]].corr(), annot=True, cmap="coolwarm")
plt.title("Matrice de corrélation")
plt.show()
