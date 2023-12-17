import requests
from datetime import datetime, timedelta
from playsound import playsound
from time import sleep
import json
import os

telegram_key = '6283120466:AAEf33L6dg3eP3DOdtZEoOrgKXlGqXbx1Vo'
telegram_chat_id = '-4097848429'
notification = "jg@notifiactionsound.wav"

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}

with open("location.txt", "r") as file:
    district_id = file.read()

def days_to_fetch(days):
    days_list = [(datetime.today() + timedelta(days=i)).strftime('%d-%m-%Y') for i in range(days)]
    return days_list

def telegram_bot(message):
    requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(telegram_key, telegram_chat_id, message))

def check_slots(results):
    count = 0
    for result in results["sessions"]:
        message = {}
        if result["min_age_limit"] == 18 and result["fee_type"] == 'Free':
            if result["available_capacity_dose1"] != 0:
                message['Name'] = result['name']
                message['Address'] = result['address']
                message['Pincode'] = result['pincode']
                message['Total_doses'] = result['available_capacity']
                message['Dose_1'] = result['available_capacity_dose1']
                message['Dose_2'] = result['available_capacity_dose2']
                message['Vaccine'] = result['vaccine']
                message['Organization_type'] = result['private/government']
                message = json.dumps(message)
                message = message.replace("{", "").replace("}", "").replace('"', "").replace(", ", "\n")
                telegram_bot(message)
                print(message)
                print('-'*25)
                count += 1
    return count

if __name__ == '__main__':
    while True:
        days_list = days_to_fetch(3)
        for day in days_list:
            results = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(district_id, day), headers=headers)
            results = results.json()
            count = check_slots(results)
            if count:
                playsound(notification)
                end_log = "- {} results at {} https://www.cowin.gov.in/home".format(count, day)
                print(end_log)
                telegram_bot(end_log)
        sleep(12)
