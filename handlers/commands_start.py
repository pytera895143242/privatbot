from aiogram import types
from misc import dp,bot
from .sqlit import reg_user,cheack_status,cheack_black
import asyncio

content_chat = -1001780671252
ids_user = []
import asyncio

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    reg_user(id=message.chat.id)
    go = 1
    for i in cheack_black():
        if str(i[0]) == str(message.chat.id):
            go = 0
            break

    await bot.delete_message(chat_id=message.chat.id, message_id= message.message_id)

    print(go)
    if (cheack_status()[0]) == '1' and go != 0:
        print('1221')
        await message.answer(text="""<b>✅ Вы успешно активировали промокод.
    Вам доступна скидка в 20% </b>""")

        await bot.copy_message(chat_id=message.chat.id,message_id=5,from_chat_id=content_chat) #Отправка приветсвия

        markup = types.InlineKeyboardMarkup()

        bat_1 = types.InlineKeyboardButton(text='🍼Р0DDOM (D0 4)🍼', callback_data='bat_1')
        bat_2 = types.InlineKeyboardButton(text='👶Л@П0ЧkИ (I0+-)👶', callback_data='bat_2')
        bat_3 = types.InlineKeyboardButton(text='🎒|||k0льNицы🎒(I4+-)', callback_data='bat_3')
        bat_4 = types.InlineKeyboardButton(text='📚STУDENТКИ (I7+-)📚', callback_data='bat_4')
        bat_5 = types.InlineKeyboardButton(text='🏆🤑Всё тарифы вместе🤑🏆', callback_data='bat_5')

        markup.add(bat_1)
        markup.add(bat_2)
        markup.add(bat_3)
        markup.add(bat_4)
        markup.add(bat_5)


        await message.answer(text="""<b>Выберите желаемый товар или категорию:</b>""",reply_markup=markup)

    else:
        text = f'''👋 Привет, {message.from_user.full_name}\n\n<b>Этот бот может найти приватные фотографии девушек, анализируя их профили во всех социальных сетях и в слитых базах данных 😏\n\n</b>🔎 Отправьте боту ссылку на страничку ВКонтакте или Instagram, или отправьте номер телефона (What\'s App/Viber/Telegram)  🔞👇'''
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        find_leaks = types.KeyboardButton('🔍 Найти сливы 🔍')
        help = types.KeyboardButton('👨🏼‍🔧 Тех. поддержка 👨🏼‍🔧')
        referals = types.KeyboardButton('🤑 Реферальная система 🤑')
        examples = types.KeyboardButton('💡 Примеры 💡')
        statistics = types.KeyboardButton('🌐 Статистика 🌐')
        keyboard.row(find_leaks)
        keyboard.row(help)
        keyboard.row(referals)
        keyboard.row(examples, statistics)

        keyboard1 = types.InlineKeyboardMarkup(1)
        instagram = types.InlineKeyboardButton('Instagram', callback_data='instagram')
        vk = types.InlineKeyboardButton('ВКонтакте', callback_data='vk')
        phone_number = types.InlineKeyboardButton('Номер телефона', callback_data='phone_number')
        tiktok = types.InlineKeyboardButton('TikTok', callback_data='tiktok')
        keyboard1.add(instagram, vk, phone_number, tiktok)

        await message.answer_photo(
            'https://sun1-95.userapi.com/impg/X3WP4VJR6QgTVolvcfobfgYM5tPU0opNeP7M9A/bLPaeXcs89Y.jpg?size=1280x1280&quality=96&sign=bf858645ce1d4ee9bd6d838d00c23095&type=album',
            text, reply_markup=keyboard)
        await message.answer('🔥 Выбери, где будем искать', reply_markup=keyboard1)


