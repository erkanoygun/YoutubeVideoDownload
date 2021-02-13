from MainWindow import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
from pytube import YouTube
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
import os

class CloneThread(QThread):
    finished = pyqtSignal()
    hata = pyqtSignal()

    def __init__(self):
        QThread.__init__(self)
        self.url = ""
        self.secim = 0
        self.d_ses = ''
        self.d_video = ''

    def run(self):
        # self.finished.emit(tmpdir)



        try:
            self.yt = YouTube(self.url)
            if self.secim == 0:
                self.yt.streams.filter(res="2160p").first().download(self.d_video)
                self.yt.streams.filter(only_audio="True").first().download(self.d_ses)
                self.finished.emit()

            elif self.secim == 1:
                self.yt.streams.filter(res="1080p").first().download(self.d_video)
                self.yt.streams.filter(only_audio="True").first().download(self.d_ses)
                self.finished.emit()

            elif self.secim == 2:
                self.yt.streams.get_highest_resolution().download(self.d_video)
                self.finished.emit()

            elif self.secim == 3:
                self.yt.streams.first().download(self.d_video)
                self.finished.emit()

            elif self.secim == 4:
                self.yt.streams.filter(only_audio="True").first().download(self.d_ses)
                self.finished.emit()
        except:
            self.hata.emit()








class Window(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.sayac = 0


        combo = self.ui.kalitesecim
        combo.addItems(['4K Kalite','1080px Kalite','Yüksek Kalite','Ortalama Kalite (480px veya 360px)','Sadece Mp3 İndir'])

        self.ui.btn_indir.clicked.connect(self.videoindir)
        self.ui.ara_btn.clicked.connect(self.videoara)




        self.thread = CloneThread()
        self.thread.finished.connect(self.finished)
        self.thread.hata.connect(self.hata)

    def videoindir(self):
        dosya_kontrol = os.path.exists(os.getcwd()+"\\YdVideo")
        dosya_kontrol2 = os.path.exists(os.getcwd()+"\\YdSes")
        if dosya_kontrol == False:
            os.mkdir(os.getcwd() + "\\YdVideo")
        if dosya_kontrol2 == False:
            os.mkdir(os.getcwd() + "\\YdSes")

        self.thread.secim = self.ui.kalitesecim.currentIndex()
        self.thread.url = self.ui.link_line.text()
        self.thread.d_ses = os.getcwd()+"\\YdSes"
        self.thread.d_video = os.getcwd()+"\\YdVideo"
        if self.thread.url == "":
            self.sayac += 1
            if self.sayac != 3:
                self.ui.info_lbl.setText(" Bilgilendirme: Lütfen Video URL Adresini Girin! ")
            else:
                QMessageBox.about(self, "Dostum Kendindemisin Sen?",
                                  "Bir video indirmek istiyorsan ona ait bir url adresi girmelisinnn ")
        else:
            try:
                self.ui.btn_indir.setEnabled(False)
                self.ui.ara_btn.setEnabled(False)
                self.ui.info_lbl.setText("\n Bilgilendirme: İçerik İNDİRİLİYOR... Lütfen İçerik İndirildi Bilgisini- "
                                         + "\n alıncaya kadar bekleyin programı kapatmayın!"
                                         + "\n indirme süresi internet bağlantınıza indirdiğiniz içeriğin uzunluğuna "
                                         + "\n ve seçtiğiniz indirme kalitesine göre değişebilir... ")
                self.thread.start()
            except:
                self.ui.btn_indir.setEnabled(True)
                self.ui.ara_btn.setEnabled(True)


    def videoara(self):
        self.thread.url = self.ui.link_line.text()
        if self.thread.url == "erkanoygun":
            QMessageBox.about(self, "M.Erkan OYGUN",
                              "Merhaba dostum benim hakkımda aramak istediklerini bana twitterdan dm atarak\nbizzat sorabilirsin, twitter kullanıcı adım: '@erkanoygun'  ")
        elif self.thread.url == "":
            self.sayac += 1
            if self.sayac != 3:
                self.ui.info_lbl.setText(" Bilgilendirme: Lütfen Video URL Adresini Girin! ")
            else:
                QMessageBox.about(self, "Dostum Kendindemisin Sen?","Bir video aramak istiyorsan ona ait bir url adresi girmelisinnn ")
        else:
            try:
                self.ui.ara_btn.setEnabled(False)
                self.ui.info_lbl.setText("Bilgilendirme: İçerik ARANIYOR!")
                self.yt = YouTube(self.thread.url)
                self.ui.video_adi_lbl.setText("Video Adı: " + self.yt.title)
                self.ui.video_sure_lbl.setText("Video Süresi: " + str(round(self.yt.length/60,2)) + " dakika")
                self.ui.info_lbl.setText("Bilgilendirme: İçerik BULUNDU!")
                self.ui.ara_btn.setEnabled(True)
            except:
                self.ui.info_lbl.setText(" Bilgilendirme: Hata Meydana Geldi! ")
                QMessageBox.about(self, "Ops Bir Sorun Oluştu Dostum",
                                  "Aradığın videoya ait url adresini doğru girdiğinden emin olup yeniden dene bakalım...")

                self.ui.ara_btn.setEnabled(True)

    def finished(self):
        #print(result)
        self.ui.btn_indir.setEnabled(True)
        self.ui.ara_btn.setEnabled(True)
        self.ui.info_lbl.setText("\n Bilgilendirme: İçerik İNDİRİLDİ!"
                                 + "\n İçerikler programı çalıştırdığınız dizinde oluşturulan 'YdVideo' ve "
                                 + "\n 'YdSes' adlı klasörlere indirilecektir!"
                                 + "\n İçeriğinizi '4K Kalite' veya '1080px Kalite' formatında indirdiyseniz "
                                 + "\n İçeriğin video dosyası 'YdVideo' adlı klasöre ses dosyası ise 'YdSes' "
                                 + "\n adlı klasöre indirilmiştir!"
                                 + "\n 'Mp3' formatında indirdiğiniz mp3 dosyası 'YdSes' klasörüne indi- "
                                 + "\n rilecektir.")
        QMessageBox.about(self, "İçerik İndirildi", "İçerik İndirildi Hazır")

    def hata(self):
        self.ui.btn_indir.setEnabled(True)
        self.ui.ara_btn.setEnabled(True)
        self.ui.info_lbl.setText("\n Bilgilendirme: İçerik indirilirken bir hata meydana geldi bu hatanın "
                                 + "\n sebepleri şunlar olabilir (Hatalı link, İçerik indirilirken yaşanan "
                                 + "\n bağlantı sorunu, youtube tarafından indirilmesi engellenen içerik, "
                                 + "\n vb diğer sebepler.) Lütfen video url adresini doğru kopyaladığınızdan "
                                 + "\n ve internet bağlantınızın olduğundan emin olun. Ve ayrıca indirmeye "
                                 + "\n çalıştığın video istediğiniz formatı desteklemiyor olabilir örneğin "
                                 + "\n '4K Kalite' formatında indirmeye çalıştıysanız ve hata aldıysanız bir de "
                                 + "\n 'Yüksek Kalite' formatında indirmeyi dene...\n ")
        QMessageBox.about(self, "Ops Bir Sorun Oluştu Dostum",
                          "Sorunun Kaynağını Anlamak İçin Bilgilendirme Metnine Bak... ")






def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    app()