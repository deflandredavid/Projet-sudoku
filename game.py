import pygame

WIDTH = 550
background_color = (251,247,245)
size = 10

def create_grid(size, win):
    for i in range(size):
        if(i%3 == 0):
            pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i, 500), 4)
            pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 4)
        pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i, 500), 2)
        pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 2)
    pygame.display.update()

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH,WIDTH))
    pygame.display.set_caption("Sudoku")
    win.fill(background_color)

    create_grid(size,win)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
main()