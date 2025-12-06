import requests 
import json 

with open('webhook_url', 'r') as file:
        WEBHOOK_URL = file.read().strip()

def sendWebhook(url, message, username, avatar_url):
    data = {
        "content": message,
        "username": username,
        "avatar_url": avatar_url
    }
    r = requests.post(url, json=data)
    if r.status_code == 204:
        print("Sent Webhook Message")
    else:
        print(f"Error Sending Message {r.status_code}")
