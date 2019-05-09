# from pymouse import PyMouseEvent, PyMouse
# import pyautogui
#
# buttons = []  # menu, input, title, build, back
#
# class Listener(PyMouseEvent):
#     def __init__(self):
#         PyMouseEvent.__init__(self)
#
#     def click(self, x, y, button, press):
#         if button == 1:
#             if press:
#                 if len(buttons) < 5:
#                     print((x, y))
#                     buttons.append((x, y))
#                 else:
#                     self.stop()
#         else:  # Exit if any other mouse button used
#             self.stop()
#
# def listen():
#     C = Listener()
#     C.run()
#
# def singleData(data):
#     pyautogui.moveTo(buttons[1][0], buttons[1][1], 1)
#     pyautogui.click()
#     pyautogui.typewrite(data)
#
# def singleTitle(title):
#     pyautogui.moveTo(buttons[2][0], buttons[2][1], 1)
#     pyautogui.click()
#     for i in range(30):
#         pyautogui.press('backspace')
#     pyautogui.typewrite(title)
#
# def selectMenu():
#     pyautogui.moveTo(buttons[0][0], buttons[0][1], 2)
#     pyautogui.click()
#
# def clickBuild():
#     pyautogui.moveTo(buttons[3][0], buttons[3][1], 1)
#     pyautogui.click()
#
#
# def clickBack():
#     pyautogui.moveTo(buttons[4][0], buttons[4][1], 5)
#     pyautogui.click()

from pynput.mouse import Button, Controller as mouseController, Listener
from pynput.keyboard import Key, Controller as keyboardController
import time

mouse = mouseController()
keyboard = keyboardController()
buttons = []  # menu, input, title, build, back
intervals = []
st_time = 0


def singleData(data):
    time.sleep(intervals[1]+2)
    mouse.position = (buttons[1][0], buttons[1][1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    keyboard.type(data)


def singleTitle(title):
    time.sleep(intervals[2]+2)
    mouse.position = (buttons[2][0], buttons[2][1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    for i in range(30):
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
    keyboard.type(title)


def selectMenu():
    time.sleep(intervals[0]+2)
    mouse.position = (buttons[0][0], buttons[0][1])
    mouse.press(Button.left)
    mouse.release(Button.left)


def clickBuild():
    time.sleep(intervals[3]+2)
    mouse.position = (buttons[3][0], buttons[3][1])
    mouse.press(Button.left)
    mouse.release(Button.left)


def clickBack():
    time.sleep(intervals[4]+2)
    mouse.position = (buttons[4][0], buttons[4][1])
    mouse.press(Button.left)
    mouse.release(Button.left)


def on_click(x, y, button, pressed):
    global st_time
    if not pressed:
        if len(buttons) < 5:
            buttons.append((x, y))
            interval = time.time() - st_time
            intervals.append(interval)
            st_time = time.time()
            print((x, y), interval)
        else:
            return False


def listen():
    global st_time
    st_time=time.time()
    with Listener(on_click=on_click) as listener:
        listener.join()

# ...or, in a non-blocking fashion:
# listener = mouse.Listener(on_click=on_click)
# listener.start()
