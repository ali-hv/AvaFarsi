from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from android.permissions import Permission, request_permissions, check_permission
from android.storage import app_storage_path, primary_external_storage_path, secondary_external_storage_path

#import arabic_reshaper
#from bidi.algorithm import get_display
from time import sleep
from bs4 import BeautifulSoup # for parsing requests content and extract musics links
import requests # for fetching requests to sites
#import urllib # for finding duplicat musics with their size
from urllib.parse import unquote # for decoding url to simple text
import os # for creating folder
#import sys

class layout(GridLayout):
    def __init__(self, **kwargs):
        super(layout, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text='Enter Singer full name:'))

        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.search = Button(text='Search')
        self.search.bind(on_press=self.search_m)
        self.add_widget(self.search)

        self.num = Label(text='')
        self.add_widget(self.num)

    def check_permissions(perms):
        for perm in perms:
            if check_permission(perm) != True:
                return False
        return True

    def search_m(self, instance):
        signer_name = self.name.text
        total_links = []

        def get_links(url): # getting musics links
            url += signer_name.replace(" ", "-").replace("ي", "ی")
            site = requests.get(url)
            text = site.text

            try:
                bs = BeautifulSoup(text, "html.parser")
                links = bs.find_all("audio") # finding audio tags from response
                links = [i["src"] for i in links] # getting links from audio tags

                url += "/page/"

                for i in range(2,99): # getting links from next pages
                    url_next_page = url + str(i)
                    site = requests.get(url_next_page)
                    if site.status_code == 200:
                        text = site.text
                        bs = BeautifulSoup(text, "html.parser")
                        links_next_page = bs.find_all("audio")
                        [links.append(j["src"]) for j in links_next_page]
                    else:
                        break

                total_links.append(links)
            except:
                total_links.append([""])


        # finding musics links from sites
        get_links("https://upmusics.com/tag/")
        get_links("https://music-fa.com/artist/")


        # find wich site has more musics from this signer
        if len(total_links[0]) > len(total_links[1]):
            links = total_links[0]
        else:
            links = total_links[1]

        if len(links) == 0:
            self.num.text = "Signer not found !!!"
        else:
            self.num.text = f'There are {len(links)} musics from this singer'

            self.how_many = Label(text='How many musics you want to download?')
            self.add_widget(self.how_many)

            self.music_num = TextInput(multiline=False)
            self.add_widget(self.music_num)

            self.download = Button(text='Download')
            self.download.bind(on_press=self.downloading)
            self.add_widget(self.download)

            self.progress = Label(text='')
            self.add_widget(self.progress)

    def downloading(self, instance):
        global links

        perms = [Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE]

        if  check_permissions(perms)!= True:
            request_permissions(perms)    # get android permissions
            exit()


        how_many_user_download = int(self.music_num.text)
        if how_many_user_download == 0:
            pass
        else:
            self.progress.text = 'downloading ...'
            folder_path = os.path.join( primary_external_storage_path(), signer_name)

            for i in range(0,how_many_user_download):
                music_name = unquote(links[i].split("/")[-1]) # getting the name of song
                music_name = music_name.split("-")[-1].replace("128", "").replace(")", "").replace("(", "").split("|")[-1]

                music_file = requests.get(links[i])

                with open(f'{folder_path}/{music_name}', 'wb') as f:
                    f.write(music_file.content)

            self.progress.text = f'Download Finished!\nYour music are stored in the {folder_path}'

class myApp(App):
    def build(self):
        return layout()

if __name__ == '__main__':
    myApp().run()
