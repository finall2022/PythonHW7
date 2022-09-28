def ii(file):
    with open(file, 'a', encoding="utf-8") as data:
        data.write('\n')
        data.write(input('Фамилия: '))
        data.write(', ')
        data.write(input('Имя: '))
        data.write(', ')
        data.write(input('Телефон: '))
        data.write(', ')
        data.write(input('Описание: '))