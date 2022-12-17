import requests
import internet_check
import os
from bs4 import BeautifulSoup
from pathlib import Path
import re

def singer_name_musicfa_upmusics(self, app):
    if internet_check.check(self):
        self.search_singer_name_btn.setDisabled(1)
        self.notice_0.setText("در حال جستجو ...")
        app.processEvents()

        self.singer_name_text = self.get_singer_name.text().strip().replace("ي", "ی")
        singer_names = os.listdir('../resources/ui/singers_img/')
        # find the singer name from incomplete name
        if self.singer_name_text+'.jpg' not in singer_names:
            for i in singer_names:
                if self.singer_name_text in i.replace('-', ' '):
                    self.singer_name_text = i.replace('.jpg', '').replace("-", " ").strip()
                    break

        total_links = []
        total_music_names = []
        
        def get_links(url, html_tag1, html_tag2): # getting musics links
            url += self.singer_name_text.replace(" ", "-")
            site = requests.get(url)
            #print(site.status_code)
            text = site.text

            try:
                bs = BeautifulSoup(text, "html.parser")
                links = bs.find_all("audio") # finding audio tags from response
                links = [i["src"] for i in links] # getting links from audio tags
                music_names = bs.find_all(html_tag1, {'class':html_tag2})
                music_names = [i.find('strong').get_text() for i in music_names]
                music_names = [i.replace('آهنگ', '').replace('دانلود', '').replace('جدید', '').replace('فیلم', '').replace('قدیم', '')
                                .replace('سریال', '').replace('تیتراژ', '').replace('موزيک', '').replace('  ', ' ')
                                .replace(self.singer_name_text, '').strip() for i in music_names]

                url += "/page/"

                for i in range(2,99): # getting links from next pages
                    url_next_page = url + str(i)
                    site = requests.get(url_next_page)
                    if site.status_code == 200:
                        text = site.text
                        bs = BeautifulSoup(text, "html.parser")
                        links_next_page = bs.find_all("audio")
                        [links.append(j["src"]) for j in links_next_page]

                        music_names_next_page = bs.find_all(html_tag1, {'class':html_tag2})
                        music_names_next_page = [i.find('strong').get_text() for i in music_names_next_page if '<audio' in str(i)]
                        music_names_next_page = [i.replace('آهنگ', '').replace('دانلود', '').replace('آلبوم', '').replace('جدید', '')
                                                    .replace('تیتراژ', '').replace('فیلم', '').replace('موزيک', '').replace('  ', ' ').replace('قدیمی', '')
                                                    .replace('سریال', '').replace(self.singer_name_text, '').strip() for i in music_names_next_page]
                        [music_names.append(j) for j in music_names_next_page]
                    else:
                        break
                
                total_links.append(links)
                total_music_names.append(music_names)
            except:
                total_links.append([""])

        if self.second_site.isChecked():
            get_links("https://music-fa.com/artist/", "div", "cntfa")
        else:
            get_links("https://upmusics.com/tag/", "article", "upsng")

        self.links = total_links[0].copy()
        self.links_unique = []
        try:
            self.music_names = total_music_names[0].copy()
            for i in total_links[0]:
                if i not in self.links_unique:
                    self.links_unique.append(i)
            
            for i in range(len(self.links)):
                self.links[i] = [self.links[i], self.music_names[i]]

            self.select_music_name.addItem("- انتخاب موزیک -")
            for i in self.links:
                self.select_music_name.addItem(i[1])
        except IndexError:
            self.links = []
        
        if len(self.links) == 0:
            self.notice_0.setText("خواننده مورد نظر یافت نشد !!!")
        else:
            self.search_singer_name.hide()
            self.singer_name.setText(self.singer_name_text)
            self.number_of_musics.setText(f"تعداد موزیک ها : {len(self.links)}")
            self.singer_img.setStyleSheet(f"background-image: url(../resources/ui/singers_img/{self.singer_name_text.replace(' ', '-')}.jpg);\n"
                                            "border-radius: 30px;")
            self.page_1.show()

        self.search_singer_name_btn.setEnabled(1)
    else:
        self.notice_0.setText('لطفا به اینترنت متصل شوید!')

def singer_name_mrtehran(self, app):
    if internet_check.check(self):
        self.search_singer_name_btn.setDisabled(1)
        self.notice_0.setText("در حال جستجو ...")
        app.processEvents()

        self.singer_name_text = self.get_singer_name.text().strip().replace("ي", "ی")
        
        links = open("../resources/musics_db/singers_links(MrTehran).txt", "r").readlines()
        links = [i.strip().split(',') for i in links]
        
        for i in links:
            if self.singer_name_text == i[0]:
                url = i[1]
                found = 1
                break
        else:
            for i in links:
                if self.singer_name_text in i[0]:
                    url = i[1]
                    self.singer_name_text = i[0]
                    found = 1
                    break
            else:
                self.notice_0.setText('خواننده مورد نظر یافت نشد !!!')
                self.search_singer_name_btn.setEnabled(1)
                found = 0
            
        if found:
            site = requests.get(url)
            text = site.text
            bs = BeautifulSoup(text, 'html.parser')
            
            music_links = bs.find_all('div', {'class':'col mb-3'})
            music_links = [re.findall('data-song="(.*\.mp3)"', str(i))[0] for i in music_links if 'data-song="' in str(i)]

            music_names = bs.find_all('a', {'class':'text-truncate'})[0:len(links)]
            music_names = [i.get_text() for i in music_names]
            
            self.select_music_name.addItem("- انتخاب موزیک -")
            for i in music_names:
                self.select_music_name.addItem(i)

            self.links_unique = music_links
            self.links = list(zip(music_links,music_names))
            
            self.search_singer_name.hide()
            self.singer_name.setText(self.singer_name_text)
            self.number_of_musics.setText(f"تعداد موزیک ها : {len(self.links_unique)}")
            self.singer_img.setStyleSheet(f"background-image: url(../resources/ui/singers_img/{self.singer_name_text.replace(' ', '-')}.jpg);\n"
                                                "border-radius: 30px;")
            self.page_1.show()

            self.search_singer_name_btn.setEnabled(1)

def music_name(self, app):
    if internet_check.check(self):
        self.select_music.clear()
        self.select_music.addItem("- انتخاب موزیک -")

        path = Path('../resources/musics_db/musics_db.txt')
        musics_db = open(path, 'r', encoding='utf-8', errors='ignore').readlines()
        musics_db = [i.split(',') for i in musics_db]

        music_name = self.music_name.text().replace('  ', ' ').strip()

        self.music_links = []

        for i in musics_db:
            if self.back.isCheckable():
                if  music_name in i[3].strip():
                    if i[2] not in self.music_links:
                        self.music_links.append(i[2])
                        self.select_music.addItem(f"{i[1]} - {i[0]}")
            else:
                if music_name == i[1].strip():
                    if i[2] not in self.music_links:
                        self.music_links.append(i[2])
                        self.select_music.addItem(f"{i[1]} - {i[0]}")

        if len(self.music_links) == 0:
            self.notice_2.setText('موزیکی پیدا نشد!')
            self.music_name.clear()
        else:
            self.notice_2.clear()
            self.dl_music_name_btn.show()
            self.select_music.show()
    else:
        self.notice_2.setText('لطفا به اینترنت متصل شوید!')
