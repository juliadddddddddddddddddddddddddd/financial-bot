import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler
from data import db_session
from incomes_fun import Incomes
from start_fun import Start
from expenses_fun import Expenses
from files_fun import Files
from entertainments import Music, Random_photo

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)


async def stop(update, context):
    await update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


incomes = Incomes()
music = Music()
random_photo = Random_photo()
expense = Expenses()
file = Files()
start = Start()

income_had = MessageHandler(filters.Text(['Доходы']), incomes.income)
expense_had = MessageHandler(filters.Text(['Расходы']), expense.expenses)
files_had = MessageHandler(filters.Text(['Что-то']), random_photo.files_fun)
conv_handler_incomes = ConversationHandler(
    entry_points=[MessageHandler(filters.Text(['Добавить доход']), incomes.add_income)],
    states={
        1: [MessageHandler(filters.TEXT, incomes.add_income_answer)]},
    fallbacks=[CommandHandler('stop', stop)]
)
conv_handler_expense = ConversationHandler(
    entry_points=[MessageHandler(filters.Text(['Добавить расходы']), expense.chose_category)],
    states={
        1: [MessageHandler(filters.TEXT, expense.add_expense)],
        2: [MessageHandler(filters.TEXT, expense.add_expense_answer)]},
    fallbacks=[CommandHandler('stop', stop)]
)

conv_staistics_expenses = ConversationHandler(
    entry_points=[MessageHandler(filters.Text(['Статистика расходов']), expense.staistics_expenses)],
    states={
        1: [MessageHandler(filters.TEXT, expense.staistics_expenses_answer)]},
    fallbacks=[CommandHandler('stop', stop)]
)

conv_show_expense = ConversationHandler(
    entry_points=[MessageHandler(filters.Text(['Посмотреть расходы']), expense.show_expenses)],
    states={
        1: [MessageHandler(filters.TEXT, expense.show_expenses_answer)]},
    fallbacks=[CommandHandler('stop', stop)]
)
conv_income_period = ConversationHandler(
    entry_points=[MessageHandler(filters.Text(['Доходы за определенный период']), incomes.income_period)],
    states={
        1: [MessageHandler(filters.TEXT, incomes.show_income_answer)]},
    fallbacks=[CommandHandler('stop', stop)]
)

conv_music = ConversationHandler(
    entry_points=[MessageHandler(filters.Text(['Выбрать музыкальное сопровождение']), music.files_fun_m)],
    states={
        1: [MessageHandler(filters.TEXT, music.files_fun_m_answer)]},
    fallbacks=[CommandHandler('stop', stop)]
)

conv_files = ConversationHandler(
    entry_points=[MessageHandler(filters.Text(['Загрузить фото']), file.get_file)],
    states={
        1: [MessageHandler(filters.Document.Category("image"), file.upload_photo)]},
    fallbacks=[CommandHandler('stop', stop)]
)


def main():
    application = Application.builder().token('6776095239:AAEuFXOBSoy-LdLdIDWywjgfJpVze0H_3Q8').build()
    application.add_handler(CommandHandler("start", start.start))
    application.add_handler(conv_income_period)
    application.add_handler(income_had)
    application.add_handler(expense_had)
    application.add_handler(conv_handler_incomes)
    application.add_handler(conv_handler_expense)
    application.add_handler(conv_staistics_expenses)
    application.add_handler(conv_show_expense)
    application.add_handler(files_had)
    application.add_handler(conv_music)
    application.add_handler(conv_files)
    db_session.global_init("db/money.db")
    application.run_polling()


if __name__ == '__main__':
    main()
