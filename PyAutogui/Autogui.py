import pyautogui
from xlrd import open_workbook

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1
width, height = pyautogui.size()

def click():
    pyautogui.click(pyautogui.position())

def typewrite(value):
    pyautogui.typewrite(value,interval=0.1)

def locateCenterOnScreen(value):
    pyautogui.click(pyautogui.locateCenterOnScreen(value))

def press(value):
    pyautogui.press(value)
    
wb = open_workbook('Commands.xlsx')
for s in wb.sheets():
    for row in range(s.nrows):
        command = s.cell(row,0).value
        value = s.cell(row,1).value
        print(command)
        if(command=='click'):
            click()
        if(command=='typewrite'):
            typewrite(value)
        if(command=='locateCenterOnScreen'):
            locateCenterOnScreen(value)   
        if(command=='press'):
            press(value)  
    

