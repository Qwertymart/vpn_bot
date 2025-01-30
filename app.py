from aiogram import types
from aiogram.types import ReplyKeyboardMarkup
from loader import dp

from aiogram.types import ReplyKeyboardRemove
from data.config import ADMINS

from aiogram import executor
from logging import basicConfig, INFO

from loader import db, bot

import handlers

user_message = 'Пользователь'
admin_message = 'Админ'


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)#задаем разметку с изменяем размером

    markup.row(user_message, admin_message) #выбор двух режимов

    await message.answer('''Привет, я тайный поклонник, хочу передать тебе за щеку  🤗
    ''', reply_markup=markup)


@dp.message_handler(text=admin_message)
async def admin_mode(message: types.Message):
    cid = message.chat.id
    if cid not in ADMINS:#тут свои условия на админа
        ADMINS.append(cid)

    await message.answer('Включен админский режим.',
                         reply_markup=ReplyKeyboardRemove())#удаление кнопок


@dp.message_handler(text=user_message)
async def user_mode(message: types.Message):
    cid = message.chat.id
    if cid in ADMINS:
        ADMINS.remove(cid)

    await message.answer('Включен пользовательский режим.',
                         reply_markup=ReplyKeyboardRemove())


async def on_startup(dp):
    basicConfig(level=INFO)
    db.create_tables() #создаем таблы


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=False)
