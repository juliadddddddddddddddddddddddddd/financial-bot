from telegram.ext import ConversationHandler
import random
import datetime

res = []
async def get_file(update, context):
    await update.message.reply_text(
        'Загрузите фото')
    return 1

async def upload_photo(update, context):
    file_id = update.message.document.file_id
    new_file = await context.bot.get_file(file_id)
    await new_file.download_to_drive(custom_path=f"./sources/{file_id}.jpg")
    res.append(update.message.document.file_id)
    await update.message.reply_text(
        'Фото успешно загружено')



def file_get():
    file = open(f'sources/{random.choice(res)}.jpg', 'rb')
    return file

async def get_photo(update, context):
    if len(res) != 0:
        await update.message.reply_photo(file_get(), has_spoiler=True)
    else:
        await update.message.reply_text(
            'Пожалуйста, загрузите сначала фото')
