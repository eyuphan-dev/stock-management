# Stok Yönetim Sistemi

Django tabanlı envanter takibi ve yönetimi için geliştirilmiş bir stok yönetim sistemi.

## Özellikler

- Envanter yönetimi
- Kullanıcı kimlik doğrulama sistemi
- Yönetici paneli
- Duyarlı (responsive) web arayüzü
- Stok takibi ve raporlama

## Kurulum

1. Repository'yi klonlayın:
```bash
git clone <repository-url>
cd stock-management
```

2. Sanal ortam oluşturun:
```bash
python -m venv virtualenv
```

3. Sanal ortamı aktifleştirin:
- Windows:
```bash
virtualenv\Scripts\activate
```
- macOS/Linux:
```bash
source virtualenv/bin/activate
```

4. Gerekli paketleri yükleyin:
```bash
pip install django
```

5. Veritabanı migration'larını çalıştırın:
```bash
python manage.py migrate
```

6. Süper kullanıcı (admin) oluşturun:
```bash
python manage.py createsuperuser
```

7. Geliştirme sunucusunu başlatın:
```bash
python manage.py runserver
```

## Kullanım

Uygulamaya `http://localhost:8000` adresinden erişebilirsiniz.

Admin paneline erişim için: `http://localhost:8000/admin`

## Kullanılan Teknolojiler

- Django - Backend framework
- SQLite - Veritabanı
- HTML/CSS/JavaScript - Frontend
- Bootstrap - UI framework
- Perfect Scrollbar - Kaydırma çubukları
- Chart.js - Grafik ve görselleştirmeler

## Proje Yapısı

- `main/` - Ana uygulama modülü
- `user/` - Kullanıcı yönetimi modülü
- `core/` - Django ayarları ve yapılandırma
- `templates/` - HTML şablonları
- `static/` - Statik dosyalar (CSS, JS, görseller)
- `media/` - Kullanıcı tarafından yüklenen dosyalar
- `pages/` - Sayfa şablonları

## Geliştirici Notları

### Yeni Uygulama Ekleme
```bash
python manage.py startapp app_adi
```

### Static Dosyaları Toplama
```bash
python manage.py collectstatic
```

### Yeni Migration Oluşturma
```bash
python manage.py makemigrations
```

## Katkıda Bulunma

1. Projeyi fork edin
2. Feature branch'i oluşturun (`git checkout -b feature/YeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/YeniOzellik`)
5. Pull Request oluşturun

## Lisans

Bu proje açık kaynak kodludur ve [MIT Lisansı](LICENSE) altında sunulmaktadır.

## İletişim

Proje ile ilgili sorularınız için issue açabilirsiniz.