import pygame
import os
import sys

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def button(text, x, y, width, height, txtSize, inColor, activateColor, action=None, param=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
##    print(click)
    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        smallText = pygame.font.SysFont(None,txtSize)
        textSurf, textRect = text_objects(text, smallText, WHITE)
        textRect.center = ( (x+(width/2)), (y+(height/2)) )
        if click[0] == 1 and action != None:
            if param == None:
                action()
            else:
                action(param)
##            print("You are clicking")
    else:
        smallText = pygame.font.SysFont(None,txtSize)
        textSurf, textRect = text_objects(text, smallText, GREY)
        textRect.center = ( (x+(width/2)), (y+(height/2)) )
    screen.blit(textSurf, textRect)

def switchScreen(screen):
    currentScene = screen
    #Information screen
    if (screen == 2):
        
    
    
pygame.init()

resX = 1150
resY = 750

#Commonly used colors
WHITE = (255,255,255)
GREY = (100, 100, 100)
BLACK = (0,0,0)

#Fonts
###Menu Font###
mMenuSize = 150
mMenu_font = pygame.font.Font(None, mMenuSize)
    
screen = pygame.display.set_mode((resX,resY))

#Window border stuff
logo = pygame.image.load(".\\art\\pixel\\logo32x32.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("Chicken: The Threequel")

#Other image loading
##testImg = pygame.image.load(".\\art\\pixel\\pain.png")

#Blits
##screen.blit(testImg,(50,50))
 

#Display stuff
pygame.display.flip()

#"First Run" stuff
currentScene = 1

running = True
try: #Using a try statement so the window actually closes
    while running:
        ##Main active here##
        
        #Menu Scene
        pygame.event.pump()
        screen.fill(BLACK)
        if currentScene == 1:
            button("Start",150,100,250,250,150,(100,100,100),(50,50,50),switchScreen,2)

        
        pygame.display.update()
        #Closing the box
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
#Actually closes the window
except SystemExit:
    pygame.quit()
