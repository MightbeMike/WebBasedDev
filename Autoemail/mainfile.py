import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, sender_email, password, recipient_email):
    # Create a MIMEText object to represent the email body
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = recipient_email

    # Establish a connection to Gmail's SMTP server over SSL
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        # Login to the SMTP server using the sender's email address and password
        server.login(sender_email, password)
        
        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())

# Email details
subject = "Test Email"
body = "This is a test email sent via Gmail SMTP using Python."
sender_email = "m.graziano.qfcp@gmail.com"
password = "Graz1300566"
recipient_email = "m.graziano@protonmail.com"

# Send the email
send_email(subject, body, sender_email, password, recipient_email)
