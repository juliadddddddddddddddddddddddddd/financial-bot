import random
from telegram.ext import ConversationHandler


class Files:
    def __init__(self):
        self.res = []

    async def get_file(self, update, context):
        await update.message.reply_text(
            'Загрузите фото')
        return 1

    async def upload_photo(self, update, context):
        file_id = update.message.document.file_id
        new_file = await context.bot.get_file(file_id)
        await new_file.download_to_drive(custom_path=f"./sources/upload_photo/{file_id}.jpg")
        self.res.append(update.message.document.file_id)
        await update.message.reply_text(
            'Фото успешно загружено')
        return ConversationHandler.END

    def file_get(self):
        file = open(f'sources/upload_photo/{random.choice(self.res)}.jpg', 'rb')
        return file

    async def get_photo(self, update, context):
        if len(self.res) != 0:
            await update.message.reply_photo(self.file_get(), has_spoiler=True)
        else:
            await update.message.reply_text(
                'Пожалуйста, загрузите сначала фото')