import tkinter as tk
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
print("Screen x is {}".format(scrX))
print("Screen y is {}".format(scrY))
print("Res x is {}".format(resX))
print("Res y is {}".format(resY))
tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=1)
root.geometry(resXY)
root.iconbitmap(r'.\art\pixel\favicon.ico')

#Fonts
menuSizeMedium = round(0.0000423*(resX*resY))
menuBtnFont = ('comic sans',menuSizeMedium)

menuSizeLarge = round(0.00006887*(resX*resY))
menuTitleFont = ('comic sans',menuSizeLarge)


def newFrame(background):
    retFrame = tk.Frame(root,bg=background)
    retFrame.grid(row=0,column=0, sticky="nsew")
    retFrame.grid_rowconfigure(0, weight = 1)
    retFrame.grid_columnconfigure(0, weight = 1)
    retFrame.grid()
    return retFrame

#Setting up info screen
def startInfo(oldFrame):
    oldFrame.grid_forget()
    frame = newFrame('black')
    

    infoLabel = tk.Label(frame,fg='white',text="This is a sample text to reference sizing and \n new lines")
   
    #Grid stuff
    infoLabel.grid

#Setting up intro screen
def startMenu():
    frame = newFrame('black')
    def urMom():
        startInfo(frame)
    #Buttons
    startGameBtn = tk.Button(frame, font=menuBtnFont, text="Start Game",command=urMom,bg=(_from_rgb((50,50,50))),foreground='white smoke',activebackground='gray58',activeforeground='white smoke')
    
    #Lables / Titles
    mMenuTitle = tk.Label(frame, font=menuTitleFont, text ="Chicken: The Threequel", fg='white smoke',bg=('black'))

    #Grid formatting
    mMenuTitle.grid()
    startGameBtn.grid()

#Init stuff
startMenu()

#Start loop
root.mainloop()
