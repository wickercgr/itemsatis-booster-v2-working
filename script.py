import requests
import re
import threading
import time
from sys import platform
from os import system
from colorama import Fore, Style
import schedule

class itemsatisup:
    print("true")
    def __init__(self):
        self.clear()
        self.ad_list = list()

        with open('ilanlar.txt', 'r', encoding='utf-8') as file:
            for ad in file.read().split('\n'):
                self.ad_list.append(re.search('(\d+)\.html$', ad).group(1))

#console temp
    def clear(self):
        if platform.startswith('win'):
            system('cls')
        else:
            system('clear')

    def process(self):
        for ad in self.ad_list:
            self.highlight_ad(ad)

    def highlight_ad(self, ad):
        try:
            cookies = {
                'PHPSESSID': 'login phpsessid',
            }

            headers = {
                'authority': 'www.itemsatis.com',
                'accept': '*/*',
                'accept-language': 'tr-TR,tr;q=0.6',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://www.itemsatis.com',
                'referer': 'https://www.itemsatis.com/ilanlarim.html',
                'sec-ch-ua': '"Not/A)Brand";v="99", "Brave";v="115", "Chromium";v="115"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0',
                'x-requested-with': 'XMLHttpRequest',
            }

            data = {
                'Id': ad,
            }

            response = requests.post('https://www.itemsatis.com/api/moveUpPost', cookies=cookies, headers=headers, data=data, timeout=60)

            if response.json()['success'] == True:
                print(f'{Fore.GREEN}WCK ✓ İlan başarıyla öne çıkarıldı: {ad}{Style.RESET_ALL}')
                print('-' * 25)
            else:
                print(f'{Fore.RED}WCK X Hata: {response.json()["message"]}{Style.RESET_ALL}')
                time.sleep(5)
                self.highlight_ad(ad)
        except Exception as e:
            print(f'{Fore.RED}X Hata: {e}{Style.RESET_ALL}')

bot = itemsatisup()
bot.process()
schedule.every(3).hours.do(bot.process)

while True:
    schedule.run_pending()
    time.sleep(1)