import calcs as calc

class Explore: #TODO: Make a window with Locations, 
    def __init__(self,mWindow,xRes,yRes,scrAsp):
        # alreadyRunning = True #Placeholder to TODO: prevent multiple Explore windows being open
        # if(not alreadyRunning):
        percentScreen = 0.85
        self.resX = calc.getResX(xRes,scrAsp,percentScreen)
        self.resY = calc.getResY(yRes,scrAsp,percentScreen)
        resXY = str(self.resX)+"x"+str(self.resY)
        mWindow.geometry(resXY)
        self.frame = calc.newFrame(mWindow,'black')