# Kişisel Harcama Takip Sistemi

Python ile geliştirilmiş, terminal üzerinden çalışan bir kişisel gelir ve gider takip uygulamasıdır.

Proje, Nesne Yönelimli Programlama (OOP) prensipleri kullanılarak geliştirilmiştir. Gelir ve gider işlemleri JSON dosyasında saklanarak verilerin program kapatıldıktan sonra da korunması sağlanmıştır.

## Özellikler

- Gelir ve gider ekleme
- Tüm işlemleri listeleme
- Toplam gelir ve gider hesaplama
- Güncel bakiye görüntüleme
- Kategorilere göre harcama analizi
- En çok ve en az harcama yapılan kategorileri belirleme
- Hatalı tutar girişlerini kontrol etme
- JSON ile verileri kaydetme ve yeniden yükleme

## Kullanılan Teknolojiler

- Python 3
- Nesne Yönelimli Programlama (OOP)
- JSON
- Git ve GitHub

## Kurulum ve Çalıştırma

**1.** Bilgisayarınızda Python 3 kurulu olmalıdır.

**2.** Projeyi bilgisayarınıza indirin veya Git ile klonlayın.

**3.** Terminali proje klasöründe açın.

**4.** Aşağıdaki komutu çalıştırın:

```bash
python main.py
```

## Menü Seçenekleri

1. Gelir ekle
2. Gider ekle
3. İşlemleri listele
4. Bakiye görüntüle
5. Harcama istatistikleri
6. Programdan çık

## Projenin Amacı

Bu proje; Python programlama, OOP, sınıf ve nesne kullanımı, döngüler, koşullu ifadeler, veri yapıları, hata kontrolü ve JSON dosya işlemleri konularındaki bilgileri uygulamalı olarak geliştirmek amacıyla hazırlanmıştır.

## Gelecekte Eklenebilecek Özellikler

- Matplotlib ile harcama grafikleri
- Aylık gelir-gider raporları
- Tarihe göre işlem filtreleme
- CSV formatında rapor oluşturma
- Kullanıcı arayüzü geliştirme

## Veri Saklama

Gelir ve gider kayıtları `harcamalar.json` dosyasında saklanır. Dosya mevcut değilse uygulama boş bir işlem listesiyle başlar. Kişisel finansal verilerin GitHub'a yüklenmemesi için bu dosya `.gitignore` kapsamına alınmıştır.

