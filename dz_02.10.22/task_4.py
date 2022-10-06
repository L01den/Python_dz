import requests

city = input('Город ')
url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)
print(res.text)

