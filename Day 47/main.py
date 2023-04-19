import bs4
import requests
import smtplib

MY_EMAIL = "maarcusreniero@gmail.com"
MY_PASSWORD = "G_maarcus@170603"

BUY_PRICE = 69900.0

URL = "https://www.amazon.in/MSI-i7-10750H-IPS-Level-Windows-10SCXR-654IN/dp/B093L8QGL7/ref=sr_1_2_sspa?keywords=msi" \
      "+gf75&qid=1640697719&sprefix=msi+gf%2Caps%2C246&sr=8-2-spons&psc=1&spLa" \
      "=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMFkxMDFCUUZPVUFUJmVuY3J5cHRlZElk" \
      "PUEwMjk2MzUyMzVBSjQ0N05PM1JMMiZlbmNyeXB0ZWRBZElkPUEw" \
      "NzAxOTk0MjNUNTBWRlE0WjZKSiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2x" \
      "pY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU= "
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/96.0.4664.110 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(URL, headers=headers)
contents = response.text

soup = bs4.BeautifulSoup(contents, "html.parser")

product_price = soup.find(name="span", class_="a-offscreen").text
product_price_without_currency = product_price.split("₹")[1]
product_price_without_currency = product_price_without_currency.replace(",", "")
product_price_float = float(product_price_without_currency)
print(product_price_float)

print(product_price_float == BUY_PRICE)

if product_price_float == BUY_PRICE:
    message = f"The price is {BUY_PRICE}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs='albionhubert.jl@gmail.com',
                            msg=f"Subject: Amazon Price Alert!\n\n{message}\n{URL}")
