import smtplib, ssl

port = 465 # For SSL connection
password = input("Type your password and press Enter: ")
smtp_server = "smtp.gmail.com"
sender_email = "ezeokewill@gmail.com"
receiver_email = "fredapaul58@gmail.com"
message = """\
    Subject: Hello From Python

    This message is sent from Python.
    """

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)

    #TODO: SEND EMAIL
    server.sendmail(sender_email, receiver_email, message)
