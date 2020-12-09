import pyautogui, time
time.sleep(3)
f = open("shrekmovie.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")

