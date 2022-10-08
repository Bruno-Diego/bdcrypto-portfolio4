import requests
import os
from updater.models import Crypto
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
if os.path.isfile('env.py'):
    import env


def _get_coins_json():
    url = 'https://coinranking1.p.rapidapi.com/coins'
    parameters = {
    "referenceCurrencyUuid":"yhjMzLPhuIDl",
    "timePeriod":"24h",
    "orderBy":"marketCap",
    "orderDirection":"desc",
    'limit':'100',
    'convert':'USD',
    }
    headers = {
        "X-RapidAPI-Key": os.environ.get('X-RapidAPI-Key'),
        "X-RapidAPI-Host": os.environ.get('X-RapidAPI-Host'),
    }
    response = requests.request("GET", url, headers=headers, params=parameters)
    try:
        response.raise_for_status()
        return response.json()
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def update_coins():
    """
    This function will update the
    list of coins with some frequency
    """
    json = _get_coins_json()
    if json is not None:
        try:
            new_coins = Crypto()
            new_coins.coins = json['data']['coins']
            new_coins.save()
            print("=========\nSaving another entry to Crypto...\n=========\n")
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)


