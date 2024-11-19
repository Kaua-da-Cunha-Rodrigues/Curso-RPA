from selenium import webdriver as wb
from time import sleep
from selenium.webdriver.common.by import By

navegador = wb.Chrome()
sleep(1)

navegador.get("https://rpachallenge.com/")
sleep(2)

listaXpath = [
    '//*[@ng-reflect-name="labelFirstName"]',
    '//*[@ng-reflect-name="labelLastName"]',
    '//*[@ng-reflect-name="labelEmail"]',
    '//*[@ng-reflect-name="labelCompanyName"]',
    '//*[@ng-reflect-name="labelRole"]',
    '//*[@ng-reflect-name="labelAddress"]',
    '//*[@ng-reflect-name="labelPhone"]'
]
listaValorInput = [
    'Kauã',
    'da Cunha Rodrigues',
    'cunhakkk@gmail.com',
    'Parque Tecnológico do Mar',
    'Estagiário',
    'Village, Rua Mafra',
    '336558'
]
i = 0

for i in range(7):
    navegador.find_element(By.XPATH, listaXpath[i]).send_keys(listaValorInput[i])
    sleep(1)

navegador.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input').click()
sleep(2)

print("Fim da aplicação")
