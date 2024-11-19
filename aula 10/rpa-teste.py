from twocaptcha import TwoCaptcha
from selenium import webdriver
import datetime,time,os
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
 
#URL do nosos site
url = "https://2captcha.com/demo/normal"
 
#Abre a url
driver.get(url)
 
#print(driver.get_screenshot_as_base64())


#Cria o nome do print. Usa o datatime para criar fotos com nomes diferentes dependendo da data
file_path = f"prints/image{datetime.datetime.now().strftime("%Y%m%d-%H%M%S")}.png"
#Tira o print
driver.get_screenshot_as_file(file_path)

time.sleep(6)

#Essa é a chave da API
api_key = 'c4dfc162187a57b625863ba16cb64dea'
#Endereço pra colocar no site do CEP
endereco = '23935005'

time.sleep(3)

#Envia a api_key pra validar a requisição
solver = TwoCaptcha(str(api_key))

try:
  # envia a foto para resolver um captcha normal "solver.normal"
  result = solver.normal(file_path)

except Exception as e:
  #Se der erro, retorna o erro
  print(e)

else:
  # Recebe o código do captcha resolvido
  code = result["code"]

  # RPA dependendo do site
  driver.find_element(By.ID,"simple-captcha-field").send_keys(str(code))
  time.sleep(2)
  driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/main/div/div/div[2]/section/div/form/div[2]/button[1]').click()

  time.sleep(10)

