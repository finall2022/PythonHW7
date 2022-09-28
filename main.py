import insert_item as ins_i
import read_item as rea_i
import import_item as imp_i
import export_item as exp_i
import find_item as find_i
import del_item as del_i


m = -1
while m != 0:
    print('\t\t<< Программа - телефонный справочник >>')
    print('\t*Меню:*')
    print('1. Просмотр записей\n2. Добавление записей\n\
3. Импорт\n4. Экспорт\n5. Поиск\n6. Удаление\n0. Выход из программы')
    m = int(input('Выберите нужное действие: '))
    if m == 1:
        rea_i.read_file('base.txt')
    if m == 2:
        ins_i.ii('base.txt')
    if m == 3:
        print('Введите имя файла для импорта')
        filename = input()
        imp_i.import_i(filename)
    if m == 4:
        print('Введите имя файла для экспорта')
        filename = input()
        print('Введите формат файла: 1 - *.txt, 2 - *.csv, 3 - *.xml')
        f = int(input())
        print('Введите представление файла: 1 - вертикальное, 2 - горизонтальное')
        p = int(input())
        exp_i.export_i(filename, p, f)
    if m == 5:
        find_i.find_item()
    if m == 6:
        del_i.del_item()
