import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#cant use storage because its not part of the free plan (have to pay for it)
#from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
  "databaseURL": "https://facerecognitionrealtime-68d6c-default-rtdb.europe-west1.firebasedatabase.app/"
  # "storageBucket": "storage"
})

ref = db.reference("Students")

data = {
  "00001": 
  {
    "name": "Felix Kjellberg",
    "major": "N/a",
    "starting_year": 2017,
    "total_attendance": 6,
    "standing": "B",
    "year": 3,
    "last_attendance_time": "2022-12-11 00:54:34"
  },
  "00002": 
  {
    "name": "Jack Ma",
    "major": "N/a",
    "starting_year": 2017,
    "total_attendance": 6,
    "standing": "B",
    "year": 3,
    "last_attendance_time": "2022-12-11 00:54:34"
  },
  "00003": 
  {
    "name": "JD Vance",
    "major": "N/a",
    "starting_year": 2017,
    "total_attendance": 6,
    "standing": "B",
    "year": 3,
    "last_attendance_time": "2022-12-11 00:54:34"
  },
  "00004": 
  {
    "name": "John Cena",
    "major": "N/a",
    "starting_year": 2017,
    "total_attendance": 6,
    "standing": "B",
    "year": 3,
    "last_attendance_time": "2022-12-11 00:54:34"
  },
  "00005": 
  {
    "name": "Charlie Brown",
    "major": "N/a",
    "starting_year": 2017,
    "total_attendance": 6,
    "standing": "C",
    "year": 3,
    "last_attendance_time": "2022-12-11 00:54:34"
  },
  "00006": 
  {
    "name": "Luis Marques",
    "major": "Games and multimedia",
    "starting_year": 2017,
    "total_attendance": 6,
    "standing": "A",
    "year": 3,
    "last_attendance_time": "2022-12-11 00:54:34"
  }
}

for key, value in data.items():
  ref.child(key).set(value)
