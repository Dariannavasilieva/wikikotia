import telebot
import time
import datetime
bot = telebot.TeleBot('7015976653:AAEf-lfm1V0ZFUaOe5wbQNBWoj9X0IVRplo')
#chat_id = 'YOUR_CHAT_ID'
@bot.message_handler(commands=['menu', 'меню'])
def show_menu(message):
    repSt = "частые_вопросы - Ответы на часто задаваемые вопросы \n"
    repSt += "таблица_расчетов - Таблица с расчетами по питанию \n" 
    repSt +="влажные_корма - Список полнорационных влажных кормов\n"
    repSt += "питание - таблицы со списком влажных кормов, гарантированным анализом влажных кормов, расчетом калорий, минералы Роял Канин "
    repSt +="минералы_роял - Минералы Royal Canin\n"
    repSt += "га_влажка - Табличка с гарантированным анализом влажных кормов на фактическое содержание и на сухое вещество \n"
    repSt += "ценообразование - Из чего формируется стоимость корма? \n"
    repSt += "аптечка - Аптечка для собак и кошек \n"
    repSt += "сбор_мочи - Как собрать мочу коту? \n"
    repSt += "мкб_помощь - Что делать, если у кота МКБ? \n"
    repSt += "банк_крови - Банки крови для животных \n"
    repSt += "видео_наполнители - Видео сравнение наполнителей \n"
    repSt += "продавцы - Проверенные продавцы кормов \n"
    repSt += "меню_викикотия - Главное меню канала Wikikotia на Дзен"
    repSt += "заказать_разбор - Закажи разбор корма"
    repSt += "покорми_админа - Реквизиты для поощрения администрации"
    repSt += "канал_софьи - Cсылка на канал Софьи про натуралку и др"
    repSt += "собачий_чат - Ссылка на чат владельцев собак Sobakopedia"
    bot.send_message(message.chat.id, repSt)


@bot.message_handler(commands=['собачий_чат', 'dogs_chat'])    
def show_table_kalor(message):     
    repSt = "Ссылка на чат владельцев собак Sobakopedia.  \n"
    repSt += "https://t.me/+ZWkxVS4GePQ3YzEy\n"
    bot.send_message(message.chat.id, repSt) 


@bot.message_handler(commands=['канал_софьи', 'sofia_channel'])    
def show_table_kalor(message):     
    repSt = "Платный канал Софьи про натуралку и многое другое.  \n"
    repSt += "https://paywall.pw/r4xl9yjpd7dj \n"

    bot.send_message(message.chat.id, repSt) 

@bot.message_handler(commands=['покорми_админа', 'admin_food'])    
def show_table_kalor(message):     
    repSt = "Админам и их котикам на вкусняшки \n"
    repSt += "https://docs.google.com/document/d/1338PW1b74zyBWcDqme0Im-aeq9SyKvyzfeM0hxEFqsY/edit. \n"

    bot.send_message(message.chat.id, repSt) 

@bot.message_handler(commands=['заказать_разбор', 'feed_analysis'])    
def show_table_kalor(message):     
    repSt = "Напиши на почту  wikikotia@yandex.ru \n"
    repSt += "Если хочешь разбор/сравнение одного/двух составов, отправь полное название корма (бренд, линейка, вкус). Если у тебя есть фото упаковки, состава - добавь в письмо. \n"
    repSt += "Если хочешь разобрать целый бренд, напиши его название для разбора. \n"
    repSt += "Проверь, был ли такой разбор по команде для меня /меню_викикотия или /menu_wikikotia"
    bot.send_message(message.chat.id, repSt) 

@bot.message_handler(commands=['таблица_расчетов', 'feeding_table'])    
def show_table_kalor(message):     
    repSt = "Таблица с расчетами по питанию(калории, минералы, БЖУ и прочее). На одном листе калории и БЖУ, на втором минералы. \n"
    repSt += "https://docs.google.com/spreadsheets/d/11xj9qsLcE2UgjEFLAUzrGigOCjJrT6-P04ojKo7XJms/edit   \n\n"
    repSt += "Как работать с таблицей: \n"
    repSt += "https://docs.google.com/document/d/1UZXC2OqM3OTY90YYGOycB8wkd2XAnSsBcceIZKhh2VE/edit?usp=sharing"
    bot.send_message(message.chat.id, repSt)

@bot.message_handler(commands=['влажные_корма', 'wet_food_table'])    
def show_table_full_korm(message):   
    repSt = "Список полнорационных влажных кормов:\n"
    repSt += "https://docs.google.com/spreadsheets/d/1HlY_I4Od8UIjyTAIE4BXxRSngL7u7ljJbAmhb9HQ65I/edit"
    
    bot.send_message(message.chat.id, repSt)

@bot.message_handler(commands=['частые_вопросы', 'questions'])   
def show_table_full_korm(message): 
    repSt = "Ответы на часто задаваемые вопросы, очень рекомендуется к ознакомлению::\n"
    repSt += "https://docs.google.com/document/d/1OOjJCa7EPV3QHG4tepcgYOoC3ISh9jQmVm3ZKXuJJyA/edit?usp=sharing"
    
    bot.send_message(message.chat.id, repSt)


@bot.message_handler(commands=['минералы_роял', 'royal_minerals'])   
def show_mineral_royal(message): 
    repSt = "Минералы Royal Canin: \n"
    repSt += "https://docs.google.com/spreadsheets/d/1fjRlh0B4VLN4T-Z6D8tmUtYuN2TqQtvZ6A8BVAnVKoM/edit#gid=71470312"
    
    bot.send_message(message.chat.id, repSt)

@bot.message_handler(commands=['питание', 'nutrition'])   
def show_pitanie(message): 
    repSt = "Таблица с расчетами по питанию(калории, минералы, БЖУ и прочее). На одном листе калории и БЖУ, на втором минералы. \n"
    repSt += "https://docs.google.com/spreadsheets/d/11xj9qsLcE2UgjEFLAUzrGigOCjJrT6-P04ojKo7XJms/edit \n"
    repSt += "Список полнорационных влажных кормов:\n"
    repSt += "https://docs.google.com/spreadsheets/d/1HlY_I4Od8UIjyTAIE4BXxRSngL7u7ljJbAmhb9HQ65I/edit \n"
    repSt += "Табличка с гарантированным анализом влажных кормов на фактическое содержание и на сухое вещество(в процессе разработки, спасибо Katlin_katlin за труд \n"
    repSt += "https://docs.google.com/spreadsheets/d/1Dg3m8MVPsPK29Gwrls-q_3QRmUAKk3YGONVrcuvU0sQ/edit#gid=2126161359 \n"
    repSt += "Минералы Royal Canin: \n"
    repSt += "https://docs.google.com/spreadsheets/d/1fjRlh0B4VLN4T-Z6D8tmUtYuN2TqQtvZ6A8BVAnVKoM/edit#gid=71470312"
    
    bot.send_message(message.chat.id, repSt)

@bot.message_handler(commands=['аптечка', 'pharmacy'])   
def show_apteka(message): 
    repSt = "Аптечка для собак и кошек \n"
    repSt += "https://docs.google.com/document/d/1n8OAKwkb9ydKhjBsOxlq7npCxohlgQuX7IYh2o7TjNo/edit"
    bot.send_message(message.chat.id, repSt)


@bot.message_handler(commands=['ценообразование', 'pricing'])   
def show_food_price(message): 
    repSt = "Из чего формируется стоимость корма? \n"
    repSt += "https://docs.google.com/document/d/1PaEKDcbm9YDNh7Ku7x-YUfrFSzaJsgW5rsP2JkQF0Kw/edit"
    bot.send_message(message.chat.id, repSt)

@bot.message_handler(commands=['сбор_мочи', 'urine'])   
def show_mocha(message): 
    repSt = "Как собрать мочу коту? \n"
    repSt += "https://t.me/wikikotiaChat/182860"
    bot.send_message(message.chat.id, repSt)

@bot.message_handler(commands=['мкб_помощь', 'mkb_help'])   
def show_mkb_help(message): 
    repSt = "Что делать, если у кота МКБ?\n"
    repSt += "https://docs.google.com/document/d/1cAhcp4VfMwX0HwfTLRNz8DUiNkrSvOmiO-b-t4chZKE/edit"
    bot.send_message(message.chat.id, repSt)

@bot.message_handler(commands=['га_влажка', 'ga_wet_food'])   
def show_ga_vlag(message): 
    repSt = "Табличка с гарантированным анализом влажных кормов на фактическое содержание и на сухое вещество(в процессе разработки, спасибо Katlin_katlin за труд \n"
    repSt += "https://docs.google.com/spreadsheets/d/1Dg3m8MVPsPK29Gwrls-q_3QRmUAKk3YGONVrcuvU0sQ/edit#gid=2126161359"
   
    bot.send_message(message.chat.id, repSt)

@bot.message_handler(commands=['банк_крови', 'blood_banks'])   
def show_bank_krovi(message): 
    repSt = "Банки крови для животных \n"
    repSt += "https://t.me/wikikotiaChat/185934"
    bot.send_message(message.chat.id, repSt)
    
@bot.message_handler(commands=['видео_наполнители', 'cat_litter_video'])   
def show_video_napolnitely(message): 
    repSt = "Видео сравнение наполнителей (спасибо KriS за реализацию): \n"
    repSt += "https://t.me/wikikotiaChat/203648"
    bot.send_message(message.chat.id, repSt)

@bot.message_handler(commands=['продавцы', 'sellers'])   
def show_bank_krovi(message): 
    repSt = "Проверенные продавцы кормов:  \n"
    repSt += "https://t.me/wikikotiaChat/179734"
    bot.send_message(message.chat.id, repSt)

@bot.message_handler(commands=['меню_викикотия', 'menu_wikikotia'])   
def show_menu_wikikotia(message): 
    repSt = "Главное меню канала Wikikotia на Дзен \n"
    repSt += "https://dzen.ru/media/wikikotia/glavnoe-meniu-wikikotiia-652ac85c9523772f00da9282"
    bot.send_message(message.chat.id, repSt)       


 

@bot.message_handler(content_types=["text"])
def handle_text(message):
   
    user_info = message.from_user
    user_id = user_info.id
    user_first_name = user_info.first_name
    st = 'user_first_name = ' + user_first_name
    mesSt = message.text
    mesSt = mesSt.lower()
    #bot.send_message(message.chat.id, st)
    if (mesSt.find(' бля') != -1) or (mesSt.find('пизд') != -1) or (mesSt.find('ебан') != -1) or (mesSt.find('ёбан') != -1):
        bot.reply_to(message, user_first_name + ', не матерись! Большой Брат все видит!')   
    if (mesSt.find('хуй') != -1): # or (mesSt.find('пизд') != -1) or (mesSt.find('ебан') != -1) or (mesSt.find('ёбан') != -1):
        bot.reply_to(message, user_first_name + ', не матерись! Большой Брат все видит!')   



while True:
    try:
        bot.polling(none_stop=True, timeout=90)
    except Exception as e:
        print(datetime.datetime.now(), e)
        time.sleep(5)
        continue

#bot.polling(none_stop=True, interval=0)

