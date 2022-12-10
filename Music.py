import logging
from getmuz import getmusic

from aiogram import Bot,Dispatcher,executor,types

API_TOKEN = '5261743873:AAECNUhhIIfGpsz5oR77mjUHRXEaYqmVxnM'


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    us=message.from_user.full_name
    await message.reply(f"Assalomu alaykum {us} \nMusic finder botga xush kelibsiz\nistalgan artist yoki qo'shiq nomini yuboring\n"
                        f"Men sizga bir zumda topib beraman\nBotdan foydalanishni o'rganish uchun "
                        f"\n/help buyrug'ini yuboring")
@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    us = message.from_user.full_name
    await message.reply(f"Assalomu alaykum {us}\n"
                        f"🔥Shunchaki menga qo'shiqchi yoki qo'shiq nomini jo'nating va men siz uchun musiqa topib beraman!")



@dp.message_handler()
async def sendwiki(message: types.Message):
    word=message.text
    lookup=getmusic(word)
    if lookup:
        await message.reply(f"{word}")
        if lookup.get('title'):
            await message.reply(f"Nomi: {word} \nList\n{lookup['title']}")
        else:
            await message.reply('Bunday musiqa topilmadi')
        if lookup.get('preview'):
            await message.reply_audio(lookup['preview'])
        else:
            await message.reply('Bunday musiqa topilmadi')
    else:
        await message.answer("😔 Kechirasiz\nBunday musiqa topilmadi")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
