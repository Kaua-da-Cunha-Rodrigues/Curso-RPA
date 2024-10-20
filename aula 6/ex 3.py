from selenium import webdriver as wb
from time import sleep
from selenium.webdriver.common.by import By
import pyautogui as pg
from selenium.webdriver.support.select import Select

#Abre navegador
navegador = wb.Chrome()

#entra no site
navegador.get("https://forms.gle/8UHHVcFBRuPqCqQP7")
sleep(2)

#preenche o campo de email
navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input').send_keys("cunhakaua2@gmail.com")
sleep(1)

#preenche o campo de nome
navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("Kauã")
sleep(1)

#preenche o campo de sobrenome
navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("da Cunha Rodrigues")

#como o select não é um select (não sei porque também), fiz o processo manual de clicar no select e depois clicar a opção

#Aqui eu abro a caixa de seleção
navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[1]/span').click()
sleep(1)

#aqui eu clico na opção que eu quero
navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[3]/span').click()
sleep(1)

#scroll pra baixo
pg.scroll(-1000, -1000)
sleep(1)

#clica no radio "não"
navegador.find_element(By.XPATH, '//*[@id="i24"]/div[3]/div').click()
sleep(1)

#clica no checkbox "amarelo"
navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[4]/label/div/div[2]/div/span').click()
sleep(1)

#clica nas 5 estrelas
navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/span/div/label[5]/div[2]').click()
sleep(2)

#scroll pra baixo
pg.scroll(-1000, -1000)
sleep(2)

#clica no muito satisfeito
navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[2]/span/div[5]/div/div/div[3]/div').click()
sleep(1)

#clica no muito satisfeito
navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[4]/span/div[5]/div/div/div[3]/div').click()
sleep(1)

#Clica no botão de enviar formulário
#navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
sleep(1)

print("Fim da execução")