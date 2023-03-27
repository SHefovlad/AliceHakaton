from flask import Flask, request
import random
app = Flask(__name__)
# Сцены для обучения
a1 = True
a2 = True
a3 = True
a4 = True
a5 = True
a6 = True
a7 = True
# Сцены для полного обучения
b1 = True
b2 = True
b3 = True
b4 = False
b5 = True
b6 = False
b7 = True
b8 = True
# сцены для игры
g1 = True
g2 = True
g3 = True
g4 = True
g5 = True
g6 = True
g7 = True
g8 = True
g9 = True
g10 = True
train = False
rules = True
startGame = False
playerPoints = 0
alicePoints = 0
playerMoney = 1500
aliceMoney = 1500
reset = 0

place = ["Начало", "город Тюмень", "Шанс", "город Самара", "Подоходный налог", "Рижская железная дорога", "город Калуга", "Шанс", "город Пермь", "город Томск", "Тюрьма(просто посетители)", "город Уфа", "Шанс", "город Казань", "город Краснодар", "Курская железная дорога", "город Архангельск", "Шанс", "город Челябинск", "город Нижний Новгород", "Бесплатная стоянка", "город Омск", "Шанс", "город Волгоград", "город Белгород", "Казанская железная дорога", "город Ставрополь", "город Ростов-на-Дону", "Шанс", "город Хабаровск", "В тюрьму", "город Екатеринбург", "город Владивосток", "Шанс", "город Санкт-Петербург", "Ленинградская железная дорога", "Шанс", "город Москва", "Шанс", "город Новосибирск"]
price = [0, 60, 0, 60, 200, 200, 100, 0, 100, 120, 0, 140, 0, 140, 160, 200, 180, 0, 180, 200, 0, 220, 0, 220, 240, 200, 260, 260, 0, 280, 0, 300, 300, 0, 320, 200, 0, 350, 0, 400]
playerCard = []
aliceCard = []
@app.route('/', methods=['POST'])

def resp():
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global a7

    global b1
    global b2
    global b3
    global b4
    global b5
    global b6
    global b7
    global b8
    global train
    global rules

    global g1
    global g2
    global g3
    global g4
    global g5
    global g6
    global g7
    global g8
    global g9
    global g10

    global startGame
    global playerPoints
    global alicePoints
    global place
    global playerMoney
    global aliceMoney
    global playerCard
    global aliceCard
    global response_text
    global reset
    text = request.json.get('request', {}).get('command')
    end = False
    req = request.json
    if req["session"]["new"]:
        response_text = 'Добро пожаловать в игру Монополия с Алисой. Правила очень просты, вы кидаете 2 кубика и передвигаете свою фишку из поля "Старт" на количество клеток, равное выпавшему числу. Хотите пройти обучение?'
    elif req["request"]["original_utterance"].lower() in ["да", "давай", "поехали", "так точно", "ок", "окей", "погнали", "вперед", "начинай"] and a4 == True:
        response_text = 'Начинаем обучение. В начале хода вы бросаете 2 кубика и ходите выпавшее число шагов. Если выпадает два одинаковых числа (дубль), ходите еще раз. Скажите: "Брось кубики".'
        a4 = False
        train = True
    elif req["request"]["original_utterance"].lower() in ["брось кубики", "бросай", "кинь кубики", "кидай", "кинь", "брось"] and a1 == True:
        response_text = 'Вам выпало 5+5=10, дубль! \n Вы попали на клетку с недвижимостью,  стоимость - 500, Ваш баланс - 1500. Желаете приобрести или оставить? Если я в дальнейшем наступлю на вашу недвижимость, то буду вынуждена заплатить Вам. Скажите: "Приобрести".'
        a1 = False
    elif req["request"]["original_utterance"].lower() in ["приобрести", "купить", "взять", "получить"] and a6 == True:
        response_text = 'Поздравляю с приобретением! Ходите еще раз.' 
        a6 = False 
    elif req["request"]["original_utterance"].lower() in ["брось кубики", "бросай", "кинь кубики", "кидай", "кинь", "брось"] and a2 == True:
        response_text = 'Вам выпало 2+2=4, дубль! Вы попали на клетку "Шанс". Итак, я снимаю верхнюю карточку... "Переместитесь на поле Вперед!". Вы перемещаетесь на поле "Вперед" (начальное поле) и получаете 200. Вы будете получать 200 каждый раз, когда будете проходить это поле. Вы ходите еще раз.'
        a2 = False
    elif req["request"]["original_utterance"].lower() in ["брось кубики", "бросай", "кинь кубики", "кидай", "кинь", "брось"] and a3 == True:
        response_text = 'Вам выпало 3+3=6, дубль! Вам несказанно везет - три дубля подряд. По правилам игры - если вам выпадает три дубля подряд, вы отправляетесь в тюрьму. Теперь вы в тюрьме и не можете ходить, пока не выйдете оттуда. Чтобы выйти из тюрьмы, в следущем ходе выбросите дубль или заплатите 100. Наконец наступил мой ход. Я бросаю кубики. Мне выпало 5+5=10. Я попала на вашу недвижимость и плачу вам 20. Чтобы я платила вам больше - улучшайте свою недвижимость Если готовы начать, то скажите "Начать игру".'
        a3 = False
    elif req["request"]["original_utterance"].lower() in ["нет", "неа", "не", "игру", "давай игру", "начать игру"] and a7 == True:
        response_text = 'Отлично! Начинаем игру, скажите "Брось кубики".'
        a7 = False
        startGame = True
    # ПОЛНЫЕ ПРАВИЛА
    elif req["request"]["original_utterance"].lower() in ["правила", "правила", "правила", "правила", "правила"] and b6 == True:
        response_text = 'В начале каждого хода вы бросаете 2 кубика и ходите вперед на выпавшее число. Если вам выпадает два одинаковых числа - дубль, то вы ходите еще раз. Если вам выпадает 3 дубля подряд, то вы отправитесь в тюрьму. Чтобы из неё выйти в следующем ходу, необходимо либо выбросить дубль, либо заплатить 100. Дальше?'
        b6 = True
    elif req["request"]["original_utterance"].lower() in ["дальше", "далее", "да", "ага", "давай", "поехали"] and b1 == True:
        response_text = 'Если остановились на ячейке «Шанс», тянут карточку с заданиями, которые сразу выполняют. Исключение — карточка «Бесплатно освободитесь от тюрьмы».Её используют не сразу, а сохраняют до подходящего момента. Дальше?'
        b1 = False
    elif req["request"]["original_utterance"].lower() in ["дальше", "далее", "да", "ага", "давай", "поехали"] and b2 == True:
        response_text = 'Когда другой игрок попал на клетку с купленной вами недвижимостью, то он обязан заплатить определенную сумму денег. Если улучшать клетку со своей недвижимостью, то другие игроки будут платить вам больше. Идём дальше?'
        b2 = False
    elif req["request"]["original_utterance"].lower() in ["дальше", "далее", "да", "ага", "давай", "поехали"] and b3 == True:
        response_text = 'Каждый раз, когда игроки доходят до поля "Начало", они получают 200 к своему капиталу. Едем дальше?'
        b3 = False
    elif req["request"]["original_utterance"].lower() in ["дальше", "далее", "да", "ага", "давай", "поехали", "едем", "вперед"] and b4 == True:
        response_text = 'Игра заканчивается тогда, когда на поле остается только один игрок, который не достиг банкротства. Ну что, готовы начать игру?'
        b4 = False
    elif req["request"]["original_utterance"].lower() in ["да", "давай", "поехали", "так точно", "ок", "окей", "погнали", "вперед", "начинай"] and b5 == True:
        startGame = True
        b5 = False
    # else:
    #     response_text = 'Извините, я вас плохо поняла, можете сказать по-другому?'
    while startGame == True:
        a1 = False
        a2 = False
        a3 = False
        a4 = False
        a5 = False
        a6 = False
        a7 = False

        b1 = False
        b2 = False
        b3 = False
        b4 = False
        b5 = False
        b6 = False
        b7 = False
        b8 = False
        
        global g1
        global g2
        global g3
        global g4
        global g5
        global g6
        global g7
        global g8
        global g9
        global g10
        if g4 == True:
            response_text = 'Отлично! Начинаем игру, скажите "Брось кубики".'
            g4 = False
        elif req["request"]["original_utterance"].lower() in ["брось кубики", "бросай", "кинь кубики", "кидай", "кинь", "брось"] and g1 == True:
            if playerPoints >= 40:
                playerPoints = 0
            g2 = False
            cubs = random.randint(2, 12)
            playerPoints += cubs
            if price[playerPoints] != 0:
                response_text = 'Вам выпало ' + str(cubs) + ' Вы попали на клетку ' + place[playerPoints] + ' цена этой клетки ' + str(price[playerPoints]) + ' ваш бюджет: ' + str(playerMoney) + '. Хотите купить эту клетку?'
                g3 = True
            elif place[playerPoints] == place[10]:
                response_text = 'Вы попали на клетку ' + place[10]
                g3 = False
            elif place[playerPoints] == place[20]:
                response_text = 'вы пришли на бесплатную стоянку'
                g3 = False
            elif place[playerPoints] == place[30]:
                response_text = 'Вы попали на запретную территорию, отправляйтесь в тюрьму'
                g3 = False
            elif place[playerPoints] == place[0] or playerPoints >= 40:
                reset += playerPoints
                playerPoints = 40
                playerPoints = reset - playerPoints
                reset = 0
            else:
                response_text = 'Вы попали на клетку шанс!'
                g3 = False
            g1 = False
        elif req["request"]["original_utterance"].lower() in ["да", "давай", "поехали", "так точно", "ок", "окей", "погнали", "вперед", "начинай"] and g3 == True:
            if playerMoney > price[playerPoints]:
                response_text = 'Отлично! карта: ' + place[playerPoints] + ' успешно куплена! Продолжаем?'
                playerMoney -= price[playerPoints]
                playerCard.append(place[playerPoints])
                g2 = True
                g3 = False
                response = {
                    'response': {
                        'text': response_text,
                        'end_session': end
                    },
                    'session': request.json["session"],
                    'version': request.json["version"]
                }
                return response
            else:
                response_text = 'Извините, у вас недостаточно средств, что бы купить эту карточку. Играем дальше?'
                g2 = True
                g3 = False
                response = {
                    'response': {
                        'text': response_text,
                        'end_session': end
                    },
                    'session': request.json["session"],
                    'version': request.json["version"]
                }
                return response
        elif req["request"]["original_utterance"].lower() in ["да", "давай", "поехали", "так точно", "ок", "окей", "погнали", "вперед", "начинай"] and g2 == True:
            if alicePoints >= 40:
                alicePoints = 0
            cubsA = random.randint(2, 12)
            alicePoints += cubsA
            response_text = 'Мне выпало ' + str(cubsA) + ' я попала на клетку ' + place[alicePoints] + ' \n скажите "Брось кубики".'
            g1 = True
            g2 = False
        
        response = {
            'response': {
                'text': response_text,
                'end_session': end
            },
            'session': request.json["session"],
            'version': request.json["version"]
        }
        return response
    response = {
        'response': {
            'text': response_text,
            'end_session': end
        },
        'session': request.json["session"],
        'version': request.json["version"]
    }
    return response
    
app.run('0.0.0.0', port=5000, debug=True)