import sqlite3 
import os 

class veritabani():
    def __init__(self):
        dizin_yol = os.path.dirname(os.path.abspath(__file__))
        self.db = os.path.join(dizin_yol,'etkinlik_bilet_platfrom.db')
        print(self.db)
        

    def vtac(self):
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()


    def vtkapat(self):
        self.cursor.close()

    
    def kayitEkle(self,_id,etkinlik_Adi,mekan,bilet_sayisi,bilet_fiyati,tarih):
       try:
        self.vtac()
        sql = "insert into etkinlik (id,etkinlik_Adi,mekan,bilet_sayisi,bilet_fiyati,tarih) values (?,?,?,?,?,?)"
        self.cursor.execute(sql,(_id,etkinlik_Adi,mekan,bilet_sayisi,bilet_fiyati,tarih))
        self.conn.commit()
        return True
       except:
          return False
       finally:
          self.vtkapat()


    def kayitGoster(self):
       try:
          self.vtac()
          sql = "select * from etkinlik order by id "
          self.cursor.execute(sql)
          veriler = self.cursor.fetchall()
          return veriler
       except:
          return False
       finally:
          self.vtkapat

    def biletKayitGoster(self):
       try:
          self.vtac()
          sql = "select * from bilet order by id "
          self.cursor.execute(sql)
          veriler = self.cursor.fetchall()
          return veriler
       except:
          return False
       finally:
          self.vtkapat
       



    def _Guncelle(self, _id, etkinlik_Adi, mekan, bilet_sayisi, bilet_fiyati, tarih):
      try:
        self.vtac()
        sql = "UPDATE etkinlik SET etkinlik_Adi = ?, mekan = ?, bilet_sayisi = ?, bilet_fiyati = ?, tarih = ? WHERE id = ?"
        self.cursor.execute(sql, (etkinlik_Adi, mekan, bilet_sayisi, bilet_fiyati, tarih, _id))
        self.conn.commit()
        return True
      except Exception as e:
        print(f'Hata: {e}')
        return False  # Hata durumunda False döndürmek önemlidir
      finally:
        self.vtkapat()



    def sil(self, _id):
       try:
          self.vtac()
          sql = "DELETE FROM etkinlik WHERE id = ?"
          self.cursor.execute(sql, (_id,))
          self.conn.commit()
          return True
       except sqlite3.Error as e:
          print("SQLite Hatası:", e) 
          return False
       finally:
        self.vtkapat()
          
    


    def ara(self, etkinlik_Adi):
      try:
        self.vtac()
        sql = "SELECT * FROM etkinlik WHERE etkinlik_Adi LIKE ? ORDER BY id DESC"
        # LIKE operatörü için parametreli sorgu kullanımı
        self.cursor.execute(sql, ('%' + etkinlik_Adi + '%',))
        veriler = self.cursor.fetchall()
        return veriler
      except Exception as e:
        print("Arama hatası:", e)
        return False
      finally:
        self.vtkapat()






    def biletKayitEkle(self,_id,etkinlik_Adi,isim,bilet_sayisi,odenecek_tutar):
       try:
        self.vtac()
        sql = "insert into bilet (id,etkinlik_adi,isim,bilet_sayisi,bilet_fiyati) values (?,?,?,?,?)"
        self.cursor.execute(sql,(_id,etkinlik_Adi,isim,bilet_sayisi,odenecek_tutar))
        self.conn.commit()
        return True
       except Exception as e:
        print("Arama hatası:", e)
        return False
       finally:
        self.vtkapat()


    def BiletSayisiGuncelle(self, bilet_Sayisi_al):
      try:
        self.vtac()
        sql = "UPDATE etkinlik SET bilet_sayisi = bilet_sayisi - ?"
        self.cursor.execute(sql, (bilet_Sayisi_al,))
        self.conn.commit()
        return True
      except sqlite3.Error as e:
        print("Veritabanı hatası:", e)
        return False
      finally:
        self.vtkapat()

    def EtkinlikBiletSayisiGetir(self, etkinlik_id):
       try:
        self.vtac()
        sql = "SELECT bilet_sayisi FROM etkinlik WHERE id = ?"
        self.cursor.execute(sql, (etkinlik_id))
        etkinlik_bilet_sayisi = self.cursor.fetchall()
        return etkinlik_bilet_sayisi[0][0]
       except sqlite3.Error as e:
        print("Veritabanı hatası:", e)
        return False
       finally:
        self.vtkapat()


    def EtkinlikBiletParasiGetir(self, etkinlik_id):
       try:
        self.vtac()
        sql = "SELECT bilet_fiyati FROM etkinlik WHERE id = ?"
        self.cursor.execute(sql, (etkinlik_id))
        etkinlik_bilet_fiyati = self.cursor.fetchall()
        return etkinlik_bilet_fiyati[0][0]
       except sqlite3.Error as e:
        print("Veritabanı hatası:", e)
        return False
       finally:
        self.vtkapat()
    

    def Biletara(self, etkinlik_Adi):
      try:
        self.vtac()
        sql = "SELECT * FROM bilet WHERE etkinlik_Adi LIKE ? ORDER BY id DESC"
        # LIKE operatörü için parametreli sorgu kullanımı
        self.cursor.execute(sql, ('%' + etkinlik_Adi + '%',))
        veriler = self.cursor.fetchall()
        return veriler
      except Exception as e:
        print("Arama hatası:", e)
        return False
      finally:
        self.vtkapat()



   






     
