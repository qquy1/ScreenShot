import time
import pyautogui

def screenshot():
    time.sleep(5)
    img = pyautogui.screenshot("test.png")
    img.show()

screenshot()