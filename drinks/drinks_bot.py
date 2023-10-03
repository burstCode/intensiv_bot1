from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import logging

API_TOKEN = '6598763289:AAFTpbeO0ve7lradTGsQlcshSYin9AojrtM'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


class KeyboardMain(ReplyKeyboardMarkup):
    def __init__(self):
        super().__init__(resize_keyboard=True, one_time_keyboard=True)
        self.add(KeyboardButton('Drink'))
        self.add(KeyboardButton('Food'))


class KeyboardDrink(ReplyKeyboardMarkup):
    def __init__(self):
        super().__init__(resize_keyboard=True, one_time_keyboard=True)
        self.insert(KeyboardButton('Juice'))
        self.insert(KeyboardButton('Sparkly water'))
        self.add(KeyboardButton('Back'))


class KeyboardSnack(ReplyKeyboardMarkup):
    def __init__(self):
        super().__init__(resize_keyboard=True, one_time_keyboard=True)
        self.insert(KeyboardButton('Chips'))
        self.insert(KeyboardButton('Burger'))
        self.add(KeyboardButton('Back'))


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.username
    await message.answer(
        f'Greetings, {user_name}! \nChoose your needs',
        reply_markup=KeyboardMain()
    )


@dp.message_handler(text='Drink')
async def get_drink(message: types.Message):
    await message.answer('Choose drink', reply_markup=KeyboardDrink())


@dp.message_handler(text='Food')
async def get_drink(message: types.Message):
    await message.answer('Choose snack', reply_markup=KeyboardSnack())


@dp.message_handler(text='Back')
async def get_drink(message: types.Message):
    await message.answer('You quited to the main menu', reply_markup=KeyboardMain())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
