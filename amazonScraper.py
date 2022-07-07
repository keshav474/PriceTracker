import smtplib
import requests
from bs4 import BeautifulSoup
import time

URL = 'https://www.amazon.in/All-new-Echo-Dot-with-clock/dp/B085M5R82K/?_encoding=UTF8&pd_rd_w=8amJO&content-id=amzn1.sym.ee853eb9-cee5-4961-910b-2f169311a086&pf_rd_p=ee853eb9-cee5-4961-910b-2f169311a086&pf_rd_r=GEZJKBWPVQZHCP42KBJM&pd_rd_wg=7GGi0&pd_rd_r=7c97c3a1-f41b-4cd7-af75-32a9f15eed8e&ref_=pd_gw_ci_mcx_mr_hp_atf_m'

headers = {
    "User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Microsoft Edge Version 103.0.1264.37'}


def priceCheck():
    page = requests.get(URL, headers=headers)

    # soup=BeautifulSoup(page.content,'html.parser')

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    price = soup2.find(class_="a-price-whole").get_text()
    numeric_filter = filter(str.isdigit, price)
    numeric_string = "".join(numeric_filter)

    endprice = float(numeric_string)
    print(endprice)
    if(endprice < 2000):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('email@gmail.com',' ')
    subject = 'IMP price drop'
    body = URL
    msg = f"SUBJECT:{subject}\n\n{body}"
    server.sendmail('email@gmail.com',
                    'email2@gmail.com', msg)
    print("mailed")
    server.quit()


while(True):
    priceCheck()
    print("done", time)
    time.sleep(60*30)
