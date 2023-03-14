from email.message import EmailMessage
import ssl, smtplib, random

class AuthenticationMail:
    sender = "mestount@gmail.com"
    password = "iquduhyskpuadboe"
    subject = "Código de confirmação"
    body = lambda self, receiver, code: f"""
Alô {receiver}, seu código de autenticação para o app é:

{code}
"""
    context = ssl.create_default_context()
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)

    def send_code_email(self, receiver):
        #Random access code
        self.code = random.randint(1000, 9999)

        #Email creating
        email = EmailMessage()
        email["From"] = self.sender
        email["To"] = receiver
        email["Subject"] = self.subject
        email.set_content(self.body(receiver, self.code))

        #Sending the email
        self.smtp.login(self.sender, self.password)
        self.smtp.sendmail(
            self.sender,
            receiver,
            email.as_string()
        )
