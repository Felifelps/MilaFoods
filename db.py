import firebase_admin
from firebase_admin import credentials, firestore

firebase_admin.initialize_app(
    credentials.Certificate("cred.json")
)
DB = firestore.client()

