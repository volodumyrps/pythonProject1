import telebot
from telebot import types



bot = telebot.TeleBot("5730686212:AAHaJ_b_dhYh2u4uu7XQion3JFbxtqYRsIU")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Розпочати!")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Вітаємо у просторі свічок, {0.first_name}!                                                       Якщо бажаєте розпочати продивлятись свічки 🕯 введіть Розпочати! (З великої букви🙃) або просто натисніть кнопку знизу!".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def size(message1):
    if message1.text == ("Розпочати!"):
        bot.send_message(message1.chat.id, text="Оберіть тематику вашій свічці😙                                                                    Із доступних: Хеллоуін🎃, Магічна🔮, Новорічна🎄, З квітами🌸, З фруктами🍑.                                                                                                (Для того щоб обрати, введіть на клавіатурі те що потрібно з великої букви та БЕЗ смайлика❗️)".format(message1.from_user))

    elif message1.text == ("Хеллоуін"):
        bot.send_message(message1.chat.id, text="Тепер оберіть в чому вона буде😘                                                                   Із доступних: У тикві🎃, У склі🕯, Таємниця🔞🤫.                                             (Для того щоб обрати, введіть на клавіатурі те що потрібно з великої букви та БЕЗ смайлика,❗️ ОКРІМ У склі🕯(саме тут смайлик потрібен))")

    elif message1.text == ("Магічна"):
        bot.send_message(message1.chat.id, text="Тепер оберіть в чому вона буде😘                                                                    Із доступних: У баночці, У склі👄.                                                                        (Для того щоб обрати, введіть на клавіатурі те що потрібно з великої букви та БЕЗ смайлика,❗️ ОКРІМ У склі👄(саме тут смайлик потрібен))")

    elif message1.text == ("Новорічна"):
        bot.send_message(message1.chat.id, text="Тепер оберіть в чому вона буде😘                                                                    Із доступних: Ні у чому🙃, У склі🌚.                                                                (Для того щоб обрати, введіть на клавіатурі те що потрібно з великої букви та ЗІ смайликом❗️)")

    elif message1.text == ("З квітами"):
        bot.send_message(message1.chat.id, text="Тепер оберіть в чому вона буде😘                                                                    Із доступних: Ні у чому😌, У склі🌝.                                                                (Для того щоб обрати, введіть на клавіатурі те що потрібно з великої букви та ЗІ смайликом❗️)")

    elif message1.text == ("З фруктами"):
        bot.send_message(message1.chat.id, text="Тепер оберіть в чому вона буде😘                                                                    Із доступних: У самому фрукті🍊, Ні у чому😚.                                                             (Для того щоб обрати, введіть на клавіатурі те що потрібно з великої букви та БЕЗ смайлика,❗️ ОКРІМ Ні у чому😚(саме тут смайлик потрібен))")

    elif message1.text == ("У тикві"):
        bot.send_message(message1.chat.id, text="Готуєтесь до цього моторошного свята😏? Зараз вже можете обирати саму свічку🕯!                                                                                                       Із доступних: З павучими лапками🕷, Просто у тикві🎃, Із воскової тикви.                                                                                                                      (Для того щоб обрати, введіть на клавіатурі те що потрібно з великої букви та БЕЗ смайлика❗️)")

    elif message1.text == ("З павучими лапками"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваша моторошна🎃 свічка буде виглядати ось так:")
        pic2 = open("E:\TelegremBot\SpiderCandleHalloween.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic2)
        bot.send_message(message1.chat.id, text="Цікаво, лапки справжні?... Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("Просто у тикві"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваша моторошна🎃 свічка буде виглядати ось так:")
        pic3 = open("E:\TelegremBot\OnlyPumpkin.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic3)
        bot.send_message(message1.chat.id, text="Озирнись... Можливо, там вже хтось з'явився?... Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("Із воскової тикви"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваша моторошна🎃 свічка буде виглядати ось так:")
        pic4 = open("E:\TelegremBot\VoskovaPumpkinHalloween.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic4)
        bot.send_message(message1.chat.id, text="Дивновате😂. Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("У склі🕯"):
        bot.send_message(message1.chat.id, text="Готуєтесь до цього моторошного свята😏? Зараз вже можете обирати саму свічку🕯!                                                                                                                       Із доступних: Звичайна з тиквою, З листям🍁, З кров'ю вампіра🧛.                                                                                                                                                                           (Для того щоб обрати, введіть на клавіатурі те що потрібно з великої букви та БЕЗ смайлика❗️)")

    elif message1.text == ("Звичайна з тиквою"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваша моторошна🎃 свічка буде виглядати ось так:")
        pic5 = open("E:\TelegremBot\SimpleCandleHalloween.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic5)
        bot.send_message(message1.chat.id, text="Естетика зашкалює🤤. Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("З листям"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваша моторошна🎃 свічка буде виглядати ось так:")
        pic6 = open("E:\TelegremBot\HalloweenCandleWithLeaf.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic6)
        bot.send_message(message1.chat.id, text="Дуже по осінньому🍂! Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("З кров'ю вампіра"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваша моторошна🎃 свічка буде виглядати ось так:")
        pic1 = open("E:\TelegremBot\VampireBloodCandle.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic1)
        bot.send_message(message1.chat.id, text="Можливо... це кровь його жертви... Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("Таємниця"):
        bot.send_message(message1.chat.id, text="О ні🤯! Ви схоже хочете продивитись наймоторошніші свічки які у нас є😵! Ви впевнені у своїх діях😶? Якщо так введіть Так, якщо ж передумали🤐 вводимо Ні.")

    elif message1.text == ("Так"):
        bot.send_message(message1.chat.id, text="Ну добре... Обирайте😬                                                                                               Із доступних: З кров'ю та павуками🩸, Хребці, Черепи💀.                                                                                                            (Для того щоб обрати, введіть на клавіатурі те що потрібно з великої букви та БЕЗ смайлика❗️)")

    elif message1.text == ("Ні"):
        bot.send_message(message1.chat.id, text="Ну і правильно😌. Потрібно берегти свою психіку. Обирайте щось інше)")
        bot.send_message(message1.chat.id, text="Обирайте далі в чому вона буде😎                                                                    Із доступних: У тикві🎃, У склі🕯.                                                                   (Для того щоб обрати, введіть на клавіатурі те що потрібно з великої букви та БЕЗ смайлика,❗️ ОКРІМ У склі🕯(саме тут смайлик потрібен))")

    elif message1.text == ("З кров'ю та павуками"):
        bot.send_message(message1.chat.id, text="Вітаємо... Надіємся ця кров'яка Вас не налякає😳")
        pic7 = open("E:\TelegremBot\BloodSpiders.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic7)
        bot.send_message(message1.chat.id, text="Сумніваємось, але бажаєте продивитись ще🥴? Якщо все ж таки так знову введіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("Хребці"):
        bot.send_message(message1.chat.id, text="Вітаємо... Надіємся ці кістки Вас не налякають😳")
        pic8 = open("E:\TelegremBot\Hrebtsi.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic8)
        bot.send_message(message1.chat.id, text="Сумніваємось, але бажаєте продивитись ще🥴? Якщо все ж таки так знову введіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("Черепи"):
        bot.send_message(message1.chat.id, text="Вітаємо... Надіємся ці черепяки Вас не дуже налякають😳")
        pic9 = open("E:\TelegremBot\Skeleton.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic9)
        bot.send_message(message1.chat.id, text="Сумніваємось, але бажаєте продивитись ще🥴? Якщо все ж таки так знову введіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("Ні у чому🙃"):
        bot.send_message(message1.chat.id, text="Мрієте щоб Новий Рік🌲 настав скоріше? Зараз вже можете обирати саму свічку🕯!                                                                                                                                                                               Із доступних: З оленями🦌, З корицею, З гілочками ялинки та прикрасами🧚.                                                                                                                                                                                  (Для того щоб обрати, введіть на клавіатурі те що потрібно з великої букви та БЕЗ смайлика❗️)")

    elif message1.text == ("З оленями"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваше новорічне🌟 щастя буде виглядати ось так😌:")
        pic10 = open("E:\TelegremBot\Oleni.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic10)
        bot.send_message(message1.chat.id, text="100% свічка самого Діда Мороза🎅!. Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("З корицею"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваше новорічне🌟 щастя буде виглядати ось так😌:")
        pic11 = open("E:\TelegremBot\MerryChristmas.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic11)
        bot.send_message(message1.chat.id, text="Навіть не уявляю як воно чудесно пахне🌲!. Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("З гілочками ялинки та прикрасами"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваше новорічне🌟 щастя буде виглядати ось так😌:")
        pic12 = open("E:\TelegremBot\Forest.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic12)
        bot.send_message(message1.chat.id, text="Саме я вже дуже мрію щоб зима прийшла скоріше☃️. Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("У склі🌚"):
        bot.send_message(message1.chat.id, text="Мрієте щоб Новий Рік🌲 настав скоріше? Зараз вже можете обирати саму свічку🕯!                                                                                                                                                                                                            Із доступних: З цитрусом🍊 та корицею, Звичайні з гірляндою🌌 та льодяником🍭, Зі засніженою хатинкою❄️.                                                                                                                                                                                                                       (Для того щоб обрати, введіть на клавіатурі те що потрібно з великої букви та БЕЗ смайлика❗️)")

    elif message1.text == ("З цитрусом та корицею"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваше новорічне🌟 щастя буде виглядати ось так😌:")
        pic13 = open("E:\TelegremBot\ChristmasWithOrange.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic13)
        bot.send_message(message1.chat.id, text="Як по новорічному!☃️. Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("Звичайні з гірляндою та льодяником"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваше новорічне🌟 щастя буде виглядати ось так😌:")
        pic14 = open("E:\TelegremBot\SimpleWithGarlandAndCandy.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic14)
        bot.send_message(message1.chat.id, text="Саме я вже дуже мрію щоб зима прийшла скоріше☃️. Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("Зі засніженою хатинкою"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваше новорічне🌟 щастя буде виглядати ось так😌:")
        pic15 = open("E:\TelegremBot\WithSnowHome.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic15)
        bot.send_message(message1.chat.id, text="Цікаво, хто у цій хатинці🤔?☃️. Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("Ні у чому😌"):
        bot.send_message(message1.chat.id, text="Полюбляєте квіти🌸? Моя сестра так сильно, що навіть працювала флористом😎🌺. Зараз вже можете обирати саму свічку🕯!                                                                                                                                        Із доступних: З сушеною лавандою💐, З маком та волошками, З орхідеєю🌺.                                                                                                                                                                    (Для того щоб обрати, введіть на клавіатурі те що потрібно з великої букви та БЕЗ смайлика❗️)")

    elif message1.text == ("З сушеною лавандою"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваш квітковий🌸 рай виглядає ось так😌:")
        pic16 = open("E:\TelegremBot\Lavanda.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic16)
        bot.send_message(message1.chat.id, text="А пахне як🤤. Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("З маком та волошками"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваш квітковий🌸 рай виглядає ось так😌:")
        pic17 = open("E:\TelegremBot\ZMakomIVoloshkamu.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic17)
        bot.send_message(message1.chat.id, text="Полюбляєте мак? Не знаю але пиріжки з ними файні😎. Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("З орхідеєю"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваш квітковий🌸 рай виглядає ось так😌:")
        pic18 = open("E:\TelegremBot\Orhideya.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic18)
        bot.send_message(message1.chat.id, text="Обрали найестетитніше🤤. Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("У склі🌝"):
        bot.send_message(message1.chat.id, text="Полюбляєте квіти🌸? Моя сестра так сильно, що навіть працювала флористом😎🌺. Обирайте саму свічку🕯!                                                                                                                                                                           Із доступних: Зі сушеними маленькими квіточками💐, З рожевими квіточками, З орхідеєю🌺.                                                                                                                                                                                             (Для того щоб обрати, введіть на клавіатурі те що потрібно з великої букви та БЕЗ смайлика❗️)")

    elif message1.text == ("Зі сушеними маленькими квіточками"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваш квітковий🌸 рай виглядає ось так😌:")
        pic19 = open("E:\TelegremBot\SuhiFlowers.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic19)
        bot.send_message(message1.chat.id, text="Моїй бабусі якраз дуже подобається все сушити😂. Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("З орхідеєю"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваш квітковий🌸 рай виглядає ось так😌:")
        pic20 = open("E:\TelegremBot\Orhideya2.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic20)
        bot.send_message(message1.chat.id, text="Схоже ця свічка для моєї мами😂. Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("З рожевими квіточками"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваш квітковий🌸 рай виглядає ось так😌:")
        pic21 = open("E:\TelegremBot\PinkFlower.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic21)
        bot.send_message(message1.chat.id, text="Саме я дуже люблю квіти сакури🌸. Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("У баночці"):
        bot.send_message(message1.chat.id, text="Хочете когось зачарувати🧚? Ці свічки стануть у нагоді, адже вони прекрасні!. Обирайте її🕯!                                                                                                                                                                            Із доступних: З синьою магією🌌, З рожевою магією🎆, З таємною магією✨.                                                                                                                                                                                                  (Для того щоб обрати, введіть на клавіатурі те що потрібно з великої букви та БЕЗ смайлика❗️)")

    elif message1.text == ("З синьою магією"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваше чаклунство🔮 виглядає ось так😌:")
        pic22 = open("E:\TelegremBot\SinyaMagic.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic22)
        bot.send_message(message1.chat.id, text="Мені здається🤔, що вона дарить спокій✨. Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("З рожевою магією"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваше чаклунство🔮 виглядає ось так😌:")
        pic23 = open("E:\TelegremBot\PinkMagic.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic23)
        bot.send_message(message1.chat.id, text="Мені здається🤔, що вона дарить любов♥️✨. Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("З таємною магією"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваше чаклунство🔮 виглядає ось так😌:")
        pic24 = open("E:\TelegremBot\Magic.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic24)
        bot.send_message(message1.chat.id, text="Ніхто не знає чому вона таємна... Моживо, із за свого кольору?🤔. Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("У склі👄"):
        bot.send_message(message1.chat.id, text="Хочете когось зачарувати🧚? Ці свічки стануть у нагоді, адже вони прекрасні!. Обирайте її🕯!                                                                                                                                                                            Із доступних: З магією моря🏝, З магією луни🌙, З магією рожевих кристалів✨.                                                                                                                                                                                                        (Для того щоб обрати, введіть на клавіатурі те що потрібно з великої букви та БЕЗ смайлика❗️)")

    elif message1.text == ("З магією моря"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваше чаклунство🔮 виглядає ось так😌:")
        pic25 = open("E:\TelegremBot\Sea.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic25)
        bot.send_message(message1.chat.id, text="Напевне, вона була створена самими русалками🧜 у Марианській впадині... Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("З магією луни"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваше чаклунство🔮 виглядає ось так😌:")
        pic26 = open("E:\TelegremBot\Luna.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic26)
        bot.send_message(message1.chat.id, text="Впала з луни🌙... Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("З магією рожевих кристалів"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваше чаклунство🔮 виглядає ось так😌:")
        pic27 = open("E:\TelegremBot\Crystal.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic27)
        bot.send_message(message1.chat.id, text="Була знайдена десь у печері посеред кучі кристалів✨... Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("У самому фрукті"):
        bot.send_message(message1.chat.id, text="Мені теж цікаво як це свічка у фрукті🤔? Зараз подивимось!). Обирайте її🕯!                                                                                                                                                                           Із доступних: У кокосі🥥, У апельсині🍊, У ківі🥝.                                                                                                                                                                                        (Для того щоб обрати, введіть на клавіатурі те що потрібно з великої букви та БЕЗ смайлика❗️)")

    elif message1.text == ("У кокосі"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваша свічка-фрукт виглядає ось так😌:")
        pic28 = open("E:\TelegremBot\Coconut.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic28)
        bot.send_message(message1.chat.id, text="Дуже дивно, але дуже прикольно! Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("У апельсині"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваша свічка-фрукт виглядає ось так😌:")
        pic29 = open("E:\TelegremBot\Orange1.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic29)
        bot.send_message(message1.chat.id, text="Дуже дивно, але дуже прикольно! Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("У ківі"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваша свічка-фрукт виглядає ось так😌:")
        pic30 = open("E:\TelegremBot\Kiwi.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic30)
        bot.send_message(message1.chat.id, text="Дуже дивно, але дуже прикольно! Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("Ні у чому😚"):
        bot.send_message(message1.chat.id, text="У прямому сенсі ви обрали корисні свічки🍏! Обирайте вже її🕯!                                                                                                                                                               Із доступних: З грушею🍐, З лаймом, З апельсином🍊.                                                                                                                                                                        (Для того щоб обрати, введіть на клавіатурі те що потрібно з великої букви та БЕЗ смайлика❗️)")

    elif message1.text == ("З грушею"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваша корисна свічка виглядає ось так😌:")
        pic31 = open("E:\TelegremBot\Grusha.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic31)
        bot.send_message(message1.chat.id, text="Виглядає апетитно! Але я не люблю груші😒. Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("З лаймом"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваша корисна свічка виглядає ось так😌:")
        pic32 = open("E:\TelegremBot\Lime.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic32)
        bot.send_message(message1.chat.id, text="Виглядає доволі кисло🤤! Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("З апельсином"):
        bot.send_message(message1.chat.id, text="Вітаємо! Ваша корисна свічка виглядає ось так😌:")
        pic33 = open("E:\TelegremBot\Orange2.jpg", "rb")
        bot.send_photo(chat_id=message1.from_user.id, photo=pic33)
        bot.send_message(message1.chat.id, text="Виглядає апетитно! Бажаєте продивитись ще?😏 Якщо так знову вводіть Розпочати!, якщо ж бажаєте завершити пишіть Завершити!")

    elif message1.text == ("Завершити!"):
        bot.send_message(message1.chat.id, text="Дякую що завітали до мене! Надіюсь, Ви насолодились естетикою свічок😌🕯 Гарного дня або вечора!")
        bot.send_sticker(message1.chat.id, "CAACAgIAAxkBAAEGBR5jQGqth3WKF1BJW2sO62BtIRgklAAC0RMAAm8LOEmE7M5bHvTAdCoE")

    else:
        bot.send_message(message1.chat.id, text="Оооу... Схоже на таку свічку мене не програмували😭 перечитайте застереження, після цього перевірьте правильність написання слова, чи було вказано вписувати слово зі смайликом чи без, та чи з великої літери надруковано😉")





bot.polling(none_stop=True)