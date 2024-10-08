import pygame
import random

WIDTH = 550
background_color = (251, 247, 245)
size = 10
default_number_color = (0, 0, 128)  # Bleu foncé pour les chiffres par défaut
input_number_color = (0, 0, 0)  # Noir pour les chiffres insérés par l'utilisateur

def create_grid(size, win):
    for i in range(size):
        if(i % 3 == 0):
            pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)
        pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
    pygame.display.update()

def is_in_block(grid, i, j, number):
    start_row = (i // 3) * 3
    start_col = (j // 3) * 3
    
    for row in range(start_row, start_row + 3):
        for col in range(start_col, start_col + 3):
            if grid[row][col] == number:
                return True
    return False

def default_numbers(win):
    size_grid = 9
    grid = [[0 for _ in range(size_grid)] for _ in range(size_grid)]
    blocked_cells = []  # Liste pour stocker les cases bloquées

    for i in range(size_grid):
        for j in range(size_grid):
            a = random.randint(0, 1)
            
            if a:
                a = random.randint(1, 9)
                
                if a not in grid[i] and all(a != grid[row][j] for row in range(size_grid)) and not is_in_block(grid, i, j, a):
                    grid[i][j] = a
                    draw_number(win, (j, i), a, default_number_color)
                    blocked_cells.append((i, j))  # Ajouter la case à la liste des cases bloquées

    return grid, blocked_cells  # Retourner la grille et les cases bloquées

def draw_number(win, pos, number, color):
    font = pygame.font.Font(None, 40)  # Taille de police
    text = font.render(str(number), True, color)

    # Correction de la position pour centrer le texte dans la case
    x = 50 + 50 * pos[0] + 25 - text.get_width() // 2  # x basé sur la colonne
    y = 50 + 50 * pos[1] + 25 - text.get_height() // 2  # y basé sur la ligne
    win.blit(text, (x, y))

def insert(win, position, grid, blocked_cells):
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
                    return

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Sudoku")
    win.fill(background_color)

    create_grid(size, win)
    grid, blocked_cells = default_numbers(win)  # Récupérer la grille et les cases bloquées
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