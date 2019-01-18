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
    resY = int(9 * (0.75*(scrY/9)))
elif (scrAsp > 1.58 and scrAsp < 1.70): #Looking for 1.6
    resX = int( 16 * (0.25*scrX))
    resY = int( 10 * (0.25*scrY))
else: #Resolution for peasents or people with weird tastes
    resX = 640
    resyY = 480
resXY = str(resX)+'x'+str(resY)
print("Screen x is {}".format(scrX))
print("Screen y is {}".format(scrY))
print("Res y is {}".format(resY))
print("Res x is {}".format(resX))
tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=1)
root.geometry(resXY)
root.iconbitmap(r'.\art\pixel\favicon.ico')

#Setting up info screen
def startGame():
    return

#Setting up intro screen
def startMenu():
    frame = tk.Frame(root,width=200,height=200,bg='black')
    frame.grid(row=0,column=0, sticky="nsew")
    frame.grid_rowconfigure(0, weight = 1)
    frame.grid_columnconfigure(0, weight = 1)
    #Fonts
    menuSizeMedium = round(0.0000423*(resX*resY))
    menuBtnFont = ('TkDefaultFont',menuSizeMedium)

    menuSizeLarge = 50
    menuTitleFont = ('TkDefaultFont',menuSizeLarge)
    #Buttons
    startGameBtn = tk.Button(frame, font=menuBtnFont, text="Start Game",action=startGame(),bg=(_from_rgb((50,50,50))),foreground='white smoke',activebackground='gray58',activeforeground='white smoke')
    
    #Lables / Titles
    mMenuTitle = tk.Label(frame, font=menuTitleFont, text ="Chicken: The Threequel", fg='white smoke',bg=('black'))

    #Grid formatting
    mMenuTitle.grid()
    startGameBtn.grid()

    return frame

#Init stuff
startMenu()

#Start loop
root.mainloop()
