import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
import gui, math_f, db
from aiogram.dispatcher.filters import Text

logging.basicConfig(level=logging.INFO)
API_TOKEN = '5656551956:AAGMqW9go5Ckj0eKGVd__UyIjAwpu3Q1Gkw'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Начать', '???']
    keyboard.add(*buttons)
    button_2 = 'Что я умею'
    keyboard.add(button_2)
    await message.answer("Выбери действие👇", reply_markup=keyboard)

@dp.message_handler(Text(equals='Начать'))
async def send_welcome(message: types.Message):
   await message.answer('''Привет! Я бот-недоматематик!
Напиши мне простой пример, через пробел, и я его решу)))
(Например:/hi 2 * 2)
Напишешь по другому я буду плакать и сломаюсь(((''')

@dp.message_handler(lambda message: message.text == '???')
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji='🎲')

@dp.message_handler(Text(equals='Что я умею'))
async def send_welcome(message: types.Message):
   await message.answer('Я умею\nСкладывать +\nВычитать -\nУмножать *\nДелить /\nВозводить в степень **') 

@dp.message_handler(commands=['help'])
async def echo(message: types.Message): 
   await message.answer('/hi\n /help\n /start')

@dp.message_handler(commands=['hi']) 
async def echo(message: types.Message): 
   msg = message.text[3:]
   my_list = math_f.example(msg)
   a = int(my_list[0])
   operatorr = my_list[1]
   b = int(my_list[2])
   resaltt = math_f.do_it(a, b, operatorr)
   db.log(f'{a} {operatorr} {b} = {resaltt}')
   value = gui.view_data(a, b, operatorr, resaltt)
   await message.answer(f'Ваш пример {value}')

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)










































# async def hi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Привет {update.effective_user.last_name}')

# async def exemp(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text('Напиши пример')
#     msg = update.massege.text
#     print(msg)


# app = ApplicationBuilder().token("5656551956:AAGMqW9go5Ckj0eKGVd__UyIjAwpu3Q1Gkw").build()

# app.add_handler(CommandHandler("hi", hi))
# app.add_handler(CommandHandler("exemp", exemp))
# print('start server')
# app.run_polling()

# pip install -r requirements.txt



