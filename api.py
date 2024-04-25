import requests
from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler


class Api:
    def __init__(self):
        self.markup_category_of_books = ReplyKeyboardMarkup(
            [['Банки'], ['Финансовая грамотность'], ['Предпринимательство'], ['Бизнес']], one_time_keyboard=False)
        self.markup = ReplyKeyboardMarkup([['Доходы', 'Расходы'],
                                           ['Загрузить фото', 'Отправить фото'], ['Как заработать деньги?'],
                                           ['Если деньги кончились'], ['Выбрать музыкальное сопровождение']],
                                          one_time_keyboard=False)

    async def category_of_books(self, update, context):
        await update.message.reply_text(
            'Выберите тему, по которой вы бы хотели прочитать книгу',
            reply_markup=self.markup_category_of_books)
        return 1

    async def get_books(self, update, context):
        res = []
        endpoint = "https://www.googleapis.com/books/v1/volumes"
        query = update.message.text

        params = {"q": query, "maxResults": 5}
        response = requests.get(endpoint, params=params).json()
        for book in response["items"]:
            volume = book["volumeInfo"]
            title = volume["title"]
            authors = volume["authors"]
            published = volume.get("publishedDate", "год издания неизвестен")
            description = volume.get("description", "описание отсутствует")
            res.append(f"{title}. Автор: {', '.join(authors)}")
        for elem in res:
            await update.message.reply_text(f"{elem}", reply_markup=self.markup)
        return ConversationHandler.END
