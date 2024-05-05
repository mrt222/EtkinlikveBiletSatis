from PyQt5.QtWidgets import *
from bilet_satin_al_python import Ui_Form
from veritabani import veritabani


class Bilet_satin_al_Sayfa(QWidget):
    def __init__(self):
        super().__init__()
        self.biletAlSayfa = Ui_Form()
        self.biletAlSayfa.setupUi(self) 

        self.bveritabani = veritabani()

        self.biletAlSayfa.satin_al_buton.clicked.connect(self.satinAl)
        



    def satinAl(self):
     veriler = None  # veya başka bir varsayılan değer
     _id = self.biletAlSayfa.id_line_edit.text()
     etkinlik_Adi = self.biletAlSayfa.etknilik_adi_line_edit.text()
     isim = self.biletAlSayfa.isim_line_edit.text()
     bilet_sayisi = self.biletAlSayfa.bilet_sayisi_line_edit.text()
     odenecek_tutar = self.biletAlSayfa.odenecek_tutar_line_edit.text()

     if _id.strip() == "":
      QMessageBox.warning(self,"Uyarı","ID kısmı boş bırakılamaz!")
     else:
        etkinlik_bilet_sayisi = self.bveritabani.EtkinlikBiletSayisiGetir(_id)
        etkinlik_bilet_fiyati = self.bveritabani.EtkinlikBiletParasiGetir(_id)

        if etkinlik_bilet_sayisi == 0:
            QMessageBox.warning(self, "Uyarı", "Etkinlik için Bilet bulunmamaktadır")
        else:
            if int(bilet_sayisi) > etkinlik_bilet_sayisi:
                QMessageBox.warning(self, "Uyarı", "İstediğiniz miktarda bilet bulunmamaktadır")
            else:
                bilet_toplam_tutar = int(bilet_sayisi) * etkinlik_bilet_fiyati
                if  bilet_toplam_tutar < int(odenecek_tutar):
                    veriler = self.bveritabani.biletKayitEkle(_id,etkinlik_Adi,isim,bilet_sayisi,odenecek_tutar)
                else:
                    QMessageBox.warning(self, "Uyarı", f"Ödemeniz yetersizdir bilet tutarları : {bilet_toplam_tutar}")

     if veriler:
        QMessageBox.information(self, 'Başarılı', 'Kayıt başarıyla eklendi.')
     else:
        QMessageBox.warning(self, 'Hata', 'Kayıt eklenirken bir hata oluştu.')

    


        
    



        

