import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587 # for starttls
sender_email = "ezeokewill@gmail.com"
receiver_email = "fredapaul58@gmail.com"
password = input("Type password and press Enter: ")
message = """\
Subject: Hi there

This message is sent from Python."""

# Create a secure SSL Context
context = ssl.create_default_context()

# Try to log in to server and send mail
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo() # optional because it is implicitly called by .starttls() and .sendmail(), if required
    server.starttls(context=context) # securing the connection
    server.ehlo() # also optional because it is implicitly called by .starttls() and .sendmail(), if required
    server.login(sender_email, password)

    #TODO: Send Email here
    server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    # Print an error message
    print(e)
finally:
    server.quit()
