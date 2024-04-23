from telegram.ext import ConversationHandler
import random
import datetime

res = []

async def get_photo(update, context):
    await update.message.reply_text(
        'Загрузите фото')
    return 1

async def upload_photo(update, context):
    file_id = update.message.document.file_id
    new_file = await context.bot.get_file(file_id)
    await new_file.download_to_drive(custom_path="./dir/test.webp")
    res.append(new_file)
    print(res)

    # НЕ РАБОТАЕТ!
    # new_file = await update.message.effective_attachment.get_file()
    # file_name = fr"C:\Users\Юлия\PycharmProjects\pythonProject4\sources\{new_file}"
    # await new_file.download_to_drive(file_name)


    # НЕ РАБОТАЕТ!
    # new_file = await update.message.effective_attachment[-1].get_file()
    # file_name = fr"C:\Users\Юлия\PycharmProjects\pythonProject4\sources\{new_file}"
    # await new_file.download_to_drive(file_name)
    # res.append(file_name)
    # print(res)

    # НЕ РАБОТАЕТ!
    # file = await context.bot.get_file(update.message.photo)
    # file_name = fr"C:\Users\Юлия\PycharmProjects\pythonProject4\sources\{file}"
    # await file.download_to_drive(custom_path=file_name)
    # res.append(file_name)

