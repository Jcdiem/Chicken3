import tkinter as tk
import os as os

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
root.iconbitmap(os.path.join("art","pixel","favicon.ico")) 

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

def newFrame(background):
    retFrame = tk.Frame(root,bg=background)
    retFrame.grid(row=0,column=0, sticky="nsew")
    retFrame.grid_rowconfigure(0, weight = 1)
    retFrame.grid_columnconfigure(0, weight = 1)
    retFrame.grid()
    retFrame.tkraise()
    return retFrame

class Human: #TODO: Finish human framework
    def __init__(self,level,vt = 0,st = 0,ag = 0,it = 0,ac = 0):
        self.stats = [
            vt, #0: Vitality/Health
            st, #1: Strength/Phys Damage
            ag, #2: Agility/Speed
            it, #3: Intelligence/Construction?
            ac  #4: Arcane Sense/Magic
        ]
        self.level = level
        self.baseHealth = (10+round(self.stats[0]*2.5+(self.stats[2]*0.5))) #10 will be the relative base for leveling
        self.modBaseHealth = 0
        self.modHealth = 0

class StartMenu:
    def __init__(self,master):
        self.root = master
        self.frame = newFrame('black')
        # self.campFrame = newFrame('black')
        #Buttons
        self.startGameBtn = tk.Button(self.frame, font=menuBtnFont, text="Start Game", command=self.switchScreen, bg='gray50', fg='white smoke',activebackground='gray58',activeforeground='white smoke')
    
        #Lables / Titles
        self.mMenuTitle = tk.Label(self.frame, font=menuTitleFont, text ="Chicken: The Threequel", fg='white smoke',bg='black')

        #Grid formatting
        self.mMenuTitle.grid()
        self.startGameBtn.grid()
    def switchScreen(self):
        self.transitionFrame = newFrame('black')
        self.app = StartInfo(self.transitionFrame)

class StartInfo:
    def __init__(self, master):
        self.frame = newFrame('black')
        self.frame.tkraise()
        self.infoLabel = tk.Label(self.frame,bg='black',fg='white',font=largeInfoFont,wraplength=fullScreenWrap,text="\"When in doubt, nuke it out\" -Ghandi 2019 ")
        self.startBtn = tk.Button(self.frame,command=self.switchScreen,fg='white',bg='gray50',text="Start",font=menuBtnFont,activebackground='gray36')
        #Grid stuff
        self.infoLabel.grid()
        self.startBtn.grid()
    def switchScreen(self):
        self.app = MainCamp()

class MainCamp:
    def __init__(self):
        #Camp site information
        self.butnFont = campButtonFont
        self.currency = 0
        self.gameClockHourStr = ""
        self.gameClockMinuteStr = ""
        self.gameClockHour = 6
        self.gameClockMinute = 30
        self.gameDays = 0
        #Set the time of day frame color
        self.backgroundC = 'black'
        self.foregroundC = 'white'
        # if(not (self.gameClockHour >= 6 and self.gameClockHour < 19)): #Do Daytime #TODO: Implement time background
        #     self.backgroundC = 'dark turquoise'
        #     self.foregroundC = 'black'
        # else: #Do Nightime
        #     self.backgroundC = 'black'
        #     self.foregroundC = 'white'
        self.frameAry = [
            newFrame(self.backgroundC),   #0: Main screen
            newFrame(self.backgroundC)    #1: Locations screen

        ]
        self.bringToFront()
        
        #Right Side Buttons
        self.sceneTitle = tk.Label(
                            self. frameAry[0],
                            bg=self.backgroundC,
                            fg=self.foregroundC,
                            font=self.butnFont,
                            text="Main Camp"
                            )
        self.sleepBtn = tk.Button(
                            self.frameAry[0],
                            bg=self.backgroundC,
                            fg=self.foregroundC,
                            font=self.butnFont,
                            text="Sleep",
                            command=self.campSleep
                            )
        self.storageBtn = tk.Button(
                            self.frameAry[0],
                            bg=self.backgroundC,
                            fg=self.foregroundC,
                            font=self.butnFont,
                            text="Storage",
                            command=self.campStorage
                            )
        self.equipBtn = tk.Button(
                            self.frameAry[0],
                            bg=self.backgroundC,
                            fg=self.foregroundC,
                            font=self.butnFont,
                            text="Equipment",
                            command=self.campEquip
                            )
        self.manageBtn = tk.Button(
                            self.frameAry[0],
                            bg=self.backgroundC,
                            fg=self.foregroundC,
                            font=self.butnFont,
                            text="Manage",
                            command=self.campManage
                            )
        self.epxloreBtn = tk.Button(
                            self.frameAry[0],
                            bg=self.backgroundC,
                            fg=self.foregroundC,
                            font=self.butnFont,
                            text="Explore",
                            command=self.campExplore
                            )
        #Right Side Stuff
        self.dayDisplay = tk.Label(
            self.frameAry[0],
            bg=self.backgroundC,
            fg=self.foregroundC,
            font=self.butnFont,
            text="Day {}".format(self.gameDays)
            )
        #Time
        self.timeToString()
        self. timeDisplay = tk.Label(
            self.frameAry[0],
            bg=self.backgroundC,
            fg=self.foregroundC,
            font=self.butnFont,
            text="Time: {}:{}".format(self.gameClockHourStr,self.gameClockMinuteStr)
            )
        #End time stuff
        self.campDefDisplay = tk.Label(
            self.frameAry[0],
            bg=self.backgroundC,
            fg=self.foregroundC,
            font=self.butnFont,
            text="Defense: {}".format("3")  #TODO: Implement camp defense
            )
        self.sizeDisplay = tk.Label(
            self.frameAry[0],
            bg=self.backgroundC,
            fg=self.foregroundC,
            font=self.butnFont,
            text="Size: {} members".format("3") #TODO: Implement camp size
            )
        self.moneyDisplay = tk.Label(
            self.frameAry[0],
            bg=self.backgroundC,
            fg=self.foregroundC,
            font=self.butnFont,
            text="Money: {} coins".format(self.currency) #TODO: Implement money
            )

        #Placing Stuff
        self.inbetweenSpace = 10
        self.leftXBuffer = 5

        self.sceneTitle.place(x=(resX/2)) #Place at middle of screen, top
        self.sceneTitle.update()
        self.sceneTitle.place(x=((resX/2)-(self.sceneTitle.winfo_width()/2)),y=0)

        #Right side button placement
        self.sleepBtn.place(x=self.findRightX(self.sleepBtn),y=10+self.inbetweenSpace)
        self.storageBtn.place(x=self.findRightX(self.storageBtn),y=self.placeBelow(self.sleepBtn))
        self.equipBtn.place(x=self.findRightX(self.equipBtn),y=self.placeBelow(self.storageBtn))
        self.manageBtn.place(x=self.findRightX(self.manageBtn),y=self.placeBelow(self.equipBtn))
        self.epxloreBtn.place(x=self.findRightX(self.epxloreBtn),y=self.placeBelow(self.manageBtn))

        #Left side info placement
        self.dayDisplay.place(x=self.leftXBuffer,y=10+self.inbetweenSpace)
        self.timeDisplay.place(x=self.leftXBuffer,y=self.placeBelow(self.dayDisplay))
        self.campDefDisplay.place(x=self.leftXBuffer,y=self.placeBelow(self.timeDisplay))
        self.sizeDisplay.place(x=self.leftXBuffer,y=self.placeBelow(self.campDefDisplay))
        self.moneyDisplay.place(x=self.leftXBuffer,y=self.placeBelow(self.sizeDisplay))
        #TODO: finish the formatting for prettiness

    def timeToString(self):
        if self.gameClockHour == 0:
            self.gameClockHourStr = "00"
        elif self.gameClockHour < 10:
            self.gameClockHourStr = "0"+str(self.gameClockHour)
        else:  
            self.gameClockHourStr = str(self.gameClockHour)

        if self.gameClockMinute < 10:
            self.gameClockMinuteStr = str(self.gameClockMinute)+"0"
        else:   
            self.gameClockMinuteStr = str(self.gameClockMinute)
    def campSleep(self):
        self.addTime(360)
        # print("Slept, hour now {} and minute now {}".format(self.gameClockHourStr,self.gameClockMinuteStr))
        # self.timeDisplay.update()
        #TODO: Make it so a daynight cycle actually works
    def campStorage(self):
        print("OOF")
        #TODO: Make a storage screen
    def campEquip(self):
        print("OOF")
        #TODO: make an equipping system (framework) for players (first) and NPCs (second)
    def campManage(self):
        print("OOF")
        #TODO: Make a window for managing the camp
    def campExplore(self):
        self.addTime(90)
        #TODO: Make a window that has location information
    def bringToFront(self): #Return to camp
        self.frameAry[0].tkraise()
    def placeBelow(self,lastButton):
        lastButton.update()
        self.spaceBelow = lastButton.winfo_y()
        self.spaceBelow += lastButton.winfo_height()
        self.spaceBelow += self.inbetweenSpace
        #print ("Placing {} pixels below".format(spaceBelow))
        return self.spaceBelow       
    def findRightX(self,butn): #Get the x position of a widget wanted to allign to right y border
        self.xSpaceAmount = -5 #Move away from border this many pixels
        butn.place(x=resX/2)
        butn.update() #place and update so can get dimesnions
        return ((resX-butn.winfo_width())+self.xSpaceAmount)
    def addTime(self,time=0):
        self.gameClockMinute += time
        while (self.gameClockHour > 23 or self.gameClockMinute > 59):
            if((self.gameClockMinute - 60) >= 0): #If more than 60 minutes then add one hour
                self.gameClockHour += 1
                self.gameClockMinute -= 60
            if((self.gameClockHour - 24) >= 0): #If more than 23 hours then add one day
                self.gameDays += 1
                self.gameClockHour -= 24
        self.timeToString()
        self.timeDisplay.config(text="Time: {}:{}".format(self.gameClockHourStr,self.gameClockMinuteStr))
        self.dayDisplay.config(text="Day {}".format(self.gameDays))

    # def makeInfoWindow(self,scenario):
    #     print("oof")


def main():
    app = StartMenu(root)
    root.mainloop()

if __name__ == '__main__':
    main()
