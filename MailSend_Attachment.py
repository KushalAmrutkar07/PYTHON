import email
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "An email with attachment using Python"
body = "This is an email with attachment sent from Python"
sender = "amrutkarkushal@gmail.com"
receiver = "susenkadam4100@gmail.com"
password = "uhazusnfpctovcpc"

message = MIMEMultipart()
message["From"] = sender
message["To"] = receiver
message["Subject"] = subject

message.attach(MIMEText(body,"plain"))

filename = "Automation.pdf"

with open(filename,"rb")as attachment:

    part = MIMEBase("application","octet-stream")
    part.set_payload(attachment.read()) 

encoders.encode_base64(part)

part.add_header(
    "Content-Disposition",
    f"attachment;filename ={filename}"
)

message.attach(part)
text = message.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context = context)as server:
    server.login(sender,password)
    server.sendmail(sender,receiver,text)

print("Mail sent successfully with attachment")

