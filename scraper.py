import requests

respons = requests.get('https://www.ceneo.pl/63419968#tab=reviews')


print(respons.status_code)
