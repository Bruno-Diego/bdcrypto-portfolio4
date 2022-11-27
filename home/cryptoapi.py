import requests
import os
if os.path.isfile('env.py'):
    import env

from requests.exceptions import ConnectionError, Timeout, TooManyRedirects, HTTPError


def _get_coins_json():
    '''
    Function to retrieve the data from API
    '''
    url = 'https://coinranking1.p.rapidapi.com/coins'
    parameters = {
    "referenceCurrencyUuid":"yhjMzLPhuIDl",
    "timePeriod":"24h",
    "orderBy":"marketCap",
    "orderDirection":"desc",
    'limit':'50',
    'convert':'USD',
    }
    headers = {
        "X-RapidAPI-Key": os.environ.get('X-RapidAPI-Key'),
        "X-RapidAPI-Host": os.environ.get('X-RapidAPI-Host')
    }
    response = requests.request("GET", url, headers=headers, params=parameters)
    try:
        response.raise_for_status()
        return response.json()
    except (ConnectionError, HTTPError, Timeout, TooManyRedirects) as e:
        print(e)


def update_coins():
    '''
    Function to add coins
    '''
    json = _get_coins_json()
    if json is not None:
        try:
            coins_list = json['data']['coins']
            return coins_list
        except (ConnectionError, HTTPError, Timeout, TooManyRedirects) as e:
            print(e)