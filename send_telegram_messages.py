import csv
import requests

BOT_TOKEN = 'Your_Bot_Token'
CHAT_ID = 'Chat_Id_Of_Bot'

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {'chat_id': CHAT_ID, 'text': text}
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("Message sent on Telegram")
        else:
            print(f"Telegram API error: {response.text}")
    except Exception as e:
        print(f"Failed to send Telegram message: {e}")

def main():
    with open('personalized_messages.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            message = f"To: {row['email']}\nMessage:\n{row['message']}"
            send_telegram_message(message)

if __name__ == '__main__':
    main()
