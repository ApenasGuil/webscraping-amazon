from bs4 import BeautifulSoup
import requests
import smtplib
import email.message

# html_doc = """<html lang="pt-br">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>beautifulsoup</title>
# </head>
# <body>
#     <p class="title">a</p>
#     <p class="story">b</p>
#     <p id="link1">c</p>
#     <p>d</p>
# </body>
# </html>"""

# soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify()) # Traz código todo
# print(soup.title)  # Traz somente o especificado, porém com as tags
# print(soup.title.get_text())  # Traz somente valor dento da tag
# print(soup.title.parent.name)  # Exibe o pai da tag name (head)
# print(soup.p)  # Exibe o primeiro <p> encontrado
# print(soup.p['class'])  # Exibe a class do primeiro <p> encontrado
# print(soup.find('p'))  # Mostra o primeiro <p> encontrado
# print(soup.find_all('p'))  # Mostra todos os <p>
# print(soup.find(id='link1'))  # Mostra o id


def send_email():
    # guilhermemoraes.auto@gmail.com

    email_content = """https://www.americanas.com.br/produto/3018509331?epar=bp_pl_00_go_inf-aces_acessorios_geral_gmv&opn=YSMESP&WT.srch=1&gclid=CjwKCAiA3L6PBhBvEiwAINlJ9O7IVGn9IcdRaQXWuFUeh57AZuQia_jY3ansRf1I2vgxbM3ExJ-LFBoC4qwQAvD_BwE&voltagem=BIVOLT"""
    msg = email.message.Message()
    msg['Subject'] = "=====> PREÇOS ABAIXARAM!"

    msg['From'] = 'guilhermemoraes.auto@gmail.com'
    msg['To'] = 'guilhermemoraes.dev@gmail.com'
    password = '@123456789@098'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string())

    print('E-mail enviado com sucesso.')


prices = []

# Americanas
URL = "https://www.americanas.com.br/produto/3018509331?epar=bp_pl_00_go_inf-aces_acessorios_geral_gmv&opn=YSMESP&WT.srch=1&gclid=CjwKCAiA3L6PBhBvEiwAINlJ9O7IVGn9IcdRaQXWuFUeh57AZuQia_jY3ansRf1I2vgxbM3ExJ-LFBoC4qwQAvD_BwE&voltagem=BIVOLT"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50"}
site = requests.get(URL, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
title = soup.find(
    'h1', class_='product-title__Title-sc-1hlrxcw-0 jyetLr').get_text().strip()
# <h1 class = "product-title__Title-sc-1hlrxcw-0 jyetLr" > Monitor Acer Predator XB253Q 24.5 240hz 1ms Ips HDMI/DP/USB < /h1 >
price = soup.find(
    'div', class_='src__BestPrice-sc-1jvw02c-5 cBWOIB priceSales').get_text().strip()
# <div class="src__BestPrice-sc-1jvw02c-5 cBWOIB priceSales">R$ <!-- -->2.699,99</div>
num_price = price[3:8]
num_price = num_price.replace('.', '')
num_price = float(num_price)
# prices.append(float(num_price))

if (num_price < 2200):
    send_email()
else:
    print('Ainda muito caro...')
