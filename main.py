import requests
from bs4 import BeautifulSoup
import smtplib


my_email = "ksenia790@yahoo.com"
password = "tqcimncwdetnauis"

AMAZON_URL = "https://www.amazon.com/Crockpot-SCV803-SS-Manual-Cooker-Stainless/dp/B004DF0CBA/ref=sr_1_1_sspa?_encoding=UTF8&c=ts&dchild=1&keywords=Slow+Cookers&qid=1616827023&s=kitchen&sr=1-1-spons&ts_id=289940&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyQ1IyODRHRDZWNlNMJmVuY3J5cHRlZElkPUEwNDgzMDg4MzlRM000RkJHVVhPTSZlbmNyeXB0ZWRBZElkPUEwODQ4OTEwMkxGVE5GTzRBQ05WUCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    "Accept-Language": "en,ru-RU;q=0.9,ru;q=0.8",
}
response = requests.get(AMAZON_URL, headers=headers)
data = response.text
soup = BeautifulSoup(data, "html.parser")
tag_price = soup.find(name="span", id="priceblock_ourprice")
price = float(tag_price.getText().split("$")[1])
print(price)
if price < 60:
    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="irbis.mr@gmail.com",
            msg="Subject: Low Price \n\n Price of Electric Pressure Cooker less than $60! Time to spend money, babe!"
            )
