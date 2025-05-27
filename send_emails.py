import smtplib
from email.message import EmailMessage

def send_email(to_email, subject, body):
    smtp_server = "localhost"
    smtp_port = 25 
    sender_email = "test@example.com"  


    message = EmailMessage()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject
    message.set_content(body)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
      
        server.send_message(message)
        print(f"Email sent to {to_email}")


send_email("recipient@example.com", "Test Subject", "This is a test email.")