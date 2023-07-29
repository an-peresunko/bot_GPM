from aiogram import types, executor, Bot, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = "6398064406:AAFqbo4-MolK2boLLkMDciZfrJKyaerHBZY"
bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@bot.message_handler(commands=['start'])
async def start_message(message):
  bot.send_message(message.chat.id,"Твоё ФИО?")
  # Пользователь вводит ФИО
  # Бот спрашивает тип практики
  # Бот спрашивает в каком отделе ты проходишь практику
  # бот спрашивает у какого наставника ты закреплен
  

if __name__ == '__main__':
    executor.start_polling(dp)