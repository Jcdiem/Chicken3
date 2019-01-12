import pygame
import os
import sys

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def button(text, x, y, width, height, txtSize, inColor, activateColor, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(screen, inColor,(x,y,width,height))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen, activateColor,(x,y,width,height))

    smallText = pygame.font.SysFont(None,txtSize)
    textSurf, textRect = text_objects(text, smallText)
    textRect.center = ( (x+(width/2)), (y+(height/2)) )
    screen.blit(textSurf, textRect)

def startGame():
    return
##class Button:
##
##    hovering = False
##    disabled = False
##
##    def __init__(self, text, pos, disabled):
##        self.text = text
##        self.pos = pos
##        self.set_rect()
##        self.draw()
##        self.disabled = False
##
##    def draw(self):
##        self.set_rend()
##        screen.blit(self.rend,self.rect)
##
##    def set_rend(self):
##        self.rend = (mMenu_font.render(self.text, True, self.get_color()))
##
##    def get_color(self):
##        if self.hovering and (not self.disabled):
##            return (255,255,255)
##        else:
##            return (100,100,100)
##
##    def set_rect(self):
##        self.set_rend()
##        self.rect = self.rend.get_rect()
##        self.rect.topleft = self.pos

pygame.init()

resX = 1150
resY = 750

#Commonly used colors
BLACK = (255,255,255)

#Fonts
###Menu Font###
mMenuSize = 150
mMenu_font = pygame.font.Font(None, mMenuSize)
    
screen = pygame.display.set_mode((resX,resY))

#Window border stuff
logo = pygame.image.load(".\\art\\pixel\\logo32x32.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("Chicken: The Threequel")

#Main Menu stuff
##mMenuButtons = [Button("Start",(25,mMenuSize+10),False),
##                Button("Load",(25,(mMenuSize*2)+10),True)]

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

##            #Initial run stuff
##            if initStart:
##                initStart = False
##                currentScene = 1
            
        #Main active here
        pygame.event.pump()
        screen.fill((0,0,0))
        if currentScene == 1:
            button("Start",150,100,250,250,150,(100,100,100),(50,50,50),startGame)

        
        pygame.display.update()
        #Closing the box
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
#Actually closes the window
except SystemExit:
    pygame.quit()
