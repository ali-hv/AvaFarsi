# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'm_down.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from bs4 import BeautifulSoup
import requests
import urllib
import regex
import os
from random import randint
from time import sleep
import platform
import pymsgbox


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(407, 373)
        Dialog.setMinimumSize(QtCore.QSize(407, 373))
        Dialog.setMaximumSize(QtCore.QSize(407, 373))
        icon = QtGui.QIcon()
        #icon.addPixmap(QtGui.QPixmap("../../Downloads/com.downloader.music.prolkjipo-logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-image: url(bg.jpg); background-repeat: no-repeat; background-position: center")
        self.input_name_list = QtWidgets.QComboBox(Dialog)
        self.input_name_list.setGeometry(QtCore.QRect(20, 50, 191, 27))
        self.input_name_list.setObjectName("input_name_list")
        self.input_name_list.setStyleSheet("background-image:url()")
        self.input_name_list.addItem("")
        self.input_name_list.setItemText(0, "")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_list.addItem("")
        self.input_name_man = QtWidgets.QLineEdit(Dialog)
        self.input_name_man.setGeometry(QtCore.QRect(20, 90, 191, 27))
        self.input_name_man.setText("")
        self.input_name_man.setObjectName("input_name_man")
        self.input_name_man.setStyleSheet("border-radius: 5px; border: 2px solid gray; background-image:url()")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(216, 90, 151, 20))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("background-image:url()")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(250, 50, 117, 20))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("background-image:url()")
        self.search = QtWidgets.QPushButton(Dialog)
        self.search.setGeometry(QtCore.QRect(130, 140, 96, 36))
        self.search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search.setStyleSheet("background-color: rgb(0, 255, 0); border-radius: 15px; background-image:url()")
        self.search.setObjectName("search")
        self.num_musics_t = QtWidgets.QLabel(Dialog)
        self.num_musics_t.setEnabled(False)
        self.num_musics_t.setGeometry(QtCore.QRect(270, 180, 101, 20))
        self.num_musics_t.setStyleSheet("background-image:url()")
        self.num_musics_t.setObjectName("num_musics_t")
        self.num_musics = QtWidgets.QLabel(Dialog)
        self.num_musics.setEnabled(False)
        self.num_musics.setGeometry(QtCore.QRect(250, 180, 21, 22))
        self.num_musics.setStyleSheet("background-image:url()")
        self.num_musics.setText("")
        self.num_musics.setObjectName("num_musics")
        self.how_meny_t = QtWidgets.QLabel(Dialog)
        self.how_meny_t.setEnabled(False)
        self.how_meny_t.setGeometry(QtCore.QRect(160, 210, 211, 20))
        self.how_meny_t.setStyleSheet("background-image:url()")
        self.how_meny_t.setObjectName("how_meny_t")
        self.how_meny = QtWidgets.QLineEdit(Dialog)
        self.how_meny.setEnabled(False)
        self.how_meny.setGeometry(QtCore.QRect(120, 206, 31, 31))
        self.how_meny.setStyleSheet("background-image:url()")
        self.how_meny.setText("")
        self.how_meny.setObjectName("how_meny")
        self.download = QtWidgets.QPushButton(Dialog)
        self.download.setEnabled(False)
        self.download.setGeometry(QtCore.QRect(130, 256, 96, 36))
        self.download.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.download.setStyleSheet("background-color: rgb(255, 0, 0); border-radius: 15px; border: 2px solid red; background-image:url()")
        self.download.setObjectName("download")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setEnabled(False)
        self.progressBar.setGeometry(QtCore.QRect(80, 310, 197, 23))
        self.progressBar.setStyleSheet("#progressBar::chunk {background-color: rgb(0, 255, 247);border-radius: 6px;}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.finish = QtWidgets.QLabel(Dialog)
        self.finish.setGeometry(QtCore.QRect(110, 340, 131, 20))
        self.finish.setStyleSheet("background-image:url()")
        self.finish.setText("")
        self.finish.setObjectName("finish")
        self.setting = QtWidgets.QPushButton(Dialog)
        self.setting.setGeometry(QtCore.QRect(2, 2, 81, 31))
        self.setting.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setting.setObjectName("setting")
        self.setting.setStyleSheet("background-color: rgb(0, 0, 255); border-radius: 15px; border: 2px solid blue; background-image:url()")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(380, 50, 18, 25))
        self.radioButton.setStyleSheet("background-image:url()")
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(380, 90, 18, 25))
        self.radioButton_2.setStyleSheet("background-image:url()")
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.setting_m = QtWidgets.QDockWidget(Dialog)
        self.setting_m.setEnabled(True)
        self.setting_m.setGeometry(QtCore.QRect(20, 160, 371, 61))
        self.setting_m.setStyleSheet("")
        self.setting_m.setObjectName("setting_m")
        self.setting_m.setVisible(False)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.checkBox = QtWidgets.QCheckBox(self.dockWidgetContents)
        self.checkBox.setGeometry(QtCore.QRect(10, 0, 361, 25))
        self.checkBox.setObjectName("checkBox")
        self.setting_m.setWidget(self.dockWidgetContents)
        self.setting_m.setStyleSheet("background-image:url()")
        
        self.retranslateUi(Dialog)
        self.radioButton.clicked.connect(self.input_name_list.setFocus)
        self.radioButton_2.clicked.connect(self.input_name_man.setFocus)
        self.radioButton.clicked.connect(self.input_name_man.clear)
        self.setting.clicked.connect(self.setting_m.show)
        self.search.clicked.connect(self.search_m)
        self.download.clicked.connect(self.download_m)
        self.checkBox.clicked.connect(self.o_d)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.radioButton, self.radioButton_2)
        Dialog.setTabOrder(self.radioButton_2, self.input_name_list)
        Dialog.setTabOrder(self.input_name_list, self.input_name_man)
        Dialog.setTabOrder(self.input_name_man, self.search)
        Dialog.setTabOrder(self.search, self.checkBox)
        Dialog.setTabOrder(self.checkBox, self.how_meny)
        Dialog.setTabOrder(self.how_meny, self.download)
        Dialog.setTabOrder(self.download, self.setting)

    def o_d(self):
        if self.checkBox.isChecked() == False:
            with open('m.conf', 'w') as f:
                f.write('False')
                f.close()
        else:
            with open('m.conf', 'w') as f:
                f.write('True')
                f.close()

    def search_m(self):
        self.finish.clear()
        global links
        global sizes
        global pla
        global name

        plt = platform.system()

        if plt == "Windows":
            pla = '\\'
        elif plt == "Linux":
            pla = '/'

        if self.radioButton_2.isChecked() == True:
            name = self.input_name_man.text()
        else:
            name = self.input_name_list.currentText()
        
        name = name.replace('ي', 'ی')
        name = name.replace(' ', '-')

        url1 = f"https://upmusics.com/tag/{name}/"
        url2 = f"https://music-fa.com/artist/{name}/"

        #print(url1, ' ', url2)

        page = []

        def search_m(url):
            site = requests.get(url)
            status = site.status_code

            global pages

            if status == 404:
                page.append(0)
            else:
                site = site.text

                bs = BeautifulSoup(site, 'html.parser')
                pages = bs.find_all('a', {'class' : 'last'})
                pages = regex.sub('.*\/(\d+)\/.*', '\g<1>', str(pages))
                page.append(pages)
                if len(pages) == 2:
                    try:
                        pages = bs.find_all('a', {'class' : 'page'})
                        pages = regex.sub('.*"(.)".*', '\g<1>', str(pages[-1]))
                        page.append(pages)
                    except IndexError:
                        page.append(1)
 
                #print(pages)


        search_m(url1)
        search_m(url2)

        #print(page)

        if page.count(0) == 2 or page.count('0') == 2:
            pymsgbox.alert("Singer not found !!!", "Wrong!")
        else:
            try:
                page.remove('[]')
                page.remove('[]')
            except ValueError:
                pass
            #print(page)
            if int(page[0]) > int(page[1]):
                pages = int(page[0])
                url = url1
                site = requests.get(url)
                a = 0
            else:
                pages = int(page[1])
                url = url2
                site = requests.get(url)
                a = 1

            site = site.text
            bs = BeautifulSoup(site, 'html.parser')
            musics = bs.find_all('audio')
            musics = str(musics)
            bs = BeautifulSoup(musics, 'html.parser')

            links = []

            for i in range(100):
                try:
                    link = bs.findAll('audio')[i]
                    links.append(link.get("src"))
                except IndexError:
                    break

            if pages >= 2:
                for i in range (2,pages+1):
                    if a == 0:
                        url = f"https://upmusics.com/tag/{name}/page/{i}"
                    else:
                        url = f"https://upmusics.com/tag/{name}/page/{i}"
                    #print(url)
                    site = requests.get(url)
                    site = site.text

                    bs = BeautifulSoup(site, 'html.parser')
                    musics = bs.find_all('audio')
                    musics = str(musics)

                    bs = BeautifulSoup(musics, 'html.parser')

                    for i in range(100):
                        try:
                            link = bs.findAll('audio')[i]
                            links.append(link.get("src"))
                        except IndexError:
                            break
            #print(len(links))
            music = len(links)
            sizes = []

            for i in range(music):
                try:
                    url = links[i]
                except IndexError:
                    break
                try:
                    size = urllib.request.urlopen(url)
                except urllib.error.HTTPError:
                    break
                except UnicodeEncodeError:
                    break
                length = size.length
                sizes.append(length)
                num = sizes.count(length)
                if num == 2:
                    b = links[i]
                    links.remove(b)

            self.num_musics_t.setEnabled(True)
            self.num_musics.setEnabled(True)
            self.num_musics.setText(str(len(links)))
            self.how_meny.setEnabled(True)
            self.how_meny_t.setEnabled(True)
            self.download.setEnabled(True)

            
            

    def download_m(self):
        self.finish.clear()
        number = int(self.how_meny.text())
        size = 0
        for i in range(number):
            size += int(sizes[i])
        size = size / 1000000
        size = int(size)
        s_y_n = pymsgbox.confirm(text=f'The size of musics are {size} MB . Do you want to download ?', title='size', buttons=('yes','no'))
        if s_y_n == 'no':
            pass
        else:
            self.search.setDisabled(True)
            self.download.setText('... در حال دانلود')
            self.download.setDisabled(True)
            pr_bar = 100 / number

            if number > 0:
                try:
                    path = os.getcwd() + pla + name
                    files = os.mkdir(path)
                    print(path)
                except FileExistsError:
                    rand = str(randint(1,50))
                    path = os.getcwd() + pla + name + rand
                    files = os.mkdir(path)
            for i in range(number):
                url = links[i]
                r = requests.get(url, allow_redirects=True)
                open(f'%s{pla}%s%i.mp3' %(path, name, i+1), 'wb').write(r.content)

                self.progressBar.setValue(int(pr_bar)*(i+1))
            self.progressBar.setValue(100)
            
            sleep(1)
            self.finish.setText('دانلود به اتمام رسید !')
            sleep(2)
            with open('m.conf', 'r') as f:
                o = f.read()
                f.close()
            if 'True' in o:
                os.system(f'xdg-open {path}')
            else:
                pass
            #print(size)

            self.download.setText('دانلود')
            self.progressBar.setValue(0)
            self.how_meny.clear()
            self.num_musics.clear()
            self.input_name_man.clear()
            self.input_name_list.setCurrentIndex(0)
            self.search.setEnabled(True)
            self.download.setEnabled(True)


    def retranslateUi(self, Dialog):
        app.processEvents()
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Music Downloader"))
        self.input_name_list.setItemText(1, _translate("Dialog", "آراد"))
        self.input_name_list.setItemText(2, _translate("Dialog", "آرون افشار"))
        self.input_name_list.setItemText(3, _translate("Dialog", "احسان خواجه امیری"))
        self.input_name_list.setItemText(4, _translate("Dialog", "احمد سلو"))
        self.input_name_list.setItemText(5, _translate("Dialog", "اشوان"))
        self.input_name_list.setItemText(6, _translate("Dialog", "افشین آذری"))
        self.input_name_list.setItemText(7, _translate("Dialog", "امو بند"))
        self.input_name_list.setItemText(8, _translate("Dialog", "امید جهان"))
        self.input_name_list.setItemText(9, _translate("Dialog", "امید حاجیلی"))
        self.input_name_list.setItemText(10, _translate("Dialog", "امیر تاجیک"))
        self.input_name_list.setItemText(11, _translate("Dialog", "امیر عباس گلاب"))
        self.input_name_list.setItemText(12, _translate("Dialog", "امین بانی"))
        self.input_name_list.setItemText(13, _translate("Dialog", "امین حبیبی"))
        self.input_name_list.setItemText(14, _translate("Dialog", "امین رستمی"))
        self.input_name_list.setItemText(15, _translate("Dialog", "ایهام"))
        self.input_name_list.setItemText(16, _translate("Dialog", "ایوان بند"))
        self.input_name_list.setItemText(17, _translate("Dialog", "بابک افرا"))
        self.input_name_list.setItemText(18, _translate("Dialog", "بابک جهانبخش"))
        self.input_name_list.setItemText(19, _translate("Dialog", "بنیامین بهادری"))
        self.input_name_list.setItemText(20, _translate("Dialog", "بهنام بانی"))
        self.input_name_list.setItemText(21, _translate("Dialog", "پازل بند"))
        self.input_name_list.setItemText(22, _translate("Dialog", "پدرام آزاد"))
        self.input_name_list.setItemText(23, _translate("Dialog", "پدرام پالیز"))
        self.input_name_list.setItemText(24, _translate("Dialog", "پرواز همای"))
        self.input_name_list.setItemText(25, _translate("Dialog", "پویا بیاتی"))
        self.input_name_list.setItemText(26, _translate("Dialog", "پیمان پهلوان"))
        self.input_name_list.setItemText(27, _translate("Dialog", "چارتار"))
        self.input_name_list.setItemText(28, _translate("Dialog", "حامد زمانی"))
        self.input_name_list.setItemText(29, _translate("Dialog", "حامد محضرنیا"))
        self.input_name_list.setItemText(30, _translate("Dialog", "حامد همایون"))
        self.input_name_list.setItemText(31, _translate("Dialog", "حجت اشرف زاده"))
        self.input_name_list.setItemText(32, _translate("Dialog", "حمید عسکری"))
        self.input_name_list.setItemText(33, _translate("Dialog", "حمید هیراد"))
        self.input_name_list.setItemText(34, _translate("Dialog", "راغب"))
        self.input_name_list.setItemText(35, _translate("Dialog", "رامین بی باک"))
        self.input_name_list.setItemText(36, _translate("Dialog", "رحیم شهریاری"))
        self.input_name_list.setItemText(37, _translate("Dialog", "رستاک حلاج"))
        self.input_name_list.setItemText(38, _translate("Dialog", "رضا شیری"))
        self.input_name_list.setItemText(39, _translate("Dialog", "رضا صادقی"))
        self.input_name_list.setItemText(40, _translate("Dialog", "رضا یزدانی"))
        self.input_name_list.setItemText(41, _translate("Dialog", "روزبه بمانی"))
        self.input_name_list.setItemText(42, _translate("Dialog", "روزبه نعمت الهی"))
        self.input_name_list.setItemText(43, _translate("Dialog", "زانیار خسروی"))
        self.input_name_list.setItemText(44, _translate("Dialog", "سالار عقیلی"))
        self.input_name_list.setItemText(45, _translate("Dialog", "سامان جلیلی"))
        self.input_name_list.setItemText(46, _translate("Dialog", "سهیل رحمانی"))
        self.input_name_list.setItemText(47, _translate("Dialog", "سون بند"))
        self.input_name_list.setItemText(48, _translate("Dialog", "سیامک عباسی"))
        self.input_name_list.setItemText(49, _translate("Dialog", "سیروان خسروی"))
        self.input_name_list.setItemText(50, _translate("Dialog", "سینا پارسیان"))
        self.input_name_list.setItemText(51, _translate("Dialog", "سینا حجازی"))
        self.input_name_list.setItemText(52, _translate("Dialog", "سینا درخشنده"))
        self.input_name_list.setItemText(53, _translate("Dialog", "سینا سرلک"))
        self.input_name_list.setItemText(54, _translate("Dialog", "سینا شعبانخانی"))
        self.input_name_list.setItemText(55, _translate("Dialog", "شهاب رمضان"))
        self.input_name_list.setItemText(56, _translate("Dialog", "شهاب مظفری"))
        self.input_name_list.setItemText(57, _translate("Dialog", "شهرام شکوهی"))
        self.input_name_list.setItemText(58, _translate("Dialog", "شهرام ناظری"))
        self.input_name_list.setItemText(59, _translate("Dialog", "علی ابراهیمی"))
        self.input_name_list.setItemText(60, _translate("Dialog", "علی اصحابی"))
        self.input_name_list.setItemText(61, _translate("Dialog", "علی زند وکیلی"))
        self.input_name_list.setItemText(62, _translate("Dialog", "علی عبدالمالکی"))
        self.input_name_list.setItemText(63, _translate("Dialog", "علی فانی"))
        self.input_name_list.setItemText(64, _translate("Dialog", "علی لهراسبی"))
        self.input_name_list.setItemText(65, _translate("Dialog", "علی یاسینی"))
        self.input_name_list.setItemText(66, _translate("Dialog", "علیرضا افتخاری"))
        self.input_name_list.setItemText(67, _translate("Dialog", "علیرضا روزگار"))
        self.input_name_list.setItemText(68, _translate("Dialog", "علیرضا طلیسچی"))
        self.input_name_list.setItemText(69, _translate("Dialog", "علیرضا عصار"))
        self.input_name_list.setItemText(70, _translate("Dialog", "علیرضا قربانی"))
        self.input_name_list.setItemText(71, _translate("Dialog", "عماد طالب زاده"))
        self.input_name_list.setItemText(72, _translate("Dialog", "فرزاد فرخ"))
        self.input_name_list.setItemText(73, _translate("Dialog", "فرزاد فرزین"))
        self.input_name_list.setItemText(74, _translate("Dialog", "فریدون اسرایی"))
        self.input_name_list.setItemText(75, _translate("Dialog", "گرشا رضایی"))
        self.input_name_list.setItemText(76, _translate("Dialog", "مازیار فلاحی"))
        self.input_name_list.setItemText(77, _translate("Dialog", "ماکان بند"))
        self.input_name_list.setItemText(78, _translate("Dialog", "مجید اخشابی"))
        self.input_name_list.setItemText(79, _translate("Dialog", "مجید خراطها"))
        self.input_name_list.setItemText(80, _translate("Dialog", "محسن ابراهیم زاده"))
        self.input_name_list.setItemText(81, _translate("Dialog", "محسن چاوشی"))
        self.input_name_list.setItemText(82, _translate("Dialog", "محسن لرستانی"))
        self.input_name_list.setItemText(83, _translate("Dialog", "محسن یگانه"))
        self.input_name_list.setItemText(84, _translate("Dialog", "محمد اضفهانی"))
        self.input_name_list.setItemText(85, _translate("Dialog", "محمد علیزاده"))
        self.input_name_list.setItemText(86, _translate("Dialog", "محمد معتمدی"))
        self.input_name_list.setItemText(87, _translate("Dialog", "محمد نوری"))
        self.input_name_list.setItemText(88, _translate("Dialog", "محمد رضا شجریان"))
        self.input_name_list.setItemText(89, _translate("Dialog", "محمدرضا گلزار"))
        self.input_name_list.setItemText(90, _translate("Dialog", "محمدرضا هدایتی"))
        self.input_name_list.setItemText(91, _translate("Dialog", "مرتضی اشرفی"))
        self.input_name_list.setItemText(92, _translate("Dialog", "مرتضی پاشایی"))
        self.input_name_list.setItemText(93, _translate("Dialog", "مسعود سعیدی"))
        self.input_name_list.setItemText(94, _translate("Dialog", "مسعود صابری"))
        self.input_name_list.setItemText(95, _translate("Dialog", "مسعود صادقلو"))
        self.input_name_list.setItemText(96, _translate("Dialog", "مسیح"))
        self.input_name_list.setItemText(97, _translate("Dialog", "مهدی آذر"))
        self.input_name_list.setItemText(98, _translate("Dialog", "مهدی احمدوند"))
        self.input_name_list.setItemText(99, _translate("Dialog", "مهدی جهانی"))
        self.input_name_list.setItemText(100, _translate("Dialog", "مهدی مقدم"))
        self.input_name_list.setItemText(101, _translate("Dialog", "مهدی یراحی"))
        self.input_name_list.setItemText(102, _translate("Dialog", "مهدی یغمایی"))
        self.input_name_list.setItemText(103, _translate("Dialog", "مهران مدیری"))
        self.input_name_list.setItemText(104, _translate("Dialog", "میثم ابراهیمی"))
        self.input_name_list.setItemText(105, _translate("Dialog", "ناصر زینعلی"))
        self.input_name_list.setItemText(106, _translate("Dialog", "همایون شجریان"))
        self.input_name_list.setItemText(107, _translate("Dialog", "هوروش بند"))
        self.input_name_list.setItemText(108, _translate("Dialog", "کاروئل"))
        self.input_name_list.setItemText(109, _translate("Dialog", "یوسف زمانی"))
        self.label_2.setText(_translate("Dialog", "انتخاب به صورت دستی :"))
        self.label_3.setText(_translate("Dialog", "انتخاب از لیست :"))
        self.search.setText(_translate("Dialog", "جستجو"))
        self.num_musics_t.setText(_translate("Dialog", "تعداد موزیک ها :"))
        self.how_meny_t.setText(_translate("Dialog", "چند موزیک را میخواهید دانلود کنید :"))
        self.download.setText(_translate("Dialog", "دانلود"))
        self.setting.setText(_translate("Dialog", "تنظیمات"))
        self.checkBox.setText(_translate("Dialog", "باز شدن پوشه موزیک ها بعد از دانلود به صورت خودکار"))
        with open('m.conf', 'r') as f:
                o = f.read()
                f.close()
        if 'True' in o:
            self.checkBox.setChecked(True)
        else:
            self.checkBox.setChecked(False)

#import ico_rc
#import md_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Breeze')
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
