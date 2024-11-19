from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

#Abre o navegador e o site
navegador = webdriver.Chrome();
sleep(1)
navegador.get("https://rpachallengeocr.azurewebsites.net/")
sleep(2)

#Pega o caminho da tabela que queremos a informação
tabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')
sleep(1)

#Pega todas as linhas da tabela
linhas = tabela.find_elements(By.TAG_NAME, "tr")
sleep(1)

#Pegamos as linhas totais e percorremos todas elas com o "linhaAtual"
for linhaAtual in linhas:
    #Printa o valor guardado naquela linha, no caso os dados que queremos
    print(linhaAtual.text)

print("Fim da execução")
