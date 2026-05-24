from flask import Flask, render_template, request

app = Flask(__name__, template_folder='html')

# Localization dictionaries
t_tr = {
    "title": "ZurBot - Gelişmiş Discord Bot ve Portfolyo Sistemi",
    "brand": "ZurBot",
    "packages": "Paketlerimiz",
    "bots": "Bot Modüllerimiz",
    "services": "Web Servislerimiz",
    "team": "Ekibimiz",
    "reviews": "Yorumlar",
    "login": "Giriş Yap",
    "cart_title": "Alışveriş Sepeti",
    "cart_empty": "Sepetiniz şu anda boş.",
    "total": "Toplam",
    "checkout_btn": "Ödemeyi Tamamla",
    "close_btn": "Kapat",
    "buy_btn": "Sepete Ekle",
    "service_btn": "Hizmeti Seç",
    "scroll_down": "Aşağı Kaydır",
    "legal_title": "Kurumsal & Yasal",
    "terms_title": "Kullanım Şartları",
    "privacy_title": "Gizlilik Politikası",
    "cookies_title": "Çerez Politikası",
    "cardholder_name": "Kart Sahibi Adı",
    "cardholder_placeholder": "Ad Soyad",
    "card_number": "Kart Numarası",
    "expiry_date": "Son Kullanma",
    "cvv": "CVV",
    "pay_now_btn": "Güvenli Ödeme Yap",
    "payment_success": "Ödeme Başarılı!",
    "payment_success_desc": "Lisansınız ve kurulum adımları kayıtlı mail adresinize gönderilmiştir.",
    
    # Billing Tabs
    "tab_monthly": "Aylık",
    "tab_3months": "3 Aylık",
    "tab_6months": "6 Aylık",
    "tab_yearly": "Yıllık",

    # Login page
    "login_card_title": "ZurBot - Giriş / Kayıt Paneli",
    "login_now": "Giriş Yap",
    "dont_have_acc": "Hesabınız yok mu?",
    "register_now": "Kayıt Ol",
    "social_signup_notice": "Verilerinizin güvenliği için Discord veya Google hesabınızla hızlıca entegre olabilirsiniz.",
    "discord_signup": "Discord ile Giriş Yap",
    "google_signup": "Google ile Giriş Yap",
    "already_have_acc": "Zaten hesabınız var mı?",
    "forgot_pass_card_title": "Şifremi Unuttum",
    "enter_email_desc": "Şifre sıfırlama linki gönderebilmemiz için kayıtlı e-posta adresinizi girin.",
    "email_address": "E-Posta Adresi",
    "send_code_btn": "Kod Gönder",
    "back_to_login": "Giriş Ekranına Dön",
    "username": "Kullanıcı Adı",
    "password": "Şifre",
    "forgot_pass_link": "Şifremi Unuttum",
    "hero_subtitle": "Discord Topluluğunuzu Geleceğe Taşıyın"
}

t_en = {
    "title": "ZurBot - Advanced Discord Bot & Portfolio System",
    "brand": "ZurBot",
    "packages": "Packages",
    "bots": "Bot Modules",
    "services": "Web Services",
    "team": "Team",
    "reviews": "Reviews",
    "login": "Login",
    "cart_title": "Shopping Cart",
    "cart_empty": "Your cart is currently empty.",
    "total": "Total",
    "checkout_btn": "Proceed to Checkout",
    "close_btn": "Close",
    "buy_btn": "Add to Cart",
    "service_btn": "Select Service",
    "scroll_down": "Scroll Down",
    "legal_title": "Corporate & Legal",
    "terms_title": "Terms of Service",
    "privacy_title": "Privacy Policy",
    "cookies_title": "Cookie Policy",
    "cardholder_name": "Cardholder Name",
    "cardholder_placeholder": "Full Name",
    "card_number": "Card Number",
    "expiry_date": "Expiry Date",
    "cvv": "CVV",
    "pay_now_btn": "Pay Securely",
    "payment_success": "Payment Successful!",
    "payment_success_desc": "Your license and installation guide have been sent to your registered email address.",
    
    # Billing Tabs
    "tab_monthly": "Monthly",
    "tab_3months": "3 Months",
    "tab_6months": "6 Months",
    "tab_yearly": "Yearly",

    # Login page
    "login_card_title": "ZurBot - Login / Register Panel",
    "login_now": "Login Now",
    "dont_have_acc": "Don't have an account?",
    "register_now": "Register Now",
    "social_signup_notice": "For your data safety, you can quickly integrate with your Discord or Google account.",
    "discord_signup": "Sign in with Discord",
    "google_signup": "Sign in with Google",
    "already_have_acc": "Already have an account?",
    "forgot_pass_card_title": "Forgot Password",
    "enter_email_desc": "Enter your registered email address to receive a password reset link.",
    "email_address": "Email Address",
    "send_code_btn": "Send Code",
    "back_to_login": "Back to Login",
    "username": "Username",
    "password": "Password",
    "forgot_pass_link": "Forgot Password?",
    "hero_subtitle": "Elevate Your Discord Community to the Future"
}

# Stats Data
stats_tr = [
    {"value": "0", "label": "Çevrimiçi Üye"},
    {"value": "0", "label": "Toplam Müşteri"},
    {"value": "4", "label": "Geliştirilen Sistem"}
]

stats_en = [
    {"value": "0", "label": "Online Members"},
    {"value": "0", "label": "Total Customers"},
    {"value": "4", "label": "Systems Engineered"}
]

# Packages Data
packages_tr = [
    {
        "title": "Başlangıç",
        "desc": "Temel moderasyon ve genel bot modülleri.",
        "price": "100.00 TL / ay",
        "price_val": 100.0,
        "features": ["Temel Moderasyon", "Kullanıcı Kayıt Sistemi", "%99.9 Aktif Kalma Süresi", "7/24 Teknik Destek"]
    },
    {
        "title": "Gelişmiş",
        "desc": "Profesyonel topluluklar için özel koruma ve moderasyon.",
        "price": "200.00 TL / ay",
        "price_val": 200.0,
        "features": ["Gelişmiş Guard & Koruma", "Özel Hoş Geldin Mesajları", "Rol Yönetim Sistemi", "1 Saatlik Kurulum Desteği"]
    },
    {
        "title": "Premium",
        "desc": "Tüm modüller, yüksek güvenlik ve özel web kontrol paneli.",
        "price": "400.00 TL / ay",
        "price_val": 400.0,
        "features": ["Siber-Güvenlik Altyapısı", "Web Kontrol Paneli", "API Entegrasyonu", "Anında VIP Teknik Destek"]
    }
]

packages_en = [
    {
        "title": "Starter",
        "desc": "Basic moderation and general bot modules.",
        "price": "$2.94 / mo",
        "price_val": 100.0,
        "features": ["Basic Moderation", "User Registration", "99.9% Uptime Guarantee", "24/7 Technical Support"]
    },
    {
        "title": "Advanced",
        "desc": "Advanced guard and protection modules for professional servers.",
        "price": "$5.88 / mo",
        "price_val": 200.0,
        "features": ["Advanced Guard & Protection", "Custom Welcome Greetings", "Role Management System", "1-Hour Setup Support"]
    },
    {
        "title": "Premium",
        "desc": "All modules included, high siber-security and custom web panel.",
        "price": "$11.76 / mo",
        "price_val": 400.0,
        "features": ["Siber-Security Infrastructure", "Web Control Dashboard", "Full API Integration", "Instant VIP Tech Support"]
    }
]

# Bot Modules Data
bots_tr = [
    {
        "title": "Guard Modülü",
        "desc": "Sunucunuzu spam, reklam ve bot saldırılarına karşı korur.",
        "price": "150.00 TL / ay",
        "price_val": 150.0,
        "features": ["Spam Filtresi", "Reklam Engelleme", "Güvenilir Yedekleme", "Giriş Limitleme"]
    },
    {
        "title": "Kayıt Modülü",
        "desc": "Üyelerinizin güvenli ve düzenli şekilde sunucuya kaydolmasını sağlar.",
        "price": "100.00 TL / ay",
        "price_val": 100.0,
        "features": ["Taglı/Tagsız Kayıt", "Yaş/İsim Doğrulama", "Cinsiyet Rolleri", "Kayıt İstatistikleri"]
    }
]

bots_en = [
    {
        "title": "Guard Module",
        "desc": "Protects your server against spam, advertisements, and bot attacks.",
        "price": "$4.41 / mo",
        "price_val": 150.0,
        "features": ["Spam Filter", "Ad Blocker", "Secure Backup", "Entry Rate Limiting"]
    },
    {
        "title": "Register Module",
        "desc": "Allows members to register safely and organized in your server.",
        "price": "$2.94 / mo",
        "price_val": 100.0,
        "features": ["Tagged/Untagged Registration", "Age & Name Verification", "Gender Role Assignment", "Registration Stats"]
    }
]

# Web Services Data
services_tr = [
    {
        "title": "Özel Bot Geliştirme",
        "desc": "Tamamen size veya topluluğunuza özel geliştirilen Discord botu.",
        "price": "0.00 TL",
        "price_val": 0.0,
        "setup": "500.00 TL",
        "features": ["Özel Kodlanmış Modüller", "Ömür Boyu Güncelleme Garantisi", "Özel İsim ve Profil", "Hızlı Teslimat"]
    },
    {
        "title": "Web Panel Kurulumu",
        "desc": "Botunuzu kolayca kontrol edebileceğiniz siber arayüz tasarımlı web panel.",
        "price": "0.00 TL",
        "price_val": 0.0,
        "setup": "800.00 TL",
        "features": ["Siber-Cam Arayüz", "Gerçek Zamanlı İstatistikler", "Rol/Kanal Yönetimi", "Bulut Sunucu Barındırma"]
    }
]

services_en = [
    {
        "title": "Custom Bot Development",
        "desc": "A custom Discord bot tailored exactly to your or your community's needs.",
        "price": "$0.00",
        "price_val": 0.0,
        "setup": "$500.00",
        "features": ["Tailor-Made Modules", "Lifetime Update Warranty", "Custom Name & Identity", "Fast-Track Delivery"]
    },
    {
        "title": "Web Dashboard Setup",
        "desc": "A premium web panel with a glassmorphic interface to control your bot.",
        "price": "$0.00",
        "price_val": 0.0,
        "setup": "$800.00",
        "features": ["Siber-Glassmorphic UI", "Real-Time Server Stats", "Role & Channel Management", "Cloud Server Hosting"]
    }
]

# Team Data
team = [
    ("tired", ""),
    ("raidenn", ""),
    ("fruzy", ""),
    ("tefocan", ""),
    ("electro", "")
]

# Reviews Data
reviews_tr = [
    ("OOG", "WhiteCity", "ZurBot ile sunucumuzu tamamen güvence altına aldık. Destek ve altyapı hızı inanılmaz derece yüksek!"),
    ("Hyperion", "DSRP", "Gelişmiş bot modülleri ve özel yönetim panelleri sayesinde topluluğumuzu yönetmek artık çok kolay."),
    ("SAFA", "Echo Community", "Web site entegrasyonu ve mesai yönetim botları mükemmel çalışıyor, ekibe çok teşekkür ederiz.")
]

reviews_en = [
    ("OOG", "WhiteCity", "We completely secured our server with ZurBot. The support and infrastructure speed are incredibly fast!"),
    ("Hyperion", "DSRP", "Thanks to advanced bot modules and custom dashboards, managing our community is now very easy."),
    ("SAFA", "Echo Community", "The website integration and shift management bots work perfectly, thanks to the team!")
]

@app.route('/')
def index():
    lang = request.args.get('lang', 'tr').lower()
    if lang == 'en':
        return render_template(
            'index.html',
            lang='en',
            t=t_en,
            stats=stats_en,
            packages=packages_en,
            bots=bots_en,
            services=services_en,
            team=team,
            reviews=reviews_en
        )
    else:
        return render_template(
            'index.html',
            lang='tr',
            t=t_tr,
            stats=stats_tr,
            packages=packages_tr,
            bots=bots_tr,
            services=services_tr,
            team=team,
            reviews=reviews_tr
        )

@app.route('/login')
def login():
    lang = request.args.get('lang', 'tr').lower()
    t = t_en if lang == 'en' else t_tr
    return render_template('login.html', lang=lang, t=t)

if __name__ == '__main__':
    app.run(debug=True)