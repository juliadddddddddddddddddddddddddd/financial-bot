from random import randint

from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler

from start_fun import markup


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