from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from module_13.module_13_2 import api_key
from crud_functions import get_all_products
from keybords import *


api = api_key.api_key
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=start_menu)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=ikb)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Упращенная формула для мужчин: 10 х вес(кг) + 6,25 x '
                              'рост(см) – 5 х возраст(г) + 5')
    await call.answer()


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    products = get_all_products()
    for product in products:
        id, title, description, price = product
        await message.answer(f'Название: {title} | Описание: {description} | Цена: {price}')
        with open(f'D:/University_Urban/module_14/file/img{id}.png', 'rb') as img:
            await message.answer_photo(img)
    await message.answer("Выберите продукт для покупки:", reply_markup=catalog_kb)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    # Для расчета используем формулу для мужчин: 10 х вес(кг) + 6,25 x рост(см) – 5 х возраст(г) + 5
    calories = (10 * weight + 6.25 * growth - 5 * age + 5) * 1.2

    await message.answer(f"Ваша норма каллорий {calories}")
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
