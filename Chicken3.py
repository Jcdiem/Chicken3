import tkinter as tk
import os
import gScreen

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

class Character: #TODO: Use char with explore encoutner
    def __init__(self,level,vt = 0,st = 0,ag = 0,it = 0,ac = 0):
        self.stats = [
            vt, #0: Vitality/Health
            st, #1: Strength/Phys Damage
            ag, #2: Agility/Speed
            it, #3: Intelligence/Construction?
            ac  #4: Arcane Sense/Magic
        ]
        self.level = level        
        self.basePhys = (5*self.stats[1])
        self.baseMag = (7+(2*self.stats[4]))
        self.baseHealth = (10+round(self.stats[0]*2.5+(self.stats[2]*0.5))) #10 will be the relative base for leveling
        self.modBaseHealth = self.baseHealth #Modded base health is what will have percent bonuses applied to it, but not modified from normal so the level calculations can work how they do
                                             #(I.E. +20 max base health would go to this)
        self.percentMax = 0.0
        self.modHealth = 0 #Modded health is applied after percent bonuses or by percent bonuses (I.E. 20% increase to max health would be taken from base and added to this)
        self.totalHealth = (self.modBaseHealth+self.modHealth) #Standard for calculating total health


    def changeHealth(self,baseAmnt = 0, modIncrease = 0, percentIncrease = 1.0): #Changes the health of character
        self.modBaseHealth = self.baseHealth
        self.modBaseHealth += baseAmnt
        self.modHealth += baseAmnt * percentIncrease
        self.modHealth += modIncrease
        self.totalHealth = (self.modBaseHealth+self.modHealth)
    def getHealth(self): #Returns health
        self.changeHealth() #Update health value, incase
        return self.totalHealth
    def getStat(self, statNum): #Returns a stat
        #Possible stats
        #0: Vitality/Health
        #1: Strength/Phys Damage
        #2: Agility/Speed
        #3: Intelligence/Construction?
        #4: Arcane Sense/Magic
        return self.stats[statNum]

def main():
    app = gScreen.StartMenu(root)
    root.mainloop()

if __name__ == '__main__':
    main()
