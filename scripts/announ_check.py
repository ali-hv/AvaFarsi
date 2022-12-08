import internet_check
import requests
from bs4 import BeautifulSoup

def check(self):
    if internet_check.check(self):
        url = 'https://gowharin.ir/collections/763'
        site = requests.get(url, timeout=10)
        bs = BeautifulSoup(site.text, 'html.parser')
        announ = bs.find_all('small')[1].get_text()
        announ_id = announ.split('\n')[0].strip()
        self.announ_content = '\n'.join(announ.split('\n')[1::]).replace(',', ' ')
        inbox_file = open('../inbox.txt', 'r', encoding='utf-8').readlines()
        if len(inbox_file) == 0:
            open('../inbox.txt', 'w').write(announ_id)
            self.new_message = True
        elif announ_id != inbox_file[0]:
            open('../inbox.txt', 'w').write(announ_id)
            self.new_message = True
        else:
            self.new_message = False
    else:
        self.new_message = False
