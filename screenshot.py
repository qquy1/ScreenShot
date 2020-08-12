import time
import pyautogui
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pynput import mouse

# region to take screenshot
def on_click(x, y, button, pressed):
    global start, end
    if pressed:
        start = (x, y)
        print(start)
    else:
        end = (x, y)
        print(end)
    if not pressed:
        # Stop listener
        return False


def screenshot():
    img_temp = pyautogui.screenshot()
    img_temp.show()
    # Collect events until released
    with mouse.Listener(
            # on_move=on_move,
            on_click=on_click,
            # on_scroll=on_scroll
    ) as listener:
        listener.join()

    img = pyautogui.screenshot(region=(start[0], start[1], end[0]-start[0], end[1]-start[1]))
    img.show()
    img.save(filedialog.asksaveasfilename(defaultextension=".png"))

# start tkinter
root = tk.Tk()
# button background
root.option_add("*Button.Background", "black")
root.option_add("*Button.Foreground", "white")
# title
root.title("Screenshot Application")
# instruction
messagebox.showinfo("Screenshot App-Instruction", "Please click and drag across area for screenshot")
frame = tk.Canvas(root, width=300, height=10)
frame.pack()
# button to take screenshot
button = tk.Button(
    root,
    text="Take Screenshot",
    command=screenshot
)
button.pack()

root.mainloop()
