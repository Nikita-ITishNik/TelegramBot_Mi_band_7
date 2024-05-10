#_________________________________________import
import telebot
from datetime import datetime
from telebot import types
#___________________________________________________________token
#token="6099916809:AAFlyaTWf3gBi7EwLhr6l4Pu4jSMeRPFUXk"
token="5871287006:AAEVlwdAlh86EJq7ca4ZiUiLT8IWDMfGWhs"
bot = telebot.TeleBot(token)
#___________________________________________________________ID_ADMIN
adms = ['1353647773']

MENU ='''
Приложения:
/calendar - Календарь с праздникими - ru приложение
/calculator - Калькулятор - ru/en приложение
/wallet - Кошель - ru приложение
/toolbox - ru приложение с дополнительными настройками
/KiN (Х_and_0) - ru игра Крестики и нолики
/SpaceGame - ru игра управление космолётом
/Wolf - ru игра волк ловит яйца
/MoreLocale - ru приложение для смены языка

Циферблаты:
/tamagochi - тамогочи - сhina игра
/dino_google - Дино_гугл - сhina игра
/snake_game - ru игра змейка

Сайты:
/BandNotes - сайт для создания заметок
/bandstudio - сайт для создания своих циферблатов (пустые циферблаты)
/melianmiko - сайт для создания галлереи для mi band 7

/Program - Програмы совместимые с Mi band 7 для смартфона
'''
#___________________________________________________________TIME
def sut():
    current_datetime = datetime.now().strftime('%H')
    det = int(current_datetime)
    if (det == 21):
        det = 0
    elif (det == 22):
        det = 1
    elif (det == 23):
        det = 2
    else:
        det = det + 3

    if (det < 4):
        sutki = 'Доброй ночи'
    elif (det >= 4) and (det < 12):
        sutki = 'Доброго утра'
    elif (det >= 12) and (det < 18):
        sutki = 'Хорошего дня'
    elif (det >= 18) and (det < 24):
        sutki = 'Доброго вечера'
    else:
        sutki = 'Ошибка во времени'
    return sutki
#___________________________________________________________START_reg
@bot.message_handler(commands=['start']) #вывод доступных команд
def start(message):
    bot.send_message(message.chat.id, str(sut()) + "! Вас приветствует TeleBot! Приложения и циферблаты для Mi band 7")
    text = "ID: " + str(message.chat.id) + " First_name: " + str(message.chat.first_name) + " Last_name: " + str(message.chat.last_name) + " Username: @" + str(message.chat.username) + " Status О \n"
    fp = open('Список_пользователей_бота.txt', 'a')
    fp.write(text)
    fp.close()
    markup = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    btn1 = types.KeyboardButton("/Menu")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "\n/Menu - Меню приложений Mi band", reply_markup=markup)

@bot.message_handler(commands=['Menu']) #вывод доступных команд
def Menu(message):
    bot.send_message(message.chat.id, str(sut()) + ", "+str(message.chat.first_name)+"! Приложения и циферблаты для Mi band 7")
    bot.send_message(message.chat.id, MENU)
    markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    btn1 = types.KeyboardButton("/Admin")
    btn2 = types.KeyboardButton("/Menu")
    btn3 = types.KeyboardButton("/Info")
#    btn4 = types.KeyboardButton("/Komment") \n/Komment - Написать отзыв   , btn4
#    btn5 = types.KeyboardButton("/ ")
#    btn6 = types.KeyboardButton("/ ")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id, "Кнопки бота успешно обновлены:\n/Admin - Написать Админам (предложка/отзывы/советы)\n/Menu - Меню Mi band\n/Info - Информация о боте и авторских прав", reply_markup=markup)

@bot.message_handler(commands=['Info'])
def Info(message):
    bot.send_message(message.chat.id, "Информация о боте и авторских прав")
    bot.send_message(message.chat.id, "Бот создан исключительно в информационых целях\n"
    "1) Все авторы приложений, програм и сайтов указаны на их продуктах\n"
    "2) Мы лишь сгруппировали самое полезное и интересное из сети интернета, не посигая на авторские права")

@bot.message_handler(commands=['Admin'])
def Admin(message):                                 #Сообщение админу
    if message.text != "/Admin":
        command = message.text.split(maxsplit=1)
        text = "Админу, от юзера: " + command[1] + "\n" + "ID: " + str(message.chat.id)
        bot.send_message(1353647773, text)
        bot.send_message(message.chat.id, "Сообщение отправлено, в течении дня вам обязаельно ответят, среднее время ответа 1-2 ч")
    else:
        bot.send_message(message.chat.id, "/Admin + сообщение через ПРОБЕЛ ")

@bot.message_handler(commands=['Program']) #вывод доступных команд
def Program(message):
    markup = types.InlineKeyboardMarkup()
    btn2 = types.InlineKeyboardButton(text='App store', url="https://apps.apple.com/ru/app/mi-band-master/id1394215417")
    markup.add(btn2)
    bot.send_message(message.from_user.id, "Master for Mi Band - Одна из лучших программ для тех, кто использует Сяоми часы.", reply_markup = markup)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Play market', url="https://play.google.com/store/apps/details?id=com.mc.miband1")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Notify_for_Mi_Band - Как и следует из названия, этот апплет по преимуществу предназначен для вывода на экран всевозможных уведомлений, а также состоянии гаджета", reply_markup = markup)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Play market', url="https://play.google.com/store/apps/details?id=hu.tiborsosdevs.mibandage")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Mi Bandage for Mi Band - Программа для смарт-часов и браслетов полностью совместима с гаджетами линеек Mi Band 2-го поколения и выше, а также серии HRX", reply_markup = markup)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Play market', url="https://play.google.com/store/apps/details?id=com.xiaomi.wearable")
    btn2 = types.InlineKeyboardButton(text='App store', url="https://apps.apple.com/ru/app/xiaomi-wear-lite/id1493500777")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id,  ' Mi Fitnes - Основное, официальное приложение. Программа в первую очередь предназначена для отслеживания ваших перемещений: во время прогулок, пробежек или поездок на велосипеде. В приложении можно составлять свои маршруты, анализировать прежние передвижения, контролировать прогресс (например, постепенное увеличение пройденных расстояний) и ставить себе задачи. Управлять апплетом можно как непосредственно со смарт-часов, так и с синхронизированного телефона.', reply_markup = markup)
    bot.send_message(message.chat.id, "Список официальных приложений:\nNike Run Club, Google Fit, Zeep Life(Mi Fit), Mi Fitness")

@bot.message_handler(commands=['calendar']) #вывод доступных команд
def calendar(message):
    bot.send_message(message.chat.id, "Календарь с праздникими - ru приложение")
    bot.send_document(message.chat.id, open(r'calendar.bin', 'rb'))

@bot.message_handler(commands=['snake_game']) #вывод доступных команд
def snake_game(message):
    bot.send_message(message.chat.id, "snake_game - ru игра змейка")
    bot.send_document(message.chat.id, open(r'snake_game_v1_0.bin', 'rb'))

@bot.message_handler(commands=['MoreLocale']) #вывод доступных команд
def MoreLocale(message):
    bot.send_message(message.chat.id, "MoreLocale - ru приложение для смены языка")
    bot.send_document(message.chat.id, open(r'MoreLocale.bin', 'rb'))

@bot.message_handler(commands=['Wolf']) #вывод доступных команд
def Wolf(message):
    bot.send_message(message.chat.id, "Wolf - ru игра волк ловит яйца")
    bot.send_document(message.chat.id, open(r'Wolf.bin', 'rb'))

@bot.message_handler(commands=['calculator']) #вывод доступных команд
def calculator(message):
    bot.send_message(message.chat.id, "Калькулятор - ru/en приложение")
    bot.send_document(message.chat.id, open(r'calculator.bin', 'rb'))

@bot.message_handler(commands=['toolbox']) #вывод доступных команд
def toolbox(message):
    bot.send_message(message.chat.id, "toolbox - ru приложение с дополнительными настройками")
    bot.send_document(message.chat.id, open(r'toolbox.bin', 'rb'))

@bot.message_handler(commands=['tamagochi'])#вывод доступных команд
def tamagochi(message):
    bot.send_message(message.chat.id, "Тамагочи - сhina циферблат")
    bot.send_message(message.chat.id, "Ссылка на русский  вариант к сожалению не работает: https://4pda.to/forum/index.php?showtopic=1048744&view=findpost&p=122426165")
    bot.send_document(message.chat.id, open(r'Tamagochi.bin', 'rb'))

@bot.message_handler(commands=['dino_google'])#вывод доступных команд
def dino_google(message):
    bot.send_message(message.chat.id, "Дино_гугл - сhina циферблат")
    bot.send_document(message.chat.id, open(r'dino_google.bin', 'rb'))

@bot.message_handler(commands=['wallet'])#вывод доступных команд
def wallet(message):
    bot.send_message(message.chat.id, "Кошель - ru приложение")
    bot.send_document(message.chat.id, open(r'wallet.bin', 'rb'))

@bot.message_handler(commands=['KiN'])#вывод доступных команд
def KiN(message):
    bot.send_message(message.chat.id, "КиН -  Крестики нолики (для 1-2 игроков) ru игра")
    bot.send_document(message.chat.id, open(r'Х_and_0.bin', 'rb'))

@bot.message_handler(commands=['SpaceGame'])#вывод доступных команд
def SpaceGame(message):
    bot.send_message(message.chat.id, "SpaceGame - ru игра")
    bot.send_document(message.chat.id, open(r'spaceGame.bin', 'rb'))

@bot.message_handler(commands=['BandNotes'])#вывод доступных команд
def BandNotes(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='BandNotes', url="https://gbowsky.github.io/bandnotes/")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "BandNotes - сайт для создания заметок", reply_markup = markup)

@bot.message_handler(commands=['bandstudio'])#вывод доступных команд
def bandstudio(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='bandstudio.su', url="https://bandstudio.su/app/edit/sb7/zepp/void/all/")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "bandstudio.su - сайт для создания своих циферблатов (пустые циферблаты)", reply_markup = markup)

@bot.message_handler(commands=['melianmiko'])#вывод доступных команд
def melianmiko(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='melianmiko', url="https://melianmiko.ru/sb7/gallery/")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "melianmiko - сайт для создания галлереи для mi band 7", reply_markup = markup)


#__________________________________________________________________________________________Конец проги
bot.polling(none_stop=True)
