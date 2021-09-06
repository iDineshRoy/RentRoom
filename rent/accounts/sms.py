import requests
import random


def num_to_register(num):
    otp = random.randint(1000,9999)
    # r = requests.post("http://api.sparrowsms.com/v2/sms/",
    #         data={'token' : 'kR2Yof4zNUuYMHhwRUsx',
    #                 'from'  : 'VPIT',
    #                 'to'    : ''+str(num),
    #                 'text'  : 'Your 4-digit OTP is '+str(otp)+'. If you do not have Android App, download it from here: bit.ly/KJagir.'})
    # status_code = r.status_code
    # response = r.text
    # response_json = r.json()
    print(otp)
    return otp
    
    # print(response_json)
    # print(response)
    # print(status_code)