from aiogram import types
from core.helpers import telegram as tg_helper

chats_msg = 'Ты бы хотел узнавать актуальную информацию о мероприятиях Фонда?'
chats = {
    ("Хочу всё знать!", "chat_1"),
    ("Я уже знаю.", "chat_2")
}

chats2 = tg_helper.create_inline_markup(*chats)

chat1_msg = 'Выбирай образовательную программу или же вечеринки for fun, а лучше все вместе - ведь в жизни должен быть баланс!'
chat1 = {
    ("Вечеринки", 'https://t.me/joinchat/HbPRcBcoCX0iUmXHWJ7xyg'),
    ('Образовательная программа', 'https://t.me/joinchat/HbPRcBYcZCT9FzaPl5fmpg'),
    ('Дальше.', 'chat_2')
}
chat_1 = tg_helper.create_inline_markup(*chat1)

chat2_msg = 'На мероприятиях всегда веселее вместе - это факт. Если присоединиться  к секретному чату, то у тебя всегда будет компания сходить в кино или на вечеринку, найти спутника в театр или обсудить за чашкой кофе последние новости. И, конечно, встретиться в Башне филиала Москвы.'
chat2 = {
    ("Буду рад!", 'https://t.me/joinchat/HbPRcBVIMByGzHCWnlHmcg'),
    ("Башня", 'https://t.me/joinchat/HbPRcBELPpoT9nyWIXGKoA'),
    ('В другой раз', 'chat_3'),
    ('Дальше.', 'chat_3')
}
chat_2 = tg_helper.create_inline_markup(*chat2)

chat3_msg = 'Но мы собрались здесь, чтобы не только отдыхать. У меня есть полезный чат и для работы, конечно. Набраться реального опыта или найти эффективного сотрудника - там можно все!'
chat3 = {
    ("Работать!", 'https://t.me/joinchat/HbPRcBcYAezviVIA3zRk-A'),
    ("Нанимать!", 'https://t.me/joinchat/HbPRcBcYAezviVIA3zRk-A'),
    ("Стажироваться!", 'https://t.me/joinchat/HbPRcBcYAezviVIA3zRk-A'),
    ('Дальше.', 'chat_4')
}
chat_3 = tg_helper.create_inline_markup(*chat3)

chat4_msg = 'А ты знаешь, что участники Фонда создают свои проекты? Возможно даже ты сам работаешь над ним. И тогда точно знаешь, как ребятам необходима помощь для его реализации.'
chat4 = {
    ("Хочу помочь!", 'https://t.me/joinchat/HbPRcBdS7TgkLqtutJpMog'),
    ("Ищу добровольцев", 'https://t.me/joinchat/HbPRcBdS7TgkLqtutJpMog'),
    ('Дальше.', 'chat_5')
}
chat_4 = tg_helper.create_inline_markup(*chat4)

chat5_msg = 'У тебя должно быть много интересов и какая-то определённая сфера деятельности, в которой твои компетенции максимально высоки. Выбирай любой признак присоединения к группе единомышленников, тебе везде будут рады!'
chat5 = {
    ("Event", 'https://t.me/joinchat/HbPRcBYhCIt6o3K4nHXY1Q'),
    ("Cоц. деятельность", 'https://t.me/joinchat/HbPRcBZQwsCuWCbqB6exuQ'),
    ("Аналитика", 'https://t.me/joinchat/HbPRcBWfIcWFvDa1WqUiNw'),
    ("IT", 'https://t.me/joinchat/HbPRcBVNHGrHFrNl2kICIg'),
    ("Маркетинг", 'https://t.me/joinchat/HbPRcBWB6XCu1UBTTYmdBQ'),
    ("Экология", 'https://t.me/joinchat/HbPRcBFQXZ4JKeE93aumFw'),
    ("Искусство", 'https://t.me/joinchat/HbPRcBE7_z0gOKy1Vaq5qw'),
    ("Медиа", 'https://t.me/joinchat/HbPRcAy1wIwKkKNNgNEs5w'),
    ('Дальше.', 'chat_6')
}
chat_5 = tg_helper.create_inline_markup(*chat5)

chat6_msg = 'Нас всех захватили кейс-турниры! Присоединяйся, чтобы предложить игру или найти команду!'
chat6 = {
    ("Кейс-турнир", 'https://t.me/joinchat/HbPRcBIXJPq8P7dDdYgWhg'),
    ('Дальше.', 'chat_7')
}
chat_6 = tg_helper.create_inline_markup(*chat6)

chat7_msg = 'Нас всех захватили кейс-турниры! Присоединяйся, чтобы предложить игру или найти команду!'
chat7 = {
    ("Вечеринки", 'https://t.me/joinchat/HbPRcBcoCX0iUmXHWJ7xyg'),
    ('Образовательная программа', 'https://t.me/joinchat/HbPRcBYcZCT9FzaPl5fmpg'),
    ('Дальше.', 'chat_8')
}
chat_7 = tg_helper.create_inline_markup(*chat7)

chat8_msg = 'На сегодня секретные чаты закончились. До новых встреч!'

all_chats_msg = [chat1_msg,chat2_msg,chat3_msg,chat4_msg,chat5_msg,chat6_msg,chat7_msg,chat8_msg]
all_chats=[chat_1,chat_2,chat_3,chat_4,chat_5,chat_6,chat_7]