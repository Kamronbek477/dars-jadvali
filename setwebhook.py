import requests
import os

url = 'https://darsjadval121212.pythonanywhere.com/webhook'

Token = '6198972222:AAFMAYd6f3bJFSh-1FA6ZnqdZTtAIRhbjyE'

payload = {
    "url":url
}

r = requests.get(f"https://api.telegram.org/bot{Token}/setWebhook", params=payload)
r = requests.get(f"https://api.telegram.org/bot{Token}/GetWebhookInfo", params=payload)



print(r.json())