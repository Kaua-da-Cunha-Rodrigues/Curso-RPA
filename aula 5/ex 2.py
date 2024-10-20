import pyautogui as pg

pg.sleep(1)
pg.hotkey("win", "d")
pg.sleep(5)

#Procura o print que está no diretório tal na tela
google_location = pg.locateOnScreen("C:\\Users\\PMAR\\Documents\\RPA - Kauã da Cunha\\aula 5\\screenshots\\google.png")
pg.sleep(1)
if google_location:
    google_center = pg.center(google_location)

    pg.moveTo(google_center)
    pg.sleep(1)
    pg.doubleClick()
else:
    print("Botão não encontrado na tela")

print("O programa terminou de rodar")