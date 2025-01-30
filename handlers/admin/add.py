from loader import dp, db
from filters import IsAdmin, IsUser
from handlers.user.menu import users_list
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram import types

category_cb = CallbackData('rate', 'id', 'action')


@dp.message_handler(IsAdmin(), text=users_list)
async def process_settings(message: types.Message):
    users = db.fetchall('SELECT * FROM users')

    if not users:
        await message.answer("Нет зарегистрированных пользователей.")
        return

    user_list_text = "Список пользователей:\n\n"

    for (user_id, tg, payment_sum, ssh_start_date, ssh_end_date, ssh_id, server_id) in users:
        user_info = (
            f"ID: {user_id}\n"
            f"Telegram: {tg}\n"
            f"Платежная сумма: {payment_sum} руб.\n"
            f"Дата начала SSH: {ssh_start_date}\n"
            f"Дата окончания SSH: {ssh_end_date}\n"
            f"SSH ID: {ssh_id}\n"
            f"Server ID: {server_id}\n\n"
        )
        user_list_text += user_info

    await message.answer(user_list_text)