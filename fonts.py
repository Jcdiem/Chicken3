import tkinter as tk
def menuBtnFont(resMult):
    menuSizeMediumNum = round(0.0000423*resMult)
    return ('default',menuSizeMediumNum)

def menuTitleFont(resMult):
    menuSizeLargeNum = round(0.00006887*resMult)
    return ('default',menuSizeLargeNum)

def largeInfoFont(resMult):
    infoFontLargeNum = round(0.000050862*resMult)
    return ('default',infoFontLargeNum)

def campButtonFont(resMult):
    campSizeMediumNum = round(0.0000454389574*resMult)
    return ('default',campSizeMediumNum)
