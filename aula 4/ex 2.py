import pyautogui as pg

pg.sleep(2)

#Pressiona mais de uma tecla ao mesmo tempo
pg.hotkey("win", "r")
pg.sleep(1)
pg.typewrite("wordpad")
pg.sleep(1)
pg.press("enter")
pg.sleep(1)

pg.typewrite("Abri com hotkey e digitei um texto")