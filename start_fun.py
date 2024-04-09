from telegram import ReplyKeyboardMarkup
from data.users import User
from data import db_session


def add_user(update, context):
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


async def start(update, context):
    await update.message.reply_text(
        "Я бот-помощник для контроля финансов. Выбери опцию.",
        reply_markup=markup
    )
    add_user(update, context)


reply_keyboard = [['Доходы', 'Расходы'],
                  ['Выбрать музыкальное сопровождение', 'Совет по финансам от нейросити']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
