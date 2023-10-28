def show_messages(text_list,sent_list):
   while text_list:
       sended = text_list.pop()
       print(f'{sended}')
       sent_list.append(sended)

text_list = ['Hello', 'you', 'are', 'bitch']
sent_list = []


show_messages(text_list[:], sent_list)

print(text_list)
print(sent_list)

