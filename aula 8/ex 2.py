from selenium import webdriver as wb
from time import sleep
from selenium.webdriver.common.by import By
import pandas

navegador = wb.Chrome()
sleep(1)
navegador.get("https://rpachallengeocr.azurewebsites.net/")
sleep(2)

tabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')
sleep(1)



i = 1

#Variável responsável por guardar todos os dados coletados para no final jogar na tabela
dataFrameLista = []
for i in range(3):

    linhas = tabela.find_elements(By.TAG_NAME, "tr")
    print(f"Tabela {i}")
    for linhaAtual in linhas:
        print(linhaAtual.text)
        #Joga o dado para dentro da variável
        dataFrameLista.append(linhaAtual.text)

    # As linhas estão separadas em páginas, então precisamos clicar em um botão "next" para ir para a nova tabela
    navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()
    sleep(1)

    print("--------------------")

#Pega os dados da coluna e a coluna onde será colocada o dado
dataFrame = pandas.DataFrame(dataFrameLista, columns=["Dados_Coluna"])

#Seleciona o arquivo Excel que vai guardar, se não existir, cria ele
arquivoExcel = pandas.ExcelWriter("DadosSite2.xlsx", engine='xlsxwriter')

#Escreve o dado dentro da tabela do excel
dataFrame.to_excel(arquivoExcel, sheet_name="Sheet1", index=False)

#Salva o arquivo Excel
arquivoExcel._save()