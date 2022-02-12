# webscrapper w/o selenium

from bs4 import BeautifulSoup
import requests

from termcolor import colored as corzinha

import smtplib
import email.message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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


# Americanas
URL = "https://www.amazon.com.br/gp/product/B084KQBYYM/ref=ewc_pr_img_2?smid=A1ZZFT5FULY4LN&psc=1"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50"}
site = requests.get(URL, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
items_list = soup.select("span[id^=productTitle]")
items_price = soup.find_all("span", class_="a-offscreen")

# print("Descrição: ", items_list[0].get_text(),
#       " Preço: ", items_price[0].get_text())


# descricao = items_list[0].get_text()
# preco = items_price[0].get_text()

# preco = preco.replace("R$", "")
# preco = preco.replace(",", ".")
# preco = float(preco)

# descricao = descricao.rstrip()

# if preco <= 799:
#     print(corzinha("SEXOOOOOOOOOOOOOOOOOOOOOOOO", "green"))
# else:
#     print(corzinha("n foi", "red"))

# if preco <= 799:
#     print(corzinha("Envia o email", "green"))
#     send_email(f"{descricao}, o preço está: R${preco}")
# else:
#     print(corzinha("O preco ainda tá alto", "red"))


######################################################
####### WITH SELENIUM #######
# driver = webdriver.Firefox()

# url = "https://www.amazon.com.br/gp/product/B084KQBYYM/ref=ewc_pr_img_2?smid=A1ZZFT5FULY4LN&psc=1"

# driver.get(url)

# time.sleep(3)

# div = driver.find_element(By.XPATH, "//*[@id='ppd']")

# html_content = div.get_attribute('outerHTML')

# soup = BeautifulSoup(html_content, 'html.parser')

# # print(soup.prettify())

# items_list = soup.select("span[id^=productTitle]")
# items_price = soup.find_all("span", class_="a-offscreen")

# print("Descrição: ", items_list[0].get_text(),
#       " Preço: ", items_price[0].get_text())

# driver.close()

# descricao = items_list[0].get_text()
# preco = items_price[0].get_text()

# preco = preco.replace("R$", "")
# preco = preco.replace(",", ".")
# preco = float(preco)

# descricao = descricao.rstrip()

# if preco <= 799:
#     print(corzinha("Envia o email", "green"))
#     send_email(f"{descricao}, o preço está: R${preco}")
# else:
#     print(corzinha("O preco ainda tá alto", "red"))
