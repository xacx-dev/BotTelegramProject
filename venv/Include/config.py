import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot_token = '1341484374:AAEinrSedgSw0YWffZkhXnzaUloMUR-eriw'
req_url = 'http://188.93.210.133:85/api/v1'
secure_code = 'tGu3R9DD7sIvDiEopYtKTtnM7olr7deL'
vk_token = 'f5d066fef5d066fef5d066fee7f581faf1ff5d0f5d066feae0c33fb289a3bc89218cd05'
vk_version = '5.124'



storage = MemoryStorage()
bot = Bot(token=bot_token,parse_mode='html')
dp = Dispatcher(bot, storage=storage)
#logging.basicConfig(level=logging.INFO)


