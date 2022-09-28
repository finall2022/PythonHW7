import os
def del_item():
    with open('base.txt', 'r', encoding="utf-8") as data:
        temp_data = open('temp.txt', 'w', encoding="utf-8")
        find_i = str(input('Введите строку для удаления:\n'))
        for line in data:
            if find_i not in line:
                temp_data.write(line)
        
    temp_data.close()
    os.remove('base.txt')
    os.rename('temp.txt', 'base.txt')