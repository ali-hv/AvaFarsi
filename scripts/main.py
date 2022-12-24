#!/usr/bin/python3
# -*- coding: utf-8 -*-

#global libs
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QPoint
import os
import sys
import platform
from tkinter import Tk

#local libs
import download
import search
import announ_check
import internet_check


class Ui_MainWindow(QWidget):
    def __init__(self):
        announ_check.check(self) # checking for new announcements from the developers
        self.root = Tk().withdraw() # for browsing download folder path by user
        self.plt = platform.system() # detecting the operating system for file directions
        self.current_path = os.getcwd() # get the working directory

        #TODO Responsive window
        super().__init__()
        uic.loadUi('../resources/ui/main.ui', self)
        
        self.move(200,150)
        if self.new_message:
            self.inbox.setStyleSheet("background-color: rgb();\n"
                                     "background-image: url(../resources/ui/widgets_img/inbox_unread.png);")
         
        self.inbox_message.document().setDefaultTextOption(QtGui.QTextOption(Qt.AlignRight))
        
        if internet_check.check(self): self.inbox_message.setPlainText(str(self.announ_content))
        else: self.inbox_message.setPlainText('!اطلاعیه ای وجود ندارد')
        
        QtCore.QMetaObject.connectSlotsByName(self)

        #signals
        self.close_window.clicked.connect(sys.exit)
        self.minimize.clicked.connect(self.showMinimized)
        self.inbox.clicked.connect(self.show_inbox)
        self.back.clicked.connect(self.back_home)
        self.dl_singer_name.clicked.connect(self.menu_page.hide)
        self.dl_singer_name.clicked.connect(self.back.show)
        self.dl_singer_name.clicked.connect(self.get_singer_name.setFocus)
        self.dl_singer_name.clicked.connect(self.search_singer_name.show)
        self.get_singer_name.textChanged.connect(self.live_singer_face)
        self.get_singer_name.returnPressed.connect(self.search_singer_name_btn.click)
        self.search_singer_name_btn.clicked.connect(self.search_singer_name_func)
        self.search_singer_name_btn.clicked.connect(self.get_singer_name.setFocus)
        self.single_dl_btn.clicked.connect(self.single_dl_p1_func)
        self.multiple_dl_btn.clicked.connect(self.multiple_dl_p1_func)
        self.multiple_dl_input.returnPressed.connect(self.multiple_dl_btn.click)
        self.dl_all_musics.clicked.connect(self.download_all_func)
        self.dl_music_name.clicked.connect(self.back.show)
        self.dl_music_name.clicked.connect(self.search_music_name.show)
        self.dl_music_name.clicked.connect(self.music_name.setFocus)
        self.dl_music_name.clicked.connect(self.music_name_clicked_signal)
        self.search_music_name_btn.clicked.connect(self.search_music_name_func)
        self.search_music_name_btn.clicked.connect(self.music_name.setFocus)
        self.dl_music_name_btn.clicked.connect(self.dl_music_name_func)
        self.music_name.returnPressed.connect(self.search_music_name_btn.click)
        self.dl_part_music.clicked.connect(self.back.show)
        self.dl_part_music.clicked.connect(self.search_music_name.show)
        self.dl_part_music.clicked.connect(self.music_name.setFocus)
        self.dl_part_music.clicked.connect(self.part_music_clicked_signal)


    def show_inbox(self):
        self.inbox.setStyleSheet("background-color: rgb();\n"
                                 "background-image: url(../resources/ui/widgets_img/inbox.png);")
        if self.inbox_message.isHidden():
            self.inbox_message.show()
        else:
            self.inbox_message.hide()

    def disable_enable(self, job):
        self.single_dl_btn.setDisabled(job)
        self.multiple_dl_btn.setDisabled(job)
        self.dl_all_musics.setDisabled(job)

    def back_home(self):
        self.inbox_message.hide()
        self.search_singer_name.close()
        self.search_music_name.close()
        self.get_singer_name.clear()
        self.notice_0.clear()
        self.multiple_dl_input.clear()
        self.select_music_name.clear()
        self.select_music.clear()
        self.select_music.hide()
        self.number_of_musics.clear()
        self.notice_1.clear()
        self.notice_2.clear()
        self.dl_music_name_btn.hide()
        self.music_name.clear()
        self.page_1.close()
        self.menu_page.show()
        self.back.hide()
        self.first_site.setChecked(1)

    def Handle_Progress(self, blocknum, blocksize, totalsize):
        ## calculate the progress
        readed_data = blocknum * blocksize
 
        if totalsize > 0:
            download_percentage = readed_data * 100 / totalsize
            #TODO specefiy the progress bar
            self.downloadBar_1.setValue(int(download_percentage))
            self.downloadBar_2.setValue(int(download_percentage))
            app.processEvents()

    def live_singer_face(self):
        singer_name = self.get_singer_name.text().replace(' ', '-')
        singers_list = os.listdir('../resources/ui/singers_img_mini/')
        if f'{singer_name}.jpg' in singers_list:
            self.live_face.setStyleSheet(f"background-image: url(../resources/ui/singers_img_mini/{singer_name}.jpg);\n"
                                          "border-radius: 15px;")
        else:
            self.live_face.setStyleSheet(f"background-image: url(../resources/ui/widgets_img/unknown_face.png);\n"
                                          "border-radius: 15px;")

    def search_singer_name_func(self):
        if self.first_site.isChecked():
            search.singer_name_mrtehran(self, app)
        else:
            search.singer_name_musicfa_upmusics(self, app)

    def part_music_clicked_signal(self):
        self.back.setCheckable(1)
        self.music_name.setPlaceholderText('متن موزیک را اینجا بنویسید')

    def music_name_clicked_signal(self):
        self.back.setCheckable(0)
        self.music_name.setPlaceholderText('اسم موزیک را اینجا بنویسید')

    def multiple_dl_p1_func(self):
        if self.multiple_dl_input.text().isdigit() == False or self.multiple_dl_input.text() == '0':
            self.notice_1.setText('لطفا یک عدد وارد کنید !')
        else:
            self.downloadBar_1.setGeometry(QtCore.QRect(70, 335, 321, 61))
            download.singer_name(self, app, int(self.multiple_dl_input.text()))

    def download_all_func(self):
        self.downloadBar_1.setGeometry(QtCore.QRect(70, 420, 321, 71))
        download.singer_name(self, app, len(self.links_unique))

    def single_dl_p1_func(self):
        download.siner_name_single(self, app)

    def search_music_name_func(self):
        search.music_name(self, app)

    def dl_music_name_func(self):
        download.music_name(self, app)

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # loading the font from local resources
    QtGui.QFontDatabase.addApplicationFont("../resources/ui/fonts/Lalezar-Regular.otf")
    Lalezar_font = QtGui.QFont()
    Lalezar_font.setFamily("Lalezar")
    app.setStyle('fusion')
    app.setFont(Lalezar_font) # set the font for whole widgets
    app.setWindowIcon(QtGui.QIcon("../resources/ui/widgets_img/app_icon.ico"))
    myApp = Ui_MainWindow()
    myApp.show()
    sys.exit(app.exec_())
