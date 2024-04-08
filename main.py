import logging
from telegram.ext import Application, CommandHandler
from data import db_session
from incomes_fun import income, income_period, add_income
from start_fun import start
from expenses_fun import expenses, staistics_expenses, show_expenses

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


def main():
    application = Application.builder().token('7031701033:AAFvF1ARw2Ag9A0qdIGYb17MHLsD843fQ0U').build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("income", income))
    application.add_handler(CommandHandler("expenses", expenses))
    application.add_handler(CommandHandler("income", income))
    application.add_handler(CommandHandler("income_period", income_period))
    application.add_handler(CommandHandler("add_income", add_income))
    application.add_handler(CommandHandler("show_expenses", show_expenses))
    application.add_handler(CommandHandler("staistics_expenses", staistics_expenses))
    db_session.global_init("db/money.db")
    application.run_polling()


if __name__ == '__main__':
    main()
