from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
import datetime
from data import db_session
from data.users import User
from data.expenses import Expense
from data.statistics import Statistic


class Expenses:
    def __init__(self):
        self.markup_timer_expenses = ReplyKeyboardMarkup(
            [['Статистика расходов', 'Посмотреть расходы', 'Добавить расходы']],
            one_time_keyboard=True)
        self.markup_show_expenses = ReplyKeyboardMarkup([['1 неделя', '2 недели'], ['Месяц']])
        self.markup = ReplyKeyboardMarkup([['Доходы', 'Расходы'],
                                           ['Загрузить фото', 'Отправить фото'], ['Как заработать деньги?'],
                                           ['Если деньги кончились'], ['Выбрать музыкальное сопровождение']], one_time_keyboard=False)

    async def expenses(self, update, context):
        await update.message.reply_text(
            "Выбери опцию",
            reply_markup=self.markup_timer_expenses
        )

    async def show_expenses(self, update, context):
        await update.message.reply_text(
            "Выбери период, за который хочешь посмотреть расходы",
            reply_markup=self.markup_show_expenses
        )
        return 1

    def show_expenses_bd(self, update, context):
        db_sess = db_session.create_session()
        user_ = update.effective_user
        cur_user = db_sess.query(User).filter(User.name.like(user_.id)).first()
        buttons = db_sess.query(Statistic.name).all()
        name_cat = []
        for i in buttons:
            name_cat.append(i[0])
        if update.message.text == '1 неделя':
            need_date = datetime.datetime.now() - datetime.timedelta(days=7)
        elif update.message.text == '2 недели':
            need_date = datetime.datetime.now() - datetime.timedelta(days=14)
        elif update.message.text == 'Месяц':
            need_date = datetime.datetime.now() - datetime.timedelta(days=30)
        else:
            return 'ошибка'

        moneys = db_sess.query(Expense.money, Expense.date, Expense.statistics_id).filter(
            Expense.date >= need_date).filter(
            Expense.user == cur_user).all()
        res = []
        for i in moneys:
            res.append(f'{i[0]} - {name_cat[i[2] - 1]} - дата {str(i[1])[:10]}')
        moneys = '\n'.join(res)
        return moneys

    async def show_expenses_answer(self, update, context):
        result = self.show_expenses_bd(update, context)
        await update.message.reply_text(
            result,
            reply_markup=self.markup
        )
        return ConversationHandler.END

    def staistics_expenses_bd(self, update, context):
        db_sess = db_session.create_session()
        user_ = update.effective_user
        cur_user = db_sess.query(User).filter(User.name.like(user_.id)).first()
        cur_category = db_sess.query(Statistic).filter(Statistic.name.like(update.message.text)).first()
        moneys = db_sess.query(Expense.money, Expense.date).filter(Expense.statistics == cur_category).filter(
            Expense.user == cur_user).all()
        res = []

        for i in moneys:
            res.append(f'{i[0]} - дата {str(i[1])[:10]}')
        moneys = '\n'.join(res)
        return moneys

    async def staistics_expenses_answer(self, update, context):
        j = self.staistics_expenses_bd(update, context)
        await update.message.reply_text(
            j,
            reply_markup=self.markup
        )
        return ConversationHandler.END

    async def staistics_expenses(self, update, context):
        await update.message.reply_text(
            "Выбери категорию, за которую хочешь узнать расходы",
            reply_markup=self.get_categories()
        )
        return 1

    def get_categories(self):
        db_sess = db_session.create_session()

        buttons = db_sess.query(Statistic.name).all()
        print(buttons)
        but = []
        for i in buttons:
            but.append(i[0])
        markup_staistics_expenses = ReplyKeyboardMarkup.from_column(but)
        return markup_staistics_expenses

    def add_expense_bd(self, update, context):
        db_sess = db_session.create_session()
        user_ = update.effective_user
        cur_user = db_sess.query(User).filter(User.name.like(user_.id)).first()
        cur_category = db_sess.query(Statistic).filter(Statistic.name.like(context.user_data['category'])).first()
        expense = Expense(money=int(update.message.text), date=datetime.datetime.now(), user=cur_user,
                          statistics=cur_category)
        db_sess.add(expense)
        db_sess.commit()
        db_sess.close()

    async def add_expense(self, update, context):
        await update.message.reply_text(
            "Внесите расход")
        context.user_data['category'] = update.message.text
        return 2

    async def chose_category(self, update, context):
        await update.message.reply_text(
            "Выберете категорию за которую хотите внести расход",
            reply_markup=self.get_categories()
        )
        return 1

    async def add_expense_answer(self, update, context):
        await update.message.reply_text(
            f"Расход внесен в базу данных",
            reply_markup=self.markup
        )
        self.add_expense_bd(update, context)
        return ConversationHandler.END