from telegram import ReplyKeyboardMarkup

reply_keyboard_income = [['/add_income', '/income_period']]
markup_income = ReplyKeyboardMarkup(reply_keyboard_income, one_time_keyboard=False)

reply_keyboard_income_period = [['/1 неделя', '/2 недели'],
                                ['/месяц']]
markup_income_period = ReplyKeyboardMarkup(reply_keyboard_income_period, one_time_keyboard=False)

reply_keyboard_add_income = [['/добавить доход']]
markup_add_income = ReplyKeyboardMarkup(reply_keyboard_add_income, one_time_keyboard=False)


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


async def add_income(update, context):
    await update.message.reply_text(
        "Внесите доход",
        reply_markup=markup_add_income
    )
