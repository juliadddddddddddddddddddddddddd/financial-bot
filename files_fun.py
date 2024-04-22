from telegram.ext import ConversationHandler
import random
import datetime

res = []

async def files_fun_m(update, context):
    await update.message.reply_text(
        'Пришлите фотографию')
    file = await context.bot.get_file(update.message.photo)
    file_name = fr"C:\Users\Юлия\PycharmProjects\pythonProject4\sources\{file}"
    await file.download_to_drive(file_name)
    res.append(file_name)
    return 1
def file_get():
    file = open(fr'C:\Users\Юлия\PycharmProjects\pythonProject4\sources\{random.choice(res)}.jpeg', 'rb')
    return file
async def files_fun_m_answer(update, context):
    if len(res) != 0:
        await update.message.reply_photo(file_get(), has_spoiler=True)
    else:
        update.message.reply_text("Извините, но загруженных фотографий нет")
    return ConversationHandler.END