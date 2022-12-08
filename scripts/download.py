import urllib
from pathlib import Path
import directory
from PyQt5 import QtCore

def singer_name(self, app, end_of_the_loop):
    self.disable_enable(1)
    self.notice_1.setText("در حال دانلود ...")
    app.processEvents()
    singer_name = self.singer_name_text

    directory.make_dir(self, singer_name)

    for i in range(0,end_of_the_loop): # downloading musics
        try:
            #print(self.links_unique[i])
            music_name = self.links_unique[i].replace('%7C', '-').replace('|', '-')
            music_name = ' '.join(music_name.split('-%20')[1].split('%20')[0:-1]) + '.mp3' # getting the name of song
        except IndexError:
            try:
                music_name = self.links_unique[i].split('/')[-1]
            except IndexError:
                self.back_home()
                break

        music_name = music_name.replace("128", "").replace(")", "").replace("(", "").replace("-", "").strip()

        file_path = Path(f"{self.path}/{singer_name}/{music_name}")

        self.downloadBar_1.show()
        app.processEvents()

        urllib.request.urlretrieve(self.links_unique[i].replace('|', '%7C'), file_path, self.Handle_Progress)

        self.notice_1.setText(f"{i+1} موزیک دانلود شد")
        app.processEvents()

    self.notice_1.setText("موزیک ها با موفقیت دانلود شدند :)")
    self.downloadBar_1.hide()
    self.stop_1.hide()
    self.disable_enable(0)

    path = Path(f'{self.path}/{singer_name}')
    directory.open_dir(self, path)

def siner_name_single(self, app):
    if self.select_music_name.currentText() == "- انتخاب موزیک -":
        self.notice_1.setText("لطفا یک آهنگ انتخاب کنید !")
    else:
        self.downloadBar_1.setGeometry(QtCore.QRect(70, 160, 321, 71))
        self.stop_1.setGeometry(QtCore.QRect(400, 164, 60, 60))
        #self.stop_1.show()
        app.processEvents()

        music_name = self.select_music_name.currentText()
        for i in self.links:
            if i[1] == music_name:
                music_link = i[0]
                music_name = i[1]
                break

        self.disable_enable(1)
        self.notice_1.setText("در حال دانلود ...")
        app.processEvents()
        singer_name = self.singer_name_text

        directory.make_dir(self, singer_name)

        music_name = music_name.replace("128", "").replace(")", "").replace("(", "").replace("-", "").strip() + '.mp3'

        file_path = Path(f"{self.path}/{singer_name}/{music_name}")

        self.downloadBar_1.show()
        app.processEvents()

        urllib.request.urlretrieve(music_link, file_path, self.Handle_Progress)

        self.notice_1.setText("موزیک دانلود شد")
        self.stop_1.hide()
        self.downloadBar_1.hide()
        self.disable_enable(0)
        app.processEvents()

        # opening the download directory
        path = Path(f'{self.path}/{singer_name}')
        directory.open_dir(self, path)

def music_name(self, app):
    index = self.select_music.currentIndex()

    if index == 0:
        self.notice_2.setText("لطفا یک موزیک انتخاب کنید!")
    else:
        music_name, singer_name = self.select_music.currentText().split('-')
        music_name, singer_name = music_name.strip(), singer_name.strip()

        self.downloadBar_2.show()
        # self.stop_2.show()
        self.notice_2.setText('در حال دانلود ...')
        app.processEvents()

        directory.make_dir(self, singer_name)

        file_path = Path(f"{self.path}/{singer_name}/{music_name}.mp3")
        urllib.request.urlretrieve(self.music_links[index-1], file_path, self.Handle_Progress)

        path = Path(f'{self.path}/{singer_name}')
        directory.open_dir(self, path)

        self.notice_2.setText("موزیک با موفقیت دانلود شد :)")
        self.select_music.hide()
        self.dl_music_name_btn.hide()
        self.notice_2.clear()
        self.music_name.clear()
        self.select_music.clear()
        self.downloadBar_2.hide()
        self.stop_2.hide()