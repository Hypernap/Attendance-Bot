import pyautogui
import time
import datetime
import webbrowser

T=True
query="https://forms.office.com/Pages/ResponsePage.aspx?id=jX15een1I0eG8wXzQoyAWihdtAJRbTZFq2ZhceA3Uh9UMVBMRVE5NE5CWlBHQTVRWEtSQzc3WE5CSi4u"
while T:
  x = datetime.datetime.now()
  if x.hour==8:
    T=False
    if x.hour==8:
      webbrowser.open(query)
      time.sleep(5)
      pyautogui.press('tab', presses=4)
      pyautogui.typewrite('Sankalp Dubedy')
      pyautogui.press('tab', presses=2,interval=1.0)
      pyautogui.write('16')
      pyautogui.press('tab', presses=2,interval=1.0)
      pyautogui.write('8:00')
      pyautogui.press('tab')
      pyautogui.press('enter')

  else:
    T=True  
    time.sleep(120)
    print(x)
