from email.message import EmailMessage
import ssl, smtplib, random
from imap_tools import MailBox, AND

class AuthenticationMail:
    sender = "mestount@gmail.com"
    cpf_cnpj_mail = "felipe.ferreira39@aluno.ce.gov.br"#"captchasolver240@gmail.com"
    password = "iquduhyskpuadboe"
    subject = "Código de confirmação"
    body = lambda self, receiver, code: f"""
Alô {receiver}, seu código de autenticação para o app é:

{code}
"""
    def __init__(self):
        self.context = ssl.create_default_context()
        self.smtp = self.load_smtp()
        self.smtp.login(self.sender, self.password)
        self.my_gmail = self.load_gmail()
    
    def load_smtp(self):
        return smtplib.SMTP_SSL("smtp.gmail.com", 465, context=self.context)
        
    def load_gmail(self):
        return MailBox('imap.gmail.com', timeout=5).login(self.sender, self.password)

    async def send_code_email(self, receiver):
        #Random access code
        self.code = random.randint(10000, 99999)

        #Email creating
        email = EmailMessage()
        email["From"] = self.sender
        email["To"] = receiver
        email["Subject"] = self.subject
        email.set_content(self.body(receiver, self.code))

        #Sending the email
        self.smtp.sendmail(
            self.sender,
            receiver,
            email.as_string()
        )
        return self.code
        
    async def send_cpf_or_cnpj_email(self, cnpj, cpf, birth_date):
        body = "Responda apenas com 'S' se for, e 'N' se não for validado, ok? Lembrando que é em até um dia depois daqui."
        if cnpj != None:
            body += "\nhttps://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_solicitacao.asp"
            body += f"\nDados => CNPJ: {cnpj}"
        elif cpf != None:
            body += "\nhttps://servicos.receita.fazenda.gov.br/Servicos/CPF/ConsultaSituacao/ConsultaPublica.asp"
            body += f"\nDados => CPF: {cpf} Data de Nascimento: {birth_date}"
        else:
            raise Exception("Attribute error")
        email = EmailMessage()
        email["From"] = self.sender
        email["To"] = self.cpf_cnpj_mail
        email["Subject"] = (cpf if cnpj == None else cnpj)
        email.set_content(body)

        #Sending the email
        self.smtp.sendmail(
            self.sender,
            self.cpf_cnpj_mail,
            email.as_string()
        )
    
    async def check_cpf_or_cnpj_confirmation(self, cpf_or_cnpj):
        for email in self.my_gmail.fetch(AND(from_=self.cpf_cnpj_mail)):
            if cpf_or_cnpj in email.subject:
                text = email.text.split()[0].lower()
                if 's' == text: return True
                elif 'n' == text: return False
        return None

                
