import random

import telebot
from telebot import types
bot = telebot.TeleBot("5980300023:AAEQEhoj7t9yrqLQKjEXBmbO00t7oFLbaN4")
max_hp = hp = damage = 0
race = ''
exp = 0
lvl = 1
victim = None
def start1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = "Эльф"
    button_2 = "Гном"
    button_3 = "Хоббит"
    button_4 = "Человек"
    markup.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id, text="Выберите расу", reply_markup=markup)

def main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton("Начать игру")
    button_2 = types.KeyboardButton("Об игре")
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, text='Вы вышли в главное меню', reply_markup=markup)

def start_quest():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = "В главное меню"
    button2 = "В путь"
    markup.add(button1, button2)
    return markup

def create_monstr():
    info = ["Зомби", "Скелет", "Вампир"]
    rand_name = random.choice(info)
    rand_hp = random.randrange(20, 70)
    rand_dammage = random.randrange(25, 65)
    return [rand_name, rand_hp, rand_dammage]

def what_do():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = "Атаковать"
    button_2 = "В главное меню"
    button_3 = "Сбежать"
    markup.add(button_1, button_2, button_3)
    return markup

def about_game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    button = "В главное меню"
    markup.add(button)
    bot.send_message(message.chat.id, text= "Описание игры", reply_markup= markup)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    button_1 = types.KeyboardButton("Начать игру")
    button_2 = types.KeyboardButton("Об игре")
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, text='Здравствуйте, вы готовы к игре?', reply_markup=markup)


@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, text='Я думаю, тебе что-то непонятно, если ты зашел сюда')


@bot.message_handler(content_types=['text'])
def start_game(message):
    global max_hp, hp, damage, race, exp, lvl, victim
    if message.text == "Начать игру":
        max_hp = damage = exp = 0
        lvl = 1
        race = ''
        start1(message)
    elif message.text == "Об игре":
        max_hp = damage = exp = 0
        lvl = 1
        race = ''
        about_game(message)
    elif message.text == "В главное меню":
        max_hp = damage = exp = 0
        lvl = 1
        race = ''
        main_menu(message)
    if message.text == "Эльф":
        max_hp = damage = 0
        max_hp = 10
        damage = 15
        race = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
        button_1 = "Лучник"
        button_2 = "Рыцарь"
        markup.add(button_1, button_2)
        bot.send_message(
            message.chat.id,
            f"Вы выбрали {race}а. \n" 
            f"Ваше здоровье -> {max_hp}\n" 
            f"Ваш урон -> {damage}\n" 
            f" \n" 
            f"Осталось выбрать класс...",
            reply_markup= markup
        )
    if message.text == "Гном":
        max_hp = damage = 0
        max_hp = 8
        damage = 1000
        race = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = "Лучник"
        button_2 = "Рыцарь"
        markup.add(button_1, button_2)
        bot.send_message(
            message.chat.id,
            f"Вы выбрали {race}а. \n"
            f"Ваше здоровье -> {max_hp}\n"
            f"Ваш урон -> {damage}\n"
            f" \n"
            f"Осталось выбрать класс...",
            reply_markup=markup
        )
    if message.text == "Хоббит":
        max_hp = damage = 0
        max_hp = 9
        damage = 21
        race = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = "Лучник"
        button_2 = "Рыцарь"
        markup.add(button_1, button_2)
        bot.send_message(
            message.chat.id,
            f"Вы выбрали {race}а. \n"
            f"Ваше здоровье -> {max_hp}\n"
            f"Ваш урон -> {damage}\n"
            f" \n"
            f"Осталось выбрать класс...",
            reply_markup=markup
        )
    if message.text == "Человек":
        max_hp = damage = 0
        max_hp = 6
        damage = 11
        race = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = "Лучник"
        button_2 = "Рыцарь"
        markup.add(button_1, button_2)
        bot.send_message(
            message.chat.id,
            f"Вы выбрали {race}а. \n"
            f"Ваше здоровье -> {max_hp}\n"
            f"Ваш урон -> {damage}\n"
            f" \n"
            f"Осталось выбрать класс...",
            reply_markup=markup
        )
    if message.text == "Лучник":
        max_hp += 7
        damage += 14
        hp = max_hp
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = "В путь"
        button_2 = "В главное меню"
        markup.add(button_1, button_2)
        bot.send_message(
            message.chat.id,
            f"Теперь вы - {race} {message.text}. \n" 
            f"Ваше здоровье -> {hp}\n" 
            f"Ваш урон -> {damage}\n",
            reply_markup = markup
        )
    if message.text == "Рыцарь":
        max_hp += 10
        damage += 12
        hp = max_hp
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = "В путь"
        button_2 = "В главное меню"
        markup.add(button_1, button_2)
        bot.send_message(
            message.chat.id,
            f"Теперь вы - {race} {message.text}. \n" 
            f"Ваше здоровье -> {hp}\n" 
            f"Ваш урон -> {damage}\n",
            reply_markup = markup
        )
    if message.text == "В путь":
        event = random.randint(0, 1)
        if event == 0:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button_1 = "В путь"
            button_2 = "В главное меню"
            markup.add(button_1, button_2)
            bot.send_message(message.chat.id, "Вы никого не встретили;\n"
                                              "Идем дальше?", reply_markup= markup)
        elif event == 1:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button_1 = "Атаковать"
            button_2 = "В главное меню"
            button_3 = "Сбежать"
            markup.add(button_1, button_2, button_3)
            victim = create_monstr()
            bot.send_message(message.chat.id, f"Вас заметил {victim[0]}\n"
                                              f"Его здоровье --> {victim[1]}\n"
                                              f"Его урон --> {victim[2]}", reply_markup= markup)
    if message.text == "Атаковать":
        victim[1] -= damage
        bot.send_message(message.chat.id, f"Вы нанесли урон: {damage}")
        if victim[1] <= 0:
            bot.send_message(message.chat.id, f'{victim[0]} повержен!')
            random_exp = random.randint(5, 10)
            exp += random_exp * lvl
            if exp >= 30 * lvl:
                lvl += 1
                hp += 15 * lvl
                max_hp = hp
                damage += 20 * lvl
                exp = 0
                bot.send_message(message.chat.id, f'Твой уровень повышен!\n'
                         f'Теперь у тебя {lvl} уровень!\n'
                         f'Твоё здоровье -> {max_hp}\n'
                         f'Твой урон -> {damage} \n'
                         f'Для следующего уровня требуется {30 * lvl} опыта! \n', reply_markup= start_quest()
                                 )
            else:
                bot.send_message(message.chat.id, f'Вам начислено {random_exp * lvl} опыта \n'
                                                  f'Ваш опыт равен: {exp}\n'
                                                  f'Ваше здоровье равно: {max_hp}\n'
                                                  f'Ваш урон равен: {damage}\n'
                                                  f'Идем дальше в путь?', reply_markup= start_quest())


        elif victim[1] > 0:
            bot.send_message(message.chat.id, f'{victim[0]} атакует!\n'
                                              f'{victim[0]} нанес {victim[2]} урона')
            max_hp -= victim[2]
            if max_hp <= 0:
                markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
                button_4 = "В главное меню"
                markup.add(button_4)
                bot.send_message(message.chat.id, f'{victim[0]} победил, игра окончена', reply_markup= markup)
            elif max_hp > 0:
                bot.send_message(message.chat.id, f"Здоровье монстра: {victim[1]}\n"
                                                  f"Ваше здоровье: {max_hp}\n"
                                                  f"Что будем делать?", reply_markup= what_do())

    elif message.text == "Сбежать":
        bot.send_message(message.chat.id, "Вы сбежали", reply_markup=start_quest())

bot.polling(none_stop=True)