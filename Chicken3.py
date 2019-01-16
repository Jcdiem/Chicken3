from tkinter import *
#import csv
from random import randint


#Tk init
mWindow = Tk()
mWindow.title("Chicken: The Threequel")
scrX = mWindow.winfo_screenwidth()
scrY = mWindow.winfo_screenheight()
resX = 0
resY = 0
scrAsp = float(scrX/scrY)
if (scrAsp > 1.68 and scrAsp < 1.8):
    resX = 16 * 64
    resY = 9 * 64
elif (scrAsp > 1.58 and scrAsp < 1.70):
    resX = 16 * 64
    resY = 10 * 64
else: #Debug for if all eslse fails
    resX = 640
    resyY = 480
resXY = str(resX)+'x'+str(resY)
print("Res y is {}".format(resY))
print("Res x is {}".format(resX))
mWindow.geometry(resXY)
mWindow.iconbitmap(r'.\art\pixel\favicon.ico')

#Start loop
mWindow.mainloop()
