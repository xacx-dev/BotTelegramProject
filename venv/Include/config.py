import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot_token = '1341484374:AAEinrSedgSw0YWffZkhXnzaUloMUR-eriw'
req_url = 'http://194.67.111.246:8000'

storage = MemoryStorage()
bot = Bot(token=bot_token)
dp = Dispatcher(bot, storage=storage)
#logging.basicConfig(level=logging.INFO)


