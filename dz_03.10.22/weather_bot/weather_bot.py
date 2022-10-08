import sys
import requests

def get_wind_direction(deg):
    l = ['С ', 'СВ', ' В', 'ЮВ', 'Ю ', 'ЮЗ', ' З', 'СЗ']
    for i in range(0, 8):
        step = 45.
        min = i*step - 45/2.
        max = i*step + 45/2.
        if i == 0 and deg > 360-45/2.:
            deg = deg - 360
        if deg >= min and deg <= max:
            res = l[i]
            break
    return res

def request_forecast(city_id):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                            params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        for i in data['list']:
            return((i['dt_txt'])[:16], '{0:+3.0f}'.format(i['main']['temp']),
                    '{0:2.0f}'.format(i['wind']['speed']) + " м/с",
                    get_wind_direction(i['wind']['deg']),
                    i['weather'][0]['description'])
    except Exception as e:
        print("Exception (forecast):", e)
        pass


appid = "a3b0e2161f273ae50bc4d3b0892e08ee"




