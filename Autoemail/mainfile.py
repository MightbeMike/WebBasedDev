#Auto Gmail sender that I used for work.
#easily constructed to be more veritile and easy to edit
#used on multiple win OS and Linux

#automation can be accomplished with Win task schedule 
# or by importing Schedule/Time 
# into the script and installing "pip install schedule" in Linux

import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, sender_email, password, recipient_file):
    
    with open(recipient_file, 'r') as file:
        recipients = [line.strip() for line in file]

    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = ', '.join(recipients)

# the fallwing would be edited depending on user acc to use Token
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        
        server.sendmail(sender_email, recipients, message.as_string())

# the senders Email details
# info will be for all sent recipents 
#this can also be edited by having CC recipients for privit messages 
subject = "What ever your subject is"
body = "This is a test email sent via Gmail SMTP using Python."
sender_email = "Your Gmail"
password = "Your Gmail login"
recipient_file = "recipients.txt"  # Path to the file containing recipients' email addresses

# Send It!
send_email(subject, body, sender_email, password, recipient_file)
