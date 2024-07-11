

req = None
tema = None
pol = None
while True:
    if req == None:
        print('\n1. Выберите тему')
        print('2. Выбрать пол')
        print('3. Досье')
        print('4. Выход')
    elif req == '1':
        while True:
            print('1. Темная')
            print('2. Светлая')
            req = input('\nВыберите тему: ')
            if req == '1':
                print('Тёмная тема установлена')
                req = None
                tema = 'Тёмная тема'
                break
            elif req == '2':
                print('Светлая тема установлена')
                req = None
                tema = 'Светлая тема'
                break
            else:
                print('Выбрана белеберда')
        continue
    elif req == '2':
        while True:
            print('1. Мужской')
            print('2. Женский')
            req = input('\nВыберите пол: ')
            if req == '1':
                print('Вы мужчина')
                req = None
                pol = 'Мужской'
                break
            elif req == '2':
                print('Вы женщина')
                req = None
                pol = 'Женский'
                break
            else:
                print('Вы выбрали белеберду')
        continue    
    elif req == '3':
        print(f'\nВаша тема: {tema}')
        print(f'Ваш пол: {pol}')
        req = None
        continue
    elif req == '4':
        status_code = 0
        if tema == None or pol == None:
            status_code = 1
        exit(status_code)
    else:
        print('Вы ввели белеберду')
        req = None 
        continue
        
    req = input('\nВыберите пункт меню: ')
    