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
    else:
        smallText = pygame.font.SysFont(None,txtSize)
        textSurf, textRect = text_objects(text, smallText, GREY)
        textRect.center = ( (x+(width/2)), (y+(height/2)) )
    screen.blit(textSurf, textRect)

def switchScreen(scene):
    global currentScene
    currentScene = scene
    print("Scene changed to {}".format(scene))

##def startGame(): #(whereFrom): Trying to build to allow for later implementation of contuing game from main menu after already starting the game once
##    screen.fill((255,100,100))
    
    
    
pygame.init()    

resX = 1024 #Will eventually allow user input for these values and use these as defaults
resY = 576

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
 

#Display stuff
pygame.display.flip()

#"First Run" stuff
global currentScene
currentScene = 1
print("Setting initial scene to main menu")

running = True
try: #Using a try statement so the window actually closes
    while running:
        ##Main active here##
##        global currentScene # Using a global for now, will find a way to just pass it through... eventualy
        #Menu Scene
        pygame.event.pump()
        if currentScene == 1:
            screen.fill(BLACK)
            button("Start",150,100,250,250,150,(100,100,100),(50,50,50),switchScreen,2)
        if currentScene == 2:
            print("Change")
            screen.fill(BLACK)
            
            button("Start",150,100,250,250,150,(100,100,100),(50,50,50),switchScreen,3)
        pygame.display.update()
        #Closing the box
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
#Actually closes the window
except SystemExit:
    pygame.quit()
