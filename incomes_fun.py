from telegram.ext import ConversationHandler
from telegram import ReplyKeyboardMarkup
from data import db_session
from data.users import User
from data.incomes import Income
import datetime
from start_fun import markup

reply_keyboard_income = [['Добавить доход', 'Доходы за определенный период']]
markup_income = ReplyKeyboardMarkup(reply_keyboard_income, one_time_keyboard=True)

reply_keyboard_income_period = [['1 неделя ', '2 недели '],
                                ['Месяц ']]
markup_income_period = ReplyKeyboardMarkup(reply_keyboard_income_period, one_time_keyboard=True)


def add_income_bd(update, context):
    db_sess = db_session.create_session()
    user_ = update.effective_user
    cur_user = db_sess.query(User).filter(User.name.like(user_.id)).first()
    income = Income(money=int(update.message.text), date=datetime.datetime.now(), user=cur_user)
    db_sess.add(income)
    db_sess.commit()
    db_sess.close()


async def add_income(update, context):
    await update.message.reply_text(
        "Внесите доход")
    return 1


async def add_income_answer(update, context):
    await update.message.reply_text(
        f"Доход внесен в базу данных",
        reply_markup=markup
    )
    add_income_bd(update, context)
    return ConversationHandler.END


async def income(update, context):
    await update.message.reply_text(
        "Выбери опцию",
        reply_markup=markup_income
    )


async def income_period(update, context):
    await update.message.reply_text(
        "Выберите период, за который вас интересуют расходы",
        reply_markup=markup_income_period
    )
    return 1


def show_income_bd(update, context):
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


async def show_income_answer(update, context):
    result = show_income_bd(update, context)
    await update.message.reply_text(
        result,
        reply_markup=markup
    )
    return ConversationHandler.END