import pyautogui as pg

#Tira um print
im2 = pg.screenshot()

#Salva no local desejado
im2.save('.\\screenshots\\screenshot2.png')
print("Automação Concluída")