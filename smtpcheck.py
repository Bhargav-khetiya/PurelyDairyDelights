import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# SMTP server settings
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587  # Gmail SMTP port for TLS

# Your Gmail credentials
EMAIL_ADDRESS = 'mca.coding.18@gmail.com'
PASSWORD = 'group18.bmv'

# Email content
sender = EMAIL_ADDRESS
receiver = 'laycanbhago@gmail.com'
subject = 'Test Email'
body = 'This is a test email sent from Python.'

# Create a MIMEText object
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

try:
    # Connect to the SMTP server
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()  # Start TLS encryption
    server.login(EMAIL_ADDRESS, PASSWORD)  # Login to the SMTP server

    # Send the email
    server.sendmail(sender, receiver, msg.as_string())
    print('Email sent successfully!')

except Exception as e:
    print(f'Error sending email: {e}')

finally:
    # Close the connection to the SMTP server
    server.quit()
