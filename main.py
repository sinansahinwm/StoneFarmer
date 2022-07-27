import configparser
import pyautogui
from win32api import GetSystemMetrics
import ctypes
import cv2 
import numpy
from time import sleep, time
import win32gui, win32ui, win32con
from ctypes import *
 

from windowcapture import WindowCapture
 

# Read Application Config File & Parse Sections
def parseAppCfg(configFile = "config.cfg"):
    appConfig = configparser.ConfigParser()
    return appConfig.read(configFile)

# Read Game Options & Parse
def parseClientCfg(appConfig):
    clientConfigFilePath = appConfig["ClientConfig"]["GamePath"] + "\\metin2.cfg"
    clientConfigFile = open(clientConfigFilePath, "r")
    configKeywords = ["WIDTH", "HEIGHT", "WINDOWED", "VIEW_CHAT", "ALWAYS_VIEW_NAME","SHOW_DAMAGE", "DAMAGE_NUMBER_STYLE"]
    configDict = {}
    for line in clientConfigFile:
        for keyword in configKeywords:
            lineStriped = line.replace("\t", "").replace("\n", "")
            if lineStriped.startswith(keyword):
                rawValue = lineStriped.replace(keyword,"")
                configDict[keyword] = int(rawValue)
    return configDict

# Read Window Names & Check
def isWindowAvailable(windowName):
    for x in pyautogui.getAllWindows():
        if x.title == windowName:
            return True
    return False

# User Screen Resolution Width & Height
def getSystemMetrics():
    (width, height) = (GetSystemMetrics(0), GetSystemMetrics(1))
    return (width, height)

# Get Client Window Rectangle From Name
def GetWindowRectFromName(name:str)-> tuple:
    hwnd = ctypes.windll.user32.FindWindowW(0, name)
    rect = ctypes.wintypes.RECT()
    ctypes.windll.user32.GetWindowRect(hwnd, ctypes.pointer(rect))
    return (rect.left, rect.top, rect.right, rect.bottom)
 

# App Starts
wincap = WindowCapture()

loopTime = time()
 
while(True):
  
    screenshot = wincap.get_screenshot()
 
 
    cv2.imshow("Computer Vision", screenshot)

    print("FPS {}".format(1/(time() - loopTime)))
    loopTime = time()

    if cv2.waitKey(1) == ord("q"):
        cv2.destroyAllWindows()
        break

 

