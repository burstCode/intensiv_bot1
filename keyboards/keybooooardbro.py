from aiogram import Bot, Dispatcher, executor, types
from keyboards import kb1, kb3, kb4

import logging

API_TOKEN = '6598763289:AAFTpbeO0ve7lradTGsQlcshSYin9AojrtM'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# хендлер на команду /start
@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    await message.reply('Привет', reply_markup=kb4)


if __name__ == '__main__':
    executor.start_polling(dp)
