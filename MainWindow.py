# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(432, 488)
        MainWindow.setMinimumSize(QtCore.QSize(432, 488))
        MainWindow.setMaximumSize(QtCore.QSize(432, 488))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 80, 241, 21))
        self.label.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.kalitesecim = QtWidgets.QComboBox(self.centralwidget)
        self.kalitesecim.setGeometry(QtCore.QRect(10, 120, 271, 22))
        self.kalitesecim.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"")
        self.kalitesecim.setObjectName("kalitesecim")
        self.btn_indir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_indir.setGeometry(QtCore.QRect(290, 110, 111, 41))
        self.btn_indir.setStyleSheet("background-color: rgb(108, 255, 108);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.btn_indir.setObjectName("btn_indir")
        self.link_line = QtWidgets.QLineEdit(self.centralwidget)
        self.link_line.setGeometry(QtCore.QRect(10, 40, 391, 20))
        self.link_line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.link_line.setObjectName("link_line")
        self.video_adi_lbl = QtWidgets.QLabel(self.centralwidget)
        self.video_adi_lbl.setGeometry(QtCore.QRect(10, 170, 391, 21))
        self.video_adi_lbl.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.video_adi_lbl.setText("")
        self.video_adi_lbl.setObjectName("video_adi_lbl")
        self.video_sure_lbl = QtWidgets.QLabel(self.centralwidget)
        self.video_sure_lbl.setGeometry(QtCore.QRect(10, 220, 391, 16))
        self.video_sure_lbl.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.video_sure_lbl.setText("")
        self.video_sure_lbl.setObjectName("video_sure_lbl")
        self.info_lbl = QtWidgets.QLabel(self.centralwidget)
        self.info_lbl.setGeometry(QtCore.QRect(10, 260, 411, 161))
        self.info_lbl.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(218, 218, 218);")
        self.info_lbl.setObjectName("info_lbl")
        self.ara_btn = QtWidgets.QPushButton(self.centralwidget)
        self.ara_btn.setGeometry(QtCore.QRect(290, 70, 111, 31))
        self.ara_btn.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(126, 132, 255);")
        self.ara_btn.setObjectName("ara_btn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 171, 21))
        self.label_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 430, 321, 16))
        self.label_3.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 432, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube Video İndirme Programı"))
        self.label.setText(_translate("MainWindow", "Videoyu indirmek istediğiniz formatı seçin."))
        self.btn_indir.setText(_translate("MainWindow", "İNDİR"))
        self.info_lbl.setText(_translate("MainWindow", " Bilgilendirme:"))
        self.ara_btn.setText(_translate("MainWindow", "ARA"))
        self.label_2.setText(_translate("MainWindow", "Video url adresini girin."))
        self.label_3.setText(_translate("MainWindow", "Youtube Video İndirme Programı | Geliştirici: M.Erkan OYGUN | sürüm: 1.0"))
