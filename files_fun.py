import random
from random import randint
from start_fun import markup
from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler

res = []


async def get_file(update, context):
    await update.message.reply_text(
        'Загрузите фото')
    return 1


async def upload_photo(update, context):
    file_id = update.message.document.file_id
    new_file = await context.bot.get_file(file_id)
    await new_file.download_to_drive(custom_path=f"./sources/upload_photo/{file_id}.jpg")
    res.append(update.message.document.file_id)
    await update.message.reply_text(
        'Фото успешно загружено')
    return ConversationHandler.END


def file_get():
    file = open(f'sources/upload_photo/{random.choice(res)}.jpg', 'rb')


async def get_photo(update, context):
    if len(res) != 0:
        await update.message.reply_photo(file_get(), has_spoiler=True)
    else:
        await update.message.reply_text(
            'Пожалуйста, загрузите сначала фото')


def file_geto():
    file = open(f'sources/pictures/{randint(1, 11)}.jpeg', 'rb')
    return file


async def files_fun(update, context):
    await update.message.reply_photo(file_geto(), has_spoiler=True)


async def files_fun_m(update, context):
    await update.message.reply_text(
        'Выберете цифру',
        reply_markup=markup_f
    )
    return 1


async def files_fun_m_answer(update, context):
    await update.message.reply_audio(f'sources/music/{update.message.text}.mp3', reply_markup=markup)
    return ConversationHandler.END


reply_keyboard = [['1'], ['2'], ['3'], ['4']]
markup_f = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
