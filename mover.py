import PySimpleGUI as sg
import threading
import pyautogui
import sys

jiggle_enabled = True

def jiggle():
    while jiggle_enabled:
        pyautogui.moveRel(1, 0, duration=0.05)
        pyautogui.moveRel(-1, 0, duration=0.05)
        pyautogui.moveRel(0, 1, duration=0.05)
        pyautogui.moveRel(0, -1, duration=0.05)

sg.theme('DarkAmber')

layout = [  [sg.Text('Jiggle your mouse!')],
            [sg.Button('Start'), sg.Button('Stop')] ]

window = sg.Window('Nader\'s Jiggler', layout, size=(180,80))

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    elif event == 'Start':
        pyautogui.FAILSAFE = False
        jiggle_enabled = True
        threading.Thread(target=jiggle).start()
    elif event == 'Stop':
        jiggle_enabled = False
        sg.Window.close(window)
        sys.exit()