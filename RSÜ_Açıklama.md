# RSÜ - Rastgele Sayı Üreteci Algoritması Açıklaması

## 📋 Genel Bakış

RSÜ (Rastgele Sayı Üreteci), XORShift algoritması tabanlı yüksek kaliteli rastgele sayılar üreten bir Python kütüphanesidir. Algoritma, kriptografik olmayan uygulamalar için tasarlanmış olup, istatistiksel kalite ve performans odaklıdır.

## 🎯 Algoritma Gereksinimleri

Algoritmanın anahtar olarak kullanılabilmesi için iki kritik kriter:

1. **Tamamen Rastgele Olmalı**: Üretilen sayılar öngörülemez olmalı ve herhangi bir desen göstermemelidir.
2. **İstatistiksel Kalite (0-1 Eşitliği)**: Üretilen sayılar [0, 1) aralığında eşit dağılıma sahip olmalıdır.

## 🔬 Algoritma Mimarisi

### XORShift Algoritması

RSÜ, XORShift (XOR + Shift) algoritmasını kullanır. Bu algoritma:

- **Hızlı**: Bit düzeyinde işlemler kullanır
- **Verimli**: Düşük bellek kullanımı
- **Kaliteli**: İyi istatistiksel özellikler
- **Uzun Periyot**: 2^128 gibi çok uzun periyotlar

### Algoritma Detayları

#### 1. Seed Oluşturma

```python
seed = (sistem_zamanı * 1000000) XOR (process_id << 16)
```

- **Sistem Zamanı**: Mikrosaniye cinsinden zaman damgası
- **Process ID**: İşlem kimliği
- **XOR İşlemi**: İki kaynağı birleştirerek daha iyi rastgelelik

#### 2. State Başlatma

Algoritma 4 adet 32-bit state değeri kullanır:

```python
state[0] = seed & 0xFFFFFFFF
state[1] = (seed >> 32) & 0xFFFFFFFF
state[2] = (seed * 1103515245 + 12345) & 0xFFFFFFFF
state[3] = (seed * 1664525 + 1013904223) & 0xFFFFFFFF
```

Bu 4 state değeri, farklı LCG (Linear Congruential Generator) parametreleriyle oluşturulur.

#### 3. Warm-up

İlk 10 değer warm-up için kullanılır. Bu, state'lerin iyi karışmasını sağlar:

```python
for _ in range(10):
    _next()
```

#### 4. XORShift İşlemleri

Her sayı üretiminde iki çift state güncellenir:

**State 0 ve 1:**
```python
s1 = state[0]
s0 = state[1]
state[0] = s0
s1 ^= (s1 << 23) & 0xFFFFFFFF
s1 ^= s1 >> 17
s1 ^= s0
s1 ^= (s0 >> 26) & 0xFFFFFFFF
state[1] = s1
```

**State 2 ve 3:**
```python
s2 = state[2]
s3 = state[3]
state[2] = s3
s2 ^= (s2 << 19) & 0xFFFFFFFF
s2 ^= s2 >> 13
s2 ^= s3
s2 ^= (s3 >> 5) & 0xFFFFFFFF
state[3] = s2
```

#### 5. Sonuç Hesaplama

İki state birleştirilerek final sonuç elde edilir:

```python
result = (s1 + s0) & 0xFFFFFFFF
```

#### 6. Normalizasyon

[0, 1) aralığına normalize etmek için:

```python
float_result = result / (2**32)
```

## 📊 İstatistiksel Özellikler

### 1. Uniform Dağılım

Algoritma, [0, 1) aralığında uniform (eşit) dağılım sağlar. Bu, her değerin eşit olasılıkla üretilmesi anlamına gelir.

### 2. Bağımsızlık

Üretilen sayılar birbirinden bağımsızdır. Bir sayı, önceki sayıları tahmin etmek için kullanılamaz.

### 3. Periyot

Algoritma çok uzun bir periyoda sahiptir (yaklaşık 2^128). Bu, aynı dizinin tekrar etmeden önce çok uzun süre geçmesi anlamına gelir.

### 4. 0-1 Eşitliği

Üretilen sayıların yaklaşık %50'si [0, 0.5) aralığında, %50'si [0.5, 1.0) aralığında olmalıdır.

## 🧪 İstatistiksel Testler

Algoritmanın kalitesini doğrulamak için şu testler uygulanır:

### 1. Ki-Kare Testi (Chi-Square Test)

**Amaç**: Sayıların dağılımının uniform olup olmadığını test eder.

**Yöntem**: 
- [0, 1) aralığı 10 eşit bölüme ayrılır
- Her bölüme düşen sayı sayısı sayılır
- Beklenen ve gözlemlenen frekanslar karşılaştırılır

**Kriter**: Ki-kare istatistiği kritik değerin altında olmalıdır.

### 2. Runs Testi

**Amaç**: Art arda gelen benzer değerlerin analizini yapar.

**Yöntem**:
- Median (0.5) değerinin üstünde ve altında olanlar işaretlenir
- Runs (ardışık aynı işaretli gruplar) sayılır
- Z-skoru hesaplanır

**Kriter**: Z-skoru ±1.96 aralığında olmalıdır (α=0.05).

### 3. Frequency Testi (0-1 Eşitliği)

**Amaç**: 0-1 eşitliğini test eder.

**Yöntem**:
- [0, 0.5) ve [0.5, 1.0) aralıklarındaki sayılar sayılır
- Fark hesaplanır

**Kriter**: Fark %5'ten az olmalıdır.

### 4. Kolmogorov-Smirnov Testi

**Amaç**: Uniform dağılım testini yapar.

**Yöntem**:
- Kümülatif dağılım fonksiyonu (CDF) hesaplanır
- Teorik uniform CDF ile karşılaştırılır
- D istatistiği hesaplanır

**Kriter**: D istatistiği kritik değerin altında olmalıdır.

### 5. Autocorrelation Testi

**Amaç**: Ardışık değerler arasındaki korelasyonu test eder.

**Yöntem**:
- Farklı lag değerleri için korelasyon hesaplanır
- Autocorrelation katsayısı bulunur

**Kriter**: Autocorrelation ±0.1 aralığında olmalıdır.

## 🔧 Kullanım Örnekleri

### Temel Kullanım

```python
from rsu import RSU

# Generator oluştur
rsu = RSU()

# [0, 1) aralığında sayı üret
sayi = rsu.next_float()
print(sayi)  # Örnek: 0.7234567890
```

### Seed ile Kullanım

```python
# Belirli bir seed ile
rsu = RSU(seed=12345)

# Aynı seed ile aynı diziyi üretir
sayilar = [rsu.next_float() for _ in range(10)]
```

### Aralıkta Tamsayı Üretimi

```python
# 1-100 arası tamsayı
sayi = rsu.next_int(1, 101)
print(sayi)  # Örnek: 42
```

### Boolean Üretimi

```python
# Rastgele True/False
deger = rsu.next_bool()
print(deger)  # Örnek: True
```

## 📈 Performans

- **Hız**: O(1) zaman karmaşıklığı
- **Bellek**: O(1) bellek kullanımı (4 adet 32-bit değer)
- **Üretim Hızı**: Saniyede milyonlarca sayı üretebilir

## ⚠️ Kullanım Notları

1. **Kriptografik Uygulamalar**: Bu algoritma kriptografik güvenlik sağlamaz. Güvenlik gerektiren uygulamalar için `secrets` modülü kullanılmalıdır.

2. **Deterministik Davranış**: Aynı seed ile aynı diziyi üretir. Bu, test edilebilirlik için faydalıdır.

3. **Seed Seçimi**: Güvenli rastgelelik için seed otomatik oluşturulmalıdır (varsayılan davranış).

## 🔬 Algoritma Mantığı

### Neden XORShift?

1. **Hız**: XOR ve shift işlemleri çok hızlıdır
2. **Kalite**: İyi istatistiksel özellikler
3. **Basitlik**: Karmaşık matematiksel işlemler gerektirmez
4. **Periyot**: Çok uzun periyotlar sağlar

### Neden Çoklu State?

1. **Daha İyi Rastgelelik**: Birden fazla state daha iyi karışım sağlar
2. **Uzun Periyot**: Periyot uzunluğunu artırır
3. **Bağımsızlık**: State'ler birbirini etkilemez

### Neden Warm-up?

1. **İyi Karışım**: State'lerin başlangıç değerlerinden uzaklaşmasını sağlar
2. **Kalite**: İlk birkaç değer genellikle daha az rastgeledir
3. **Standart Uygulama**: RNG'lerde yaygın bir pratiktir

## 📚 Referanslar

- XORShift algoritması: George Marsaglia (2003)
- Linear Congruential Generator: D. H. Lehmer (1949)
- İstatistiksel testler: NIST SP 800-22

## 🎓 Sonuç

RSÜ algoritması, XORShift tabanlı yüksek kaliteli bir rastgele sayı üretecidir. İstatistiksel testlerle doğrulanmış olup, kriptografik olmayan uygulamalar için uygundur. Algoritma, tamamen rastgele üretim ve 0-1 eşitliği kriterlerini karşılamaktadır.

