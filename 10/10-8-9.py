def read_animal(file_name):
    try:
        with open(file_name) as file:
            name = file.readlines()
    except:
        pass
    else:
        print(name)

read_animal('.\\10\\cat.txt')