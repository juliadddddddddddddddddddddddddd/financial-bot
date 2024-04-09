import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler
from data import db_session
from incomes_fun import income, income_period, add_income, add_income_answer
from start_fun import start
from expenses_fun import expenses, staistics_expenses, show_expenses, chose_category, add_expense, add_expense_answer

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)


async def stop(update, context):
    await update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


income_had = MessageHandler(filters.Text(['Доходы']), income)
expense_had = MessageHandler(filters.Text(['Расходы']), expenses)
income_period_had = MessageHandler(filters.Text(['Доходы за определенный период']), income_period)
show_expenses_had = MessageHandler(filters.Text(['Посмотреть расходы']), show_expenses)
staistics_expenses_had = MessageHandler(filters.Text(['Статистика расходов']), staistics_expenses)
conv_handler_incomes = ConversationHandler(
    entry_points=[MessageHandler(filters.Text(['Добавить доход']), add_income)],
    states={
        1: [MessageHandler(filters.TEXT, add_income_answer)]},
    fallbacks=[CommandHandler('stop', stop)]
)
conv_handler_expense = ConversationHandler(
    entry_points=[MessageHandler(filters.Text(['Добавить расходы']), chose_category)],
    states={
        1: [MessageHandler(filters.TEXT, add_expense)],
        2: [MessageHandler(filters.TEXT, add_expense_answer)]},
    fallbacks=[CommandHandler('stop', stop)]
)


def main():
    application = Application.builder().token('7031701033:AAFvF1ARw2Ag9A0qdIGYb17MHLsD843fQ0U').build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(show_expenses_had)
    application.add_handler(income_period_had)
    application.add_handler(income_had)
    application.add_handler(expense_had)
    application.add_handler(staistics_expenses_had)
    application.add_handler(conv_handler_incomes)
    application.add_handler(conv_handler_expense)
    db_session.global_init("db/money.db")
    application.run_polling()


if __name__ == '__main__':
    main()
