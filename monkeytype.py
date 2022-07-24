import pytesseract
from pyautogui import screenshot
from pynput.keyboard import Key, Controller
from time import sleep

sleep(1)

keyboard = Controller()
screen = screenshot(region=(500, 825, 1920, 300))
message = pytesseract.image_to_string(screen).replace('\n', ' ')

if (message[0] == 'l'): message = message[1:]

for c in message:
    sleep(0.011)
    keyboard.press(c)
