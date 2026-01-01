# 🔢 CDSNG - Cubic Congruential Number Generator

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-mbesirkesen-lightgrey.svg)](https://github.com/mbesirkesen)

> Kübik kongruansiyel yöntem kullanarak deterministik rastgele sayı üreten profesyonel bir Python kütüphanesi.

## 📋 İçindekiler

- [Özellikler](#-özellikler)
- [Kurulum](#-kurulum)
- [Hızlı Başlangıç](#-hızlı-başlangıç)
- [Kullanım](#-kullanım)
- [Algoritma](#-algoritma)
- [Dokümantasyon](#-dokümantasyon)
- [Katkıda Bulunma](#-katkıda-bulunma)
- [Lisans](#-lisans)

## ✨ Özellikler

- 🎯 **Deterministik Üretim**: Aynı seed değeri ile her zaman aynı sayı dizisini üretir
- 🔢 **Çift Mod Desteği**: Hem tamsayı hem de [0, 1) aralığında ondalık sayı üretimi
- 🚀 **Yüksek Performans**: Optimize edilmiş matematiksel işlemler
- 🎨 **Basit API**: Kolay kullanım için temiz sınıf yapısı
- 📚 **Kapsamlı Dokümantasyon**: Detaylı algoritma açıklamaları ve örnekler
- 🔧 **Özelleştirilebilir**: Parametreler kolayca değiştirilebilir

## 📦 Kurulum

### Gereksinimler

- Python 3.6 veya üzeri

### Yükleme

1. **Projeyi klonlayın:**
```bash
git clone https://github.com/mbesirkesen/bsg1.git
cd bsg1
```

2. **Gerekli paketleri yükleyin (opsiyonel):**
```bash
pip install -r requirements.txt
```

> **Not:** Bu proje harici bağımlılık gerektirmez, Python standart kütüphanesi yeterlidir.

## 🚀 Hızlı Başlangıç

```python
from sayiüreteci import CDSNG

# Generator'ü seed ile başlat
generator = CDSNG(seed=12345)

# Tamsayı üret
sayi = generator.next_int()
print(f"Üretilen tamsayı: {sayi}")

# Ondalık sayı üret (0 ile 1 arası)
ondalik = generator.next_float()
print(f"Üretilen ondalık: {ondalik}")
```

## 📖 Kullanım

### Temel Kullanım

```python
from sayiüreteci import CDSNG

# Varsayılan parametrelerle başlat
gen = CDSNG(seed=42)

# Birden fazla sayı üret
for i in range(10):
    print(gen.next_int())
```

### Özelleştirilmiş Parametreler

```python
# Özel parametrelerle başlat
gen = CDSNG(
    seed=100,
    a=7,      # Kübik katsayı
    b=19,     # Karesel katsayı
    c=43,     # Doğrusal katsayı
    d=17,     # Sabit terim
    m=2**31   # Modül değeri
)
```

### Komut Satırı Kullanımı

```bash
python sayiüreteci.py
```

Program sizden seed değeri ve üretilecek sayı adedini isteyecektir.

### Örnek Çıktı

```
Seed değerini gir: 12345
Kaç sayı üretilecek?: 5

CDSNG ile üretilen sayılar:
987654321
123456789
456789012
789012345
234567890
```

## 🔬 Algoritma

CDSNG (Cubic Congruential Number Generator) algoritması, kübik kongruansiyel yöntem kullanarak deterministik rastgele sayılar üretir.

### Matematiksel Formül

```
X_{n+1} = (a × X_n³ + b × X_n² + c × X_n + d) mod m
```

### Varsayılan Parametreler

| Parametre | Değer | Açıklama |
|-----------|-------|----------|
| `a` | 5 | Kübik katsayı |
| `b` | 17 | Karesel katsayı |
| `c` | 41 | Doğrusal katsayı |
| `d` | 13 | Sabit terim |
| `m` | 2³¹ | Modül değeri |

### Algoritma Özellikleri

- **Periyod**: Yüksek periyodlu sayı dizileri üretir
- **Dağılım**: İyi bir istatistiksel dağılım sağlar
- **Hız**: O(1) zaman karmaşıklığı ile hızlı üretim
- **Bellek**: O(1) bellek kullanımı

## 📚 Dokümantasyon

Detaylı algoritma açıklamaları için `docs/` klasöründeki dosyaları inceleyin:

- 📊 `Akış Diyagramı.txt`: Program akış diyagramı
- 💻 `Pseudocode.txt`: Algoritmanın sözde kodu

### API Dokümantasyonu

#### `CDSNG` Sınıfı

```python
class CDSNG:
    def __init__(self, seed, a=5, b=17, c=41, d=13, m=2**31):
        """
        CDSNG generator'ü başlatır.
        
        Args:
            seed (int): Başlangıç değeri (X0)
            a (int): Kübik katsayı (varsayılan: 5)
            b (int): Karesel katsayı (varsayılan: 17)
            c (int): Doğrusal katsayı (varsayılan: 41)
            d (int): Sabit terim (varsayılan: 13)
            m (int): Modül değeri (varsayılan: 2^31)
        """
    
    def next_int(self) -> int:
        """
        Bir sonraki tamsayıyı üretir.
        
        Returns:
            int: Üretilen tamsayı
        """
    
    def next_float(self) -> float:
        """
        [0, 1) aralığında ondalık sayı üretir.
        
        Returns:
            float: 0 ile 1 arasında ondalık sayı
        """
```

## ⚠️ Güvenlik Notu

Bu sayı üretici, **eğlence, eğitim veya basit simülasyon** amaçları için uygundur. 

**Kriptografik uygulamalarda kullanılmamalıdır**, çünkü:
- Deterministik yapısı nedeniyle güvenli rastgelelik sağlamaz
- Kriptografik güvenlik için uygun değildir
- Güvenlik açısından kritik uygulamalarda kullanılmamalıdır

Kriptografik amaçlar için Python'un `secrets` modülünü veya diğer kriptografik güvenli RNG'leri kullanın.

## 🤝 Katkıda Bulunma

Katkılarınızı memnuniyetle karşılıyoruz! 

1. Bu projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Bir Pull Request açın

Detaylı bilgi için [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını inceleyin.

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 👤 Yazar

**Muhammed Beşir Keşen**

- GitHub: [@mbesirkesen](https://github.com/mbesirkesen)
- LinkedIn: [Muhammed Beşir Keşen](https://www.linkedin.com/in/muhammed-besir-kesen-110926334)

## 🙏 Teşekkürler

- Algoritma geliştirmesinde katkıda bulunan herkese
- Açık kaynak topluluğuna
- Geri bildirim sağlayan tüm kullanıcılara

## 📊 Proje İstatistikleri

![GitHub repo size](https://img.shields.io/github/repo-size/mbesirkesen/bsg1)
![GitHub language count](https://img.shields.io/github/languages/count/mbesirkesen/bsg1)
![GitHub top language](https://img.shields.io/github/languages/top/mbesirkesen/bsg1)

---

⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!
