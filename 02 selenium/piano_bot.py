import pyautogui as pg
import time
from PIL import ImageGrab
import keyboard

taps = [(328,753),(607,753),(420,753),(517,753)]
state = False

width , height = pg.size()
box = (0,0,width/2,height)

def play():
    screen = ImageGrab.grab(box)
    for tap in taps :
        if (0,0,0) == screen.getpixel(tap) :
            pg.click(*tap) #unpakking 연산자

while True :
    if not state and keyboard.is_pressed('a'):
        state = True
        print('Start!')
    elif state and keyboard.is_pressed('s'):
        state = False
        print('Stop!')
        break;
    if state:
        play()
    # print(pg.position())
    # time.sleep(.5)

