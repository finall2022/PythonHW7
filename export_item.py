def export_i(filename, p, f):
    print(p)
    if p != 1 and p != 2:
        print('Выбран неверный формат')
        return
    if f == 1:
        ext = '.txt'
        file = filename+ext
        data_export = open(file, 'w', encoding="utf-8")
        data = open('base.txt', 'r', encoding="utf-8")
        if p == 1:
            for line in data:
                it = line.replace(' ', '')
                items = it.split(',')
                for i in items:
                    data_export.writelines(f'{i}\n')
        if p == 2:
            for line in data:
                items = (line)
                data_export.writelines(items)

    if f == 2:
        ext = '.csv'
        file = filename+ext
        data_export = open(file, 'w')  # , encoding="utf-8")
        data = open('base.txt', 'r', encoding="utf-8")
        if p == 1:
            for line in data:
                it = line.replace(' ', '')
                items = it.split(',')
                for i in items:
                    data_export.writelines(f'{i}\n')
        if p == 2:
            for line in data:
                it = line.replace(',', ';')
                items = (it)
                data_export.writelines(items)

    if f == 3:
        ext = '.xml'
        file = filename+ext
        data_export = open(file, 'w', encoding="utf-8")
        data = open('base.txt', 'r', encoding="utf-8")
        data_export.write('<?xml version="1.0"?>\n')
        data_export.write('<ДАННЫЕ>\n')
        tag = ('Фамилия', 'Имя', 'Телефон', 'Описание')
        id_contact = 1
        for line in data:
            it = line.replace(' ', '')
            items = it.split(',')
            data_export.write(f'<Контакт{id_contact}>\n')
            ind = 0
            for i in items:
                tg = tag[ind]
                data_export.write(f'<{tg}>{i}</{tg}>\n')
                ind += 1
            data_export.write(f'</Контакт{id_contact}>\n')
            id_contact+=1
        data_export.write('</ДАННЫЕ>')
    data.close()
    data_export.close()
