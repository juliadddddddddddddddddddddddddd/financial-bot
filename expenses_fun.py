from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
from datetime import datetime
from data import db_session
from data.statistics import Statistic
from start_fun import markup
from data.users import User
from data.expenses import Expense
from data.statistics import Statistic


async def expenses(update, context):
    await update.message.reply_text(
        "Выбери опцию",
        reply_markup=markup_timer_expenses
    )


async def show_expenses(update, context):
    await update.message.reply_text(
        "Выбери период, за который хочешь посмотреть расходы",
        reply_markup=markup_show_expenses
    )


def get_id(name_table, name):
    db_sess = db_session.create_session()
    res = db_sess.query(name_table.id).filter(name_table.name.like(name)).first()
    print('h')
    db_sess.close()
    return res


def staistics_expenses_bd(update, context):
    db_sess = db_session.create_session()
    user_ = update.effective_user
    cur_user = db_sess.query(User).filter(User.name.like(user_.id)).first()
    cur_category = db_sess.query(Statistic).filter(Statistic.name.like(update.message.text)).first()
    moneys = db_sess.query(Expense.money, Expense.date).filter(Expense.statistics == cur_category).filter(
        Expense.user == cur_user).all()
    res = []

    for i in moneys:
        res.append(f'{i[0]} - дата {str(i[1])[:10]}')
        print(i)
    moneys = '\n'.join(res)
    return moneys


async def staistics_expenses_answer(update, context):
    j = staistics_expenses_bd(update, context)
    await update.message.reply_text(
        j,
        reply_markup=markup
    )
    return ConversationHandler.END


async def staistics_expenses(update, context):
    await update.message.reply_text(
        "Выбери категорию, за которую хочешь узнать расходы",
        reply_markup=get_categories()
    )
    return 1


def get_categories():
    db_sess = db_session.create_session()

    buttons = db_sess.query(Statistic.name).all()
    print(buttons)
    but = []
    for i in buttons:
        but.append(i[0])
    markup_staistics_expenses = ReplyKeyboardMarkup.from_column(but)
    return markup_staistics_expenses


def add_expense_bd(update, context):
    db_sess = db_session.create_session()
    user_ = update.effective_user
    cur_user = db_sess.query(User).filter(User.name.like(user_.id)).first()
    cur_category = db_sess.query(Statistic).filter(Statistic.name.like(context.user_data['category'])).first()
    expense = Expense(money=int(update.message.text), date=datetime.datetime.now(), user=cur_user,
                      statistics=cur_category)
    db_sess.add(expense)
    db_sess.commit()
    db_sess.close()


async def add_expense(update, context):
    await update.message.reply_text(
        "Внесите расход")
    context.user_data['category'] = update.message.text
    return 2


async def chose_category(update, context):
    await update.message.reply_text(
        "Выберете категорию за которую хотите внести расход",
        reply_markup=get_categories()
    )
    return 1


async def add_expense_answer(update, context):
    await update.message.reply_text(
        f"Расход внесен в базу данных",
        reply_markup=markup
    )
    add_expense_bd(update, context)
    return ConversationHandler.END


reply_keyboard_expenses = [['Статистика расходов', 'Посмотреть расходы', 'Добавить расходы']]
markup_timer_expenses = ReplyKeyboardMarkup(reply_keyboard_expenses, one_time_keyboard=True)
reply_keyboard_show_expenses = [['1 неделя', '2 недели']]
markup_show_expenses = ReplyKeyboardMarkup(reply_keyboard_show_expenses, one_time_keyboard=True)
