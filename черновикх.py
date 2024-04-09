import datetime

from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, filters
from data.incomes import Income


async def add_income(update, context):
    await update.message.reply_text(
        "Внесите доход",
        reply_markup=markup_add_income
    )
    return 1

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
    cur_user = db_sess.query(User).filter(User.id = context.user_data['id_user']).first()
    income = Income(money=context.user_data['income'], data=datetime.datetime.now(), user=cur_user)
    db_sess.add(income)
    db_sess.commit()
    db_sess.close()
