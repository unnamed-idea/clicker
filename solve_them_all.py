import time
import pyautogui
import random


def click_next():
    buttons = [[1760,580],
               [1500,620],
               [1730,630]]
    for loc in buttons:
        print(loc)
        pyautogui.moveTo(loc)
        time.sleep(0.01)
        pyautogui.click()


def click_next2():
    pyautogui.moveTo(1500, 620)
    pyautogui.click()
def click_next3():
    pyautogui.moveTo(1730, 630)
    pyautogui.click()

def go_random():
    minx = 1000
    miny = 120
    maxx = 1769
    maxy = 580
    randx = random.randint(minx, maxx)
    randy = random.randint(miny, maxy)
    return randx, randy


def click_random(randnum=10):
    for i in range(randnum):
        pyautogui.moveTo(go_random())
        time.sleep(0.001)
        pyautogui.click()


def locate_button():
    res = pyautogui.locateCenterOnScreen('pi/orange.png', confidence=0.85, region=(1000, 120, 1769, 580))
    if res is not None:
        pyautogui.moveTo(res)
        pyautogui.click()


def drag_random(randnum=10):
    for i in range(randnum):
        pyautogui.moveTo(go_random())
        time.sleep(0.0001)
        pyautogui.dragTo(go_random())
        time.sleep(0.0001)


def main(slides=10):
    for _ in range(slides):
        click_next()
        time.sleep(10)
        click_next()
        click_random(1000)
        click_next()
        drag_random(1000)
        click_next()

pyautogui.PAUSE = 0

if __name__ == "__main__":
    main(20) #pass 20 slides
