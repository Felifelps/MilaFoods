# MilaFoods

O MilaFoods é um aplicativo cujo objetivo é criar uma rede social de restaurantes, conectando as empresas aos seus clientes.

Foi desenvolvido como trabalho de conclusão da disciplina de Laboratório de Software do curso técnico em informática da EEEP Irmã Ana Zélia da Fonseca, Milagres-CE.

Desenvolvido com o framework python Kivy (e KivyMD), utiliza Firebase como banco de dados remoto e SQlite3 localmente.

O projeto foi descontinuado após a conclusão da disciplina.

# Instalação

1. Primeiro, instale o python em sua máquina, a partir [desse link.](https://www.python.org/downloads/)
2. Clone o repositório com o código:
  ```shell
  git clone https://github.com/Felifelps/MilaFoods
  ```
3. Crie um ambiente virtual:
  ```shell
  python -m venv .venv
  ```
4. Ative o ambiente virtual:
  - No WIndows: `.venv\Scripts\Activate`;
  - No Linux: `$ source .venv/bin/activate`;
5. No diretório do projeto, instale as dependências do projeto:
  ```shell
  pip install -r requirements.txt
  ```
6. Coloque suas [credenciais do Firestore](https://console.firebase.google.com) no arquivo `/firebase/crendetials.json`;
7. Rode o projeto:
  ```shell
  python app.py
  ```



