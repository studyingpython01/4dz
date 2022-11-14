print('Šāmürâī X')
import random

while True:

    birthdays = {'napoleon': '15.08.1769',
    'zuckerberg' : '14.05.1984',
    'musk' : '28.06.1971',
    'bezos' : '12.01.1964',
    'da_vinci' : '02.04.1452',
    'newton' : '04.01.1643',
    'einstein' :'14.03.1879',
    'columbus' : '31.10.1451',
    'paster' : '27.12.1822',
    'darwin' : '12.02.1809'
                 }
    answer = {
    '15.08.1769': 'Пятнадцатое августа 1769 года',
    '14.05.1984': 'Четырнадцатое мая 1984 года',
    '28.06.1971': 'Двадцать восьмое июня 1971 года',
    '12.01.1964': 'Двенадцатое января 1964 года',
    '02.04.1452': 'Второе апреля 1452 года',
    '04.01.1643': 'Четвёртое января 1643 года',
    '14.03.1879': 'Четырнадцатое марта 1879 года',
    '31.10.1451': ' Тридцать первое октября 1451 года',
    '27.12.1822': 'Двадцать седьмое декабря 1822 года',
    '12.02.1809': 'Двенадцатое февраля'
    }
    mistakes = 0
    right = 0

    keys = random.sample(list(birthdays), 5)
    for key in list(keys):
        answer_m = input( 'Укажите дату рождения(dd.mm.yyyy): ' + key + '\n')
        if answer_m != birthdays[key]:
            mistakes += 1
            print(answer.get(birthdays[key]))
        else:
            right += 1

    def calculate(x, y, z):
      result = x * (y / z)
      return result


    print('Ошибки:', mistakes)
    print('Правильные ответы:', right)
    right = int(right)
    mistakes = int(mistakes)
    print('Процент правильных ответов:', calculate(right, 100, 5))
    print('Процент неправильных ответов:', calculate(mistakes, 100, 5))
    answer_last = input("Хотите начать игру с начала? Если нет, введите 'нет'. Если да, введите 'да'.")
    if answer_last == 'нет':
        break

