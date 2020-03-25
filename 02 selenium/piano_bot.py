import pyautogui as pg
import time
from PIL import ImageGrab

taps = [(328,753),(607,753),(420,753),(517,753)]
while True :
    # print(pg.position())
    # time.sleep(.5)
    screen = ImageGrab.grab()
    for tap in taps :
        if (0,0,0) == screen.getpixel(tap) :
            pg.click(*tap) #unpakking 연산자
