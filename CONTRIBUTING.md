# Katkıda Bulunma Rehberi

CDSNG projesine katkıda bulunmak istediğiniz için teşekkürler! 🎉

## Nasıl Katkıda Bulunabilirim?

### 🐛 Hata Bildirimi

1. GitHub Issues'da yeni bir issue açın
2. Hatanın detaylı açıklamasını yapın
3. Hatanın nasıl tekrarlanabileceğini belirtin
4. Beklenen ve gerçek davranışı karşılaştırın
5. Sistem bilgilerinizi ekleyin (Python versiyonu, işletim sistemi vb.)

### ✨ Yeni Özellik Önerisi

1. Önce bir issue açarak özelliğinizi tartışın
2. Özelliğin neden gerekli olduğunu açıklayın
3. Özelliğin nasıl çalışacağını detaylandırın
4. Alternatif çözümleri değerlendirin

### 🔧 Pull Request Gönderme

1. **Fork edin**: Projeyi fork edin
2. **Branch oluşturun**: 
   ```bash
   git checkout -b feature/yeni-ozellik
   ```
3. **Değişikliklerinizi yapın**: Kodunuzu yazın ve test edin
4. **Commit edin**: 
   ```bash
   git commit -m "feat: yeni özellik eklendi"
   ```
5. **Push edin**: 
   ```bash
   git push origin feature/yeni-ozellik
   ```
6. **Pull Request açın**: GitHub'da PR açın

## Kod Standartları

### Python Stili

- PEP 8 kod stilini takip edin
- Satır uzunluğu maksimum 100 karakter
- Docstring'leri kullanın
- Type hints ekleyin (mümkünse)

### Commit Mesajları

Commit mesajlarınızı şu formatta yazın:

```
<tip>: <kısa açıklama>

<detaylı açıklama (opsiyonel)>
```

**Tipler:**
- `feat`: Yeni özellik
- `fix`: Hata düzeltmesi
- `docs`: Dokümantasyon değişikliği
- `style`: Kod formatı (kod değişikliği yok)
- `refactor`: Kod refaktörü
- `test`: Test ekleme/düzeltme
- `chore`: Build süreçleri, araçlar vb.

**Örnek:**
```
feat: next_range() metodu eklendi

Kullanıcıların belirli bir aralıkta sayı üretmesine
olanak sağlayan yeni bir metod eklendi.
```

## Test Etme

Değişikliklerinizi test etmek için:

```bash
python sayiüreteci.py
```

## Dokümantasyon

- Yeni özellikler için README.md'yi güncelleyin
- Kod içi dokümantasyon ekleyin
- Örnek kullanımlar ekleyin

## Sorular?

Herhangi bir sorunuz varsa, issue açmaktan çekinmeyin!

Teşekkürler! 🙏

