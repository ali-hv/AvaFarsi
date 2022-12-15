#!/usr/bin/python3
# -*- coding: utf-8 -*-

#global libs
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget
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
        # loading the font from local resources
        QtGui.QFontDatabase.addApplicationFont("../resources/ui/fonts/Lalezar-Regular.otf")
        self.Lalezar_font = QtGui.QFont()
        self.Lalezar_font.setFamily("Lalezar") # set the font for whole widgets
        self.plt = platform.system() # detecting the operating system for file directions
        self.current_path = os.getcwd() # get the working directory

        #TODO Responsive window
        #TODO load_ui
        super().__init__()
        self.window_width, self.window_height = 832, 550
        self.setMinimumSize(self.window_width, self.window_height)
        self.setGeometry(QtCore.QRect(200,150,832,550))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet('border-radius: 30px;')

        ## menu page
        self.menu_page = QtWidgets.QWidget(self)
        self.menu_page.setGeometry(QtCore.QRect(0, 0, 832, 530))
        self.menu_page.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.menu_page.setObjectName("menu_page")

        self.inbox = QPushButton(self.menu_page)
        self.inbox.setObjectName("inbox")
        self.inbox.setGeometry(QtCore.QRect(10, 9, 32, 32))
        self.inbox.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        if self.new_message:
            self.inbox.setStyleSheet("border: 0;\n"
                                     "background-image: url(../resources/ui/widgets_img/inbox_unread.png);")
        else:
            self.inbox.setStyleSheet("border: 0;\n"
                                     "background-image: url(../resources/ui/widgets_img/inbox.png);")

        self.inbox_message = QtWidgets.QPlainTextEdit(self)
        self.inbox_message.setObjectName("inbox_message")
        self.inbox_message.setEnabled(False)
        self.inbox_message.setGeometry(QtCore.QRect(7, 42, 221, 261))
        self.inbox_message.setFont(self.Lalezar_font)
        self.Lalezar_font.setPointSize(15)
        self.inbox_message.setFont(self.Lalezar_font)
        self.inbox_message.document().setDefaultTextOption(QtGui.QTextOption(Qt.AlignRight))
        self.inbox_message.setStyleSheet("background-color: rgb(122, 122, 122);\n"
                                         "border-radius: 20px;\n"
                                         "color: white;")
        self.inbox_message.hide()

        self.settings = QPushButton(self.menu_page)
        self.settings.setObjectName("settings")
        self.settings.setGeometry(QtCore.QRect(45, 9, 32, 32))
        self.settings.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.settings.setStyleSheet("border: 0;\n"
                                    "background-image: url(../resources/ui/widgets_img/settings.png);")
        self.settings.hide()

        self.title = QtWidgets.QLabel(self.menu_page)
        self.title.setGeometry(QtCore.QRect(271, 30, 199, 51))
        self.Lalezar_font.setPointSize(28)
        self.title.setFont(self.Lalezar_font)
        self.title.setStyleSheet("color: rgb(255, 255, 255);")
        self.title.setObjectName("title")

        self.title_line = QtWidgets.QFrame(self.menu_page)
        self.title_line.setGeometry(QtCore.QRect(255, 90, 322, 1))
        self.title_line.setStyleSheet("background-color: rgb(90, 90, 90);")
        self.title_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.title_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.title_line.setObjectName("title_line")

        self.dl_singer_name = QtWidgets.QPushButton(self.menu_page)
        self.dl_singer_name.setGeometry(QtCore.QRect(235, 145, 361, 90))
        self.Lalezar_font.setPointSize(16)
        self.dl_singer_name.setFont(self.Lalezar_font)
        self.dl_singer_name.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dl_singer_name.setStyleSheet("QPushButton{\n"
                                          "background-color: rgb(120, 70, 252);\n"
                                          "color: white;\n"
                                          "border-radius: 35px;}\n"
                                          "\n"
                                          "QPushButton:hover{\n"
                                          "background-color: rgb(20, 98, 252);\n"
                                          "color: white;\n"
                                          "border-radius: 35px;}")
        self.dl_singer_name.setObjectName("dl_singer_name")

        self.dl_music_name = QtWidgets.QPushButton(self.menu_page)
        self.dl_music_name.setGeometry(QtCore.QRect(235, 250, 361, 90))
        self.Lalezar_font.setPointSize(16)
        self.dl_music_name.setFont(self.Lalezar_font)
        self.dl_music_name.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dl_music_name.setStyleSheet("QPushButton{\n"
                                         "background-color: rgb(120, 70, 252);\n"
                                         "color: white;\n"
                                         "border-radius: 35px;}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "background-color: rgb(20, 98, 252);\n"
                                         "color: white;\n"
                                         "border-radius: 35px;}")
        self.dl_music_name.setObjectName("dl_music_name")

        self.dl_part_music = QtWidgets.QPushButton(self.menu_page)
        self.dl_part_music.setGeometry(QtCore.QRect(235, 355, 361, 90))
        self.Lalezar_font.setPointSize(16)
        self.dl_part_music.setFont(self.Lalezar_font)
        self.dl_part_music.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dl_part_music.setStyleSheet("QPushButton{\n"
                                         "background-color: rgb(120, 70, 252);\n"
                                         "color: white;\n"
                                         "border-radius: 35px;}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "background-color: rgb(20, 98, 252);\n"
                                         "color: white;\n"
                                         "border-radius: 35px;}")
        self.dl_part_music.setObjectName("dl_part_music")

        ## Search with singer name page
        self.search_singer_name = QtWidgets.QWidget(self)
        self.search_singer_name.setGeometry(QtCore.QRect(0, 0, 832, 530))
        self.search_singer_name.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.search_singer_name.setObjectName("search_singer_name_page")
        self.search_singer_name.hide()

        self.search_singer_name_btn = QtWidgets.QPushButton(self.search_singer_name)
        self.search_singer_name_btn.setGeometry(QtCore.QRect(262, 290, 310, 71))
        self.Lalezar_font.setPointSize(16)
        self.search_singer_name_btn.setFont(self.Lalezar_font)
        self.search_singer_name_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_singer_name_btn.setStyleSheet("QPushButton{\n"
                                              "background-color: rgb(120, 70, 252);\n"
                                              "color: white;\n"
                                              "border-radius: 30px;}\n"
                                              "\n"
                                              "QPushButton:hover{\n"
                                              "background-color: rgb(20, 98, 252);\n"
                                              "color: white;\n"
                                              "border-radius: 30px;}")
        self.search_singer_name_btn.setObjectName("search_singer_name_btn")

        self.get_singer_name = QtWidgets.QLineEdit(self.search_singer_name)
        self.get_singer_name.setGeometry(QtCore.QRect(262, 230, 310, 50))
        self.Lalezar_font.setPointSize(16)
        self.get_singer_name.setFont(self.Lalezar_font)
        self.get_singer_name.setStyleSheet("color: white;\n"
                                       "border-radius: 20px;\n"
                                       "border: 2px solid rgb(130, 130, 130)\n")
        self.get_singer_name.setPlaceholderText("   نام خواننده را اینجا بنویسید")
        self.get_singer_name.returnPressed.connect(self.search_singer_name_btn.click)

        self.live_face = QtWidgets.QPushButton(self.search_singer_name)
        self.live_face.setObjectName("live_face")
        self.live_face.setGeometry(QtCore.QRect(580, 229, 50, 50))
        self.live_face.setStyleSheet("background-image: url(../resources/ui/widgets_img/unknown_face.png);\n"
                                     "border-radius: 15px;")

        self.notice_0 = QtWidgets.QLabel(self.search_singer_name)
        self.notice_0.setGeometry(QtCore.QRect(262, 190, 310, 30))
        self.Lalezar_font.setPointSize(14)
        self.notice_0.setFont(self.Lalezar_font)
        self.notice_0.setStyleSheet("color: rgb(255, 37, 21);")
        self.notice_0.setAlignment(QtCore.Qt.AlignHCenter)
        
        self.first_site = QtWidgets.QRadioButton(self.search_singer_name)
        self.first_site.setObjectName("first_site")
        self.first_site.setGeometry(QtCore.QRect(110, 188, 131, 41))
        self.Lalezar_font.setPointSize(15)
        self.first_site.setFont(self.Lalezar_font)
        self.first_site.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.first_site.setStyleSheet("QRadioButton {\n"
                                      "color :rgb(165, 165, 165);\n"
                                      "}\n"
                                      "QRadioButton::indicator {\n"
                                      "width: 25px;\n"
                                      "height: 25px;\n"
                                      "}")
        self.first_site.setChecked(True)

        self.second_site = QtWidgets.QRadioButton(self.search_singer_name)
        self.second_site.setObjectName("first_site")
        self.second_site.setGeometry(QtCore.QRect(110, 222, 131, 41))
        self.Lalezar_font.setPointSize(15)
        self.second_site.setFont(self.Lalezar_font)
        self.second_site.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.second_site.setStyleSheet("QRadioButton {\n"
                                      "color :rgb(165, 165, 165);\n"
                                      "}\n"
                                      "QRadioButton::indicator {\n"
                                      "width: 25px;\n"
                                      "height: 25px;\n"
                                      "}")

        self.third_site = QtWidgets.QRadioButton(self.search_singer_name)
        self.third_site.setObjectName("second_site")
        self.third_site.setGeometry(QtCore.QRect(110, 255, 141, 31))
        self.third_site.setFont(self.Lalezar_font)
        self.third_site.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.third_site.setStyleSheet("QRadioButton {\n"
                                       "color:  rgb(165, 165, 165);\n"
                                       "}\n"
                                       "QRadioButton::indicator {\n"
                                       "width: 25px;\n"
                                       "height: 25px;\n"
                                       "}")

        ## Download with singer name
        self.page_1 = QtWidgets.QWidget(self)
        self.page_1.setGeometry(QtCore.QRect(0, 0, 832, 530))
        self.page_1.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.page_1.setObjectName("dl_singer_name_page")
        self.page_1.hide()

        self.select_music_name = QtWidgets.QComboBox(self.page_1)
        self.select_music_name.setGeometry(QtCore.QRect(70, 100, 321, 50))
        self.Lalezar_font.setPointSize(14)
        self.select_music_name.setFont(self.Lalezar_font)
        self.select_music_name.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.select_music_name.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.select_music_name.setStyleSheet("QComboBox{\n"
                                           "border: 2px solid gray;\n"
                                           "color: white;\n"
                                           "border-radius: 20px;\n"
                                           "background-color: rgb(85, 85, 85);}\n"
                                           "QComboBox::drop-down {\n"
                                           "border-width: 0px;\n"
                                           "}")
        self.select_music_name.setObjectName("select_music_p1")

        self.singer_img = QtWidgets.QPushButton(self.page_1)
        self.singer_img.setGeometry(QtCore.QRect(470, 55, 340, 340))
        self.singer_img.setObjectName("singer_img")
       
        self.singer_info = QtWidgets.QWidget(self.page_1)
        self.singer_info.setGeometry(QtCore.QRect(470, 420, 340, 71))
        self.singer_info.setStyleSheet("background-color: rgb(113, 113, 113);\n"
                                       "border-radius: 30px;")
        self.singer_info.setObjectName("singer_info")

        self.singer_name = QtWidgets.QLabel(self.singer_info)
        self.singer_name.setGeometry(QtCore.QRect(10, 7, 321, 41))
        self.Lalezar_font.setPointSize(22)
        self.singer_name.setFont(self.Lalezar_font)
        self.singer_name.setStyleSheet("color: white;")
        self.singer_name.setAlignment(QtCore.Qt.AlignCenter)
        self.singer_name.setObjectName("singer_name")

        self.number_of_musics = QtWidgets.QLabel(self.singer_info)
        self.number_of_musics.setGeometry(QtCore.QRect(20, 41, 301, 21))
        self.Lalezar_font.setPointSize(14)
        self.number_of_musics.setFont(self.Lalezar_font)
        self.number_of_musics.setStyleSheet("color: white;")
        self.number_of_musics.setAlignment(QtCore.Qt.AlignCenter)
        self.number_of_musics.setObjectName("number_of_musics_p1")

        self.dl_all_musics = QtWidgets.QPushButton(self.page_1)
        self.dl_all_musics.setGeometry(QtCore.QRect(70, 420, 321, 71))
        self.Lalezar_font.setPointSize(15)
        self.dl_all_musics.setFont(self.Lalezar_font)
        self.dl_all_musics.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dl_all_musics.setStyleSheet("QPushButton{\n"
                                            "border-radius: 30px;\n"
                                            "background-color: rgb(120, 70, 252);\n"
                                            "color: white;}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "border-radius: 30px;\n"
                                            "background-color: rgb(20, 98, 252);\n"
                                            "color: white;}")
        self.dl_all_musics.setObjectName("dl_all_musics_p1")

        self.single_dl_label = QtWidgets.QLabel(self.page_1)
        self.single_dl_label.setGeometry(QtCore.QRect(70, 45, 321, 51))
        self.Lalezar_font.setPointSize(20)
        self.single_dl_label.setFont(self.Lalezar_font)
        self.single_dl_label.setStyleSheet("color: white;")
        self.single_dl_label.setAlignment(QtCore.Qt.AlignCenter)
        self.single_dl_label.setObjectName("single_dl_label_p1")

        self.single_dl_btn = QtWidgets.QPushButton(self.page_1)
        self.single_dl_btn.setGeometry(QtCore.QRect(70, 160, 321, 60))
        self.Lalezar_font.setPointSize(30)
        self.single_dl_btn.setFont(self.Lalezar_font)
        self.single_dl_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.single_dl_btn.setStyleSheet("QPushButton{\n"
                                            "border-radius: 25px;\n"
                                            "background-color: rgb(120, 70, 252);\n"
                                            "color: white;}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "border-radius: 25px;\n"
                                            "background-color: rgb(20, 98, 252);\n"
                                            "color: white;}")
        self.single_dl_btn.setObjectName("single_dl_btn_p1")

        self.multiple_dl_btn = QtWidgets.QPushButton(self.page_1)
        self.multiple_dl_btn.setGeometry(QtCore.QRect(70, 335, 321, 60))
        self.Lalezar_font.setPointSize(30)
        self.multiple_dl_btn.setFont(self.Lalezar_font)
        self.multiple_dl_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.multiple_dl_btn.setStyleSheet("QPushButton{\n"
                                              "border-radius: 25px;\n"
                                              "background-color: rgb(120, 70, 252);\n"
                                              "color: white;}\n"
                                              "\n"
                                              "QPushButton:hover{\n"
                                              "border-radius: 25px;\n"
                                              "background-color: rgb(20, 98, 252);\n"
                                              "color: white;}")
        self.multiple_dl_btn.setObjectName("multiple_dl_btn_p1")

        self.multiple_dl_input = QtWidgets.QLineEdit(self.page_1)
        self.multiple_dl_input.setGeometry(QtCore.QRect(70, 275, 321, 50))
        self.Lalezar_font.setPointSize(14)
        self.multiple_dl_input.setFont(self.Lalezar_font)
        self.multiple_dl_input.setStyleSheet("color: white;\n"
                                                "border-radius: 20px;\n"
                                                "border: 2px solid rgb(130, 130, 130)")
        self.multiple_dl_input.setObjectName("multiple_dl_input_p1")
        self.multiple_dl_input.setPlaceholderText("   تعداد موزیک هایی که میخواهید دانلود شود")
        self.multiple_dl_input.returnPressed.connect(self.multiple_dl_btn.click)
        
        self.multiple_dl_label = QtWidgets.QLabel(self.page_1)
        self.multiple_dl_label.setGeometry(QtCore.QRect(70, 224, 321, 51))
        self.Lalezar_font.setPointSize(18)
        self.multiple_dl_label.setFont(self.Lalezar_font)
        self.multiple_dl_label.setStyleSheet("color: white;")
        self.multiple_dl_label.setAlignment(QtCore.Qt.AlignCenter)
        self.multiple_dl_label.setObjectName("multiple_dl_label_p1")

        self.notice_1 = QtWidgets.QLabel(self.page_1)
        self.notice_1.setGeometry(QtCore.QRect(130, 0, 571, 51))
        self.Lalezar_font.setPointSize(20)
        self.notice_1.setFont(self.Lalezar_font)
        self.notice_1.setStyleSheet("color: rgb(255, 37, 21);")
        self.notice_1.setAlignment(QtCore.Qt.AlignCenter)
        self.notice_1.setObjectName("notice")

        self.downloadBar_1 = QtWidgets.QProgressBar(self.page_1)
        self.downloadBar_1.setObjectName("downloadBar_p1")
        self.downloadBar_1.setGeometry(QtCore.QRect(70, 335, 321, 61))
        self.downloadBar_1.setStyleSheet("QProgressBar {\n"
                                          "text-align: center;\n"
                                          "border-radius: 20px;\n"
                                          "}\n"
                                          "QProgressBar::chunk {\n"
                                          "border-top-left-radius: 20px;\n"
                                          "border-bottom-left-radius: 20px;\n"
                                          "background-color:  rgb(120, 70, 252);}")
        self.downloadBar_1.setValue(0)
        self.downloadBar_1.hide()

        self.stop_1 = QtWidgets.QPushButton(self.page_1)
        self.stop_1.setObjectName("stop_p1")
        self.stop_1.setGeometry(QtCore.QRect(400, 335, 60, 60))
        self.stop_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Lalezar_font.setPointSize(20)
        self.stop_1.setFont(self.Lalezar_font)
        self.stop_1.setStyleSheet("QPushButton{\n"
                                   "border-radius: 30px;\n"
                                   "background-color: rgb(255, 24, 28);\n"
                                   "color: white;}\n"
                                   "QPushButton:hover{\n"
                                   "border-radius: 30px;\n"
                                   "background-color: rgb(20, 98, 252);\n"
                                   "color: white;\n"
                                   "}")
        self.stop_1.hide()

        #search by muisc name
        self.search_music_name = QtWidgets.QWidget(self)
        self.search_music_name.setGeometry(QtCore.QRect(0, 0, 832, 530))
        self.search_music_name.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.search_music_name.setObjectName("search_music_name_p2")
        self.search_music_name.hide()

        self.search_music_name_btn = QtWidgets.QPushButton(self.search_music_name)
        self.search_music_name_btn.setGeometry(QtCore.QRect(262, 290, 310, 71))
        self.Lalezar_font.setPointSize(16)
        self.search_music_name_btn.setFont(self.Lalezar_font)
        self.search_music_name_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_music_name_btn.setStyleSheet("QPushButton{\n"
                                              "background-color: rgb(120, 70, 252);\n"
                                              "color: white;\n"
                                              "border-radius: 30px;}\n"
                                              "\n"
                                              "QPushButton:hover{\n"
                                              "background-color: rgb(20, 98, 252);\n"
                                              "color: white;\n"
                                              "border-radius: 30px;}")
        self.search_music_name_btn.setObjectName("search_music_name_btn")

        self.music_name = QtWidgets.QLineEdit(self.search_music_name)
        self.music_name.setGeometry(QtCore.QRect(262, 230, 310, 50))
        self.Lalezar_font.setPointSize(16)
        self.music_name.setFont(self.Lalezar_font)
        self.music_name.setStyleSheet("color: white;\n"
                                       "border-radius: 20px;\n"
                                       "border: 2px solid rgb(130, 130, 130)\n")
        self.music_name.setPlaceholderText("   نام موزیک را اینجا بنویسید")
        self.music_name.returnPressed.connect(self.search_music_name_btn.click)

        self.dl_music_name_btn = QtWidgets.QPushButton(self.search_music_name)
        self.dl_music_name_btn.setGeometry(QtCore.QRect(262, 290, 310, 71))
        self.Lalezar_font.setPointSize(18)
        self.dl_music_name_btn.setFont(self.Lalezar_font)
        self.dl_music_name_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dl_music_name_btn.setStyleSheet("QPushButton{\n"
                                              "background-color: rgb(120, 70, 252);\n"
                                              "color: white;\n"
                                              "border-radius: 30px;}\n"
                                              "\n"
                                              "QPushButton:hover{\n"
                                              "background-color: rgb(20, 98, 252);\n"
                                              "color: white;\n"
                                              "border-radius: 30px;}")
        self.dl_music_name_btn.setObjectName("dl_music_name_btn")
        self.dl_music_name_btn.hide()

        self.select_music = QtWidgets.QComboBox(self.search_music_name)
        self.select_music.setGeometry(QtCore.QRect(262, 230, 310, 50))
        self.Lalezar_font.setPointSize(14)
        self.select_music.setFont(self.Lalezar_font)
        self.select_music.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.select_music.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.select_music.setStyleSheet("QComboBox{\n"
                                           "border: 2px solid gray;\n"
                                           "color: white;\n"
                                           "border-radius: 20px;\n"
                                           "background-color: rgb(85, 85, 85);}\n"
                                           "QComboBox::drop-down {\n"
                                           "border-width: 0px;\n"
                                           "}")
        self.select_music.setObjectName("select_music_p2")
        self.select_music.hide()

        self.notice_2 = QtWidgets.QLabel(self.search_music_name)
        self.notice_2.setGeometry(QtCore.QRect(262, 190, 310, 30))
        self.Lalezar_font.setPointSize(14)
        self.notice_2.setFont(self.Lalezar_font)
        self.notice_2.setStyleSheet("color: rgb(255, 37, 21);")
        self.notice_2.setAlignment(QtCore.Qt.AlignHCenter)

        
        self.downloadBar_2 = QtWidgets.QProgressBar(self.search_music_name)
        self.downloadBar_2.setObjectName("downloadBar_p2")
        self.downloadBar_2.setGeometry(QtCore.QRect(262, 290, 310, 71))
        self.downloadBar_2.setStyleSheet("QProgressBar {\n"
                                          "text-align: center;\n"
                                          "border-radius: 20px;\n"
                                          "}\n"
                                          "QProgressBar::chunk {\n"
                                          "border-top-left-radius: 20px;\n"
                                          "border-bottom-left-radius: 20px;\n"
                                          "background-color:  rgb(120, 70, 252);}")
        self.downloadBar_2.setValue(0)
        self.downloadBar_2.hide()

        self.stop_2 = QtWidgets.QPushButton(self.search_music_name)
        self.stop_2.setObjectName("stop_p2")
        self.stop_2.setGeometry(QtCore.QRect(576, 293, 60, 60))
        self.stop_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Lalezar_font.setPointSize(20)
        self.stop_2.setFont(self.Lalezar_font)
        self.stop_2.setStyleSheet("QPushButton{\n"
                                   "border-radius: 30px;\n"
                                   "background-color: rgb(255, 24, 28);\n"
                                   "color: white;}\n"
                                   "QPushButton:hover{\n"
                                   "border-radius: 30px;\n"
                                   "background-color: rgb(20, 98, 252);\n"
                                   "color: white;\n"
                                   "}")
        self.stop_2.hide()


        self.back = QtWidgets.QPushButton(self)
        self.back.setGeometry(QtCore.QRect(10, 10, 101, 33))
        self.Lalezar_font.setPointSize(15)
        self.back.setFont(self.Lalezar_font)
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back.setStyleSheet("QPushButton{\n"
                                   "border-radius: 10px;\n"
                                   "background-color: rgb(20, 98, 252);\n"
                                   "color: white;\n"
                                   "background-image: url(../resources/ui/widgets_img/purple_back.PNG);}\n"
                                   "\n"
                                   "QPushButton:hover{\n"
                                   "border-radius: 30px;\n"
                                   "background-color: rgb(20, 98, 252);\n"
                                   "color: white;\n"
                                   "background-image: url(../resources/ui/widgets_img/blue_back.PNG);}")
        self.back.setObjectName("back")
        self.back.hide()

        self.close = QtWidgets.QPushButton(self)
        self.close.setGeometry(QtCore.QRect(805, 13, 16, 16))
        self.close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close.setStyleSheet("QPushButton{\n"
                                 "background-color: rgb(255, 0, 0);\n"
                                 "color: white;\n"
                                 "border-radius: 8px;}\n"
                                 "\n"
                                 "QPushButton:hover{\n"
                                 "background-color: rgb(200, 0, 0);\n"
                                 "color: white;\n"
                                 "border-radius: 8px;}")
        self.close.setObjectName("close")

        self.minimize = QtWidgets.QPushButton(self)
        self.minimize.setGeometry(QtCore.QRect(785, 13, 16, 16))
        self.minimize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minimize.setStyleSheet("QPushButton{\n"
                                    "background-color: rgb(255, 255, 0);\n"
                                    "color: white;\n"
                                    "border-radius: 8px;}\n"
                                    "\n"
                                    "QPushButton:hover{\n"
                                    "background-color: rgb(200, 200, 0);\n"
                                    "color: white;\n"
                                    "border-radius: 8px;}")
        self.minimize.setObjectName("minimize")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        #signals
        self.close.clicked.connect(sys.exit)
        self.minimize.clicked.connect(self.showMinimized)
        self.inbox.clicked.connect(self.show_inbox)
        self.back.clicked.connect(self.back_home)
        self.dl_singer_name.clicked.connect(self.menu_page.hide)
        self.dl_singer_name.clicked.connect(self.back.show)
        self.dl_singer_name.clicked.connect(self.get_singer_name.setFocus)
        self.dl_singer_name.clicked.connect(self.search_singer_name.show)
        self.get_singer_name.textChanged.connect(self.live_singer_face)
        self.search_singer_name_btn.clicked.connect(self.search_singer_name_func)
        self.search_singer_name_btn.clicked.connect(self.get_singer_name.setFocus)
        self.single_dl_btn.clicked.connect(self.single_dl_p1_func)
        self.multiple_dl_btn.clicked.connect(self.multiple_dl_p1_func)
        self.dl_all_musics.clicked.connect(self.download_all_func)
        self.dl_music_name.clicked.connect(self.back.show)
        self.dl_music_name.clicked.connect(self.search_music_name.show)
        self.dl_music_name.clicked.connect(self.music_name.setFocus)
        self.dl_music_name.clicked.connect(self.music_name_clicked_signal)
        self.search_music_name_btn.clicked.connect(self.search_music_name_func)
        self.search_music_name_btn.clicked.connect(self.music_name.setFocus)
        self.dl_music_name_btn.clicked.connect(self.dl_music_name_func)
        self.dl_part_music.clicked.connect(self.back.show)
        self.dl_part_music.clicked.connect(self.search_music_name.show)
        self.dl_part_music.clicked.connect(self.music_name.setFocus)
        self.dl_part_music.clicked.connect(self.part_music_clicked_signal)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "آوا فارسی"))
        self.title.setText(_translate("self", "آوا فارسی"))
        if internet_check.check(self): self.inbox_message.setPlainText(str(self.announ_content))
        else: self.inbox_message.setPlainText('!اطلاعیه ای وجود ندارد')
        # self.music_player.setText(_translate("self", "موزیک پلیر"))
        self.dl_singer_name.setText(_translate("self", "دانلود موزیک با نام خواننده"))
        self.dl_music_name.setText(_translate("self", "دانلود موزیک با نام موزیک"))
        self.dl_part_music.setText(_translate("self", "دانلود موزیک با متن بخشی از موزیک"))
        self.search_singer_name_btn.setText(_translate("self", "جستجو"))
        self.search_music_name_btn.setText(_translate("self", "جستجو"))
        self.multiple_dl_btn.setText(_translate("self", "دانلود"))
        self.dl_all_musics.setText(_translate("Dialog", "دانلود تمام موزیک ها به صورت یکجا"))
        self.single_dl_label.setText(_translate("Dialog", "دانلود به صورت تکی"))
        self.single_dl_btn.setText(_translate("Dialog", "دانلود"))
        self.multiple_dl_btn.setText(_translate("Dialog", "دانلود"))
        self.multiple_dl_label.setText(_translate("Dialog", "دانلود چندتایی"))
        self.stop_1.setText(_translate("Dialog", "توقف"))
        self.stop_2.setText(_translate("Dialog", "توقف"))
        self.first_site.setText(_translate("Dialog", "MrTehran"))
        self.second_site.setText(_translate("Dialog", "music-fa"))
        self.third_site.setText(_translate("Dialog", "upmusics"))
        self.dl_music_name_btn.setText(_translate("Dialog", "دانلود"))


    def show_inbox(self):
        self.inbox.setStyleSheet("border: 0;\n"
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
        self.second_site.setChecked(1)

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
            self.stop_1.setGeometry(QtCore.QRect(400, 335, 60, 60))
            # self.stop_p1.show()

            download.singer_name(self, app, int(self.multiple_dl_input.text()))

    def download_all_func(self):
        self.downloadBar_1.setGeometry(QtCore.QRect(70, 420, 321, 71))
        self.stop_1.setGeometry(QtCore.QRect(400, 422, 60, 60))

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
    app.setStyle('fusion')
    app.setWindowIcon(QtGui.QIcon("../resources/ui/widgets_img/app_icon.ico"))
    myApp = Ui_MainWindow()
    myApp.show()
    sys.exit(app.exec_())
