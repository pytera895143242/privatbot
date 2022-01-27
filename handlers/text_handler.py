from aiogram import types
from misc import dp,bot
import asyncio
from .sqlit import black

ADMIN_ID_1 = 2078570944
ADMIN_ID =[ADMIN_ID_1]

@dp.message_handler(content_types=['text','voice','video','video_note'])
async def all_other_messages(message: types.message):
    print('1231231312')
    if message.from_user.id in ADMIN_ID:
        black(message.text)
