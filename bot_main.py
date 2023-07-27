from aiogram import types, executor, Bot, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = "6398064406:AAFqbo4-MolK2boLLkMDciZfrJKyaerHBZY"
bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

if __name__ == '__main__':
    executor.start_polling(dp)