from  PyQt5.QtWidgets import *
from etkinlik_duzenle_python import Ui_Form
from veritabani import veritabani


class EtkinlikSayfa(QWidget):
    def __init__(self):
        super().__init__()
        self.etkinlikSayfa = Ui_Form()
        self.etkinlikSayfa.setupUi(self)

        self.everitabani = veritabani()

        self.etkinlikSayfa.ekle_buton.clicked.connect(self.etkinlikEkle)
        self.etkinlikSayfa.sil_buton.clicked.connect(self.etkinlikSil)
        self.etkinlikSayfa.guncelle_buton.clicked.connect(self.etkinlikGuncelle)





    def etkinlikEkle(self):
        _id = self.etkinlikSayfa.id_line_edit.text()
        etkinlik_Adi = self.etkinlikSayfa.etkinlik_adi_line_Edit.text()
        mekan = self.etkinlikSayfa.mekan_line_edit.text()
        bilet_sayisi = self.etkinlikSayfa.bilet_sayisi_line_edit.text()
        bilet_fiyati = self.etkinlikSayfa.bilet_fiyat_line_edit.text()
        tarih = self.etkinlikSayfa.tarih_line_Edit.text()


        if _id.strip() == "":
            QMessageBox.warning(self,"Uyarı","ID kısmı boş bırakılamaz!")
        else:
            
            veriler = self.everitabani.kayitEkle(_id,etkinlik_Adi,mekan,bilet_sayisi,bilet_fiyati,tarih)

        
        if veriler:
            
            QMessageBox.information(self, 'Başarılı', 'Kayıt başarıyla eklendi.')
        else:
            QMessageBox.warning(self, 'Hata', 'Kayıt eklenirken bir hata oluştu.')



    def etkinlikSil(self):
        _id = self.etkinlikSayfa.id_line_edit.text()
        sil = self.everitabani.sil(_id)

        if sil:
            
            QMessageBox.information(self,"Bilgi","Kayıt Başarıyla Silindi")
        else:
            QMessageBox.warning(self,"Bilgi","Kayıt Silinemedi.")

    
    def etkinlikGuncelle(self):
        _id = self.etkinlikSayfa.id_line_edit.text()
        etkinlik_Adi = self.etkinlikSayfa.etkinlik_adi_line_Edit.text()
        mekan = self.etkinlikSayfa.mekan_line_edit.text()
        bilet_sayisi = self.etkinlikSayfa.bilet_sayisi_line_edit.text()
        bilet_fiyati = self.etkinlikSayfa.bilet_fiyat_line_edit.text()
        tarih = self.etkinlikSayfa.tarih_line_Edit.text()

        if _id.strip() == "":
            QMessageBox.warning(self,"Uyarı","ID kısmı boş bırakılamaz!")
        else:
            
            veriler = self.everitabani._Guncelle(_id,etkinlik_Adi,mekan,bilet_sayisi,bilet_fiyati,tarih)




        if veriler:
            
            QMessageBox.information(self, 'Başarılı', 'Kayıt başarıyla güncellendi.')
        else:
            QMessageBox.warning(self, 'Hata', 'Kayıt güncellenirken bir hata oluştu.')
        



