import sys, pygame
from pygame.locals import*
import time

width = 1000
height = 500
screen_color = (0, 0, 0)
line_color = (255, 0, 0)

def DISPLAY(path:list):
    screen=pygame.display.set_mode((width,height))
    screen.fill(screen_color)
    while True:
        for events in pygame.event.get():
            for i in range(2):
                pygame.draw.line(screen,line_color, path[i],path[i+1],1)
                time.sleep(0.5)
                pygame.display.flip()
                if events.type == QUIT:
                    sys.exit(0)
#DISPLAY(path)
