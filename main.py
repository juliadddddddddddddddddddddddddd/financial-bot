import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler
from start_fun import start
from files_fun import files_fun_m, files_fun_m_answer

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)


async def stop(update, context):
    await update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


conv_music = ConversationHandler(
    entry_points=[MessageHandler(filters.Text(['Выбрать музыкальное сопровождение']), files_fun_m)],
    states={
        1: [MessageHandler(filters.TEXT, files_fun_m_answer)]},
    fallbacks=[CommandHandler('stop', stop)]
)

def main():
    application = Application.builder().token('7030384710:AAHMZq8L3MqlclUi5WE7QCeeVgWcan8SOJ4').build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(conv_music)
    application.run_polling()


if __name__ == '__main__':
    main()
