# Import a library of functions called 'pygame'
import pygame
from random import *
import time
import math

def FT(x):
    result = 20*math.sin(x*0.1)
    return result

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
GARY  = (200, 200, 200)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

pygame.init()

screenWidth = 500
screenHeight = 500
size   = [screenWidth, screenHeight]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Title")

screen.fill(WHITE)


step = 50
stepX = step
stepY = step/5
myfont = pygame.font.SysFont('Comic Sans MS', (int)(step / 5))
centor = (screenWidth / 2) - 1
# abc = 1
for tempN in range(0, screenWidth):
    if tempN % step == step - 1:
        pygame.draw.line(screen, GARY, [tempN , 0], [tempN, screenHeight], 1)
        # pygame.draw.line(screen, GARY, [0 , tempN], [screenWidth, tempN], 1)
        
        textsurface = myfont.render(str((tempN - screenWidth / 2 + 1) / stepX), True, (0, 0, 0))
        screen.blit(textsurface, (tempN + 3, screenHeight / 2))

    if tempN % step == step - 1:
        # pygame.draw.line(screen, GARY, [tempN , 0], [tempN, screenHeight], 1)
        pygame.draw.line(screen, GARY, [0 , tempN], [screenWidth, tempN], 1)
        
        if tempN != centor:
            textsurface = myfont.render(str((screenHeight / 2 - tempN - 1) / stepY), True, (0, 0, 0))
            screen.blit(textsurface, (screenWidth / 2 + 3, tempN))

pygame.draw.line(screen, BLACK, [0, centor], [screenWidth, centor], 2)
pygame.draw.line(screen, BLACK, [centor, 0], [centor, screenHeight], 2)

myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('JHS', True, (0, 0, 0))
screen.blit(textsurface, (10, 0))

count = 0.01
for i in range(1, 10000):
    tempX = count
    tempY = math.log(tempX)
    tempX = tempY
    tempY = count
    # print(tempX, ", ", tempY)

    drawX = (tempX * stepX) + centor
    drawY = screenHeight - ((tempY * stepY) + centor)
    # print(drawX, ", ", drawY)

    pygame.draw.rect(screen, RED, [drawX, drawY, 1, 1])

    count += 0.01

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
start = time.time()  # 시작 시간 저장

while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    pygame.display.flip()

pygame.quit()
