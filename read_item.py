def read_file(file):
    with open(file, 'r', encoding="utf-8") as data:
        for line in data:
            print(line)