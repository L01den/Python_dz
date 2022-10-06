from pytube import *
from pytube.cli import on_progress

def choice_res(url: str):
    while True:
        match input(f'Выбери качество: 720, 360 или audio. Для выходы введи - exit '):
            case '720':
                return yt.filter(type='video').get_by_resolution(resolution='720p')
            case '360':
                return yt.filter(type='video').get_by_resolution(resolution='360p')
            case 'audio':
                return yt.filter(only_audio=True).desc().first()
            case 'exit':
                return

url = input('Введите ссылку на видео: ')  # https://www.youtube.com/watch?v=1Z6CHioIn3s&list=RDPKu-L6B-NBU&index=4

path = 'download'
yt = YouTube(url, on_progress_callback=on_progress).streams
res = choice_res(url)
res.download(path)

