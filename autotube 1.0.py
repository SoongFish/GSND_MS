import pyautogui as ag
import time

def ts(sec = 1):
    time.sleep(sec)

 # init emtpy click
def init_click():
    ag.moveTo(145,270)
    ts()
    ag.click()
    ts()
    
 # main
init_click()
init_click()
ag.hotkey('ctrl', '9')
ts()
ag.moveTo(175, 134)
ts()
ag.click()
ts(15)
ag.moveTo(124, 76)
ts()
ag.click()
ts()
ag.press('backspace')
ts()
ag.write('https://www.youtube.com/channel/UCGrCoKvEGnI-7XgkjVSd-zA', interval = 0.05)
ts()
ag.press('enter')
ts(15)
ag.moveTo(265, 75)
ts()
ag.click()
ts()
ag.moveTo(253, 343)
ts()
ag.click()
ts(15)
ag.moveTo(83, 208)
ts()
ag.click()
ts(15)
ag.moveTo(16, 296)
ts()
ag.click()
ts()
ag.moveTo(30, 296)
ts()
ag.click()
ts()
ag.moveTo(33, 262)
ts()
ag.click()