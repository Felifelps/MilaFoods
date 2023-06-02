from email.message import EmailMessage
import ssl, smtplib, random
from imap_tools import MailBox, AND

class AuthenticationMail:
    sender = "mestount@gmail.com"
    cpf_cnpj_mail = "captchasolver240@gmail.com"
    password = "iquduhyskpuadboe"
    subject = "Código de confirmação"
    body = lambda self, receiver, code: f"""
Alô {receiver}, seu código de autenticação para o app é:

{code}
"""
    my_gmail = MailBox('imap.gmail.com').login(sender, password)
    context = ssl.create_default_context()
    
    def load_smtp(self):
        self.smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=self.context)

    def send_code_email(self, receiver):
        #Load smtp
        self.load_smtp()

        #Random access code
        self.code = random.randint(10000, 99999)

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
        
    def send_cpf_or_cnpj_email(self, cpf_and_date=None, cnpj=None):
        """
        Sends an email to the captcha solver team, with the data.
        cpf_and_date: [cpf str, birth date (dd/mm/yyyy)]
        cnpj: cnpj str
        
        """
        body = "É ou não é?"
        if cnpj != None:
            body += "\nhttps://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_solicitacao.asp"
            body += f"\nDados => CNPJ: {cnpj}"
        elif cpf_and_date != None:
            body += "\nhttps://servicos.receita.fazenda.gov.br/Servicos/CPF/ConsultaSituacao/ConsultaPublica.asp"
            body += f"\nDados => CPF: {cpf_and_date[0]} Aniversário: {cpf_and_date[1]}"
        else:
            raise Exception("Attribute error")
        email = EmailMessage()
        email["From"] = self.sender
        email["To"] = self.cpf_cnpj_mail
        email["Subject"] = "Trabaiar man"
        email.set_content(body)

        #Sending the email
        self.smtp.login(self.sender, self.password)
        self.smtp.sendmail(
            self.sender,
            self.cpf_cnpj_mail,
            email.as_string()
        )
    
    def check_cpf_or_cnpj_confirmation(self):
        """
        Returns a list with itens like:
            [data sended, answer]
        
        If nothing was find, returns []
        
        """
        answers = [] 
        for email in self.my_gmail.fetch(AND(from_="captchasolver240@gmail.com")):
            if "Trabaiar man" in email.subject:
                answer = email.text.split(".")[0]
                data = email.text.split("Dados =>")[1].split("\n")[0].strip()
                answers.append([data, answer])
        return answers
        

                
