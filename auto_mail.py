import smtplib, ssl

port = 465 # For SSL connection
password = input("Type your password and press Enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("ezeokewill@gmail.com", password)

    #TODO: SEND EMAIL
