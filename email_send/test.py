from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'rishikumarashokan@gmail.com'
email_password = 'hrnrahelxepqhyet'

email_receiver='xidop29184@nasskar.com'

subject="gsgfyyaudsyfgvyadhyvaydh"
body="""iusdhufhuadshufhuadhuadufhudsvuuhduvuUHFUUIHFUHWUHFDIJSNIGUARH"""

em=EmailMessage()
em['From']= email_sender
em['To'] = email_receiver
em['Subject'] =subject
em.set_content(body)

content= ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=content) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())




