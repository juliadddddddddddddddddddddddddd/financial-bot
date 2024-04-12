from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
from data import db_session
from data.users import User
from data.incomes import Income
import datetime
from start_fun import markup
import datetime

from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, filters
from data.incomes import Income

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

def incomess_period_db(update, context):
    db_sess = db_session.create_session()
    user_ = update.effective_user
    cur_user = db_sess.query(User).filter(User.name.like(user_.id)).first()
    cur_period = db_sess.query(Income).filter(Income.date.like(update.message.text)).first()
    moneys = db_sess.query(Income.money, Income.date).filter(Income.date == cur_period).filter(
        Income.user == cur_user).all()
    res = []

    for i in moneys:
        res.append(f'{i[0]} - дата {str(i[1])[:10]}')
    moneys = '\n'.join(res)
    return moneys


async def add_income_answer(update, context):
    # Это ответ на первый вопрос.
    # Мы можем использовать его во втором вопросе.
    context.user_data['income'] = int(update.message.text)
    await update.message.reply_text(
        f"Доход внесен в базу данных")
    add_income_bd(update, context)

    return ConversationHandler.END


def add_income_bd(update, context):
    db_sess = db_session.create_session()
    cur_user = db_sess.query(User).filter(User.id == context.user_data['user_id']).first()
    income = Income(money=context.user_data['income'], data=datetime.datetime.now(), user=cur_user)
    db_sess.add(income)
    db_sess.commit()
    db_sess.close()