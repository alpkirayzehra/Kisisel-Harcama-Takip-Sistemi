
import json

class Harcama():
    def __init__(self,tur ,tutar,kategori,aciklama,tarih):
        self.tur=tur
        self.tutar=tutar
        self.kategori=kategori
        self.aciklama=aciklama
        self.tarih=tarih

class HarcamaTakip():
    def __init__(self):
        self.harcamalar = []
    def harcama_ekle(self,harcama):
        self.harcamalar.append(harcama)
    def harcamalari_listele(self):
        for harcama in self.harcamalar:
           print(harcama.tur ,
                 harcama.tutar ,
                 harcama.kategori ,
                 harcama.aciklama ,
                 harcama.tarih
                 )
    def toplam_gider_hesapla(self):
        toplam_gider=0
        for harcama in self.harcamalar:
            if harcama.tur == "gider" :
                toplam_gider += harcama.tutar
        return toplam_gider
    def toplam_gelir_hesapla(self):
        toplam_gelir=0
        for harcama in self.harcamalar:
            if harcama.tur == "gelir" :
                toplam_gelir += harcama.tutar
        return toplam_gelir
    def bakiye_hesapla(self):
        bakiye= self.toplam_gelir_hesapla() - self.toplam_gider_hesapla()
        return bakiye
    def kategori_toplamlari_hesapla(self):
        kategori_toplamlari= {}

        for harcama in self.harcamalar:
            kategori = harcama.kategori
            tutar=harcama.tutar
            if harcama.tur == "gider":
              if kategori in kategori_toplamlari:
                  kategori_toplamlari[kategori] +=tutar
              else:
                 kategori_toplamlari[kategori]=tutar  # boş sözlüğe kategori ve tutar ekledik.
        return kategori_toplamlari
    def en_cok_harcama_kategorisi(self):
        kategori_toplamlari=self.kategori_toplamlari_hesapla()

        if not kategori_toplamlari:
          return None
        
        en_yuksek_tutar=0
        en_yuksek_kategori = ""
        
        for kategori, tutar in kategori_toplamlari.items():
            if tutar > en_yuksek_tutar:
                en_yuksek_tutar = tutar
                en_yuksek_kategori = kategori
        return en_yuksek_kategori , en_yuksek_tutar
    def en_az_harcama_kategorisi(self):
        kategori_toplamlari=self.kategori_toplamlari_hesapla()

        if not kategori_toplamlari:
            return None

        en_dusuk_tutar=list(kategori_toplamlari.values())[0]
        en_dusuk_kategori =list(kategori_toplamlari.keys())[0]
        
        for kategori, tutar in kategori_toplamlari.items():
            if tutar < en_dusuk_tutar:
                en_dusuk_tutar = tutar
                en_dusuk_kategori = kategori
        return en_dusuk_kategori , en_dusuk_tutar
    def istatistik_raporu(self):
        toplam_gider=self.toplam_gider_hesapla()
        toplam_gelir=self.toplam_gelir_hesapla()
        kategori_toplamlari=self.kategori_toplamlari_hesapla()
        en_az=self.en_az_harcama_kategorisi()
        en_cok=self.en_cok_harcama_kategorisi()
        bakiye=self.bakiye_hesapla()
        print(f"Toplam Gelir: {toplam_gelir} TL")
        print(f"Toplam Gider: {toplam_gider} TL")

        print("Kategori Toplamları:")
        for kategori,tutar in kategori_toplamlari.items():
            print(f"{kategori} : {tutar} TL")

        if en_cok is None:
          print("Henüz gider kaydı bulunmuyor.")
        else:
          print(f"En çok harcama: {en_cok[0]} : {en_cok[1]} TL")
          print(f"En az harcama: {en_az[0]} : {en_az[1]} TL")

        print(f"Bakiye : {bakiye} TL ")
    def verileri_kaydet(self):
      veriler = []

      for harcama in self.harcamalar:
        veriler.append({
            "tur": harcama.tur,
            "tutar": harcama.tutar,
            "kategori": harcama.kategori,
            "aciklama": harcama.aciklama,
            "tarih": harcama.tarih
        })

      with open("harcamalar.json", "w", encoding="utf-8") as dosya:
         json.dump(veriler, dosya, ensure_ascii=False, indent=4)
    def verileri_yukle(self):
      try:
        with open("harcamalar.json", "r", encoding="utf-8") as dosya:
            veriler = json.load(dosya)

        self.harcamalar = []

        for veri in veriler:
            harcama = Harcama(
                veri["tur"],
                veri["tutar"],
                veri["kategori"],
                veri["aciklama"],
                veri["tarih"]
            )
            self.harcamalar.append(harcama)

      except FileNotFoundError:
        self.harcamalar = []


t1=HarcamaTakip()
t1.verileri_yukle()

islem1 = Harcama("gider",300,"Yemek","Market alışverişi","2026-10-17")
islem2 = Harcama("gider",150,"Yemek","Manav alışverişi","2026-10-17")
islem3 = Harcama("gelir", 15000, "Maaş", "Ekim maaşı", "2026-10-20")
islem4 = Harcama("gelir", 5000, "Prim", "Ekim primi", "2026-10-20")
islem5 = Harcama("gider", 7000, "Kira", "Ekim kirası", "2026-10-20")

t1.harcama_ekle(islem1)  # işlemler listeye eklendi.
t1.harcama_ekle(islem2)
t1.harcama_ekle(islem3)
t1.harcama_ekle(islem4)
t1.harcama_ekle(islem5)


def menu_goster():
    print("""     KİŞİSEL HARCAMA TAKİP SİSTEMİ
                    - Ana Menü -
        
     1. Gelir ekle
     2. Gider ekle
     3. İşlemleri listele
     4. Bakiye görüntüle
     5. Harcama istatistikleri
     6. Programdan çık  """)

while True:
    menu_goster()
    
    try:
      i= int(input("Yapmak istediğiniz işlemi seçin : "))
      if i == 1 :
        tutar=float(input("Tutarı giriniz: "))
        if tutar<=0:
          print("Tutar sıfırdan büyük olmalı.")
          continue
        kategori=input("Kategori:")
        aciklama=input("Açıklama:")
        tarih=input("Tarih (yy-aa-gg):")

        yeni_gelir = Harcama("gelir", tutar, kategori, aciklama, tarih)
        t1.harcama_ekle(yeni_gelir)
        t1.verileri_kaydet()
        print("Gelir başarıyla eklendi.")
        
      elif i == 2 :
        tutar=float(input("Tutarı giriniz: "))
        if tutar<=0:
           print("Tutar sıfırdan büyük olmalı.")
           continue
        kategori=input("Kategori:")
        aciklama=input("Açıklama:")
        tarih=input("Tarih (yy-aa-gg):")

        yeni_gider=Harcama("gider",tutar,kategori,aciklama,tarih)
        t1.harcama_ekle(yeni_gider)
        t1.verileri_kaydet()
        print("Gider başarıyla eklendi.")

      elif i == 3 :
        print("Kayıt sayısı:", len(t1.harcamalar))
        t1.harcamalari_listele()
      elif i == 4 :
        print(t1.bakiye_hesapla())
      elif i == 5 :
        t1.istatistik_raporu()
      elif i == 6 :
        print("Programdan çıkış yapıldı..")
        break
      else:
        print("Geçersiz bir sayı girdiniz.")
    except ValueError:
       print("Lütfen bir sayı değeri girin.")





