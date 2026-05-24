# 🌌 ZurBot Website

Proje; el yazımı (vanilla) **Siber-Cam (Glassmorphism)** görsel estetiğini, Python/Flask tabanlı dinamik çok dilli (TR/EN) backend altyapısını ve tarayıcı yerel depolama alanıyla entegre çalışan gerçek zamanlı sepet/ödeme simülasyonlarını tek bir gövdede birleştirmektedir.
---

## ✨ Teknik Yetkinlik Alanları & Öne Çıkan Özellikler

### 1. 🎨 Gelişmiş Arayüz Mühendisliği (Glassmorphism & Neon)
- **Siber-Cam Estetiği**: Tamamen el yazımı (vanilla) CSS ile oluşturulmuş, arka plandan süzülen neon ışıkları harika şekilde kıran yarı saydam (`rgba(255, 255, 255, 0.015)`) ve belirgin kenarlıklı cam kartlar ile navigasyon docks.
- **Neon Işık Auraları**: Sayfalarda gezindikçe arka planda hareket eden ve cam kartların arkasından süzülerek arayüze muazzam bir 3D derinlik hissi veren yeşil neon auralar.
- **Akıcı Mikro-Animasyonlar**: Butonlar, kartlar ve form alanlarında etkileşimi artıran akıcı geçiş efektleri.
- **HUD Siber Footer**: Sayfanın en altında yer alan, periyodik olarak parıldayan canlı güvenlik durum ledine (`SYSTEM SECURE`) sahip asimetrik siber kokpit paneli.

### 2. 🛠️ Python Flask & Dinamik Çok Dilli Altyapı (Localization)
- **Sunucu Tarafında Dil Yönetimi**: Tarayıcı diline veya kullanıcının seçimine göre tüm web sitesi içeriğini (yasal belgeler dahil) anında yerelleştiren (TR/EN) dinamik Python Flask dil motoru.
- **Temiz Yönlendirme (Routing)**: Modüler, genişletilebilir ve temiz backend endpoint tasarımları.

### 3. 🛒 İnteraktif Alışveriş Sepeti Çekmecesi (State Management)
- **localStorage Entegrasyonu**: Kullanıcının eklediği bot lisanslarını tarayıcı hafızasında saklayan, sayfa yenilense veya tarayıcı kapatılsa dahi sepeti koruyan kalıcı sepet çekmecesi.
- **Anlık Hesaplama Motoru**: Ürün ekleme/çıkarma işlemlerinde toplam tutarı, indirim oranlarını ve kur birimini (TR/EN durumuna göre TL veya USD bazında) dinamik hesaplayan JavaScript motoru.

### 4. 💳 3D Kredi Kartı & Güvenli Ödeme Simülasyonu
- **Canlı Kart Önizleme & BIN Algılama**: Kullanıcı kredi kartı numarasını yazarken ilk hanelerden kartın markasını (Visa, Mastercard, Amex) anlık tespit edip logosunu yansıtan ve form girdilerini eşzamanlı olarak kart görseline işleyen interaktif ödeme ekranı.
- **ZUR ZUR Maskelemesi**: Kart sahibi ismi kısmını portfolyoya özel olarak anlık "ZUR ZUR" olarak maskeleyen dinamik veri maskeleme mekanizması.
- **256-Bit SSL Ödeme Adımları**: Kart döndürme animasyonları ve güvenlik takılarıyla zenginleştirilmiş animasyonlu sanal ödeme deneyimi.

### 5. 📜 Dinamik Yasal Belgeler Sistemi
- Kullanım Şartları, Gizlilik Politikası ve Çerez Politikası sayfalarını ana ekranı terk etmeden, şık cam pencereler (Modals) içerisinde AJAX benzeri bir hızla çağıran optimize edilmiş yasal belgeler tetikleyicisi.

---

## 🛠️ Yerel Kurulum ve Çalıştırma Adımları

1. **Depoyu Bilgisayarınıza Klonlayın:**
   ```bash
   git clone <github-depo-adresi>
   cd botsite
   ```

2. **Sanal Ortamı (Virtual Environment) Aktifleştirin:**
   - **Windows (PowerShell):**
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   - **macOS / Linux:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Bağımlılıkları Yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Projeyi Çalıştırın:**
   ```bash
   python app.py
   ```
   Ardından tarayıcınızda `http://127.0.0.1:5000/` adresine giderek projeyi yerel olarak inceleyebilirsiniz.

---

## 📁 Proje Dosya Yapısı

```text
botsite/
│
├── ⚙️ app.py                  # Backend motoru ve dinamik çok dilli (TR/EN) yerelleştirme sözlüğü
├── 📄 requirements.txt        # Projenin çalışması için gereken Python kütüphaneleri (Flask)
├── 📄 .gitignore              # .venv, derleyici cache'leri ve IDE ayarlarını gizleyen kilit dosya
├── 📄 README.md               # Portfolyo tanıtım belgesi (Şu an okuduğunuz dosya)
│
├── 🎨 static/
│   └── style.css              # Geliştirilen siber-cam ve neon tasarım sistemi CSS kodları
│
└── 🗂️ html/
    ├── index.html             # Alışveriş sepeti çekmecesi, kart simülatörü ve siber modallar
    └── login.html             # Siber-cam tasarımlı üye giriş ve kayıt ekranı şablonları
```

---
*Bu proje, profesyonel bir yazılım mühendisliği portfolyosu kapsamında **itsravn** tarafından tutkuyla tasarlanıp geliştirilmiştir.*
