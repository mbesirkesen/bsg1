"""
RSÜ - Rastgele Sayı Üreteci (Random Number Generator)
XORShift algoritması kullanarak yüksek kaliteli rastgele sayılar üretir.

Algoritma Özellikleri:
- Tamamen rastgele üretim
- İstatistiksel kalite (0-1 eşitliği)
- Yüksek performans
- Uzun periyot
"""

import time
import os


class RSU:
    """
    Rastgele Sayı Üreteci (Random Number Generator)
    XORShift algoritması kullanarak rastgele sayılar üretir.
    """
    
    def __init__(self, seed=None):
        """
        RSÜ generator'ü başlatır.
        
        Args:
            seed (int, optional): Başlangıç değeri. 
                                 None ise sistem zamanı ve PID kullanılır.
        """
        if seed is None:
            # Sistem zamanı ve process ID'yi birleştirerek seed oluştur
            seed = int(time.time() * 1000000) ^ (os.getpid() << 16)
            seed = seed & 0xFFFFFFFFFFFFFFFF  # 64-bit mask
        
        # Seed'i 4 parçaya böl (XORShift128+ için)
        self.state = [0] * 4
        self.state[0] = seed & 0xFFFFFFFF
        self.state[1] = (seed >> 32) & 0xFFFFFFFF
        self.state[2] = (seed * 1103515245 + 12345) & 0xFFFFFFFF
        self.state[3] = (seed * 1664525 + 1013904223) & 0xFFFFFFFF
        
        # İlk değerleri karıştır (warm-up)
        for _ in range(10):
            self._next()
    
    def _next(self):
        """
        Bir sonraki 32-bit rastgele sayıyı üretir (internal).
        XORShift algoritması kullanır.
        
        Returns:
            int: 32-bit rastgele sayı
        """
        # XORShift128+ benzeri algoritma
        s1 = self.state[0]
        s0 = self.state[1]
        
        # XOR ve shift işlemleri
        self.state[0] = s0
        s1 ^= (s1 << 23) & 0xFFFFFFFF
        s1 ^= s1 >> 17
        s1 ^= s0
        s1 ^= (s0 >> 26) & 0xFFFFFFFF
        self.state[1] = s1
        
        # İkinci state'i de güncelle
        s2 = self.state[2]
        s3 = self.state[3]
        self.state[2] = s3
        s2 ^= (s2 << 19) & 0xFFFFFFFF
        s2 ^= s2 >> 13
        s2 ^= s3
        s2 ^= (s3 >> 5) & 0xFFFFFFFF
        self.state[3] = s2
        
        # İki state'i birleştir
        result = (s1 + s0) & 0xFFFFFFFF
        return result
    
    def next_int(self, min_val=0, max_val=None):
        """
        Belirli bir aralıkta tamsayı üretir.
        
        Args:
            min_val (int): Minimum değer (varsayılan: 0)
            max_val (int, optional): Maksimum değer. None ise 2^32-1
        
        Returns:
            int: [min_val, max_val) aralığında rastgele sayı
        """
        if max_val is None:
            return self._next()
        
        range_size = max_val - min_val
        if range_size <= 0:
            return min_val
        
        # Modulo bias'ı önlemek için rejection sampling
        max_acceptable = (0xFFFFFFFF // range_size) * range_size
        
        while True:
            value = self._next()
            if value < max_acceptable:
                return min_val + (value % range_size)
    
    def next_float(self):
        """
        [0, 1) aralığında ondalık sayı üretir.
        
        Returns:
            float: 0 ile 1 arasında rastgele ondalık sayı
        """
        # 32-bit sayıyı [0, 1) aralığına normalize et
        return self._next() / (2**32)
    
    def next_bool(self):
        """
        Rastgele boolean değer üretir.
        
        Returns:
            bool: Rastgele True veya False
        """
        return (self._next() & 1) == 1
    
    def next_bits(self, n_bits):
        """
        N bitlik rastgele sayı üretir.
        
        Args:
            n_bits (int): Üretilecek bit sayısı (1-32)
        
        Returns:
            int: N bitlik rastgele sayı
        """
        if n_bits <= 0 or n_bits > 32:
            raise ValueError("n_bits must be between 1 and 32")
        
        mask = (1 << n_bits) - 1
        return self._next() & mask


def generate_sample(n, seed=None):
    """
    Örnek sayı dizisi üretir.
    
    Args:
        n (int): Üretilecek sayı adedi
        seed (int, optional): Seed değeri
    
    Returns:
        list: Rastgele sayı listesi
    """
    rsu = RSU(seed=seed)
    return [rsu.next_float() for _ in range(n)]


if __name__ == "__main__":
    print("=" * 60)
    print("RSÜ - Rastgele Sayı Üreteci")
    print("=" * 60)
    
    # Seed al
    seed_input = input("Seed değeri (Enter = otomatik): ").strip()
    seed = int(seed_input) if seed_input else None
    
    # Sayı adedi al
    n = int(input("Kaç sayı üretilecek?: "))
    
    # Generator oluştur
    rsu = RSU(seed=seed)
    
    print(f"\n{'='*60}")
    print(f"Üretilen {n} adet rastgele sayı (0-1 arası):")
    print(f"{'='*60}\n")
    
    # Sayıları üret ve göster
    for i in range(n):
        value = rsu.next_float()
        print(f"{i+1:4d}. {value:.10f}")
    
    print(f"\n{'='*60}")
    print("İstatistiksel Bilgiler:")
    print(f"{'='*60}")
    
    # İstatistiksel analiz
    rsu2 = RSU(seed=seed)
    values = [rsu2.next_float() for _ in range(n)]
    
    mean = sum(values) / n
    min_val = min(values)
    max_val = max(values)
    
    # 0-1 eşitliği kontrolü
    zeros = sum(1 for v in values if v < 0.5)
    ones = n - zeros
    
    print(f"Ortalama:        {mean:.10f} (beklenen: 0.5)")
    print(f"Minimum:         {min_val:.10f}")
    print(f"Maksimum:        {max_val:.10f}")
    print(f"0-0.5 arası:     {zeros} ({zeros/n*100:.2f}%)")
    print(f"0.5-1.0 arası:   {ones} ({ones/n*100:.2f}%)")
    print(f"Eşitlik farkı:   {abs(zeros - ones)} (ideal: 0)")
    print(f"{'='*60}\n")

