import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler
from data import db_session
from incomes_fun import income, income_period, add_income, add_income_answer, show_income_answer
from start_fun import start
from expenses_fun import expenses, staistics_expenses, show_expenses, chose_category, add_expense, add_expense_answer, \
    staistics_expenses_answer, show_expenses_answer
from files_fun import get_file, upload_photo, get_photo

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)


async def stop(update, context):
    await update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


income_had = MessageHandler(filters.Text(['Доходы']), income)
expense_had = MessageHandler(filters.Text(['Расходы']), expenses)
send_photo = MessageHandler(filters.Text(['Отправить фото']), get_photo)
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

conv_staistics_expenses = ConversationHandler(
    entry_points=[MessageHandler(filters.Text(['Статистика расходов']), staistics_expenses)],
    states={
        1: [MessageHandler(filters.TEXT, staistics_expenses_answer)]},
    fallbacks=[CommandHandler('stop', stop)]
)

conv_show_expense = ConversationHandler(
    entry_points=[MessageHandler(filters.Text(['Посмотреть расходы']), show_expenses)],
    states={
        1: [MessageHandler(filters.TEXT, show_expenses_answer)]},
    fallbacks=[CommandHandler('stop', stop)]
)
conv_income_period = ConversationHandler(
    entry_points=[MessageHandler(filters.Text(['Доходы за определенный период']), income_period)],
    states={
        1: [MessageHandler(filters.TEXT, show_income_answer)]},
    fallbacks=[CommandHandler('stop', stop)]
)

conv_upload_document = ConversationHandler(
    entry_points=[MessageHandler(filters.Text(['Загрузить фото']), get_file)],
    states={
        1: [MessageHandler(filters.Document.Category("image"), upload_photo)]},
    fallbacks=[CommandHandler('stop', stop)]
)


def main():
    application = Application.builder().token('7030384710:AAHMZq8L3MqlclUi5WE7QCeeVgWcan8SOJ4').build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(conv_income_period)
    application.add_handler(income_had)
    application.add_handler(expense_had)
    application.add_handler(conv_handler_incomes)
    application.add_handler(conv_handler_expense)
    application.add_handler(conv_staistics_expenses)
    application.add_handler(conv_show_expense)
    application.add_handler(send_photo)
    application.add_handler(conv_upload_document)
    db_session.global_init("db/money.db")
    application.run_polling()


if __name__ == '__main__':
    main()
