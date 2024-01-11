
from aip import AipNlp


def compare(sen_one, sen_two):
    APP_ID = '17068982'
    API_KEY = 'B2lQiKIkdsGhaA1vK4p9ifGe'
    SECRET_KEY = 'mZLqRGPUFKQYlrPmLrSr73elI4qMl0rA'

    client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
    result = client.simnet(sen_one, sen_two)
    if 'score' in result:
        return round(result['score'], 3)
    else:
        return -1
