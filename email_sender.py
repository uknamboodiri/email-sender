import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path('greet.html').read_text())
html = html.substitute(name='Unni')

data = EmailMessage()
data['from'] = 'Just Tech Labs, Pune'
data['to'] = 'uknamboodiri@gmail.com'
data['subject'] = 'Welcome - Your account is active'
data.set_content(html, 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('me', '<my_password>')
    smtp.send_message(data)
    print('All good')
