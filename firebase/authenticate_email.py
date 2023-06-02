from .gmail import AuthenticationMail


auth = AuthenticationMail()
def send_code_email(receiver):
    auth.send_code_email(receiver)
    return auth.code

def send_auth_email():
    auth.send_cpf_or_cnpj_email(cpf_and_date=["testando", "o código"])
