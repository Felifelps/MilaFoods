from email.message import EmailMessage
import ssl, smtplib, random
from imap_tools import MailBox, AND

class AuthenticationMail:
    sender = "mestount@gmail.com"
    cpf_cnpj_mail = "felipefelipe23456@gmail.com" #"captchasolver240@gmail.com"
    password = "iquduhyskpuadboe"
    subject = "Código de confirmação"
    body = lambda receiver, code: f"""
Alô {receiver}, seu código de autenticação para o app é:

{code}
"""
    my_gmail = MailBox('imap.gmail.com').login(sender, password)
    context = ssl.create_default_context()
    smtp_connection_is_done = False
    
    def load_smtp():
        try:
            AuthenticationMail.smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=AuthenticationMail.context)
            AuthenticationMail.smtp_connection_is_done = True
        except:
            return False

    def send_code_email(receiver):
        #Load smtp
        if not AuthenticationMail.smtp_connection_is_done: AuthenticationMail.load_smtp()

        #Random access code
        AuthenticationMail.code = random.randint(10000, 99999)

        #Email creating
        email = EmailMessage()
        email["From"] = AuthenticationMail.sender
        email["To"] = receiver
        email["Subject"] = AuthenticationMail.subject
        email.set_content(AuthenticationMail.body(receiver, AuthenticationMail.code))

        #Sending the email
        AuthenticationMail.smtp.login(AuthenticationMail.sender, AuthenticationMail.password)
        AuthenticationMail.smtp.sendmail(
            AuthenticationMail.sender,
            receiver,
            email.as_string()
        )
        return AuthenticationMail.code
        
    def send_cpf_or_cnpj_email(cnpj, cpf, birth_date):
        #Load smtp
        if not AuthenticationMail.smtp_connection_is_done: AuthenticationMail.load_smtp()
        
        body = "Responda apenas com 'É' se for, e 'Não' se não for validado, ok? Lembrando que é em até um dia depois daqui."
        if cnpj != None:
            body += "\nhttps://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_solicitacao.asp"
            body += f"\nDados => CNPJ: {cnpj}"
        elif cpf != None:
            body += "\nhttps://servicos.receita.fazenda.gov.br/Servicos/CPF/ConsultaSituacao/ConsultaPublica.asp"
            body += f"\nDados => CPF: {cpf} Data de Nascimentp: {birth_date}"
        else:
            raise Exception("Attribute error")
        email = EmailMessage()
        email["From"] = AuthenticationMail.sender
        email["To"] = AuthenticationMail.cpf_cnpj_mail
        email["Subject"] = (cpf if cnpj == None else cnpj)
        email.set_content(body)

        #Sending the email
        AuthenticationMail.smtp.login(AuthenticationMail.sender, AuthenticationMail.password)
        AuthenticationMail.smtp.sendmail(
            AuthenticationMail.sender,
            AuthenticationMail.cpf_cnpj_mail,
            email.as_string()
        )
    
    def check_cpf_or_cnpj_confirmation(cpf_or_cnpj):
        #Load smtp
        if not AuthenticationMail.smtp_connection_is_done: AuthenticationMail.load_smtp()
        for email in AuthenticationMail.my_gmail.fetch(AND(from_=AuthenticationMail.cpf_cnpj_mail)):
            print(email.subject, email.text)
            if cpf_or_cnpj in email.subject:
                text = email.text.split()[0].lower()
                if 'é' == text: return True
                elif 'não' == text: return False
        return None

                
