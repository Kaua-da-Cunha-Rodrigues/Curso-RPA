from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import pandas


#Abre o navegador e o site
navegador = webdriver.Chrome();
sleep(1)
navegador.get("https://rpachallengeocr.azurewebsites.net/")
sleep(2)

#Pega o caminho da tabela que queremos a informação
tabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')
sleep(1)

linhas = tabela.find_elements(By.TAG_NAME, "tr")
dataFrameLista = []
for linhaAtual in linhas:
    print(linhaAtual.text)
    dataFrameLista.append(linhaAtual.text)

dataFrame = pandas.DataFrame(dataFrameLista, columns=['Nome-Coluna-Dados'])
arquivoExcel = pandas.ExcelWriter('DadosSite.xlsx', engine='xlsxwriter')
dataFrame.to_excel(arquivoExcel, sheet_name='Sheet1', index=False)
arquivoExcel._save()