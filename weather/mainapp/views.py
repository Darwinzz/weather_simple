from django.conf import settings
from django.shortcuts import render
import requests


def index(request):
    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=riga&appid={settings.WEATHER_API_KEY}')
    print("My Status Code")
    print(r.status_code)
    weather_data = r.json()

    context = {
        "cod": weather_data.get('cod'),
        "message": weather_data.get('message')
    }
    return render(request, 'index.html', context)
