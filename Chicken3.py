import tkinter as tk
import os as os
#import csv
##end imports

#TODO: Replace globals with python-style variable use

#RGB to tkinter readable
def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

#Tk init
root = tk.Tk()
root.title("Chicken: The Threequel")
scrX = root.winfo_screenwidth()
scrY = root.winfo_screenheight()
resX = 0
resY = 0
scrAsp = float(scrX/scrY)
percentTakenUp = 0.85

if (scrAsp > 1.68 and scrAsp < 1.8): #Looking for 1.77
    resX = int(16 * (percentTakenUp*(scrX/16)))
    resY = int( 9 * (percentTakenUp*(scrY/ 9)))
elif (scrAsp > 1.58 and scrAsp < 1.70): #Looking for 1.6
    resX = int(16 * (percentTakenUp*(scrX/16)))
    resY = int(10 * (percentTakenUp*(scrY/10)))
else: #Resolution for peasents or people with weird tastes
    resX = 640
    resyY = 480
resXY = str(resX)+'x'+str(resY)
resMult = (resX*resY)
print("Screen x is {}".format(scrX))
print("Screen y is {}".format(scrY))
print("Res x is {}".format(resX))
print("Res y is {}".format(resY))
tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=1)
root.geometry(resXY)
root.iconbitmap(os.path.join(".","art","pixel","favicon.ico")) 

#Fonts
xWrapSideBuffer = 5
fullScreenWrap = resX - xWrapSideBuffer

menuSizeMedium = round(0.0000423*resMult)
menuBtnFont = ('default',menuSizeMedium)

menuSizeLarge = round(0.00006887*resMult)
menuTitleFont = ('default',menuSizeLarge)

infoFontLarge = round(0.000050862*resMult)
largeInfoFont = ('default',infoFontLarge)

campSizeMedium = round(0.0000454389574*resMult)
campButtonFont = ('default',campSizeMedium)

#Game vars
global gameClockHour
gameClockHour = 6
global gameClockMinute 
gameClockMinute = 0
global gameDays
gameDays = 0
global campCreated
campCreated = 0

#Game Functions
def makeInfoWindow(scenario):
        t = tk.Toplevel()
        t.wm_title("Info Wnidow")

def newFrame(background):
    retFrame = tk.Frame(root,bg=background)
    retFrame.grid(row=0,column=0, sticky="nsew")
    retFrame.grid_rowconfigure(0, weight = 1)
    retFrame.grid_columnconfigure(0, weight = 1)
    retFrame.grid()
    retFrame.tkraise()
    return retFrame

def addTime(time):
    global gameClockHour
    global gameClockMinute
    global gameDays
    gameClockMinute += time
    while (gameClockHour > 23 or gameClockMinute > 59):
        if((gameClockMinute - 60) <= 0): #If more than 60 minutes then add one hour
            gameClockHour += 1
            gameClockMinute %= 60
        if((gameClockHour - 24) <= 0): #If more than 23 hours then add one day
            gameDays += 1
            gameClockHour %= 24
    return


##Scene Functions

#Setting up the main game screen
def mainCamp(oldFrame):
    # oldFrame.grid_froget()

    #Color management based on time of day
    backgroundC = 'black'
    foregroundC = 'white'
    if(not (gameClockHour >= 6 and gameClockHour < 19)): # Do Daytime TODO: Change back from inverse
        backgroundC = 'dark turquoise'
        foregroundC = 'black'
    else: #Do Nightime
        backgroundC = 'black'
        foregroundC = 'white'
    global campCreated
    
    def siwtchScreen(screen):
        return

    campCreated = 1
    frame = newFrame(backgroundC)
    #Widget definitions
    butnFont = campButtonFont
    sceneTitle = tk.Label(
                        frame,
                        bg=backgroundC,
                        fg=foregroundC,
                        font=butnFont,
                        text="Main Camp"
                        )
    sleepBtn = tk.Button(
                        frame,
                        bg=backgroundC,
                        fg=foregroundC,
                        font=butnFont,
                        text="Sleep",
                        command=campSleep
                        )
    storageBtn = tk.Button(
                        frame,
                        bg=backgroundC,
                        fg=foregroundC,
                        font=butnFont,
                        text="Storage",
                        command=campStorage
                        )
    equipBtn = tk.Button(
                        frame,
                        bg=backgroundC,
                        fg=foregroundC,
                        font=butnFont,
                        text="Equipment",
                        command=campEquip
                        )
    manageBtn = tk.Button(
                        frame,
                        bg=backgroundC,
                        fg=foregroundC,
                        font=butnFont,
                        text="Manage",
                        command=campManage
                        )
    epxloreBtn = tk.Button(
                        frame,
                        bg=backgroundC,
                        fg=foregroundC,
                        font=butnFont,
                        text="Explore",
                        command=campExplore
                        )
    
    dayDisplay = tk.Label(
        frame,
        bg=backgroundC,
        fg=foregroundC,
        font=butnFont,
        text="Day {}".format(gameDays)
        )
    #Time
    if (gameClockMinute != 0):
        timeDisplay = tk.Label(
            frame,
            bg=backgroundC,
            fg=foregroundC,
            font=butnFont,
            text="Time: {}:{}".format(gameClockHour,gameClockMinute)
            )
    else:
        timeDisplay = tk.Label(
            frame,
            bg=backgroundC,
            fg=foregroundC,
            font=butnFont,
            text="Time: {}:{}0".format(gameClockHour,gameClockMinute)
            )
    #End time stuff
    campDefDisplay = tk.Label(
        frame,
        bg=backgroundC,
        fg=foregroundC,
        font=butnFont,
        text="Defence: {}".format("3")  #TODO: Implement camp defence
        )
    sizeDisplay = tk.Label(
        frame,
        bg=backgroundC,
        fg=foregroundC,
        font=butnFont,
        text="Size: {} members".format("3") #TODO: Implement camp size
        )
    moneyDisplay = tk.Label(
        frame,
        bg=backgroundC,
        fg=foregroundC,
        font=butnFont,
        text="Money: {} coins".format("3") #TODO: Implement money
        )

    #Formatting
    def placeBelow(lastButton):
        lastButton.update()
        spaceBelow = lastButton.winfo_y()
        spaceBelow += lastButton.winfo_height()
        spaceBelow += inbetweenSpace
        #print ("Placing {} pixels below".format(spaceBelow))
        return spaceBelow
        
    def findRightX(butn): #Get the x position of a widget wanted to allign to right y border
        xSpaceAmount = -5 #Move away from border this many pixels
        butn.place(x=resX/2)
        butn.update() #place and update so can get dimesnions
        return ((resX-butn.winfo_width())+xSpaceAmount)

    # def findLeftX(butn): #Get the x position of a widget wanted to allign to left y border
    #     xSpaceAmount = 5 #Move away from border this many pixels
    #     butn.place(x=resX/2)
    #     butn.update() #place and update so can get dimesnions
    #     return (butn.winfo_width()-xSpaceAmount)

    inbetweenSpace = 10


    sceneTitle.place(x=(resX/2)) #Place at middle of screen, top
    sceneTitle.update()
    sceneTitle.place(x=((resX/2)-(sceneTitle.winfo_width()/2)),y=0) #Have to double run so that I can get size and then place it based upon its size

    #Right side button placement
    sleepBtn.place(x=findRightX(sleepBtn),y=10+inbetweenSpace)
    storageBtn.place(x=findRightX(storageBtn),y=placeBelow(sleepBtn))
    equipBtn.place(x=findRightX(equipBtn),y=placeBelow(storageBtn))
    manageBtn.place(x=findRightX(manageBtn),y=placeBelow(equipBtn))
    epxloreBtn.place(x=findRightX(epxloreBtn),y=placeBelow(manageBtn))

    #Left side button placement
    leftXBuffer = 5
    dayDisplay.place(x=leftXBuffer,y=10+inbetweenSpace)
    timeDisplay.place(x=leftXBuffer,y=placeBelow(dayDisplay))
    campDefDisplay.place(x=leftXBuffer,y=placeBelow(timeDisplay))
    sizeDisplay.place(x=leftXBuffer,y=placeBelow(campDefDisplay))
    moneyDisplay.place(x=leftXBuffer,y=placeBelow(sizeDisplay))
    #TODO: finish the template

def campSleep():
    makeInfoWindow(1)
def campStorage():
    makeInfoWindow(2)
def campEquip():
    makeInfoWindow(3)
def campManage():
    makeInfoWindow(4)
def campExplore():
    makeInfoWindow(5)

#Setting up info screen
def startInfo(oldFrame):
    oldFrame.grid_forget()
    frame = newFrame('black')
    def switchScreen():
        mainCamp(frame)
    
    infoLabel = tk.Label(frame,bg='black',fg='white',font=largeInfoFont,wraplength=fullScreenWrap,text="This is a sample string to test sizing and new lines")
    startBtn = tk.Button(frame,command=switchScreen,fg='white',bg='gray50',text="Start",font=menuBtnFont,activebackground='gray36')
    #Grid stuff
    infoLabel.grid()
    startBtn.grid()

#Setting up intro screen
def startMenu():
    frame = newFrame('black')
    def switchScreen():
        startInfo(frame)


    #Buttons
    startGameBtn = tk.Button(frame, font=menuBtnFont, text="Start Game",command=switchScreen,bg='gray50',foreground='white smoke',activebackground='gray58',activeforeground='white smoke')
    
    #Lables / Titles
    mMenuTitle = tk.Label(frame, font=menuTitleFont, text ="Chicken: The Threequel", fg='white smoke',bg='black')

    #Grid formatting
    mMenuTitle.grid()
    startGameBtn.grid()

#Init stuff
startMenu()

#Start loop
root.mainloop()
