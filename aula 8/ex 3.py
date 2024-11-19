from selenium import webdriver as wb
from time import sleep
from selenium.webdriver.common.by import By
import pyautogui
import pandas

#Abre navegador
navegador = wb.Chrome()
sleep(1)

#Entra no site
navegador.get('https://www.siterastreio.com.br/')
sleep(2)

#Clica no botão "CEP"
navegador.find_element(By.XPATH, '/html/body/header/div/div/div[2]/a[2]').click()
sleep(1)

#Acha o input pra inserir o CEP
navegador.find_element(By.XPATH, '/html/body/section[1]/div/div/div[1]/div/input').send_keys("23902300")

#Clica no botão "Procurar CEP"
navegador.find_element(By.XPATH, '/html/body/section[1]/div/div/div[1]/div/a/button').click()
sleep(2)

i = 0

#Guarda os XPATH dos dados que eu quero coletar
listaXpath = [
    '/html/body/div[1]/div[4]/div/div[3]/div[2]/div/div[1]/div[2]',
    '/html/body/div[1]/div[4]/div/div[3]/div[2]/div/div[2]/div[2]',
    '/html/body/div[1]/div[4]/div/div[3]/div[2]/div/div[3]/div[2]',
    '/html/body/div[1]/div[4]/div/div[3]/div[2]/div/div[4]/div[2]',
    '/html/body/div[1]/div[4]/div/div[3]/div[2]/div/div[5]/div[2]',
    '/html/body/div[1]/div[4]/div/div[3]/div[2]/div/div[6]/div[2]'
]
dataFrameLista = []
for i in range(6):

    #Entra no XPATH do dado
    dado = navegador.find_element(By.XPATH, listaXpath[i])

    #Printa o dado
    print(dado.text)

    #Guarda o text do XPATH dado
    dataFrameLista.append(dado.text)

dataFrame = pandas.DataFrame(dataFrameLista, columns=["Dados_Endereço"])
arquivoExcel = pandas.ExcelWriter("DadosEndereço.xlsx", engine='xlsxwriter')
dataFrame.to_excel(arquivoExcel, sheet_name="Sheet1", index=False)
arquivoExcel._save()
print('Fim da Execução')