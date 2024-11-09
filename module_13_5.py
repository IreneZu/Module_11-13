# # Клавиатура кнопок
# # Задача "Меньше текста, больше кликов":

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# from aiogram.dispatcher import FSMContext
# import asyncio

api = "MyAPI"

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button = KeyboardButton(text="Рассчитать")
button2 = KeyboardButton(text="Информация")
kb.row(button, button2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text=['Рассчитать'])
async def set_age(message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(text="Информация")
async def inform(message):
    await message.answer("Формула расчета для женщин: \n"
                         "(10 × вес в килограммах) + (6,25 × рост в сантиметрах) \n− (5 × возраст в годах) − 161")


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

    # await message.answer(f'age: {data["age"]}, growth: {data["growth"]}, weight: {data["weight"]}')
    norm = 10.0 * float(data["weight"]) + 6.25 * float(data["growth"]) - 5.0 * float(data["age"]) - 161.0
    await message.answer(f'Ваша норма калорий: {norm}')

    await state.finish()


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
