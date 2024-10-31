##Consumir una api que se encuentra en API  CoinGeccko APIV3 #simple/price
## Obtener el valor del bitcoin y guardar esta información en un archivo llamado price.txt
import time
import requests
import logging
from cysystemd import  journal



logging.basicConfig()

logger=logging.getLogger()
logger.setLevel(logging.INFO) #mensajes mayor o igual a 20
journald_handler =journal.JournaldLogHandler()
journald_handler.setFormatter(logging.Formatter('%(levelname)$ - El precio de la cripto es %(message)$'))
logger.addHandler(journald_handler)

def get_current_price(id):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={id}&vs_currencies=usd'
    response = requests.get(url)
    
    if response.status_code==200:
        payload =response.json()
        return payload[id]['usd']

if __name__== '__main__':
    while True:
        price = get_current_price('bitcoin')
        message = str(price) + '\n'
        logger.info(message)
        with open('price.txt', 'a') as file:
            file.write(message)
        
        time.sleep(5)
