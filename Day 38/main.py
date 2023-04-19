from datetime import datetime

import requests

GENDER = "male"
WEIGHT_KG = "50"
HEIGHT_CM = "175"
AGE = "18"

APP_ID = "f6ef2d1e"
API_KEY = "6d7a8ff7ccf8d46f888d14955d81e6ae"

SHEETY_API = "4d0bdbfc50ee3ed960ea36c720006ec9"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/4d0bdbfc50ee3ed960ea36c720006ec9/workoutTracker/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    'Content-Type': 'application/json'
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth=("maarcus", "wt_maarcus@170603"))

print(sheet_response.text)
