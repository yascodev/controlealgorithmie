# Représentation d'une grille de Sudoku 9x9
# 0 représente une case vide
GRILLE = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

def est_valide(grille, ligne, col, num):
    """Vérifie si un numéro peut être placé dans une position donnée."""
    # Vérifier la ligne
    for x in range(4):
        if grille[ligne][x] == num:
            return False

    # Vérifier la colonne
    for x in range(4):
        if grille[x][col] == num:
            return False

    # Vérifier le carré 2x2
    start_ligne = ligne - ligne % 2
    start_col = col - col % 2
    for i in range(2):
        for j in range(2):
            if grille[i + start_ligne][j + start_col] == num:
                return False
    return True

def resoudre_sudoku(grille):
    """Résout le Sudoku en utilisant la méthode de backtracking."""
    for ligne in range(4):
        for col in range(4):
            if grille[ligne][col] == 0:  # Trouver une case vide
                for num in range(1, 5):  # Essayer les numéros de 1 à 4
                    if est_valide(grille, ligne, col, num):
                        grille[ligne][col] = num  # Placer le numéro
                        if resoudre_sudoku(grille):
                            return True
                        grille[ligne][col] = 0  # Réinitialiser (backtrack)
                return False  # Aucun numéro valide trouvé, revenir en arrière
    return True  # Sudoku résolu