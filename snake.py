# pygame.transform module
# https://www.pygame.org/docs/ref/transform.html
#
# How to animate the position of an object or sprite in Pygame and move it towards predefined positions or along a defined path?
# https://stackoverflow.com/questions/74163435/how-to-animate-the-position-of-an-object-or-sprite-in-pygame-and-move-it-towards/74163522#74163522
#
# Is it possible to implement gradual movement of an object to given coordinates in Pygame?
# https://stackoverflow.com/questions/60356812/is-it-possible-to-implement-gradual-movement-of-an-object-to-given-coordinates-i/60356995#60356995
#
# How to make a circle move diagonally from corner to corner in pygame
# https://stackoverflow.com/questions/65814020/how-to-make-a-circle-move-diagonally-from-corner-to-corner-in-pygame/65814431#65814431
# 
# How to move the object in squared path repeatedly?
# https://stackoverflow.com/questions/71340195/how-to-move-the-object-in-squared-path-repeatedly/71340468#71340468
#
# GitHub - PyGameExamplesAndAnswers - Motion and movement - Move and rotate - Move in grid
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_movement_and_motion.md 


#import os
#os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

import pygame
import time

pygame.init()
station = pygame.image.load("s2.jpg")
background= pygame.image.load("land_1920x1080.jpg")
window = pygame.display.set_mode((0,0), 
                                 pygame.RESIZABLE)
#window = pygame.display.set_mode((400, 400))
#window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()

corner_points = [(100,100),(1630,450),(300, 300),(730,450),(280,450)]
#corner_points = [(100, 100), (300, 300), (300, 100), (100, 300)]
pos = corner_points[0]

speed = 2

def move(pos, speed, points):
    direction = pygame.math.Vector2(points[0]) - pos
    if direction.length() <= speed:
        pos = points[0]
        points.append(points[0])
        points.pop(0)
    else:
        direction.scale_to_length(speed)
        new_pos = pygame.math.Vector2(pos) + direction
        pos = (new_pos.x, new_pos.y) 
    return pos

image = pygame.image.load('ship.bmp').convert_alpha()

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pos = move(pos, speed, corner_points)
    time.sleep(1)
    image_rect = image.get_rect(center = pos)
           
    window.fill(0)
    #pygame.draw.lines(window, "red", True, corner_points) 
    window.blit(station,(1630,450))
    window.blit(station,(1170,450))
    window.blit(station,(730,450))
    window.blit(station,(280,450))

    window.blit(background,(0,0))
    window.blit(image, image_rect)
    pygame.display.update()

pygame.quit()
exit()
