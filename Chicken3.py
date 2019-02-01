import tkinter as tk
import os as os
#import csv


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
if (scrAsp > 1.68 and scrAsp < 1.8): #Looking for 1.77
    resX = int(16 * (0.75*(scrX/16)))
    resY = int( 9 * (0.75*(scrY/ 9)))
elif (scrAsp > 1.58 and scrAsp < 1.70): #Looking for 1.6
    resX = int(16 * (0.75*(scrX/16)))
    resY = int(10 * (0.75*(scrY/10)))
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
fullScreenWrap = round(0.001298868*resMult)

menuSizeMedium = round(0.0000423*resMult)
menuBtnFont = ('default',menuSizeMedium)

menuSizeLarge = round(0.00006887*resMult)
menuTitleFont = ('default',menuSizeLarge)

infoFontLarge = round(0.000050862*resMult)
largeInfoFont = ('default',infoFontLarge)

#Game vars
global gameClockHour
gameClockHour = 6
global gameClockMinute 
gameClockMinute = 0
global gameDays
gameDays = 0

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

    frame = newFrame(backgroundC)
    def siwtchScreen(screen):
        return
    #Widget definitions
    sceneTitle = tk.Label(
                        frame,
                        bg=backgroundC,
                        fg=foregroundC,
                        font=largeInfoFont,
                        text="Main Camp"
                        )
    sleepBtn = tk.Button(
                        frame,
                        bg=backgroundC,
                        fg=foregroundC,
                        font=largeInfoFont,
                        text="Sleep",
                        command=campSleep
                        )
    
    #Formatting
    sceneTitle.place(x=(resX/2)) #Place at middle of screen, top
    sceneTitle.update()
    sceneTitle.place(x=((resX/2)-(sceneTitle.winfo_width()/2)),y=0) #Have to double run so that I can get size and then place it based upon its size

    sleepBtn.place(x=resX/2)
    sleepBtn.update()
    sleepBtn.place(x=(resX-sleepBtn.winfo_width()),y=0)
#TODO: finish working on button placement

    
def campSleep():
    makeInfoWindow(1)


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
