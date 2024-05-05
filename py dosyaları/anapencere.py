from  PyQt5.QtWidgets import *
from anapencere_python import Ui_MainWindow
from bilet_satin_al import Bilet_satin_al_Sayfa
from etkinlik_duzenle import EtkinlikSayfa
from satilan_biletler import BiletGosterSayfa
from veritabani import veritabani

class AnapencereSayfa(QMainWindow):
    def __init__(self):
        super().__init__()
        self.anapencereform = Ui_MainWindow()
        self.anapencereform.setupUi(self)
        self.satinAl = Bilet_satin_al_Sayfa()
        self.etkinlik = EtkinlikSayfa()
        self.biletGoster = BiletGosterSayfa()
        self.averitabani = veritabani()


        self.anapencereform.bilet_satin_al_sayfa.triggered.connect(self.satinAlGoster)
        self.anapencereform.etkinlik_duzenle_sayfa.triggered.connect(self.etkinlikGoster)
        self.anapencereform.satilan_biletler_sayfa.triggered.connect(self.biletgosterSayfa)

        self.kayitGoster()

        self.anapencereform.arama_yap_line_edit.textChanged[str].connect(self.EtkinlikAra)


    
    def kayitGoster(self):
     kolonlar = ["ID", "ETKİNLİK ADI", "MEKAN", "BİLET SAYISI", "BİLET FİYATI","TARİH"]
     self.anapencereform.bilgi_tableWidget.setColumnCount(len(kolonlar))  # Sütun sayısını ayarla
     self.anapencereform.bilgi_tableWidget.setHorizontalHeaderLabels(kolonlar)  # Kolon başlıklarını ayarla

     veriler = self.averitabani.kayitGoster()
     if veriler:
        self.anapencereform.bilgi_tableWidget.setRowCount(len(veriler))  # Satır sayısını ayarla
        for satir, veri in enumerate(veriler):
            self.anapencereform.bilgi_tableWidget.setItem(satir, 0, QTableWidgetItem(str(veri[0])))  # ID değerini ekleyin
            for sutun, deger in enumerate(veri[1:], 1):  # 1'den başlayarak diğer sütunları ekleyin
                self.anapencereform.bilgi_tableWidget.setItem(satir, sutun, QTableWidgetItem(str(deger)))

     # Tablonun genişliğini sığabilecek şekilde ayarlayın
     self.anapencereform.bilgi_tableWidget.horizontalHeader().setStretchLastSection(True)


    def EtkinlikAra(self):
     kolonlar = ["ID", "KİTAP ADI", "YAZAR ADI", "SAYFA SAYISI", "KATEGORİ","EKLENDİĞİ TARİH"]
     self.anapencereform.bilgi_tableWidget.setColumnCount(len(kolonlar))  # Sütun sayısını ayarla
     self.anapencereform.bilgi_tableWidget.setHorizontalHeaderLabels(kolonlar)  # Kolon başlıklarını ayarla
     etkinlik_Adi = self.anapencereform.arama_yap_line_edit.text()

     veriler = self.averitabani.ara(etkinlik_Adi)
     if veriler:
        self.anapencereform.bilgi_tableWidget.setRowCount(len(veriler))  # Satır sayısını ayarla
        for satir, veri in enumerate(veriler):
            self.anapencereform.bilgi_tableWidget.setItem(satir, 0, QTableWidgetItem(str(veri[0])))  # ID değerini ekleyin
            for sutun, deger in enumerate(veri[1:], 1):  # 1'den başlayarak diğer sütunları ekleyin
                self.anapencereform.bilgi_tableWidget.setItem(satir, sutun, QTableWidgetItem(str(deger)))

    # Tablonun genişliğini sığabilecek şekilde ayarlayın
     self.anapencereform.bilgi_tableWidget.horizontalHeader().setStretchLastSection(True)
















    def satinAlGoster(self):
        self.satinAl.show()


    def etkinlikGoster(self):
        self.etkinlik.show()
    
    def biletgosterSayfa(self):
        self.biletGoster.show()

















app = QApplication([])
pencere = AnapencereSayfa()
pencere.show()
app.exec_()