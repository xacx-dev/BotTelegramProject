from aiogram import types
from core.helpers import telegram as tg_helper

btns = {
    ("Да", "yes_reg"),
    ("Нет, хочу быть его частью!", "https://russianleaders.org" )
}
REG_INLINE_KB = tg_helper.create_inline_markup(*btns)
print(REG_INLINE_KB)


# -- Start Messages
msg_start = 'Ты уже состоишь в сообществе Фонда «Будущие Лидеры»?'
