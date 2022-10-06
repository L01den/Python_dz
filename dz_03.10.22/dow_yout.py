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


# yt = YouTube(url)

# print(yt.streams)

# print('''Выберите формат скачивания:
#     видео 720р -> 22
#     видео 360р -> 18
#     видео 144р -> 17
#     аудио 48kbps -> 139 (говёный звук)
#     аудио 128kbps -> 140 (нормальный звук)
#     посмотреть все доступные форматы -> 6''')

# value = int(input('Ваш выбор: '))

# if value == 6:
#     list_stream =[]
#     for i in yt.streams:
#         list_stream.append(str(i))

#     for i in list_stream:
#         i = i[9:-1]
#         print(i)
# else:
#     stream = yt.streams.get_by_itag(value)
#     path = 'download'
#     yt = YouTube(url, on_progress_callback=on_progress).streams
#     res = yt.streams.get_by_itag(value)
#     res.download(path)

url = input('Введите ссылку на видео: ')  # https://www.youtube.com/watch?v=1Z6CHioIn3s&list=RDPKu-L6B-NBU&index=4

path = 'download'
yt = YouTube(url, on_progress_callback=on_progress).streams
res = choice_res(url)
res.download(path)
# video_best = yt.str
# order_by('resolution').desc().first()
