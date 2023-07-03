import logging
import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = '5992006176:AAE-uprtVKllQKDLbi-2BDuf420C5GC7-ZM'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

glavniy_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Savollar"),
            KeyboardButton(text="Videolar"),
            KeyboardButton(text="Audiolar"),
        ],
        [
            KeyboardButton(text="Giflar"),
            KeyboardButton(text="Voicelar"),
            KeyboardButton(text="Rasmlar"),
        ],       
        [
            KeyboardButton(text="Contactlar"),
            KeyboardButton(text="Lakatsiyalar"),
            KeyboardButton(text="Stickerlar"),
        ],
    ],
    resize_keyboard=True
)

savollar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-chi savol"),
            KeyboardButton(text="2-chi savol"),
            KeyboardButton(text="3-chi savol"),
        ],
        [
            KeyboardButton(text="Orqaga")
        ],
    ],
    resize_keyboard=True
)

videolar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-chi video"),
            KeyboardButton(text="2-chi video"),
            KeyboardButton(text="3-chi video"),
        ],
        [
            KeyboardButton(text="Orqaga")
        ],
    ],
    resize_keyboard=True
)

audiolar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-chi audio"),
            KeyboardButton(text="2-chi audio"),
            KeyboardButton(text="3-chi audio"),
        ],
        [
            KeyboardButton(text="Orqaga")
        ],
    ],
    resize_keyboard=True
)

contactlar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-chi contact"),
            KeyboardButton(text="2-chi contact"),
            KeyboardButton(text="3-chi contact"),
        ],
        [
            KeyboardButton(text="Orqaga")
        ],
    ],
    resize_keyboard=True
)

stickerlar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-chi sticker"),
            KeyboardButton(text="2-chi sticker"),
            KeyboardButton(text="3-chi sticker"),
        ],
        [
            KeyboardButton(text="Orqaga")
        ],
    ],
    resize_keyboard=True
)

lakatsiyalar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-chi lakatsiya"),
            KeyboardButton(text="2-chi lakatsiya"),
            KeyboardButton(text="3-chi lakatsiya"),
        ],
        [
            KeyboardButton(text="Orqaga"),
        ],
    ],
    resize_keyboard=True
)

rasmlar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-chi rasm"),
            KeyboardButton(text="2-chi rasm"),
            KeyboardButton(text="3-chi rasm"),
        ],
        [
            KeyboardButton(text="Orqaga")
        ],
    ],
    resize_keyboard=True
)

giflar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-chi gif"),
            KeyboardButton(text="2-chi gif"),
            KeyboardButton(text="3-chi gif"),
        ],
        [
            KeyboardButton(text="Orqaga"),
        ],
    ],
    resize_keyboard=True
)

voicelar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-chi voice"),
            KeyboardButton(text="2-chi voice"),
            KeyboardButton(text="3-chi voice"),
        ],
        [
            KeyboardButton(text="Orqaga"),
        ],
    ],
    resize_keyboard=True
)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalamu aleykum", reply_markup=glavniy_menu)

# Stickerlar

@dp.message_handler(text="Savollar")
async def send_welcome(message: types.Message):
    await message.reply("Savollar", reply_markup=savollar_menu)

@dp.message_handler(text="1-chi savol")
async def send_welcome(message: types.Message):
    await message.answer_poll("https://t.me/giwoek/16")

@dp.message_handler(text="2-chi savol")
async def send_welcome(message: types.Message):
    await message.answer_poll("https://t.me/giwoek/16")

@dp.message_handler(text="3-chi savol")
async def send_welcome(message: types.Message):
    await message.answer_poll("https://t.me/giwoek/16")

@dp.message_handler(text="Orqaga")
async def send_welcome(message: types.Message):
    await message.reply("Orqaga", reply_markup=glavniy_menu)

@dp.message_handler(text="Stickerlar")
async def send_welcome(message: types.Message):
    await message.reply("Stickerlar", reply_markup=stickerlar_menu)

@dp.message_handler(text="1-chi sticker")
async def send_welcome(message: types.Message):
    await message.answer_sticker("https://t.me/giwoek/11")

@dp.message_handler(text="2-chi sticker")
async def send_welcome(message: types.Message):
    await message.answer_sticker("https://t.me/giwoek/12")

@dp.message_handler(text="3-chi sticker")
async def send_welcome(message: types.Message):
    await message.answer_sticker("https://t.me/giwoek/13")

@dp.message_handler(text="Orqaga")
async def send_welcome(message: types.Message):
    await message.reply("Orqaga", reply_markup=glavniy_menu)

# Contactlar

@dp.message_handler(text="Contactlar")
async def send_welcome(message: types.Message):
    await message.reply("Contactlar", reply_markup=contactlar_menu)

@dp.message_handler(text="1-chi contact")
async def send_welcome(message: types.Message):
    await message.answer_contact("+998 90 512 21 80", "Sharifjon.me")

@dp.message_handler(text="2-chi contact")
async def send_welcome(message: types.Message):
    await message.answer_contact("+998 90 335 82 42", "ravshanovich_pm")

@dp.message_handler(text="3-chi contact")
async def send_welcome(message: types.Message):
    await message.answer_contact("+998 94 695 77 97", "w")

@dp.message_handler(text="Orqaga")
async def send_welcome(message: types.Message):
    await message.reply("Orqaga", reply_markup=glavniy_menu)

# Lakatsiyalar

@dp.message_handler(text="Lakatsiyalar")
async def send_welcome(message: types.Message):
    await message.reply("Lakatsiyalar", reply_markup=lakatsiyalar_menu)

@dp.message_handler(text="1-chi lakatsiya")
async def send_welcome(message: types.Message):
    await message.answer_location(40.45320195081691, 3.68835516125439)

@dp.message_handler(text="2-chi lakatsiya")
async def send_welcome(message: types.Message):
    await message.answer_location(34.101812151988156, 118.32670510389991)

@dp.message_handler(text="3-chi lakatsiya")
async def send_welcome(message: types.Message):
    await message.answer_location(21.422657671923396, 39.82617562496446)

@dp.message_handler(text="Orqaga")
async def send_welcome(message: types.Message):
    await message.reply("Orqaga", reply_markup=glavniy_menu)

# Rasmlar

@dp.message_handler(text="Rasmlar")
async def send_welcome(message: types.Message):
    await message.reply("Rasmlar", reply_markup=rasmlar_menu)

@dp.message_handler(text="1-chi rasm")
async def send_welcome(message: types.Message):
    await message.answer_photo(photo="https://t.me/giwoek/8", 
                               caption="""        
BBC
                               """)

@dp.message_handler(text="2-chi rasm")
async def send_welcome(message: types.Message):
    await message.answer_photo(photo="https://t.me/giwoek/9", 
                               caption="""        
M12
                               """)

@dp.message_handler(text="3-chi rasm")
async def send_welcome(message: types.Message):
    await message.answer_photo(photo="https://t.me/giwoek/10", 
                               caption="""        
B10
                               """)

@dp.message_handler(text="Orqaga")
async def send_welcome(message: types.Message):
    await message.reply("Orqaga", reply_markup=glavniy_menu)

# Voicelar

@dp.message_handler(text="Voicelar")
async def send_welcome(message: types.Message):
    await message.reply("Voicelar", reply_markup=voicelar_menu)

@dp.message_handler(text="1-chi voice")
async def send_welcome(message: types.Message):
    await message.answer_voice(voice="https://t.me/YAKUDZAForever/8514", 
                               caption="""        
Yakudzaaa
                               """)

@dp.message_handler(text="2-chi voice")
async def send_welcome(message: types.Message):
    await message.answer_voice(voice="https://t.me/YAKUDZAForever/8513", 
                               caption="""        
Yakudzaaaa
                               """)

@dp.message_handler(text="3-chi voice")
async def send_welcome(message: types.Message):
    await message.answer_voice(voice="https://t.me/YAKUDZAForever/8507", 
                               caption="""        
Yakudzaaaaa
                               """)

@dp.message_handler(text="Orqaga")
async def send_welcome(message: types.Message):
    await message.reply("Orqaga", reply_markup=glavniy_menu)

# Audiolar

@dp.message_handler(text="Audiolar")
async def send_welcome(message: types.Message):
    await message.reply("Audiolar", reply_markup=audiolar_menu)

@dp.message_handler(text="1-chi audio")
async def send_welcome(message: types.Message):
    await message.answer_video(video="https://t.me/SBA_001/740", 
                               caption="""        
Asphalt
                               """)
    
@dp.message_handler(text="2-chi audio")
async def send_welcome(message: types.Message):
    await message.answer_video(video="https://t.me/SBA_001/741", 
                               caption="""         
Kino
                               """)

@dp.message_handler(text="3-chi audio")
async def send_welcome(message: types.Message):
    await message.answer_video(video="https://t.me/SBA_001/864", 
                               caption="""       
Sog'indim
                               """)

@dp.message_handler(text="Orqaga")
async def send_welcome(message: types.Message):
    await message.reply("Orqaga", reply_markup=glavniy_menu)

# Giflar

@dp.message_handler(text="Giflar")
async def send_welcome(message: types.Message):
    await message.reply("Giflar", reply_markup=giflar_menu)

@dp.message_handler(text="1-chi gif")
async def send_welcome(message: types.Message):
    await message.answer_animation(animation="https://t.me/giwoek/2", 
                               caption="""        
Siuuuuuu
                               """)

@dp.message_handler(text="2-chi gif")
async def send_welcome(message: types.Message):
    await message.answer_video(video="https://t.me/giwoek/3", 
                               caption="""        
Siuuuuuuuu
                               """)

@dp.message_handler(text="3-chi gif")
async def send_welcome(message: types.Message):
    await message.answer_video(video="https://t.me/giwoek/4", 
                               caption="""        
Siuuuuuuu
                               """)

# Videolar

@dp.message_handler(text="Videolar")
async def send_welcome(message: types.Message):
    await message.reply("Videolar", reply_markup=videolar_menu)

@dp.message_handler(text="1-chi video")
async def send_welcome(message: types.Message):
    await message.answer_video(video="https://t.me/giwoek/5", 
                               caption="""
Sad
                               """)

@dp.message_handler(text="2-chi video")
async def send_welcome(message: types.Message):
    await message.answer_video(video="https://t.me/SBA_001/898",
                               caption="""
Macan Asphalt
                               """)

@dp.message_handler(text="3-chi video")
async def send_welcome(message: types.Message):
    await message.answer_video(video="https://t.me/giwoek/7", 
                               caption="""
BMW
                               """)

@dp.message_handler(text="Orqaga")
async def send_welcome(message: types.Message):
    await message.reply("Orqaga", reply_markup=glavniy_menu)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
