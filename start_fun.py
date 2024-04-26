from telegram import ReplyKeyboardMarkup
from data.users import User
from data import db_session


class Start:
    def __init__(self):
        self.markup = ReplyKeyboardMarkup([['Доходы', 'Расходы'],
                                           ['Загрузить фото', 'Отправить фото'], ['Как заработать деньги?'],
                                           ['Если деньги кончились'], ['Выбрать музыкальное сопровождение']], one_time_keyboard=False)

    def add_user(self, update, context):
        db_sess = db_session.create_session()
        user_ = update.effective_user
        if not db_sess.query(User).filter(User.name.like(user_.id)).first():
            user = User()
            user.name = f"{user_.id}"
            db_sess.add(user)
            db_sess.commit()
        cur_user = db_sess.query(User).filter(User.name.like(user_.id)).first()
        context.user_data['id_user'] = cur_user.id
        context.user_data['name_user'] = cur_user.name
        db_sess.close()

    async def start(self, update, context):
        await update.message.reply_text(
            "Я бот-помощник для контроля финансов. Выбери опцию.",
            reply_markup=self.markup
        )
        self.add_user(update, context)