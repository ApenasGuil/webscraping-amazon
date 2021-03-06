from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

from termcolor import colored as corzinha

import smtplib
import email.message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# msg['From'] = 'guilhermemoraes.auto@gmail.com'
# msg['To'] = 'guilhermemoraes.dev@gmail.com'
# password = '@123456789@098'


def send_email(conteudo):
    # Configuração
    host = 'smtp.gmail.com'
    port = 587
    user = 'guilhermemoraes.auto@gmail.com'
    password = '@123456789@098'

    # Criando objeto
    print('Criando objeto servidor...')
    server = smtplib.SMTP(host, port)

    # Login com servidor
    print('Login...')
    server.ehlo()
    server.starttls()
    server.login(user, password)

    # Criando mensagem
    message = conteudo
    print('Criando mensagem...')
    email_msg = MIMEMultipart()
    email_msg['From'] = user
    email_msg['To'] = 'guilhermemoraes.dev@gmail.com'
    email_msg['Subject'] = "=====> PREÇOS ABAIXARAM!"
    print('Adicionando texto...')
    email_msg.attach(MIMEText(message, 'plain'))

    # Enviando mensagem
    print('Enviando mensagem...')
    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
    print('Mensagem enviada!')
    server.quit()


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

url = "https://www.amazon.com.br/gp/product/B084KQBYYM/ref=ewc_pr_img_2?smid=A1ZZFT5FULY4LN&psc=1"

driver.get(url)

time.sleep(3)

div = driver.find_element(By.XPATH, "//*[@id='ppd']")

html_content = div.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html.parser')

# print(soup.prettify())

items_list = soup.select("span[id^=productTitle]")
items_price = soup.find_all("span", class_="a-offscreen")

driver.close()

descricao = items_list[0].get_text()
preco = items_price[0].get_text()

preco = preco.replace("R$", "")
preco = preco.replace(",", ".")
preco = float(preco)

descricao = descricao.strip()

print(corzinha(descricao, "yellow"),
      "o preço está: R$", corzinha(preco, "yellow"))

if preco <= 300:
    print(corzinha("Envia o email", "green"))
    send_email(f"{descricao}, o preço está: R${preco}")
else:
    print(corzinha("O preco ainda tá alto", "red"))
