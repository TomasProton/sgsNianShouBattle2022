import pyautogui

confidence = 0.9
pos = (0,0, 1500, 900)

button7location = pyautogui.locateOnScreen('calc7key.png')
print(button7location)

button7point = pyautogui.center(button7location)
print(button7point)
button7x, button7y = button7point
pyautogui.click(button7x, button7y)
# pyautogui.click('calc7key.png')

center_on_screen = pyautogui.locateCenterOnScreen('calc7key.png')
print(center_on_screen)