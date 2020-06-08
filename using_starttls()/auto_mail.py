import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server = "smtp.gmail.com"
port = 587 # for starttls
sender_email = "ezeokewill@gmail.com"
receiver_email = "fredapaul58@gmail.com"
password = input("Type password and press Enter: ")
subject = "An email with attachment from Python"
body = "This is an email with attachment sent from Python"
# message = """\
# Subject: Hi there

# This message is sent from Python."""

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))

filename = "document.pdf"  # should be in same directory as the script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream

    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

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
    server.sendmail(sender_email, receiver_email, text)
except Exception as e:
    # Print an error message
    print(e)
finally:
    server.quit()
