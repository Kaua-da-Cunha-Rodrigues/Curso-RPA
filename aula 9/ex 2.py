from selenium import webdriver as wb
from time import sleep
from selenium.webdriver.common.by import By
import pyautogui as pg
import pandas

navegador = wb.Chrome()
sleep(1)

navegador.get('https://www.magazineluiza.com.br/')
sleep(2)

navegador.find_element(By.XPATH, '//*[@id="input-search"]').send_keys("Playstion 5")
pg.press("enter")
sleep(5)

listaProdutos = navegador.find_elements(By.CLASS_NAME, 'bDaikj')
dadosFrame = []
for produto in listaProdutos:

    #Nome começa vazio
    nomeProduto = ''

    #Se o nome for vazio, entra no if
    if nomeProduto == ' ':

        #Como a tag de nome tem várias classes, vamos procurar em CADA classe esse nome
        try:
            #Procura na primeira classe
            nomeProduto = produto.find_element(By.CLASS_NAME, 'cQhIqz').text

        #Se não achar, passa para o elif
        except Exception:
            pass

    #Como ele não achou o nome, o "nomeProduto" continua vazio. Então entra aqui
    elif nomeProduto == '':
        #Procura na outra classe
        try:
            nomeProduto = produto.find_element(By.CLASS_NAME, 'sc - cvalOF').text
        except Exception:
            pass
    #Se não achar nome nenhum em nenhuma classe, deixa sem nome mesmo
    else:
        nomeProduto = "SEM NOME"

    #Eu poderia fazer o mesmo esquema do nome para todos esses outros itens abaixo, pois todos também tem várias classes
    precoProduto = produto.find_element(By.CLASS_NAME, 'etFOes').text
    linkProduto = produto.find_element(By.CLASS_NAME, 'gftEET').get_attribute('href')

    print(nomeProduto, " ", precoProduto, " ", linkProduto)
    dadosFrame.append(nomeProduto + "; " + precoProduto + "; " + linkProduto)

dataFrame = pandas.DataFrame(dadosFrame, columns=["Dados_Produto"])
arquivoExcel = pandas.ExcelWriter("DadosProduto.xlsx", engine='xlsxwriter')
dataFrame.to_excel(arquivoExcel, sheet_name="Sheet1", index=False)
arquivoExcel._save()
print("Fim da Execução")
