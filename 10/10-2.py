with open('C:\\Users\\svy\\OneDrive\\Рабочий стол\\vss\\py\\10\\learning_python.txt') as file:
    new_lines = file.readlines()

rep_str = ''

for line in new_lines:
    rep_str += line.replace('Python', 'JS')

print(rep_str)