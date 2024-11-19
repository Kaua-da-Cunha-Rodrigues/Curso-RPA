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

#inicia uma variável auxiliar
x = 0

#Temos três tabelas no total para pegarmos os dados, então por isso o for com range 3
for x in range(3):

    #Como as três tabelas compartilham o mesmo caminho dado la em cima, só pegamos as novas linhas
    linhas = tabela.find_elements(By.TAG_NAME, "tr")
    sleep(1)

    #Incrementei +1 para imprimir tabela 1, tabela 2 e tabela 3, pois nosso x começa com 0
    print(f"Tabela {x+1}")

    #Pegamos as linhas totais e percorremos todas elas com o "linhaAtual"
    for linhaAtual in linhas:
        #Printa o valor guardado naquela linha, no caso os dados que queremos
        print(linhaAtual.text)

    #As linhas estão separadas em páginas, então precisamos clicar em um botão "next" para ir para a nova tabela
    navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()
    sleep(1)

    print("--------------------")

print("Fim da execução")
