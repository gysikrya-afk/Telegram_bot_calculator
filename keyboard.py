from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Запустить калькулятор')],
        [KeyboardButton(text='Что умеет бот')]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)
