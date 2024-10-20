from selenium import webdriver as wb

#Abre o Chrome
navegador = wb.Chrome()

#No input de navegação do Chrome digita isso
navegador.get("https://www.google.com.br")

print("Fim da execução")