from  PyQt5.QtWidgets import *
from satilan_biletler_python_2 import Ui_Form
from veritabani import veritabani


class BiletGosterSayfa(QWidget):
    def __init__(self):
        super().__init__()
        
        self.biletbilgisayfa = Ui_Form()
        self.biletbilgisayfa.setupUi(self)  

        self.gveritabani = veritabani()

        self.biletKayitGoster()

        self.biletbilgisayfa.arama_yap_line_edit.textChanged[str].connect(self.BiletAra)



    def biletKayitGoster(self):
     kolonlar = ["ID", "ETKİNLİK ADI", "İSİM", "BİLET SAYISI", "BİLET FİYATI"]
     self.biletbilgisayfa.bilgi_tableWidget.setColumnCount(len(kolonlar))  # Sütun sayısını ayarla
     self.biletbilgisayfa.bilgi_tableWidget.setHorizontalHeaderLabels(kolonlar)  # Kolon başlıklarını ayarla

     veriler = self.gveritabani.biletKayitGoster()
     if veriler:
        self.biletbilgisayfa.bilgi_tableWidget.setRowCount(len(veriler))  # Satır sayısını ayarla
        for satir, veri in enumerate(veriler):
            self.biletbilgisayfa.bilgi_tableWidget.setItem(satir, 0, QTableWidgetItem(str(veri[0])))  # ID değerini ekleyin
            for sutun, deger in enumerate(veri[1:], 1):  # 1'den başlayarak diğer sütunları ekleyin
                self.biletbilgisayfa.bilgi_tableWidget.setItem(satir, sutun, QTableWidgetItem(str(deger)))

     # Tablonun genişliğini sığabilecek şekilde ayarlayın
     self.biletbilgisayfa.bilgi_tableWidget.horizontalHeader().setStretchLastSection(True)




    def BiletAra(self):
     kolonlar = ["ID", "ETKİNLİK ADI", "İSİM", "BİLET SAYISI", "BİLET FİYATI"]
     self.biletbilgisayfa.bilgi_tableWidget.setColumnCount(len(kolonlar))  # Sütun sayısını ayarla
     self.biletbilgisayfa.bilgi_tableWidget.setHorizontalHeaderLabels(kolonlar)  # Kolon başlıklarını ayarla
     etkinlik_Adi = self.biletbilgisayfa.arama_yap_line_edit.text()

     veriler = self.gveritabani.Biletara(etkinlik_Adi)
     if veriler:
        self.biletbilgisayfa.bilgi_tableWidget.setRowCount(len(veriler))  # Satır sayısını ayarla
        for satir, veri in enumerate(veriler):
            self.biletbilgisayfa.bilgi_tableWidget.setItem(satir, 0, QTableWidgetItem(str(veri[0])))  # ID değerini ekleyin
            for sutun, deger in enumerate(veri[1:], 1):  # 1'den başlayarak diğer sütunları ekleyin
                self.biletbilgisayfa.bilgi_tableWidget.setItem(satir, sutun, QTableWidgetItem(str(deger)))

    # Tablonun genişliğini sığabilecek şekilde ayarlayın
     self.biletbilgisayfa.bilgi_tableWidget.horizontalHeader().setStretchLastSection(True)

     

        