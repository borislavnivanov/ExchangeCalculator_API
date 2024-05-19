import sys
from datetime import datetime

import requests

API_KEY = 'SdtAGGFjKA9bRbxvtYoiNWv5WVDGQA3M'
last_updated: datetime = datetime.min


def get_api_update(base: str = 'BGN'):
    global last_updated
    time = datetime.now()
    if last_updated.hour == time.hour:
        print('Already updated, try again later')
    else:
        api_response = requests.get(
            "https://api.currencybeacon.com/v1/latest?base=" + base + "&api_key=" + API_KEY)
        value = api_response.json()
        last_updated = time
        return value


def get_rate(_rates, currency) -> float:
    n = _rates["response"]
    b = n["rates"]
    return b.get(currency)


def calculate_exchange(_rate: float, amount: float) -> float:
    return round(amount * _rate, 2)


current_rate = get_api_update()

while True:
    input_currency = input('Enter Currency to compare to BGN or END for exit or UPDATE to update /'
                           'the rates:\n').upper()
    if input_currency == 'END':
        # implement exit option
        sys.exit()
    elif input_currency == 'UPDATE':
        # force update event
        current_rate = get_api_update()
    # TODO: implement option to choose to change base currency

    input_amount = float
    while True:
        try:
            a = input('Enter amount you wish to exchange:\n').strip()
            input_amount = float(a)
        except ValueError:
            print('Please enter valid floating point number!')
            continue
        else:
            break

    cur_rate = get_rate(current_rate, input_currency)
    print(f'{input_amount:.2f}BGN = {calculate_exchange(cur_rate, float(input_amount)):.2f}/'
          f'{input_currency}'
          f' as of {current_rate['date']}')
