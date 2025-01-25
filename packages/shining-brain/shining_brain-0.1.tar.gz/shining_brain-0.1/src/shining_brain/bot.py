import os, requests

user_id = os.environ.get("TELEGRAM_USER_ID")
token = os.environ.get("TELEGRAM_TOKEN")

url = f"https://api.telegram.org/bot{token}/sendmessage?text=test&chat_id={user_id}"
print(url)
response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print("Error:", response.status_code)

