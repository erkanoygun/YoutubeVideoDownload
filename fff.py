from MainWindow import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
from pytube import YouTube
import time
from PyQt5.QtWidgets import QMessageBox
from iki_pencere import Window2


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        combo = self.ui.kalitesecim
        combo.addItems(['4K KALİTE','1080px KALİTE','YÜKSEK KALİTE','ORALAMA KALİTE (480px veya 360px)','mp3 FORMATINDA İNDİR'])

        self.ui.btn_indir.clicked.connect(self.videoindir)
        self.ui.dnme_btn.clicked.connect(self.denemee)

        self.iki_pencere = Window2()

        self.i = 0


    def videoindir(self):
        url = self.ui.link_line.text()
        self.yt = YouTube(url)
        print(self.ui.kalitesecim.currentIndex())

        if self.ui.kalitesecim.currentIndex() == 0:
            self.yt.streams.filter(res="1440p").first().download()
            self.yt.streams.filter(only_audio="True").first().download()

        elif self.ui.kalitesecim.currentIndex() == 1:
            self.yt.streams.filter(res="1080").first().download()
            self.yt.streams.filter(only_audio="True").first().download()

        elif self.ui.kalitesecim.currentIndex() == 2:
            self.yt.streams.get_highest_resolution().download()
            print("video iniyor")

        elif self.ui.kalitesecim.currentIndex() == 3:
            self.yt.streams.first().download()

        elif self.ui.kalitesecim.currentIndex() == 4:

            #QMessageBox.about(self, "Video İndirme Başlatıldı", "Lütfen Video İndirildi Bilgisini Alıncaya Kadar Programda Herhangi Bir İşlem Yapmayın")
            self.yt.streams.filter(only_audio="True").first().download()
            #QMessageBox.about(self, "Video İndirildi", "Video İndirildi Hazır")
            self.iki_pencere.close()




    def denemee(self):
        # msgBox = QMessageBox(QMessageBox.Warning, "My title", "My text.", QMessageBox.NoButton)
        # msgBox.show()
        # time.sleep(10)
        # msgBox.close()
        # QMessageBox.about(self, "Video İndirildi", "Video İndirildi Hazır")
        self.iki_pencere.show()
        time.sleep(5)
        self.iki_pencere.close()













def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())


app()