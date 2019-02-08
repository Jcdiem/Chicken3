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

#Start loop
root.mainloop()
