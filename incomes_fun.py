from telegram.ext import ConversationHandler
from telegram import ReplyKeyboardMarkup
from data import db_session
from data.users import User
from data.incomes import Income
import datetime


class Incomes:
    def __init__(self):
        self.markup = ReplyKeyboardMarkup([['Доходы', 'Расходы'],
                                           ['Загрузить фото', 'Отправить фото'], ['Как заработать деньги?'],
                                           ['Если деньги кончились'], ['Выбрать музыкальное сопровождение']],
                                          one_time_keyboard=False)
        self.markup_income = ReplyKeyboardMarkup([['Добавить доход', 'Доходы за определенный период']],
                                                 one_time_keyboard=True)
        self.markup_income_period = ReplyKeyboardMarkup([['1 неделя ', '2 недели '],
                                                         ['Месяц ']], one_time_keyboard=True)

    def add_income_bd(self, update, context):
        db_sess = db_session.create_session()
        user_ = update.effective_user
        cur_user = db_sess.query(User).filter(User.name.like(user_.id)).first()
        income = Income(money=int(update.message.text), date=datetime.datetime.now(), user=cur_user)
        db_sess.add(income)
        db_sess.commit()
        db_sess.close()

    async def add_income(self, update, context):
        await update.message.reply_text(
            "Внесите доход")
        return 1

    async def add_income_answer(self, update, context):
        await update.message.reply_text(
            f"Доход внесен в базу данных",
            reply_markup=self.markup
        )
        self.add_income_bd(update, context)
        return ConversationHandler.END

    async def income(self, update, context):
        await update.message.reply_text(
            "Выбери опцию",
            reply_markup=self.markup_income
        )

    async def income_period(self, update, context):
        await update.message.reply_text(
            "Выберите период, за который вас интересуют расходы",
            reply_markup=self.markup_income_period
        )
        return 1

    def show_income_bd(self, update, context):
        db_sess = db_session.create_session()
        user_ = update.effective_user
        cur_user = db_sess.query(User).filter(User.name.like(user_.id)).first()
        if update.message.text == '1 неделя':
            need_date = datetime.datetime.now() - datetime.timedelta(days=7)
        elif update.message.text == '2 недели':
            need_date = datetime.datetime.now() - datetime.timedelta(days=14)
        elif update.message.text == 'Месяц':
            need_date = datetime.datetime.now() - datetime.timedelta(days=30)
        else:
            return 'ошибка'

        moneys = db_sess.query(Income.money, Income.date).filter(
            Income.date >= need_date).filter(
            Income.user == cur_user).all()
        res = []
        for i in moneys:
            res.append(f'{i[0]}  - дата {str(i[1])[:10]}')
        moneys = '\n'.join(res)
        return moneys

    async def show_income_answer(self, update, context):
        result = self.show_income_bd(update, context)
        result = result if result else 'Нет доходов за данный период'
        await update.message.reply_text(
            result,
            reply_markup=self.markup
        )
        return ConversationHandler.END
