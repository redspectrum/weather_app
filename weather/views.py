import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
from WeatherApp.settings import APPID

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + APPID

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    cities = City.objects.all()

    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }
        all_cities.append(city_info)

    return render(request, 'weather/index.html', context={'all_info': all_cities, 'form': form})