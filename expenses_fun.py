from telegram import ReplyKeyboardMarkup


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


async def staistics_expenses(update, context):
    await update.message.reply_text(
        "Выбери категорию, за которую хочешь узнать расходы",
        reply_markup=markup_staistics_expenses
    )


reply_keyboard_expenses = [['Статистика расходов', 'Посмотреть расходы']]
markup_timer_expenses = ReplyKeyboardMarkup(reply_keyboard_expenses, one_time_keyboard=False)

reply_keyboard_staistics_expenses = [['магазины', '/образование']]
markup_staistics_expenses = ReplyKeyboardMarkup(reply_keyboard_staistics_expenses, one_time_keyboard=False)

reply_keyboard_show_expenses = [['1 неделя', '2 недели']]
markup_show_expenses = ReplyKeyboardMarkup(reply_keyboard_show_expenses, one_time_keyboard=False)
