from flask import Flask, request
import random
app = Flask(__name__)
a1 = True
a2 = True
a3 = True
a4 = True
a5 = True
a6 = True

@app.route('/', methods=['POST'])

def resp():
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    text = request.json.get('request', {}).get('command')
    end = False
    req = request.json
    if req["session"]["new"]:
        response_text = 'Добро пожаловать в игру Монополия с Алисой. Правила очень просты, вы кидаете 2 кубика и передвигаете свою фишку из поля "Старт" на количество клеток, равное выпавшему числу. Хотите пройти обучение?'
    elif req["request"]["original_utterance"].lower() in ["да", "давай", "поехали", "так точно", "ок", "окей", "погнали", "вперед", "начинай"] and a4 == True:
       response_text = 'Начинаем обучение. В начале хода вы бросаете 2 кубика и ходите выпавшее число шагов. Если выпадает два одинаковых числа (дубль), ходите еще раз. Скажите: "Брось кубики".'
       a4 = False
    elif req["request"]["original_utterance"].lower() in ["брось кубики", "бросай", "кинь кубики", "кидай"] and a1 == True:
        response_text = 'Вам выпало 5+5=10, дубль! \n Вы попали на клетку с недвижимостью,  стоимость - 500, Ваш баланс - 1500. Желаете приобрести или оставить? Если я в дальнейшем наступлю на вашу недвижимость, то буду вынуждена заплатить Вам. Скажите: "Приобрести".'
        a1 = False
    elif req["request"]["original_utterance"].lower() in ["приобрести", "купить", "взять", "получить"] and a6 == True:
        response_text = 'Поздравляю с приобретением! Ходите еще раз.' 
        a6 = False
    elif req["request"]["original_utterance"].lower() in ["брось кубики", "бросай", "кинь кубики", "кидай"] and a2 == True:
        response_text = 'Вам выпало 2+2=4, дубль! Вы попали на клетку "Шанс". Итак, я снимаю верхнюю карточку... "Переместитесь на поле Вперед!". Вы перемещаетесь на поле "Вперед" (начальное поле) и получаете 200. Вы будете получать 200 каждый раз, когда будете проходить это поле. Вы ходите еще раз.'
        a2 = False
    elif req["request"]["original_utterance"].lower() in ["брось кубики", "бросай", "кинь кубики", "кидай"] and a3 == True:
        response_text = 'Вам выпало 3+3=6, дубль! Вам несказанно везет - три дубля подряд. По правилам игры - если вам выпадает три дубля подряд, вы отправляетесь в тюрьму. Теперь вы в тюрьме и не можете ходить, пока не выйдете оттуда. Чтобы выйти из тюрьмы, в следущем ходе выбросите дубль или заплатите 100. Продолжаем?'
        a3 = False
    elif req["request"]["original_utterance"].lower() in ["да", "давай", "поехали", "так точно", "ок", "окей", "погнали", "вперед", "начинай"] and a5 == True:
        response_text = 'Наконец наступил мой ход. Я бросаю кубики. Мне выпало 5+5=10. Я попала на вашу недвижимость и плачу вам 20. Чтобы я платила вам больше - улучшайте свою недвижимость (подробнее об этом и других тонкостях игры в полых правилах). \n Показать полные правила или начать игру?'
        a5 = False
    
    response = {
        'response': {
            'text': response_text,
            'end_session': end
        },
        'session': request.json["session"],
        'version': request.json["version"]
    }
    return response

# def game():
#     text = request.json.get('request', {}).get('command')
#     if text == '':
#         response_text = "Начало игры!"
#         end = False
#         response_text = "Определяем, кто будет первым ходить. Если выпадет 1-первым ходишь ты, а если 2, то я"
#         why_first = random.randint(1, 2)
#     if why_first == 1:
#         response_text = "Чтож тебе повезло, ходи первым"
#     else:
#         response_text = "В этот раз посчястливелось мне, я хожу первая"
#     response = {
#         'response': {
#             'text': response_text,
#             'end_session': end
#         },
#         'session': request.json["session"],
#         'version': request.json["version"]
#     }
#     return response


app.run('0.0.0.0', port=5000, debug=True)