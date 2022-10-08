import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
import weather_bot
from aiogram.dispatcher.filters import Text

'''Бот не захотел искать id городов, поэтому города только 4'''

logging.basicConfig(level=logging.INFO)
API_TOKEN = '5449883791:AAFSkg9qrFTXxbeo9bdBD-65jukYcaNXu7Y'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Москва', 'Краснодар']
    keyboard.add(*buttons)
    button_2 = ['Санкт-Петербург', 'Иркутск']
    keyboard.add(*button_2)
    await message.answer("Выбери город", reply_markup=keyboard)



@dp.message_handler(Text(equals='Москва'))
async def echo(message: types.Message): 
   msg = str(weather_bot.request_forecast(524901))
   res_str = msg.replace("'", '') 
   await message.answer(res_str)

@dp.message_handler(Text(equals='Краснодар'))
async def echo(message: types.Message): 
   msg = str(weather_bot.request_forecast(542420))
   res_str = msg.replace("'", '') 
   await message.answer(res_str)

@dp.message_handler(Text(equals='Санкт-Петербург'))
async def echo(message: types.Message): 
   msg = str(weather_bot.request_forecast(498817))
   res_str = msg.replace("'", '') 
   await message.answer(res_str)

@dp.message_handler(Text(equals='Иркутск'))
async def echo(message: types.Message): 
   msg = str(weather_bot.request_forecast(2023469))
   res_str = msg.replace("'", '') 
   await message.answer(res_str)


if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)