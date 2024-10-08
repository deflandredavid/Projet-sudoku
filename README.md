# Projet-sudoku

Création d'un jeu de Sudoku avec Pygame.

## Table des Matières

- Introduction
- Fonctionnalités
- Installation
- Fonctions Principales
  - create_grid
  - is_in_block
  - can_place
  - solve
  - generate_complete_grid
  - remove_numbers
  - generate_sudoku
  - draw_number
  - insert
  - check_win
  - show_victory_message
- Comment Jouer
- Contributeurs
- Licence

## Introduction

Ce projet consiste à créer un jeu de Sudoku interactif en utilisant la bibliothèque Pygame. L'utilisateur peut jouer au Sudoku, insérer des chiffres dans les cellules de la grille et vérifier s'il a gagné.

## Fonctionnalités

- Génération automatique d'une grille de Sudoku valide.
- Possibilité d'insérer des chiffres dans les cellules.
- Vérification des conditions de victoire.
- Affichage d'un message de victoire sur un fond blanc.

## Installation

1. Clonez le dépôt :
git clone https://github.com/deflandredavid/Projet-sudoku.git cd Projet-sudoku

2. Assurez-vous d'avoir Pygame installé. Si ce n'est pas le cas, installez-le avec pip :
pip install pygame

3. Exécutez le script :
python sudoku.py

## Fonctions Principales

### create_grid(size, win)

Dessine la grille de Sudoku sur la fenêtre win en utilisant la taille spécifiée.

### is_in_block(grid, i, j, number)

Vérifie si un numéro donné (number) se trouve déjà dans le bloc 3x3 qui contient la position (i, j) dans la grille grid.

### can_place(grid, row, col, num)

Détermine si un numéro (num) peut être placé à la position (row, col) de la grille. Vérifie les lignes, les colonnes et le bloc 3x3 pour les conflits.

### solve(grid)

Résout la grille de Sudoku donnée. Utilise une approche de backtracking pour remplir les cellules vides.

### generate_complete_grid()

Génère une grille de Sudoku complète et valide. Utilise la fonction solve pour remplir la grille.

### remove_numbers(grid, num_to_remove)

Supprime un certain nombre de cellules de la grille pour créer un puzzle de Sudoku. La fonction garantit que le puzzle reste solvable.

### generate_sudoku(num_to_remove)

Génère une grille de Sudoku avec un certain nombre de cellules retirées, prête à être jouée.

### draw_number(win, pos, number, color)

Affiche un numéro (number) à une position donnée (pos) sur la fenêtre win en utilisant la couleur spécifiée (color).

### insert(win, position, grid, blocked_cells)

Insère un numéro dans la grille à la position spécifiée (position). Vérifie si la case est bloquée (c'est-à-dire si elle a été remplie par défaut) et met à jour l'affichage.

### check_win(grid)

Vérifie si le joueur a gagné en s'assurant que toutes les lignes et colonnes contiennent des chiffres de 1 à 9 sans répétition, et que toutes les cases sont remplies.

### show_victory_message(win)

Affiche un message de victoire sur fond blanc et relance une nouvelle partie après un délai.

## Comment Jouer

1. Exécutez le script pour lancer le jeu.
2. Cliquez sur une cellule pour la sélectionner.
3. Appuyez sur une touche de chiffre (1-9) pour insérer un numéro dans la cellule sélectionnée.
4. Le message "Vous avez gagné!" apparaîtra lorsque toutes les cellules seront correctement remplies.

## Contributeurs

- David Deflandre

## Licence

Ce projet est sous licence MIT. Pour plus de détails, consultez le fichier LICENSE.