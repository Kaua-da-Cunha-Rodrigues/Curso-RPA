import pyautogui

#Tempo de esperar para o computador pensar
pyautogui.sleep(2)

#Mostrar na tela posição do mouse
print(pyautogui.position())

#Movendo o moseu até o botão iniciar
pyautogui.moveTo(790, 1054)

pyautogui.sleep(2)

pyautogui.click(790, 1054)

pyautogui.typewrite("Calculadora")

pyautogui.sleep(2)

pyautogui.press("enter")
pyautogui.sleep(2)

pyautogui.typewrite("5")
pyautogui.typewrite("+")
pyautogui.typewrite("5")
pyautogui.typewrite("=")
#Desse jeito abaixo move o mouse para o item e clica
#pyautogui.moveTo(822, 428)[


#pyautogui.click(822, 428)
print("Programa Encerado com sucesso!")