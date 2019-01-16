from tkinter import *
#import csv

#Tk init
root = Tk()
root.title("Chicken: The Threequel")
scrX = root.winfo_screenwidth()
scrY = root.winfo_screenheight()
resX = 0
resY = 0
scrAsp = float(scrX/scrY)
if (scrAsp > 1.68 and scrAsp < 1.8): #Looking for 1.77
    resX = int(16 * (0.75*(scrX/16)))
    resY = int(9 * (0.75*(scrY/9)))
elif (scrAsp > 1.58 and scrAsp < 1.70): #Looking for 1.6
    resX = int( 16 * (0.75*(scrX/16)))
    resY = int( 10 * (0.75*(scrY/10)))
else: #Resolution for peasents or people with weird tastes
    resX = 640
    resY = 480
resXY = str(resX)+'x'+str(resY)
print("Screen x is {}".format(scrX))
print("Screen y is {}".format(scrY))
print("Game y is {}".format(resY))
print("Game x is {}".format(resX))
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
root.geometry(resXY)
root.iconbitmap(r'.\art\pixel\favicon.ico')

#Setting up main screen
mainFrame = Frame(root,)
def startMenu():
    startGameBtn = Button(mainFrame, text="Start Game", command=loadInfoScreen)
    startGameBtn.grid()

def loadInfoScreen():
    return

#Init stuff
startMenu()

#Start loop
root.mainloop()
