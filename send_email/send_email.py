#We have to set up the account if is google use this link https://myaccount.google.com/apppasswords

from email.message import EmailMessage
from password import email_password
import ssl
import smtplib

email_sender = 'jalvarezpimiento@gmail.com'
email_pass = email_password()
email_receiver = 'pinav65847@pixiil.com'

subject = "This is a email test"
body = """Greetings this an stupid email so check it... XD part 2 battle tendency"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

the_context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=the_context) as smtp:
    smtp.login(email_sender, email_pass)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
