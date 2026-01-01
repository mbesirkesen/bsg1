"""
CDSNG Kullanım Örnekleri
Bu dosya, CDSNG sınıfının farklı kullanım senaryolarını gösterir.
"""

from sayiüreteci import CDSNG


def ornek_1_temel_kullanim():
    """Temel kullanım örneği"""
    print("=" * 50)
    print("Örnek 1: Temel Kullanım")
    print("=" * 50)
    
    gen = CDSNG(seed=42)
    
    print("İlk 5 tamsayı:")
    for i in range(5):
        print(f"  {i+1}. sayı: {gen.next_int()}")
    
    print("\nİlk 5 ondalık sayı:")
    gen2 = CDSNG(seed=42)  # Aynı seed ile başlat
    for i in range(5):
        print(f"  {i+1}. sayı: {gen2.next_float():.6f}")


def ornek_2_ozel_parametreler():
    """Özel parametrelerle kullanım"""
    print("\n" + "=" * 50)
    print("Örnek 2: Özel Parametreler")
    print("=" * 50)
    
    gen = CDSNG(
        seed=100,
        a=7,
        b=19,
        c=43,
        d=17,
        m=2**31
    )
    
    print("Özel parametrelerle üretilen sayılar:")
    for i in range(5):
        print(f"  {i+1}. sayı: {gen.next_int()}")


def ornek_3_simulasyon():
    """Basit simülasyon örneği"""
    print("\n" + "=" * 50)
    print("Örnek 3: Basit Simülasyon (Zar Atma)")
    print("=" * 50)
    
    gen = CDSNG(seed=12345)
    
    print("10 kez zar atılıyor:")
    for i in range(10):
        # 1-6 arası sayı üret
        zar = (gen.next_int() % 6) + 1
        print(f"  {i+1}. zar: {zar}")


def ornek_4_istatistik():
    """İstatistiksel analiz örneği"""
    print("\n" + "=" * 50)
    print("Örnek 4: İstatistiksel Analiz")
    print("=" * 50)
    
    gen = CDSNG(seed=999)
    n = 1000
    
    # 0-1 arası sayılar üret
    sayilar = [gen.next_float() for _ in range(n)]
    
    ortalama = sum(sayilar) / n
    minimum = min(sayilar)
    maksimum = max(sayilar)
    
    print(f"Üretilen sayı adedi: {n}")
    print(f"Ortalama: {ortalama:.6f}")
    print(f"Minimum: {minimum:.6f}")
    print(f"Maksimum: {maksimum:.6f}")
    print(f"Beklenen ortalama (0.5): {abs(ortalama - 0.5):.6f} farkla")


def ornek_5_deterministik():
    """Deterministik özellik gösterimi"""
    print("\n" + "=" * 50)
    print("Örnek 5: Deterministik Özellik")
    print("=" * 50)
    
    seed = 42
    
    # İlk generator
    gen1 = CDSNG(seed=seed)
    sayilar1 = [gen1.next_int() for _ in range(5)]
    
    # Aynı seed ile ikinci generator
    gen2 = CDSNG(seed=seed)
    sayilar2 = [gen2.next_int() for _ in range(5)]
    
    print("Aynı seed (42) ile iki farklı generator:")
    print(f"Generator 1: {sayilar1}")
    print(f"Generator 2: {sayilar2}")
    print(f"Sonuçlar aynı mı? {sayilar1 == sayilar2}")


if __name__ == "__main__":
    print("\n" + "🔢 CDSNG Kullanım Örnekleri 🔢\n")
    
    ornek_1_temel_kullanim()
    ornek_2_ozel_parametreler()
    ornek_3_simulasyon()
    ornek_4_istatistik()
    ornek_5_deterministik()
    
    print("\n" + "=" * 50)
    print("Tüm örnekler tamamlandı!")
    print("=" * 50 + "\n")

