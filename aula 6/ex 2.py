from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
import pyautogui

#Abre o Chrome
navegador = wb.Chrome()

#Escreve no input do Chrome
navegador.get("https://form.jotform.com/221436066464051")
sleep(2)

#Acha o elemento de Id "first_3", que é um input e depois escreve o nome "Kauã"
navegador.find_element(By.ID, "first_3").send_keys("Kauã")
sleep(1)

navegador.find_element(By.NAME, "q3_nome[last]").send_keys("Cunha Rodrigues")
sleep(2)

navegador.find_element(By.XPATH, '//*[@id="input_4"]').send_keys("cunhakaua2@gmail.com")
sleep(2)

#Esse é pra caixa de seleção, onde ele acha a caixa
select = navegador.find_element(By.ID, "input_5")
#Seleciona a caixa de seleção (Como se desse um click para abrir as opções da caixa)
option = Select(select)
#Seleciona o item dessa caixa que você deseja. No caso queremos a primeira opção que diz "Solteiro(a)"
option.select_by_index(1)
sleep(2)

#Clica no elemento x
navegador.find_element(By.ID, "label_input_6_1").click()
sleep(2)


pyautogui.scroll(-500, -500)
navegador.find_element(By.XPATH, '//*[@id="label_input_7_1"]').click()
sleep(2)

print("Fim da execução")