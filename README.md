# STOKMAN - Stok Yönetim Sistemi

Django ile geliştirilmiş profesyonel stok ve envanter yönetim sistemi.

## Proje Hakkında

STOKMAN, küçük ve orta ölçekli işletmelerin stok takibini kolaylaştırmak için geliştirilmiş web tabanlı bir uygulamadır. Kullanıcı dostu arayüzü ve kapsamlı özellikleri ile envanter yönetimini basitleştirir.

## Özellikler

**Ürün Yönetimi**
- Ürün ekleme, düzenleme, silme ve listeleme
- Ürün görseli yükleme ve görüntüleme
- SKU (Stok Kodu) ile takip
- Kategori bazlı ürün organizasyonu
- Minimum stok seviyesi tanımlama
- Aktif/Pasif ürün durumu

**Kategori Yönetimi**
- Kategori oluşturma ve listeleme
- Kategori bazlı ürün gruplandırma
- Kategori başına ürün sayısı takibi

**Stok Takibi**
- Stok giriş, çıkış ve düzeltme hareketleri
- Ürün bazlı hareket geçmişi
- Düşük stok uyarıları
- Stokta tükenen ürün bildirimleri
- Hareket notları ve kullanıcı takibi

**Raporlama ve İstatistikler**
- Toplam stok değeri hesaplama
- Kategori bazlı analiz
- Tarih filtreleme (7/30/90 gün, tüm zamanlar)
- Stok giriş/çıkış özeti
- En çok hareket gören ürünler
- Grafik ve görsel istatistikler

**Kullanıcı Yönetimi**
- Güvenli giriş ve kayıt sistemi
- Kullanıcı bazlı yetkilendirme
- Oturum yönetimi

**Arayüz**
- Modern ve responsive tasarım
- Türkçe dil desteği
- Mobil uyumlu
- Kolay navigasyon
- Dashboard ile hızlı genel bakış

## Teknoloji Yığını

- **Backend:** Django 5.x
- **Veritabanı:** SQLite
- **Frontend:** HTML5, CSS3, JavaScript
- **UI Framework:** Bootstrap 4
- **Template Engine:** Django Templates
- **Görsel İşleme:** Pillow
- **Admin Panel:** Django Admin (Türkçe)

## Kurulum

### Gereksinimler
- Python 3.12 veya üzeri
- pip (Python paket yöneticisi)
- Git

### Adımlar

1. Projeyi klonlayın:
```bash
git clone https://github.com/eyuphan-dev/stock-management.git
cd stock-management
```

2. Sanal ortam oluşturun ve aktifleştirin:
```bash
python -m venv virtualenv
virtualenv\Scripts\activate
```

3. Gerekli paketleri yükleyin:
```bash
pip install django pillow
```

4. Veritabanını oluşturun:
```bash
python manage.py migrate
```

5. Yönetici hesabı oluşturun:
```bash
python manage.py createsuperuser
```

6. Sunucuyu başlatın:
```bash
python manage.py runserver
```

7. Tarayıcınızda açın: `http://localhost:8000`

## Kullanım

### İlk Giriş
- Kayıt sayfasından yeni hesap oluşturun: `/kayit/`
- Veya superuser ile giriş yapın: `/giris/`

### Ana Özellikler
- **Dashboard:** Genel istatistikler ve hızlı erişim
- **Ürünler:** `/stok/` - Tüm ürünleri görüntüleyin
- **Yeni Ürün:** `/stok/urun/ekle/` - Ürün ekleyin
- **Kategoriler:** `/stok/kategoriler/` - Kategori yönetimi
- **Raporlar:** `/stok/raporlar/` - Detaylı istatistikler
- **Admin Panel:** `/admin/` - Gelişmiş yönetim

## Proje Yapısı

```
stock-management/
├── core/               # Django ayarları
│   ├── settings.py     # Proje yapılandırması
│   └── urls.py         # Ana URL yönlendirmeleri
├── main/               # Ana sayfa uygulaması
│   └── views.py        # Dashboard görünümleri
├── user/               # Kimlik doğrulama
│   ├── views.py        # Giriş/Çıkış/Kayıt
│   └── urls.py         # Auth URL'leri
├── inventory/          # Stok yönetimi
│   ├── models.py       # Ürün, Kategori, StokMovement
│   ├── views.py        # İş mantığı
│   ├── forms.py        # Form tanımları
│   ├── admin.py        # Admin panel özelleştirme
│   └── urls.py         # Stok URL'leri
├── templates/          # HTML şablonları
│   ├── base.html       # Ana şablon
│   ├── main/           # Dashboard şablonları
│   ├── inventory/      # Stok şablonları
│   └── authentication/ # Giriş/Kayıt sayfaları
├── static/             # Statik dosyalar
│   ├── css/
│   ├── js/
│   └── images/
├── media/              # Yüklenen dosyalar
└── manage.py           # Django yönetim scripti
```

## Veritabanı Modelleri

**Category (Kategori)**
- İsim, açıklama
- Oluşturulma tarihi

**Product (Ürün)**
- İsim, SKU, kategori
- Açıklama, birim fiyat
- Miktar, minimum stok seviyesi
- Ürün görseli
- Aktif/Pasif durum
- Oluşturan kullanıcı ve tarih

**StockMovement (Stok Hareketi)**
- Ürün referansı
- Hareket tipi (Giriş/Çıkış/Düzeltme)
- Miktar, not
- Oluşturan kullanıcı ve tarih

## Katkıda Bulunma

1. Projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request açın

## Lisans

Bu proje MIT Lisansı altında sunulmaktadır.

## Geliştirici

Eyüphan İpek - 2025