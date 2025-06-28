import requests

def send_alert(message, token, chat_id):
    url = f"https://api.telegram.org/bot7593052286:AAF6yIOxxxxxxxxxxxxx/sendMessage"
    data = {"chat_id": '6196340xxx', "text": message}
    
    try:
        response = requests.post(url, data=data)
        if response.status_code != 200:
            print("❌ Telegram API error:", response.text)
    except Exception as e:
        print("❌ Failed to send alert:", e)