import random
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    CallbackContext,
    filters,
    MessageHandler,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Привет, я бот Sigma, я был создан в качестве учебного материала и не имею никаких полезных функций. Я просто существую для теста, ничего больше.\n"
        f"Вот мой список команд:\n"
        f"/who выводит ID чата, ID сообщения, ID отправителя, имя отправителя и дату отправки сообщения.\n"
        f"/rand %i %j выводит случайное число между %i и %j.",
    )


async def who(update: Update, context: ContextTypes.DEFAULT_TYPE):
    formatted_date = update.message.date.strftime("%d.%m.%Y")
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(
            f"ID чата: {update.effective_chat.id}\n"
            f"ID сообщения: {update.message.message_id}\n"
            f"ID отправителя: {update.effective_user.id}\n"
            f"Имя отправителя: {update.effective_user.username}\n"
            f"Дата отправки сообщения: {formatted_date}"
        ),
    )


async def rand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    i = int(context.args[0])
    j = int(context.args[1])
    if i > j:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Введены неверные аргументы. %i должно быть меньше %j.",
        )
    elif i == j:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Введены одинаковые аргументы. %i должно быть меньше %j.",
        )

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=str(random.randint(i, j))
    )


async def sigma(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await context.bot.send_voice(
            chat_id=update.effective_chat.id,
            voice=open(
                "C:/Users/Admincheg/Sigma/INTERWORLD_-_METAMORPHOSIS_73761657.mp3", "rb"
            ),
        )



async def voice(update: Update, context: CallbackContext) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Я бумер и не понимаю голосовые сообщения.",
    )


async def photo(update: Update, context: CallbackContext) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Боже, какое красивое изображение, отправьте мне ещё таких.",
    )



if __name__ == "__main__":
    application = (
        ApplicationBuilder()
        .token("7673937109:AAHhxtBNTwPe-YYPR0p3qP5KXWIC0a6L1k4")
        .build()
    )

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    who_handler = CommandHandler("who", who)
    application.add_handler(who_handler)

    rand_handler = CommandHandler("rand", rand)
    application.add_handler(rand_handler)

    sigma_handler = CommandHandler("sigma", sigma)
    application.add_handler(sigma_handler)

    photo_handler = MessageHandler(filters.PHOTO, photo)
    application.add_handler(photo_handler)

    voice_handler = MessageHandler(filters.VOICE, voice)
    application.add_handler(voice_handler)

    application.run_polling()
