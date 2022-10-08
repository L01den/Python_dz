import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
import pogoda_py
from aiogram.dispatcher.filters import Text


logging.basicConfig(level=logging.INFO)
API_TOKEN = '5449883791:AAFSkg9qrFTXxbeo9bdBD-65jukYcaNXu7Y'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# @dp.message_handler(commands=['start'])
# async def cmd_start(message: types.Message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     buttons = ['Начать', '???']
#     keyboard.add(*buttons)
#     button_2 = 'Что я умею'
#     keyboard.add(button_2)
#     await message.answer("Выбери действие👇", reply_markup=keyboard)



@dp.message_handler(commands=['weather']) 
async def echo(message: types.Message): 
   # s_city_name = message.text[8:]
   msg = pogoda_py.request_forecast(548442)
   await message.answer(msg)


      
   


if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)