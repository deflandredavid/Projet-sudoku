import pygame
import random

WIDTH = 550
background_color = (251,247,245)
size = 10
default_number_color = (0,0,128)

def create_grid(size, win):
    for i in range(size):
        if(i%3 == 0):
            pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i, 500), 4)
            pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 4)
        pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i, 500), 2)
        pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 2)
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

    for i in range(size_grid):
        for j in range(size_grid):
            a = random.randint(0,1)
            
            if a:
                a = random.randint(1, 9)
                
                if a not in grid[i] and all(a != grid[row][j] for row in range(size_grid)) and not is_in_block(grid, i, j, a):
                    grid[i][j] = a 
                    draw_number(win, (i, j), a)

    return grid

def draw_number(win,pos,number):
    font = pygame.font.Font(None, 30)
    text = font.render(str(number), True, default_number_color)
    text_rect = text.get_rect(topleft=(20 + 50 * (pos[0]+1), 20 + 50 * (pos[1]+1)))
    win.blit(text, text_rect)
            
def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH,WIDTH))
    pygame.display.set_caption("Sudoku")
    win.fill(background_color)

    create_grid(size,win)
    default_numbers(win)
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
main()