import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('./firebase_credentials.json')

firebase_admin.initialize_app(cred)
db = firestore.client()


# only uploaded 20,000 to firebase
pictures = json.load(open('img_data.json'))
for picture in pictures:
    db.collection(u'pictures').add(picture)