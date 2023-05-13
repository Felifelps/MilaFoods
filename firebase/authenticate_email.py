from .gmail import AuthenticationMail
"""
authenticator = AuthenticationMail()
sender = input("Digite seu e-mail: ")
if "@gmail.com" not in sender:
    input("Email inválido")
    quit()
authenticator.send_code_email(sender)
code = input("Email enviado, não feche o programa!.\nDigite o código de acesso: ")
if code == str(authenticator.code):
    input("Felipe info 3 ;)")
else:
    input("Código errado")

"""


auth = AuthenticationMail()
#print(auth.check_cpf_or_cnpj_confirmation())
auth.send_cpf_or_cnpj_email(cpf_and_date=["testando", "o código"])
