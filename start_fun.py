from telegram import ReplyKeyboardMarkup


async def start(update, context):
    await update.message.reply_text(
        "Я бот-помощник для контроля финансов. Выбери опцию.",
        reply_markup=markup
    )


reply_keyboard = [['/income', '/expenses'],
                  ['/выбрать музыкальное сопровождение']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
