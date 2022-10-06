import requests
s_city = "Petersburg,RU"
city_id = 0
appid = "6d8e495ca73d5bbc1d6bf8ebd52c4"
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                        params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    for i in data['list']:
        print( i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'] )
except Exception as e:
    print("Exception (forecast):", e)
    pass