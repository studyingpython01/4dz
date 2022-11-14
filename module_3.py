card = 0
buyings = []
print('На вашем счету', card, 'рублей.')
money = []
while True:
    print('Вы можете:')
    print('1. Пополнить свой счёт;')
    print('2. Что-либо купить;')
    print('3. Просмотреть историю покупок;')
    print('4. Выйти из программы.')
    choice = input('Выберите пункт меню')
    if choice == '1':
        money_in = int(input('Сколько денег вы хотите положить на свой счёт?'))
        card += money_in
        print('Перевод средств осуществлён.')
        pass
    elif choice == '2':
        answer0 = int(input('Сколько денег вы хотите потратить?'))
        if answer0 > card:
            print('К сожалению, на вашем счёте недостаточно денег.')
            pass
        else:
            answer1 = input('Вы совершили покупку. Пожалуйста, назовите её.')
            card -= answer0
            buyings.append(answer1, answer0)
        pass
    elif choice == '3':
        print('Ваш лист покупок:', list(buyings))
        pass
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
