import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
import json
import unicodedata
from time import sleep

# Send a get request to the site, returns raw HTML
URL = "https://www.berrybase.de/raspberry-pi/"
page = requests.get(URL)
priceArray = []
stringArray = []
msg = EmailMessage()
dictToSend = {}

# Find and parse data
soup = BeautifulSoup(page.text, "html.parser")
header = soup.find_all('h3')
content = soup.find_all('span', {"class": 'price--default'})

# Extract data into arrays
for price in content:
    prices = price.text
    stripped = prices.replace("€", "").replace(",", ".")
    priceArray.append(float(stripped))
for message in header:
    stringArray.append(message.text)

# Send mail
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('coaltail420@gmail.com', 'lebeujmyrxfljoxq')
    msg['Subject'] = 'Raspberry Prices'
    msg['From'] = 'coaltail420@gmail.com'
    msg['To'] = 'baksaluka24@gmail.com'
    for i in range(0, len(priceArray)):
        if 'Raspberry' in stringArray[i]:
            dictToSend[stringArray[i]] = str(priceArray[i]) + '€'
    jsonData = json.dumps(dictToSend, indent=4, sort_keys=True, ensure_ascii=False)
    msg.set_content(jsonData)
    smtp.send_message(msg)
