import pygame
import numpy as np
import sys
import time

pygame.init()

bg = (25, 25, 25)
width, height = 500, 500

screen = pygame.display.set_mode((height, width))
screen.fill(bg)

cells = 50
nxC, nyC = cells, cells

dimCW = width / nxC
dimCH = height / nyC


gameState = np.zeros((nxC, nyC))

#Automata palo
gameState[5,3] = 1
gameState[5,4] = 1
gameState[5,5] = 1


#Automata Movil
gameState[21,21] = 1
gameState[22,22] = 1
gameState[22,23] = 1
gameState[21,23] = 1
gameState[20,23] = 1

#Weird thing
gameState[10,10] = 1
gameState[11,11] = 1
gameState[12,12] = 1
gameState[13,13] = 1
gameState[14,14] = 1
gameState[15,15] = 1
gameState[14,13] = 1
gameState[17,13] = 1
gameState[13,17] = 1

pauseExect = False


while True:

    newGameState = np.copy(gameState)

    screen.fill(bg)
    #time.sleep(0.1)

    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif evt.type == pygame.KEYDOWN:
            pauseExect = not pauseExect

        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = 1
    


    for y in range(0, nxC):
        for x in range(0, nyC):

            if not pauseExect:

                n_neigh =   gameState[(x-1) % nxC, (y-1)    % nyC] + \
                            gameState[(x)   % nxC, (y-1)    % nyC] + \
                            gameState[(x+1) % nxC, (y-1)    % nyC] + \
                            gameState[(x-1) % nxC, (y)      % nyC] + \
                            gameState[(x+1) % nxC, (y)      % nyC] + \
                            gameState[(x-1) % nxC, (y+1)    % nyC] + \
                            gameState[(x)   % nxC, (y+1)    % nyC] + \
                            gameState[(x+1) % nxC, (y+1)    % nyC]
                

                #Rule 1:
                if gameState[x,y] == 0 and n_neigh == 3:
                    newGameState[x,y] = 1
                
                #Rule 2
                elif gameState[x,y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x,y] = 0




                poly = [((x)    * dimCW, y      * dimCH),
                        ((x+1)  * dimCW, y      * dimCH), 
                        ((x+1)  * dimCW, (y+1)  * dimCH), 
                        ((x)    * dimCW, (y+1)  * dimCH)]


                if newGameState[x,y] == 0:
                    pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
                else:
                    pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    gameState = np.copy(newGameState)

    pygame.display.flip()
    




