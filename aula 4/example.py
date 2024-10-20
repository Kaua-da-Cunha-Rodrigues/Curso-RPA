import pyautogui

#Tempo de esperar para o computador pensar
pyautogui.sleep(2)

#Mostrar na tela posição do mouse
print(pyautogui.position())

#Movendo o moseu até o botão iniciar
pyautogui.moveTo(790, 1054)

pyautogui.sleep(2)

pyautogui.click(790, 1054)


print("Programa Encerado com sucesso!")