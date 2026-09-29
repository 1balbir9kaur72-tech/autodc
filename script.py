import time
import requests

USER_TOKEN = "MTExODkwMDU1MDUzMzEzMjMwMA"
CHANNEL_ID = "1415929532916957194"

messages = [
    "play.redx.fun",
    "sabse best server mcpe + java play.redx.fun port - 25575",
    "unqiue concept wala server books smp plugin ip - play.redx.fun",
    "hi guys whats up?"
]

url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages"

headers = {
    "Authorization": USER_TOKEN,  # Fixed: Variable correctly assigned here
    "Content-Type": "application/json"
}

index = 0

print("Script start ho gayi hai...")

while True:
    payload = {
        "content": messages[index]
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print(f"Sent: {messages[index]}")
    else:
        print(f"Failed ({response.status_code}): {response.text}")
    
    index = (index + 1) % len(messages)
    time.sleep(180)