import pyautogui
import time
from plyer import notification

right = 0
con, grey = 0.9, True #Confident
screen = (0,0,1920,1080) #Screen that will be processed
prevPicture = False

notification.notify(
        title = 'Baccarat Assistant',
        message = 'Program Started',
        app_icon = "asset/icon.ico",
        timeout = 2,    
        )

def locate(image,cursor):
    global con, screen,grey,pos
    pos = pyautogui.locateCenterOnScreen(image, region= screen, grayscale= grey, confidence= con)
    if pos != None:
        if cursor == True:
            x, y = pos
            pyautogui.moveTo(x, y, 0.1) 
            if right == 1:
                pyautogui.mouseDown(button='right')
                time.sleep(.1)
                pyautogui.mouseUp(button='right')
            else:
                pyautogui.mouseDown()
                time.sleep(.1)
                pyautogui.mouseUp()
        return True
    else:
        return False
    
while 1:
    if locate('asset/GR.png',False) == True and prevPicture == False:
        print("Moment Ready")
        notification.notify(
        title = 'Baccarat Assistant',
        message = 'Ready to the moon',
        app_icon = "asset/icon.ico",
        timeout = 2,    
        )
    prevPicture = locate('asset/GR.png',False)
    time.sleep(1)
