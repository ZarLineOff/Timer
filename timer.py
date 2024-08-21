import time
while True:
    try:
        second = int(input('Здравствуйте!Напишите кол-во сек для таймера!Если вы хотите выйти,введите 00'))
        if second == 00:
            print('До свидания')
            break
    except Exception:
        print('Ошибка ввода!')
    else:
        i = 0
        while i != second:
            i += 1
            print(f"Прошло секунд:{i}")
            print(f'Осталось секунд:{second-i}')
            if i == second:
                print('Время вышло!')
            time.sleep(1)