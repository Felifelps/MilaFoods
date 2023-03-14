from "C:\Users\ALUNO.DESKTOP-PC2N668\Desktop\Nova pasta\LabSoft\gmail.py" import AuthenticationMail

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
