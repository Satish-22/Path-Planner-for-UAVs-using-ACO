import pygame
from aco import ACO,Water_Graph,Grains_Graph,Pesticide_Graph
import time

width = 800
win = pygame.display.set_mode((width, width))
pygame.display.set_caption("drone")

green = (0, 255, 0)
blue = (173, 216, 230)
white = (255, 255, 255)
orange  = (255, 165 ,0)
yellow = (255, 255, 0)
grey  = (128, 128, 128)
water = (0, 0, 255)
black = (0,0,0)

class spots:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width + width//10
        self.y = col * width + width//10
        self.color = yellow
        self.width = (width*4)//5
        self.total_rows = total_rows
        self.elastic = True

    def reset(self):
        self.color = yellow
        
    def position(self):
        width=self.width
        x = self.x + width/2
        y = self.y + width/2
        return (x,y)
    
    def make_road(self,color):
        width=80
        self.x=self.row * width
        self.y=self.col * width
        self.color = color
        self.width = width
        self.elastic = False

    def req_pesticide(self):
        return self.color == white

    def req_grains(self):
        return self.color == orange

    def req_water(self):
        return self.color == blue

    def give_pesticide(self):
        self.color = white

    def give_grains(self):
        self.color = orange

    def give_water(self):
        self.color = blue
        
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))


def generate(grid):
    WG=Water_Graph(grid)
    GG=Grains_Graph(grid)
    PG=Pesticide_Graph(grid)
    return WG,GG,PG


def terain(rows,grid):
    for i in range(rows):
        spot = grid[i][7]
        spot.make_road(water)
    for i in range(rows):
        spot = grid[7][i]
        spot.make_road(grey)
    grid[7][1].make_road((255, 255, 252))
    grid[7][3].make_road((255, 165 ,2))
    grid[7][5].make_road((173, 216, 231))


def make_grid(rows, width):
    grid = []  
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = spots(i, j, gap, rows)
            grid[i].append(spot)
    terain(rows,grid)

    return grid

station = pygame.image.load("images/water.png")
pest = pygame.image.load("images/pest.png")
grain = pygame.image.load("images/grain.png")
def draw(win, grid, rows, width):
    win.fill(green)

    for row in grid:
        for spot in row:
            spot.draw(win)
    win.blit(station,(560,400))
    win.blit(pest,(560,80))
    win.blit(grain,(560,240))
    pygame.display.flip()
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def Get_INP(win, width):
    ROWS = 10
    grid = make_grid(ROWS, width)
    
    draw(win,grid,ROWS,width)
    
    require='o'
    
    run = True
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]: # LEFT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not spot.elastic:
                    continue
                if require == 'w' :
                    spot.give_water()
                if require == 'p' :
                    spot.give_pesticide()
                if require == 'g' :
                    spot.give_grains()

            elif pygame.mouse.get_pressed()[2]: # RIGHT  used for reset the spot
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not spot.elastic:
                    continue
                spot.reset()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return generate(grid)
                if event.key == pygame.K_UP:
                    require = 'w'
                if event.key == pygame.K_DOWN:
                    require = 'o'
                if event.key == pygame.K_RIGHT:
                    require = 'g'
                if event.key == pygame.K_LEFT:
                    require = 'p'

def DISPLAY(points,path,win,color):
    x_cor=[]
    y_cor=[]
    for i in range( len(path)):
        x_cor.append(points[path[i]][0])
        y_cor.append(points[path[i]][1])
    
    #print(x_cor)
    #print(y_cor)
    for i in range(len(path)-1):
        pygame.draw.line(win,color, (x_cor[i],y_cor[i]),(x_cor[i+1],y_cor[i+1]),5)
        #win.blit(station,(100,100))
        #pygame.display.flip()

        time.sleep(1)
        pygame.display.flip()



aco = ACO(10, 100, 1.0, 10.0, 0.5, 10, 2)
WG,GG,PG = Get_INP(win, width)

Wpath, Wcost = aco.solve(WG)
Gpath, Gcost = aco.solve(GG)
Ppath, Pcost = aco.solve(PG)

Wpath.append(0)
Gpath.append(0)
Ppath.append(0)

DISPLAY(WG.pts,Wpath,win,black)
DISPLAY(GG.pts,Gpath,win,black)
DISPLAY(PG.pts,Ppath,win,black)
run = True
while run:
    pass
