import os
import requests

# get the information from caincap api and convert into json format
def get_coin_data(id):
    coin_url_template = 'https://api.coincap.io/v2/assets/{id}'
    
    coin_url = coin_url_template.format(id=id)
    resp = requests.get(coin_url)
    
    if resp.ok:
        return resp.json()
    else:
        return resp.reason


def retrieve_coin_data(id):
    coin_data = get_coin_data(id)['data']
    info = ['name','supply','volumeUsd24Hr', 'priceUsd', 'changePercent24Hr']
    info_dict = dict((i, coin_data[i]) for i in info if i in coin_data)
    return info_dict


