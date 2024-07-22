from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

main_menu =  ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="Выберите пункт меню", keyboard=[
    [KeyboardButton(text='💸Валютные пары',)],
    [KeyboardButton(text='🧾Новости'), KeyboardButton(text='⭐️Избранное')],
])

ikb_currency = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='EUR/USD', callback_data='eur/usd'), InlineKeyboardButton(text='USD/CAD', callback_data='usd/cad')],
])

ikb_return = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Возврат', callback_data='return')],
])