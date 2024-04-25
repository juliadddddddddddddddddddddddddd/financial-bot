from random import randint

from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler


class Music:
    def __init__(self):
        self.markup_f = ReplyKeyboardMarkup([['1'], ['2'], ['3'], ['4'], ['5'], ['6'], ['7'], ['8'], ['9'], ['10']],
                                            one_time_keyboard=False)
        self.markup = ReplyKeyboardMarkup([['Доходы', 'Расходы'],
                                           ['Загрузить фото', 'Отправить фото'], ['Как заработать деньги?'],
                                           ['Если деньги кончились'], ['Выбрать музыкальное сопровождение']],
                                          one_time_keyboard=False)

    async def files_fun_m(self, update, context):
        await update.message.reply_text(
            'Выберете цифру',
            reply_markup=self.markup_f
        )
        return 1

    async def files_fun_m_answer(self, update, context):
        await update.message.reply_audio(f'sources/music/{update.message.text}.mp3', reply_markup=self.markup)
        return ConversationHandler.END


class Random_photo:

    async def files_fun(self, update, context):
        await update.message.reply_photo(self.file_geto(), has_spoiler=True)

    def file_geto(self):
        file = open(f'sources/pictures/{randint(1, 14)}.jpeg', 'rb')
        return file
