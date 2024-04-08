import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from data import db_session
from incomes_fun import income, income_period, add_income
from start_fun import start
from expenses_fun import expenses, staistics_expenses, show_expenses

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)
income_had = MessageHandler(filters.Text(['Доходы']), income)
expense_had = MessageHandler(filters.Text(['Расходы']), expenses)
add_income_had = MessageHandler(filters.Text(['Добавить доход']), add_income)
income_period_had = MessageHandler(filters.Text(['Доходы за определенный период']), income_period)
show_expenses_had = MessageHandler(filters.Text(['Посмотреть расходы']), show_expenses)
staistics_expenses_had = MessageHandler(filters.Text(['Статистика расходов']), staistics_expenses)


def main():
    application = Application.builder().token('7031701033:AAFvF1ARw2Ag9A0qdIGYb17MHLsD843fQ0U').build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(add_income_had)
    application.add_handler(show_expenses_had)
    application.add_handler(income_period_had)
    application.add_handler(income_had)
    application.add_handler(expense_had)
    application.add_handler(staistics_expenses_had)



    application.add_handler(CommandHandler("staistics_expenses", staistics_expenses))
    db_session.global_init("db/money.db")
    application.run_polling()


if __name__ == '__main__':
    main()
