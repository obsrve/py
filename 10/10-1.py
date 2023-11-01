with open('C:\\Users\\svy\\OneDrive\\Рабочий стол\\vss\\py\\10\\learning_python.txt') as file:
    new_file = file.readlines()

print(new_file)

for line in new_file:
    print(line.strip())

