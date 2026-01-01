# Sayı Üreteci (CDSNG)

Bu proje, kübik kongruansiyel yöntem kullanarak deterministik rastgele sayı üreten bir Python uygulamasıdır. CDSNG (Cubic Congruential Number Generator) algoritması temel alınarak geliştirilmiştir.

## Özellikler

- **Deterministik Üretim**: Aynı seed değeri ile her zaman aynı sayı dizisini üretir.
- **Tamsayı ve Ondalık Üretim**: Hem tamsayı hem de [0, 1) aralığında ondalık sayı üretme desteği.
- **Kolay Kullanım**: Basit bir sınıf yapısı ile entegre edilebilir.

## Gereksinimler

- Python 3.x

## Kurulum

1. Bu projeyi bilgisayarınıza indirin veya klonlayın.
2. Python 3.x'in yüklü olduğundan emin olun.

## Kullanım

### Temel Kullanım

```python
from sayiüreteci import CDSNG

# Seed ile başlat
gen = CDSNG(seed=12345)

# Tamsayı üret
print(gen.next_int())  # Örnek: 987654321

# Ondalık sayı üret
print(gen.next_float())  # Örnek: 0.456789
```

### Komut Satırı Kullanımı

Dosyayı doğrudan çalıştırarak etkileşimli kullanım:

```bash
python sayiüreteci.py
```

Program sizden seed değeri ve üretilecek sayı adedini isteyecektir.

## Algoritma Açıklaması

CDSNG algoritması aşağıdaki formülü kullanır:

```
X_{n+1} = (a * X_n^3 + b * X_n^2 + c * X_n + d) mod m
```

Burada:
- `a = 5`
- `b = 17`
- `c = 41`
- `d = 13`
- `m = 2^31`

## Dokümantasyon

Detaylı algoritma açıklaması için `docs/` klasöründeki dosyaları inceleyin:
- `Akış Diyagramı.txt`: Program akış diyagramı
- `Pseudocode.txt`: Algoritmanın sözde kodu

## Güvenlik Notu

Bu sayı üretici, eğlence, eğitim veya basit simülasyon amaçları için uygundur. Kriptografik uygulamalarda kullanılmamalıdır, çünkü deterministik yapısı nedeniyle güvenli rastgelelik sağlamaz.

## Katkıda Bulunma

Katkılarınızı memnuniyetle karşılıyoruz! Lütfen pull request gönderin veya issue açın.

## Lisans

Bu proje açık kaynak kodludur. Detaylar için lisans dosyasını inceleyin.