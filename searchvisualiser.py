import pygame
import time
from dpingrid import depth_first_search
BLACK = (0,0,0)
WHITE = (250,250,250)
GREEN = (0,250,0)
RED = (250,0,0)
BLUE = (0,0,255)
PURPLE = (255,0,255)


MARGIN = 5.9
WIDTH = 20
HEIGHT = 20

rows = 23

grid = []
for row in range(rows):
    grid.append([])
    for column in range(rows):
        grid[row].append(0)

# starting and ending 
# path will be determined between these 2 points..
endx, endy = 0, 0
startr, startc = 3,2

grid[endx][endy] = 1
pygame.init()
WINDOW_SIZE = [600,600]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("ARRAY GRID ")
Clock = pygame.time.Clock()
Running = True

def depth_first(row, col):
    global rows, grid
    search_path = depth_first_search(row,col,rows,grid,1)
    return search_path

def draw():
    for row in range(rows):
        for col in range(rows):
            color = WHITE
            if startr == row and startc ==col:
                color = BLUE
            if grid[row][col] == 1:
                color = GREEN
            if grid[row][col] == 2:
                color = RED 
                if row == startr and col == startc:
                    color = PURPLE
            pygame.draw.rect(screen,color,[(MARGIN + WIDTH) * col + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
        

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
            pygame.quit()
    if Running:
        screen.fill(BLACK)
        draw()
        search = depth_first(startr,startc)
        # search.reverse()
        for block in search:
            if grid[block[0]][block[1]] == 0:
                grid[block[0]][block[1]] = 2
                time.sleep(0.01)
                break
        
        Clock.tick(60)
        pygame.display.flip()
pygame.quit()
