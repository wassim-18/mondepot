import numpy as np

connexions = np.array([
    [12, 18, 22, 30, 28, 40, 65, 80, 95, 110, 130, 115, 100, 90, 85, 70, 60, 55, 48, 42, 35, 30, 25, 20],
    [10, 15, 20, 28, 32, 45, 60, 75, 85, 105, 125, 140, 110, 95, 88, 75, 65, 50, 45, 38, 32, 28, 22, 18],
    [8, 12, 16, 25, 30, 50, 70, 90, 120, 135, 150, 130, 100, 85, 80, 65, 55, 48, 40, 36, 30, 25, 20, 15],
    [11, 14, 19, 26, 34, 48, 72, 95, 105, 120, 145, 160, 125, 100, 92, 78, 62, 50, 43, 37, 30, 26, 21, 17],
    [9, 13, 18, 27, 35, 52, 75, 98, 108, 118, 138, 142, 112, 96, 89, 73, 60, 51, 44, 39, 33, 29, 24, 19],
    [7, 11, 17, 24, 33, 49, 68, 88, 104, 119, 133, 147, 120, 101, 91, 76, 64, 53, 46, 41, 36, 31, 27, 22],
    [6, 10, 15, 22, 31, 47, 66, 84, 102, 116, 129, 143, 118, 99, 87, 72, 61, 52, 47, 43, 38, 34, 30, 25]
])

jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

# Utilisation de where pour détecter les indices où les connexions > 100
indices = np.where(connexions > 100)
print(indices)
# Affichage des alertes
for i in range(len(indices[0])):
    jour = jours[indices[0][i]]
    heure = indices[1][i]
    nb_connexions = connexions[indices[0][i], indices[1][i]]
    print(f"⚠️ Alerte : possible attaque détectée le jour {jour} à {heure} h ({nb_connexions} connexions)")
