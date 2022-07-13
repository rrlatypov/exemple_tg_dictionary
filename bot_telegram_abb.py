# В google colab добавить: !pip install pyTelegramBotAPI

from telebot import TeleBot, types

bot = TeleBot(token='5453750451:AAGYVQ1ZgLprjj-kE9ieoEjDPmfDbaxb-LQ', parse_mode='html') # создание бота

# словарь с определениями и аббревиатурами, которые знает бот
# в формате:
# 'ключевая фраза': 'соответствующее ей определение'
DEFINITOINS = {
    'регресс': 'Проверить что новый функционал не сломал существующий',
    'пси': 'приемо-сдаточные испытания',
    'ктв': 'камера телевизионная',
    'нсци': 'нашлемная система целеуказания и индикации',
    'бп': 'блок питания',
    'бпх': 'блок питания холодильника',
    'мо': 'модуль определения',
    'муо': 'модуль управления объективом',
    'sdlc': 'software development life cycle - жизненный цикл разработки ПО',
    'stlc': 'software testing life cycle - жизненный цикл процесса тестирования',
    'по': 'програмное обеспечение',
    'sql': 'structured query lanaguage - структурированный язык запросов',
    'ttd': 'test driven development - разработка через тестирование',
    'api': 'application programming itterface',
    'gui': 'graphical user interface',
    'http': 'HyperText Transfer Protocol — «протокол передачи гипертекста»',
    'https': 'HyperText Transfer Protocol Secure - протокол передачи гипертекста защищенный',
    'rest api': 'representational state transfer',
    'get': 'получение данных з сервера',
    'post': 'создание новой сущности или внесение изменения',
    'delete': 'удаление существующей сущности',
    'crud': 'Create (создание сущности) Read (чтение сущности) Update (редактирование данных) Delete (удаление)',
    'agile': 'методология гибкой разработки (одна из...)',

}

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='Привет! Я помогу тебе расшифровать сложные аббревиатуры и термины 🤓\nВведи интересующий термин, например, регресс (ввод слов и сокращений с маленькой буквы)', # текст сообщения
    )

# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    # пробуем найти ключевую фразу в словаре
    definition = DEFINITOINS.get(
        message.text.lower(), # приводим текст сообщения к нижнему регистру
    )
    # если фразы нет в словаре, то переменная definition будет иметь значение None
    # проверяем это условие
    if definition is None:
        # если ключевая фраза не была найдена в словаре
        # отправляем ответ
        bot.send_message(
            chat_id=message.chat.id,
            text=' 🤷‍♂️ Этот вопрос поставил меня в тупик. Спроси у кого нибудь другого  ',
        )
        # выходим из функции
        return
    
    # если ключевая фраза была найдена, формируем текст сообщения и отправляем его
    # если перед строкой поставить букву f, то в фигурных скобках {} можно использовать переменные :)
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Определение:\n<code>{definition}</code>',
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=f'Могу еще что-то подсказать?',
    )


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()
