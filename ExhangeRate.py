import sys
from datetime import datetime

import requests

API_KEY = 'SdtAGGFjKA9bRbxvtYoiNWv5WVDGQA3M'
last_updated: datetime = datetime.min


def get_api_update(base: str = 'BGN'):
        api_response = requests.get(
            "https://api.currencybeacon.com/v1/latest?base=" + base + "&api_key=" + API_KEY)
        value = api_response.json()
        return value


def get_rate(_rates, currency) -> float:
    n = _rates["response"]
    b = n["rates"]
    return b.get(currency)


def calculate_exchange(_rate: float, amount: float) -> float:
    return round(amount * _rate, 2)


while True:
    input_currency = input('Enter Currency to compare to BGN or END for exit:\n').upper()
    if input_currency == 'END':
        sys.exit()
    input_amount = float(input('Enter amount you wish to exchange:\n'))

    rates = get_api_update()
    cur_rate = get_rate(rates, input_currency)
    print(f'{input_amount:.2f}BGN = {calculate_exchange(cur_rate, input_amount):.2f}{input_currency}'
          f' as of {rates['date']}')
