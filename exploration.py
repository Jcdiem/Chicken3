import calcs as calc

class Explore: #TODO: Make a window with Locations, 
    def __init__(self,mWindow,xRes,yRes,scrAsp):
        # alreadyRunning = True #Placeholder to TODO: prevent multiple Explore windows being open
        # if(not alreadyRunning):
<<<<<<< HEAD
        percentScreen = 0.85
        self.resX = calc.getResX(xRes,scrAsp,percentScreen)
        self.resY = calc.getResY(yRes,scrAsp,percentScreen)
=======
        percentCmp = 0.8
        self.resX = calc.getResX(xRes,scrAsp,percentCmp)
        self.resY = calc.getResY(yRes,scrAsp,percentCmp)
>>>>>>> 099985933403a351439d9daf49cca2b929d4fdcc
        resXY = str(self.resX)+"x"+str(self.resY)
        mWindow.geometry(resXY)
        self.frame = calc.newFrame(mWindow,'black')