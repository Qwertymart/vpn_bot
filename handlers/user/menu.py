from aiogram.types import Message, ReplyKeyboardMarkup
from loader import dp
from filters import IsAdmin, IsUser

pay = 'Оплата'
instruction = 'Инструкции'
my_key = 'Мой ключ'

add_ssh = 'добавить SSh'
remove_ssh = 'удалить SSH'
users_list = 'список пользователей'


#можно вынести в админа
@dp.message_handler(IsAdmin(), commands='menu')
async def admin_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(add_ssh)
    markup.add(remove_ssh)
    markup.add(users_list)
    await message.answer('Меню', reply_markup=markup)


@dp.message_handler(IsUser(), commands='menu')
async def user_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(pay)
    markup.add(instruction)
    markup.add(my_key)

    await message.answer('Меню', reply_markup=markup)
