import pyrebase
fr
config = {
  "apiKey": "AIzaSyB32-Rr3GAGTY1TG2wGkrHcwq6Hb-k2HPg",
  "authDomain": "book-store-management-app.firebaseapp.com",
  "databaseURL": "https://book-store-management-app-default-rtdb.firebaseio.com/",
"storageBucket": "book-store-management-app.appspot.com"
}

firebase = pyrebase.initialize_app(config)
# Get a reference to the database service
db = firebase.database()

print(db)