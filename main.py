import requests
import datetime

APP_ID="eca90511"
API_KEY= "aebbbe46e6dd560b64edfed7f49681ab"
time=datetime.datetime.now()
Date=time.strftime("%m/%d/%Y")
# time=time.strftime("%H:%M:%S") #24 hour format
Time=time.strftime("%I:%M:%S %p") # 12 hour format with am pm
# print(time)

input=input("tell me about your workout: ")
input_dict={
    "query":input
    }

headers={
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

response=requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",json=input_dict, headers=headers)
response.raise_for_status()
result=response.json()
# data=response.json()["exercises"][0]
# Duration=data["duration_min"]
# Exercise=data["name"]
# Calories=data["nf_calories"]
# print(Date, Time, Duration, Exercise, Calories)

for exercise in result["exercises"]:
    workout = {
        "workout": {
            "Date": Date,
            "Time": Time,
            "Duration": exercise["duration_min"],
            "Exercise": exercise["name"].title(),
            "Calories": exercise["nf_calories"],
        }
    }
    sheet_headers={
        'content-Type': 'application/json',
    }
    sheet_url="https://api.sheety.co/8d283ef8b2c8759c4a98c9f221e01dcd/myWorkouts/workouts"
    sheet_response=requests.post(url=sheet_url,json=workout, headers=headers)
    sheet_response.raise_for_status()
    sheet_data=sheet_response.json()
    print(sheet_data)