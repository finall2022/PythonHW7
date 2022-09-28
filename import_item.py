def import_i(file):
    e = file.split('.')
    ext = e[1]

    if ext == 'txt':
        data_import = open(file, 'r', encoding="utf-8")
        data = open('base.txt', 'a', encoding="utf-8")
        data.writelines('\n')

        for line in data_import:
            data.writelines(line)

    if ext == 'csv':
        data_import = open(file, 'r')
        data = open('base.txt', 'a', encoding="utf-8")
        data.writelines('\n')

        for line in data_import:
            data.writelines(line.replace(';', ','))

    data.close()
    data_import.close()
