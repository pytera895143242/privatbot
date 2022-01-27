from aiogram import types
from misc import dp, bot
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import random
from .sqlit import cheack_status

Price1 = 310
Price2 = 310
Price3 = 310
Price4 = 310
Price5 = 310

content_chat = -1001780671252

url = 'https://oplata.qiwi.com/create?'
key = 'publicKey=48e7qUxn9T7RyYE1MVZswX1FRSbE6iyCj2gCRwwF3Dnh5XrasNTx3BGPiMsyXQFNKQhvukniQG8RTVhYm3iPsZPmVFjj6M3Tgts8VLcUi2mAp14a2BbyqbQAsx5oYX7KmzANtyXsdy4sUxFmh7w1oBmBRrSN4yCq7vPCxXxrwPiT5HV9vf4CZuvQStx3n'


@dp.callback_query_handler(lambda call: True, state = '*')
async def answer_push_inline_button(call, state: FSMContext):
    markup = types.InlineKeyboardMarkup()
    bat_exit = types.InlineKeyboardButton(text='👈 НАЗАД', callback_data='bat_exit')

    if call.data == 'bat_1': #🍼Р0DDOM (D0 4)🍼
        price = f'&amount={Price1}'
        finish_url = url+key+price
        bat_pay = types.InlineKeyboardButton(text='🎫ОПЛАТИТЬ', url = finish_url)
        markup.add(bat_pay)
        markup.add(bat_exit)
        await bot.copy_message(chat_id=call.message.chat.id,message_id=11,from_chat_id=content_chat,reply_markup=markup)


    if call.data == 'bat_2': #👶Л@П0ЧkИ (I0+-)👶
        price = f'&amount={Price2}'
        finish_url = url + key + price

        bat_pay = types.InlineKeyboardButton(text='🎫ОПЛАТИТЬ', url=finish_url)
        markup.add(bat_pay)
        markup.add(bat_exit)
        await bot.copy_message(chat_id=call.message.chat.id,message_id=8,from_chat_id=content_chat,reply_markup=markup)


    if call.data == 'bat_3':#🎒|||k0льNицы🎒(I4+-)
        price = f'&amount={Price3}'
        finish_url = url + key + price

        bat_pay = types.InlineKeyboardButton(text='🎫ОПЛАТИТЬ', url=finish_url)
        markup.add(bat_pay)
        markup.add(bat_exit)
        await bot.copy_message(chat_id=call.message.chat.id,message_id=7,from_chat_id=content_chat,reply_markup=markup)


    if call.data == 'bat_4':#📚STУDENТКИ (I7+-)📚
        price = f'&amount={Price4}'
        finish_url = url + key + price

        bat_pay = types.InlineKeyboardButton(text='🎫ОПЛАТИТЬ', url=finish_url)
        markup.add(bat_pay)
        markup.add(bat_exit)
        await bot.copy_message(chat_id=call.message.chat.id,message_id=12,from_chat_id=content_chat,reply_markup=markup)


    if call.data == 'bat_5':#🏆🤑Всё тарифы вместе🤑🏆
        price = f'&amount={Price5}'
        finish_url = url + key + price

        bat_pay = types.InlineKeyboardButton(text='🎫ОПЛАТИТЬ', url=finish_url)
        markup.add(bat_pay)
        markup.add(bat_exit)
        await bot.copy_message(chat_id=call.message.chat.id,message_id=6,from_chat_id=content_chat,reply_markup=markup)

    if call.data == 'bat_exit':  # 🏆🤑Всё тарифы вместе🤑🏆
        await bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)

    if call.data == 'instagram':
        await call.message.edit_text(
            '<b>Отправте ссылку на профиль instagram</b>\n\nПримеры:\nhttps://www.instagram.com/karna.val/\ninstagram.com/samoylovaoxana/')

    if call.data == 'vk':
        await call.message.edit_text('<b>Отправте ссылку на профиль ВКонтакте</b>\n\nПримеры:\nhttps://vk.com/id494445129\nvk.com/id173811890')

    if call.data =='phone_number':
        await call.message.edit_text('<b>Отправте номер телефона, начинающийся с +</b>\n\n+7...\n+3...')

    if call.data =='tiktok':
        await call.message.edit_text('<b>Отправте никнейм пользователя</b>\n\nПримеры:\n@karinakross\n@buzova86')


    await bot.answer_callback_query(callback_query_id=call.id)