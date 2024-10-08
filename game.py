import pygame
import random

# Dimensions de la fenêtre
WIDTH = 550
background_color = (251, 247, 245)
size = 10
default_number_color = (0, 0, 128)  # Bleu foncé pour les chiffres par défaut
input_number_color = (0, 0, 0)  # Noir pour les chiffres insérés par l'utilisateur

def create_grid(size, win):
    """
    Crée et dessine la grille de Sudoku sur la fenêtre.

    Args:
        size (int): Taille de la grille (doit être 9 pour un Sudoku standard).
        win (pygame.Surface): La fenêtre Pygame où dessiner la grille.
    """
    for i in range(size):
        if i % 3 == 0:
            pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)
        pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
    pygame.display.update()

def is_in_block(grid, i, j, number):
    """
    Vérifie si un nombre est déjà présent dans le bloc 3x3 correspondant.

    Args:
        grid (list): La grille de Sudoku.
        i (int): L'indice de la ligne.
        j (int): L'indice de la colonne.
        number (int): Le nombre à vérifier.

    Returns:
        bool: True si le nombre est dans le bloc, False sinon.
    """
    start_row = (i // 3) * 3
    start_col = (j // 3) * 3
    
    for row in range(start_row, start_row + 3):
        for col in range(start_col, start_col + 3):
            if grid[row][col] == number:
                return True
    return False

def can_place(grid, row, col, num):
    """
    Vérifie si un numéro peut être placé à une position donnée dans la grille.

    Args:
        grid (list): La grille de Sudoku.
        row (int): L'indice de la ligne.
        col (int): L'indice de la colonne.
        num (int): Le numéro à vérifier.

    Returns:
        bool: True si le numéro peut être placé, False sinon.
    """
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    if is_in_block(grid, row, col, num):
        return False
    return True

def solve(grid):
    """
    Résout la grille de Sudoku en utilisant la récursion et la technique de backtracking.

    Args:
        grid (list): La grille de Sudoku à résoudre.

    Returns:
        bool: True si la grille a été résolue, False sinon.
    """
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for num in range(1, 10):
                    if can_place(grid, i, j, num):
                        grid[i][j] = num
                        if solve(grid):
                            return True
                        grid[i][j] = 0  # Backtrack
                return False
    return True

def generate_complete_grid():
    """
    Génère une grille de Sudoku complète et valide.

    Returns:
        list: Une grille de Sudoku remplie de manière valide.
    """
    grid = [[0 for _ in range(9)] for _ in range(9)]
    numbers = list(range(1, 10))
    
    for i in range(9):
        for j in range(9):
            random.shuffle(numbers)  # Mélanger les numéros
            for num in numbers:
                if can_place(grid, i, j, num):
                    grid[i][j] = num
                    if solve(grid):
                        break
            if grid[i][j] == 0:  # Si on ne peut rien placer, recommencer
                return generate_complete_grid()
    return grid

def remove_numbers(grid, num_to_remove):
    """
    Supprime un certain nombre de numéros aléatoirement de la grille.

    Args:
        grid (list): La grille de Sudoku complète.
        num_to_remove (int): Le nombre de numéros à supprimer.

    Returns:
        list: La grille de Sudoku avec les numéros supprimés.
    """
    count = num_to_remove
    while count > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if grid[row][col] != 0:
            grid[row][col] = 0
            count -= 1
    return grid

def generate_sudoku(num_to_remove):
    """
    Génère une grille de Sudoku avec un certain nombre de numéros retirés.

    Args:
        num_to_remove (int): Le nombre de numéros à retirer.

    Returns:
        list: La grille de Sudoku générée.
    """
    complete_grid = generate_complete_grid()
    return remove_numbers(complete_grid, num_to_remove)

def draw_number(win, pos, number, color):
    """
    Dessine un numéro à une position donnée dans la fenêtre.

    Args:
        win (pygame.Surface): La fenêtre Pygame où dessiner le numéro.
        pos (tuple): La position (colonne, ligne) où dessiner le numéro.
        number (int): Le numéro à dessiner.
        color (tuple): La couleur du numéro.
    """
    font = pygame.font.Font(None, 40)  # Taille de police
    text = font.render(str(number), True, color)

    # Correction de la position pour centrer le texte dans la case
    x = 50 + 50 * pos[0] + 25 - text.get_width() // 2  # x basé sur la colonne
    y = 50 + 50 * pos[1] + 25 - text.get_height() // 2  # y basé sur la ligne
    win.blit(text, (x, y))

def insert(win, position, grid, blocked_cells):
    """
    Insère un numéro à une position donnée dans la grille si la case n'est pas bloquée.

    Args:
        win (pygame.Surface): La fenêtre Pygame où dessiner le numéro.
        position (tuple): La position (ligne, colonne) où insérer le numéro.
        grid (list): La grille de Sudoku.
        blocked_cells (list): Les cellules bloquées qui ne peuvent pas être modifiées.
    """
    i, j = position[1], position[0]
    
    # Vérifie si la case sélectionnée est occupée par un nombre
    if (i, j) in blocked_cells:  # Vérifie si la case est bloquée
        return  # Si la case est bloquée, ne rien faire

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                # Si une touche de nombre est pressée, insère-la dans la grille
                if pygame.K_1 <= event.key <= pygame.K_9:
                    number = event.key - pygame.K_0
                    
                    # Effacer l'ancien chiffre s'il y en a un
                    if grid[i][j] != 0:  # Vérifie si un chiffre est déjà présent
                        # Effacer le chiffre par un rectangle de fond de 42x42 px
                        pygame.draw.rect(win, background_color, (50 + 50 * j + 4, 50 + 50 * i + 4, 42, 42))  # Rectangle de 42x42 px

                    # Insérer le nouveau chiffre
                    grid[i][j] = number
                    draw_number(win, (j, i), number, input_number_color)  # Ajouter le nouveau chiffre

                    pygame.display.update()
                    if check_win(grid):  # Vérifie si le joueur a gagné
                        show_victory_message(win)  # Affiche le message de victoire
                    return

def check_win(grid):
    """
    Vérifie si le joueur a gagné en remplissant correctement la grille.

    Args:
        grid (list): La grille de Sudoku à vérifier.

    Returns:
        bool: True si le joueur a gagné, False sinon.
    """
    # Vérifie si la grille est complètement remplie
    for row in grid:
        if 0 in row:
            return False  # Si une case est vide, retourner faux
    
    # Vérifie chaque ligne
    for i in range(9):
        if len(set(grid[i])) != 9:  # Tous les chiffres de 1 à 9 doivent être présents
            return False

    # Vérifie chaque colonne
    for j in range(9):
        if len(set(grid[i][j] for i in range(9))) != 9:  # Tous les chiffres de 1 à 9 doivent être présents
            return False

    return True  # Tout est correct, le joueur a gagné

def show_victory_message(win):
    """
    Affiche un message de victoire sur la fenêtre.

    Args:
        win (pygame.Surface): La fenêtre Pygame où afficher le message.
    """
    win.fill((255, 255, 255))  # Remplit la fenêtre avec du blanc pour le fond
    font = pygame.font.Font(None, 60)  # Taille de police pour le message
    text = font.render("Vous avez gagné!", True, (0, 0, 0))  # Noir pour le message
    text_rect = text.get_rect(center=(WIDTH // 2, WIDTH // 2))
    win.blit(text, text_rect)
    pygame.display.update()
    
    # Attendre un moment avant de relancer une nouvelle partie
    pygame.time.delay(3000)  # Afficher pendant 3 secondes
    main()  # Relance la fonction principale pour recommencer le jeu

def main():
    """
    Fonction principale qui initialise Pygame, crée la fenêtre, génère la grille de Sudoku,
    et gère les événements de jeu.
    """
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Sudoku")
    win.fill(background_color)

    create_grid(size, win)
    grid = generate_sudoku(num_to_remove=40)  # Générez une grille de Sudoku avec 40 numéros retirés
    blocked_cells = [(i, j) for i in range(9) for j in range(9) if grid[i][j] != 0]

    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                draw_number(win, (j, i), grid[i][j], default_number_color)  # Dessiner les numéros par défaut

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                # Obtenir la position de la grille en fonction du clic de la souris (compte tenu de l'offset de 50px)
                grid_pos = (pos[0] // 50 - 1, pos[1] // 50 - 1)
                
                # S'assurer que le clic est à l'intérieur des limites de la grille
                if 0 <= grid_pos[0] < 9 and 0 <= grid_pos[1] < 9:
                    insert(win, grid_pos, grid, blocked_cells)  # Passer les cases bloquées

main()