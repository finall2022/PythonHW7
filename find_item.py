def find_item():
    with open('base.txt', 'r', encoding="utf-8") as data:
        find_i = str(input('Введите строку для поиска:\n'))
        count = 0
        for line in data:
            if find_i in line:
                print(line)
                count += 1
        print(f'Найдено записей: {count} шт.')