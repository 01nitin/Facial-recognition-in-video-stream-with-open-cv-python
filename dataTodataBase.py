import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("service.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-96653-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "12012002":
        {
            "name": "Nitin",
            "major": "singing",
            "starting_year": 2023,
            "total_attendance": 0,
            "Grade": 'G',
            "year": 3,
            "last_attendance_time": "2023-04-10 20:00:00"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
