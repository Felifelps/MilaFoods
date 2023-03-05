import firebase_admin
from firebase_admin import credentials, firestore

firebase_admin.initialize_app(
    credentials.Certificate("C:\\Users\\Felipe\\OneDrive\\Área de Trabalho\\Projects\\cred.json")
)
DB = firestore.client()

