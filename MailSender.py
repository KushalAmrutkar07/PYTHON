import smtplib 

sender = "amrutkarkushal@gmail.com"
receiver = "susenkadam4100@gmail.com"
password = "uhazusnfpctovcpc"

smtp_server = smtplib.SMTP('smtp.gmail.com',587)
smtp_server.ehlo()

smtp_server.starttls()
smtp_server.ehlo

smtp_server.login(sender,password)

message = "Hiii"

smtp_server.sendmail(sender,receiver,message)
print("Successfully the send email")

smtp_server.quit()