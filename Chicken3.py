import tkinter as tk
import os
import char
import exploration as expl
import calcs as calc

#Tk init
root = tk.Tk()
root.title("Chicken: The Threequel")

scrX = root.winfo_screenwidth()
scrY = root.winfo_screenheight()
resX = 0
resY = 0
scrAsp = float(scrX/scrY)

percentTakenUp = 0.85
resX = calc.getResX(scrX,scrAsp,percentTakenUp)
resY = calc.getResY(scrY,scrAsp,percentTakenUp)
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



class StartMenu:
    def __init__(self,master):
        self.root = master
        self.frame = calc.newFrame(root,'black')
        # self.campFrame = newFrame('black')
        #Buttons
        self.startGameBtn = tk.Button(
            self.frame, 
            font=menuBtnFont,
            text="Start Game",
            command=self.switchScreen,
            bg='gray50',
            fg='white smoke',
            activebackground='gray58',
            activeforeground='white smoke'
        )
    
        #Lables / Titles
        self.mMenuTitle = tk.Label(
            self.frame,
            font=menuTitleFont,
            text ="Chicken: The Threequel", 
            fg='white smoke',bg='black'
        )

        #Grid formatting
        self.mMenuTitle.grid()
        self.startGameBtn.grid()
    def switchScreen(self):
        self.transitionFrame = calc.newFrame(root,'black')
        return StartInfo(self.transitionFrame)

class StartInfo:
    def __init__(self, master):
        self.frame = calc.newFrame(root,'black')
        self.frame.tkraise()
        self.infoLabel = tk.Label(self.frame,bg='black',fg='white',font=largeInfoFont,wraplength=fullScreenWrap,text="\"When in doubt, nuke it out\" -Ghandi 2019 ")
        self.startBtn = tk.Button(self.frame,command=self.switchScreen,fg='white',bg='gray50',text="Start",font=menuBtnFont,activebackground='gray36')
        #Grid stuff
        self.infoLabel.grid()
        self.startBtn.grid()
    def switchScreen(self):
        return MainCamp()

class MainCamp:
    def __init__(self): #Creation of camp
        #Camp site information
        self.butnFont = campButtonFont
        self.currency = 0
        self.campMembers = []
        self.Discovery = [
            0, #Destroyed town
            0, #Old Watchtower
            0  #Debug room
        ]
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
            calc.newFrame(root,self.backgroundC),   #0: Main screen
            calc.newFrame(root,self.backgroundC)    #1: Locations screen

        ]
        self.bringToFront()
        
        #Right Side Buttons
        sceneTitle = tk.Label(
                            self. frameAry[0],
                            bg=self.backgroundC,
                            fg=self.foregroundC,
                            font=self.butnFont,
                            text="Main Camp"
                            )
        sleepBtn = tk.Button(
                            self.frameAry[0],
                            bg=self.backgroundC,
                            fg=self.foregroundC,
                            font=self.butnFont,
                            text="Sleep",
                            command=self.campSleep
                            )
        storageBtn = tk.Button(
                            self.frameAry[0],
                            bg=self.backgroundC,
                            fg=self.foregroundC,
                            font=self.butnFont,
                            text="Storage",
                            command=self.campStorage
                            )
        equipBtn = tk.Button(
                            self.frameAry[0],
                            bg=self.backgroundC,
                            fg=self.foregroundC,
                            font=self.butnFont,
                            text="Equipment",
                            command=self.campEquip
                            )
        manageBtn = tk.Button(
                            self.frameAry[0],
                            bg=self.backgroundC,
                            fg=self.foregroundC,
                            font=self.butnFont,
                            text="Manage",
                            command=self.campManage
                            )
        epxloreBtn = tk.Button(
                            self.frameAry[0],
                            bg=self.backgroundC,
                            fg=self.foregroundC,
                            font=self.butnFont,
                            text="Explore",
                            command=self.campExplore
                            )
        #Left Side Stuff
        self.dayDisplay = tk.Label(
            self.frameAry[0],
            bg=self.backgroundC,
            fg=self.foregroundC,
            font=self.butnFont,
            text="Day {}".format(self.gameDays)
            )
        ###Time
        self.timeToString()
        self. timeDisplay = tk.Label(
            self.frameAry[0],
            bg=self.backgroundC,
            fg=self.foregroundC,
            font=self.butnFont,
            text="Time: {}:{}".format(self.gameClockHourStr,self.gameClockMinuteStr)
            )
        ###End time stuff
        self.campDefDisplay = tk.Label(
            self.frameAry[0],
            bg=self.backgroundC,
            fg=self.foregroundC,
            font=self.butnFont,
            text="Defense: {}".format("3")  #TODO: Create a defense system
            )
        self.sizeDisplay = tk.Label(
            self.frameAry[0],
            bg=self.backgroundC,
            fg=self.foregroundC,
            font=self.butnFont,
            text="People: {} ".format((len(self.campMembers)+1)) #Number of members in camp plus self
            )
        self.moneyDisplay = tk.Label(
            self.frameAry[0],
            bg=self.backgroundC,
            fg=self.foregroundC,
            font=self.butnFont,
            text="Money: {} coins".format(self.currency)
            )

        #Placing Stuff
        self.inbetweenSpace = 10

        sceneTitle.place(x=(resX/2)) #Place at middle of screen, top
        sceneTitle.update()
        sceneTitle.place(x=((resX/2)-(sceneTitle.winfo_width()/2)),y=0)

        #Right side button placement
        self.placeOnX(sleepBtn, None, 1, 1)
        self.placeOnX(storageBtn, sleepBtn, 1)
        self.placeOnX(equipBtn, storageBtn, 1)
        self.placeOnX(manageBtn, equipBtn, 1)
        self.placeOnX(epxloreBtn, manageBtn, 1)

        #Left side info placement
        self.placeOnX(self.dayDisplay, None, 0, 1)
        self.placeOnX(self.timeDisplay,self.dayDisplay)
        self.placeOnX(self.campDefDisplay,self.timeDisplay)
        self.placeOnX(self.sizeDisplay,self.campDefDisplay)
        #TODO: finish the formatting for prettiness

    def timeToString(self): #Update the time string with current time
        #Hour
        if self.gameClockHour == 0:
            self.gameClockHourStr = "00"
        elif self.gameClockHour < 10:
            self.gameClockHourStr = "0"+str(self.gameClockHour)
        else:  
            self.gameClockHourStr = str(self.gameClockHour)
        #Minute
        if self.gameClockMinute < 10:
            self.gameClockMinuteStr = str(self.gameClockMinute)+"0"
        else:   
            self.gameClockMinuteStr = str(self.gameClockMinute)
    def campSleep(self): #Sleep for 6 hours
        hoursSleep = 6
        self.addTime(hoursSleep*60)
        # print("Slept, hour now {} and minute now {}".format(self.gameClockHourStr,self.gameClockMinuteStr))
        # self.timeDisplay.update()
    def campStorage(self):
        print("OOF")
        #TODO: Make a storage screen
    def campEquip(self):
        print("OOF")
        #TODO: make an equipping system (framework) for player (first) and NPCs (second)
    def campManage(self):
        print("OOF")
        #TODO: Make a window for managing the camp
    def campExplore(self):
        eWindow = tk.Toplevel() #Keeping here until I can confirm I won't be needing it
        self.exploreTab = expl.Explore(eWindow,resX,resY,scrAsp) #Same with the exploreTab
    def bringToFront(self): #Return to camp
        self.frameAry[0].tkraise()
    def placeOnX(self,block,previousBlock,right = 0,first = 0): #Place something on left side of screen
        leftXBuffer = 5
        if(first == 0 and right == 0): #If (block, previousBlock, 0, 0)
            block.place(x=leftXBuffer,y=self.placeBelow(previousBlock))
        elif(first == 1 and right != 1): #If (block, None, 0, 1)
            block.place(x=leftXBuffer,y=10+self.inbetweenSpace)
        elif(first != 1 and right == 1): #If (Block, previousBlock, 1, 0)
            block.place(x=self.findRightX(block),y=self.placeBelow(previousBlock))
        else: #If (block, None, 1, 1)
            block.place(x=self.findRightX(block),y=10+self.inbetweenSpace)
    def placeBelow(self,lastButton): #Place a widget a certain amount y under
        lastButton.update()
        self.spaceBelow = lastButton.winfo_y()
        self.spaceBelow += lastButton.winfo_height()
        self.spaceBelow += self.inbetweenSpace        
        return self.spaceBelow       
    def findRightX(self,butn): #Get the x position of a widget wanted to allign to right y border
        self.xSpaceAmount = -5 #Move away from border this many pixels
        butn.place(x=resX/2)
        butn.update() #place and update so can get dimesnions
        return ((resX-butn.winfo_width())+self.xSpaceAmount)
    def addTime(self,time=0): #Add time to the clock
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
    def printDebug(self):
        print("Class function can be used")



def main():
    app = StartMenu(root)
    root.mainloop()

if __name__ == '__main__':
    main()
