import pygame
import numpy
import sys

pygame.init()

bg = (25, 25, 25)
width, height = 500, 500

screen = pygame.display.set_mode((height, width))
screen.fill(bg)

nxC, nyC = 25, 25

dimCW = width / nxC
dimCH = height / nyC


gameState = np.zeros((nxC, nyC))


while True:

    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for y in range(0, nxC):
        for x in range(0, nyC):

            poly = [((x)    * dimCW, y      * dimCH),
                    ((x+1)  * dimCW, y      * dimCH), 
                    ((x+1)  * dimCW, (y+1)  * dimCH), 
                    ((x)    * dimCW, (y+1)  * dimCH)]

            pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            

    pygame.display.flip()




