import firebase_admin, os
from firebase_admin import credentials, firestore

firebase_admin.initialize_app(
    credentials.Certificate(os.path.join("functions", "credentials.json"))
)
DB = firestore.client()

