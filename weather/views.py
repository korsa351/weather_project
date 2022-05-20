from django.shortcuts import render
import requests


def index(request):
    if request.method == "GET":
        return render(request, "weather/index.html")

    if request.method == "POST":
        city = request.POST.get("city")
        appid = "7e730075309f5bb74a997ad11aa17be4"
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&lang=ru&units=Metric&appid=" + appid
        res = requests.get(url.format(city)).json()
        data = {
            'description': res['weather'][0]['description'].capitalize(),
            'temp': round(res['main']['temp']),
            'city': res['name'],
            'icon': f"http://openweathermap.org/img/wn/{res['weather'][0]['icon']}@2x.png",
            "humidity": res['main']['humidity'],
            'clouds': res['clouds']['all'],
            'pressure': round((res['main']['pressure']) * 0.75),

        }
        return render(request, 'weather/index.html', context=data)


def test(request):
    return render(request, 'weather/test.html')
