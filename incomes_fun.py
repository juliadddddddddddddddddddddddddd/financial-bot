from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
from data import db_session
from data.users import User
from data.incomes import Income
import datetime

reply_keyboard_income = [['Добавить доход', 'Доходы за определенный период']]
markup_income = ReplyKeyboardMarkup(reply_keyboard_income, one_time_keyboard=False)

reply_keyboard_income_period = [['1 неделя ', '2 недели '],
                                ['Месяц ']]
markup_income_period = ReplyKeyboardMarkup(reply_keyboard_income_period, one_time_keyboard=False)

reply_keyboard_add_income = [['Добавить доход:']]
markup_add_income = ReplyKeyboardMarkup(reply_keyboard_add_income, one_time_keyboard=False)


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
        "Внесите доход",
        reply_markup=markup_add_income
    )
    return 1


async def add_income_answer(update, context):
    # Это ответ на первый вопрос.
    # Мы можем использовать его во втором вопросе.
    # context.user_data['income'] = int(update.message.text)
    await update.message.reply_text(
        f"Доход внесен в базу данных")
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
