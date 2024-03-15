from django.shortcuts import render
import requests

def index(request):
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'brl',
        'order': 'market_cap_desc',
        
        'per_page': 5,
        'page': 1
    }



    response = requests.get(url, params=params)
    coins = response.json()

    return render(request, 'coin_see/coins.html', {'coins': coins})

