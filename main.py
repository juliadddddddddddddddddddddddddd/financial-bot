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
    await update.message.reply_text(
        "Внесите доход",
        reply_markup=markup_add_income
    )

async def expenses(update, context):
    await update.message.reply_text(
        "Выбери опцию",
        reply_markup=markup_timer_expenses
    )

async def show_expenses(update, context):
    await update.message.reply_text(
        "Выбери период, за который хочешь посмотреть расходы",
        reply_markup=markup_show_expenses
    )

async def staistics_expenses(update, context):
    await update.message.reply_text(
        "Выбери категорию, за которую хочешь узнать расходы",
        reply_markup=markup_staistics_expenses
    )

reply_keyboard = [['/income', '/expenses'],
                  ['/выбрать музыкальное сопровождение']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

reply_keyboard_income = [['/add_income', '/income_period']]
markup_income = ReplyKeyboardMarkup(reply_keyboard_income, one_time_keyboard=False)

reply_keyboard_income_period = [['/1 неделя', '/2 недели'],
                                ['/месяц']]
markup_income_period = ReplyKeyboardMarkup(reply_keyboard_income_period, one_time_keyboard=False)

reply_keyboard_add_income = [['/добавить доход']]
markup_add_income = ReplyKeyboardMarkup(reply_keyboard_add_income, one_time_keyboard=False)

reply_keyboard_expenses = [['/staistics_expenses', '/show_expenses']]
markup_timer_expenses = ReplyKeyboardMarkup(reply_keyboard_expenses, one_time_keyboard=False)

reply_keyboard_staistics_expenses = [['/магазины', '/образование']]
markup_staistics_expenses = ReplyKeyboardMarkup(reply_keyboard_staistics_expenses, one_time_keyboard=False)

reply_keyboard_show_expenses = [['/1 неделя', '/2 недели']]
markup_show_expenses = ReplyKeyboardMarkup(reply_keyboard_show_expenses, one_time_keyboard=False)
def main():
    application = Application.builder().token('7030384710:AAHMZq8L3MqlclUi5WE7QCeeVgWcan8SOJ4').build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("income", income))
    application.add_handler(CommandHandler("expenses", expenses))
    application.add_handler(CommandHandler("income", income))
    application.add_handler(CommandHandler("income_period", income_period))
    application.add_handler(CommandHandler("add_income", add_income))
    application.add_handler(CommandHandler("show_expenses", show_expenses))
    application.add_handler(CommandHandler("staistics_expenses", staistics_expenses))
    application.run_polling()

# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()