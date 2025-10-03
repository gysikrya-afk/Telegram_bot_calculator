import numexpr
from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from app.keyboard import menu
from app.fsm_group import Calculator

router = Router()

@router.message(F.text == '/start')
async def start(msg):
    await msg.answer('Добро пожаловать в калькулятор!',reply_markup=menu)

@router.message(F.text == 'Что умеет бот')
async def about(msg):
    await msg.answer('Бот имеет функции калькулятора')

@router.message(F.text == 'Запустить калькулятор')
async def start_calculator(msg,state:FSMContext):
    await msg.answer('Калькулятор запущен.Введите пример.')
    await state.set_state(Calculator.operations)

@router.message(Calculator.operations)
async def calculator_operations(msg):
    expr = msg.text.replace(',', '.')
    try:
        result = numexpr.evaluate(expr)
        await msg.answer(f'Результат: {result}')
    except Exception:
        await msg.answer('Ошибка! Введите корректное число или математическое выражение.')
      
