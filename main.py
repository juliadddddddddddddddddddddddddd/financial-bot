import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler
import config
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import time as t
import random


# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def start(update, context):
    await update.message.reply_text(
        "Я бот-помощник для контроля финансов. Выбери опцию.",
        reply_markup=markup
    )

async def income(update, context):
    await update.message.reply_text(
        "Выбери опцию",
        reply_markup=markup_income
    )


async def income_period(update, context):
    await update.message.reply_text(
        "Выберите период, за который вас интересуют расходы",
        reply_markup=markup_income_period
    )

async def add_income(update, context):
    data = int(context.args[0])
    await update.message.reply_text(f"{data}")


reply_keyboard = [['/income', '/expenses'],
                  ['/выбрать музыкальное сопровождение']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

reply_keyboard_income = [['/add_income', '/income_period']]
markup_income = ReplyKeyboardMarkup(reply_keyboard_income, one_time_keyboard=False)

reply_keyboard_income_period = [['/1 week', '/2 weeks'],
                                ['/month']]
markup_income_period = ReplyKeyboardMarkup(reply_keyboard_income_period, one_time_keyboard=False)


def main():
    application = Application.builder().token('7030384710:AAHMZq8L3MqlclUi5WE7QCeeVgWcan8SOJ4').build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("income", income))
    application.add_handler(CommandHandler("income_period", income_period))
    application.add_handler(CommandHandler("add_income", add_income))
    application.run_polling()

# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()