'''
Welcome to the Candy Crush lives bot! This bot can automatically give
lives to people in the web-based version of Candy Crush Soda Saga!
'''

import time
import webbrowser
from pynput.mouse import Button, Controller
from win32api import GetSystemMetrics

mouse = Controller()
screen = True if GetSystemMetrics(78) > 1920 else False

def set_up(lives=0):
    '''The set-up. Open the website and find the appropriate screen proportions'''
    webbrowser.open('http://bit.ly/cclifebot')

    time.sleep(70)

    start_time = time.time()

    time.sleep(5)

    return lives, start_time

def clearing():
    '''Clearing any initial pop-ups'''
    #start the race
    mouse.position = (3099, 257) if screen else (1179, 257) 
    time.sleep(1)
    mouse.click(Button.left, 1)

    time.sleep(3)

    #click if start the race not there
    mouse.position = (2355, 261) if screen else (435, 261) 
    time.sleep(1)
    mouse.click(Button.left, 1)

    time.sleep(3)
    mouse.scroll(0, -500)
    time.sleep(1)

    #new race has begun
    mouse.position = (2739, 700) if screen else (819, 700)
    time.sleep(1)
    mouse.click(Button.left, 1)

    time.sleep(3)

def mainloop(lives: int):
    '''Main loop, where lives are given'''
    #click the HEART button
    mouse.position = (2564, 249) if screen else (644, 249)
    time.sleep(.5)
    mouse.click(Button.left, 1)

    time.sleep(1)

    #click the SEND button
    mouse.position = (2734, 657) if screen else (814, 657)
    time.sleep(.5)
    mouse.click(Button.left, 1)

    time.sleep(2)

    #click the SELECT ALL button
    mouse.position = (2427, 719) if screen else (507, 719)
    time.sleep(.7)
    mouse.click(Button.left, 1)

    time.sleep(.5)

    #click the NAYOUNG button
    mouse.position = (2584, 459) if screen else (664, 459)
    time.sleep(.5)
    mouse.click(Button.left, 1)

    time.sleep(.5)

    #click the NICOLE button
    mouse.position = (3005, 595) if screen else (1085, 595)
    time.sleep(.5)
    mouse.click(Button.left, 1)

    time.sleep(.5)

    #click the SEND button
    mouse.position = (2739, 718) if screen else (819, 718)
    time.sleep(.5)
    mouse.click(Button.left, 1)

    time.sleep(3.8)

    lives += 1
    print(lives)

def refresh(lives: int):
    '''Refreshes the webpage to avoid a timeout'''
    time.sleep(10)

    #click the refresh button
    mouse.position = (2006,5) if screen else (86,50)
    mouse.click(Button.left, 1)

    time.sleep(70)

    #start a new timer
    start_time = time.time()

    time.sleep(5)

    return lives, start_time
    

if __name__ == '__main__':
    lives, start_time = set_up()
    
    while True:
        clearing()
        
        while time.time() - start_time <= 2700:
            mainloop(lives)
            
        lives, start_time = refresh(lives)
