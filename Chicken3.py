import pygame
import os
import sys

# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((750,650))
    
    #Game logo
    logo = pygame.image.load(".\\art\\pixel\\logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    #Other image loading
    testImg = pygame.image.load(".\\art\\pixel\\pain.png")

    #Blits
    screen.blit(testImg,(50,50))
     

    #Display stuff
    pygame.display.flip()

    running = True
    #Using a try statement so the window actually closes
    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()
    except SystemExit:
        pygame.quit()
     
if __name__=="__main__":
    main()
