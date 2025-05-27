import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = 'localhost'   
SMTP_PORT = 25              

SENDER_EMAIL = 'your_email@example.com'  

def send_email(to_email, subject, body):
    try:
       
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.send_message(msg)

        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send to {to_email}: {e}")

def main():
    subject = "Personalized Greetings"

    with open('personalized_messages.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            to_email = row['email']
            
            message = row['message']

            send_email(to_email, subject, message)

if __name__ == '__main__':
    main()
