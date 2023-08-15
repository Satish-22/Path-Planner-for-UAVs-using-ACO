import operator
import time

import matplotlib.pyplot as plt
import sys, pygame
from pygame.locals import*
import time

width = 1000
height = 500
screen_color = (0, 0, 0)
line_color = (255, 0, 0)


def plot(points, path: list):
    x = []
    y = []
    for point in points:
        x.append(point[0])
        y.append(point[1])
    # noinspection PyUnusedLocal
    plt.plot(x, y, 'co')

    for _ in range(1, len(path)):
        i = path[_ - 1]
        j = path[_]
        # noinspection PyUnresolvedReferences
        #time.sleep(1)
        plt.arrow(x[i], y[i], x[j] - x[i], y[j] - y[i], color='r', length_includes_head=True)

    # noinspection PyTypeChecker
    plt.xlim(0, max(x) * 1.1)
    # noinspection PyTypeChecker
    plt.ylim(0, max(y) * 1.1)
    plt.show()


def DISPLAY(points,path:list):
    screen=pygame.display.set_mode((width,height))
    screen.fill(screen_color)
    x_cor=[]
    y_cor=[]
    for i in range( len(path)):
        x_cor.append(points[path[i]][0]/10)
        y_cor.append(points[path[i]][1]/10)
    
    print(x_cor)
    print(y_cor)
    while True:
        for events in pygame.event.get():
            for i in range(len(path)-1):
                pygame.draw.line(screen,line_color, (x_cor[i],y_cor[i]),(x_cor[i+1],y_cor[i+1]),1)
                time.sleep(0.5)
                pygame.display.flip()
                if events.type == QUIT:
                    sys.exit(0)