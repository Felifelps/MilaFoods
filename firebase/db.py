import firebase_admin, os
from firebase_admin import credentials, firestore_async

firebase_admin.initialize_app(
    credentials.Certificate("credentials.json")
)
DB = firestore_async.client()

