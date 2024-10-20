import pyautogui as pg

pg.hotkey("win", "r")
pg.sleep(1)

#abre o wordpad
pg.typewrite("wordpad")
pg.press("enter")
pg.sleep(4)

#Escreve o texto
pg.typewrite("Arquivo aberto com pyautogui que será salvo")
pg.sleep(1)

#salva o arquivo
pg.hotkey("ctrl", "b")
pg.sleep(1)

#escreve o nome do arquivo
pg.typewrite("arquivo_texto")
pg.sleep(1)

#entra na pasta desejada para guardar
pg.doubleClick(834, 467)
pg.sleep(1)
pg.doubleClick(802, 584)
pg.sleep(1)
pg.doubleClick(769, 467)
pg.sleep(1)

#clica no botão "salvar"
pg.click(1358, 793)

#o arquivo já existe, então ele substitui
pg.press("left")
pg.sleep(1)
pg.press("enter")
pg.sleep(2)

#fecha o wordpad
pg.hotkey("alt", "f4")

pg.alert(text="Função concluída", title="Código terminou de rodar", button="ok")

