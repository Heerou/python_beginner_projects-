from credentials import tel_number
import requests
import schedule
import time

def send_text_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': tel_number,
        'message': "This a test text message XD",
        'key': 'textbelt'
    })

    print(resp.json)

# schedule.every().day.at('20:45').do(send_text_message)
schedule.every(10).seconds.do(send_text_message)
while True:
    schedule.run_pending()
    time.sleep(1)