def user_order(ingridients):
    print(f"You wish next ingridients in birger:")
    for ingridient in ingridients:
        print(f' - {ingridient}')

ingridients = ['bread', 'cheese', 'onion', 'tomato', 'meat']

user_order(ingridients)