import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465 # For SSL connection
password = input("Type your password and press Enter: ")
smtp_server = "smtp.gmail.com"
sender_email = "ezeokewill@gmail.com"
receiver_email = "fredapaul58@gmail.com"
# message = """\
#     Subject: Hello From Python

#     This message is sent from Python.
#     """
message = MIMEMultipart("alternative")
message["Subject"] = "An Email From Python"
message["From"] = sender_email
message["To"] = receiver_email

# Plain-Text and HTML version of the message
text = """\
        HI,
        How're you?
        This is a message from a Python script.
    """
html = """\
        <html>
            <body>
                <p>Hi,<br>
                How are you?<br>
                <em> This is a message from a Python script. </em>
                </p>
            </body>
        </html>
    """

# Convert these to plain/html MIMEText objects
first = MIMEText(text, "plain")
second = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the list part first.
message.attach(first)
message.attach(second)

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)

    #TODO: SEND EMAIL
    server.sendmail(sender_email, receiver_email, message.as_string())
