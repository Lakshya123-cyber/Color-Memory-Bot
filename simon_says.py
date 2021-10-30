import pyautogui
# pyautogui.displayMousePosition()
import keyboard
import time
import win32api, win32con

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01) # This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# GREEN -> X: 1345 Y: 648 RGB: (65, 106, 39) 1
# YELLOW -> X: 1529 Y: 653 RGB: (168, 169, 48) 2 
# BLUE -> X: 1345 Y: 846 RGB: (43, 0, 167) 3
# RED -> X: 1527 Y: 846 RGB: (144, 48, 35) 4

def colorCheck(x, listen):
    if pyautogui.pixel(1345, 648)[0] != 65:
        while pyautogui.pixel(1345, 648)[0] != 65:
            time.sleep(0.05)
        print("green")
        x += 1
        if x > len(color_to_press):
            color_to_press.append(1)
            listen = False

    if pyautogui.pixel(1529, 653)[0] != 168:
        while pyautogui.pixel(1529, 653)[0] != 168:
            time.sleep(0.05)
        print("yellow")
        x += 1
        if x > len(color_to_press):
            color_to_press.append(2)
            listen = False

    if pyautogui.pixel(1345, 846)[0] != 43:
        while pyautogui.pixel(1345, 846)[0] != 43:
            time.sleep(0.05)
        print("blue")
        x += 1
        if x > len(color_to_press):
            color_to_press.append(3)
            listen = False

    if pyautogui.pixel(1527, 846)[0] != 144:
        while pyautogui.pixel(1527, 846)[0] != 144:
            time.sleep(0.05)
        print("red")
        x += 1
        if x > len(color_to_press):
            color_to_press.append(4)
            listen = False

    return x, listen


color_to_press = []

x = 0
listen = True


while 1:
    if keyboard.is_pressed('q'):
        while 1:
            if listen:
                x, listen = colorCheck(x, listen)
            else:
                for num in color_to_press: # Cycle through elements in the list
                    if num == 1: # GREEN
                        click(1345, 648)
                    if num == 2: # YELLOW
                        click(1529, 653)
                    if num == 3: # BLUE
                        click(1345, 846)
                    if num == 4: # RED
                        click(1527, 846)

                time.sleep(0.2)

                listen = True
                x = 0