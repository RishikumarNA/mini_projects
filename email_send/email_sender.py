import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Rishikumar NA'
email['to'] = 'rishikumar.na2020@vitstudent.ac.in'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('rishikumarashokan@gmail.com', 'Rishi2912@2002...')
  smtp.send_message(email)
  print('all good boss!')