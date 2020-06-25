import pyautogui

pyautogui.hotkey('alt', 'tab')
pyautogui.leftClick(580,950,1,.3)

x = 1
while x == 1:
    pyautogui.typewrite(['a', 'enter'])
