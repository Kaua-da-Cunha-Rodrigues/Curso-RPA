# RPA Resolvedor de captcha do correios com Selenium e 2Captcha
-O projeto tirará um print da tela do Chrome no site dos correios, salvará isso na pasta `prints` e utilizará o arquivo .png para mandar uma requisição à API 2captcha, após isso, tendo respondido a requisição, ele preencherá os campos de  endereço e do captcha no site.

## criação ambiente
-`python -m venv rpa_venv`

## instalação
-`pip install -r requirements.txt`
-`Criar pasta "prints" onde será armazenada as capturas de tela"`

## .env template
```
API_KEY=API_KEY_2captcha
ENDERECO=CEP

```

