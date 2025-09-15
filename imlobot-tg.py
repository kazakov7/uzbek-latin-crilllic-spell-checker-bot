import asyncio
import logging
import sys
import nest_asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from checkword import checkWord


# 🔹 Bot tokeningizni shu yerga yozing
API_TOKEN = "7187392308:AAHmkRWaApbJKLDfniJmVZCo10Lcxf82oyw"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Salom! Menga so'z yuboring, men uni tekshirib beraman ✅")


@dp.message()
async def echo_handler(message: Message):
    if not message.text:  # faqat matn ishlasin
        await message.answer("❌ Iltimos, matn yuboring!")
        return

    result = checkWord(message.text)
    if result["available"]:
        await message.answer(f"✅ So'z to'g'ri yozilgan: {result['matches'][0]}")
    else:
        if result["matches"]:  # agar tahminlar bo'lsa
            await message.answer(
                "❌ So'z topilmadi.\n👉 Ehtimoliy to‘g‘ri variantlar:\n" +
                "\n".join(result["matches"])
            )
        else:
            await message.answer("❌ So'z topilmadi va o‘xshash variantlar ham yo‘q.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    nest_asyncio.apply()
    asyncio.get_event_loop().run_until_complete(main())
