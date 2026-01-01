"""
RSÜ İstatistiksel Testlerini Otomatik Çalıştır
"""

from statistical_tests import run_all_tests, print_test_results
from rsu import RSU

def main():
    # Test için örnek boyutu
    sample_size = 10000
    
    print(f"RSÜ İstatistiksel Test Modülü")
    print("=" * 70)
    print(f"{sample_size} adet rastgele sayı üretiliyor...")
    
    # Rastgele sayıları üret
    rsu = RSU()
    values = [rsu.next_float() for _ in range(sample_size)]
    
    print("İstatistiksel testler çalıştırılıyor...\n")
    
    # Tüm testleri çalıştır
    results = run_all_tests(values, sample_size)
    
    # Sonuçları yazdır
    print_test_results(results)
    
    # Sonuçları dosyaya kaydet
    with open('test_results.txt', 'w', encoding='utf-8') as f:
        f.write("RSÜ İSTATİSTİKSEL TEST SONUÇLARI\n")
        f.write("=" * 70 + "\n")
        f.write(f"Örnek Boyutu: {results['sample_size']}\n")
        f.write(f"Toplam Test: {results['total_tests']}\n")
        f.write(f"Başarılı: {results['passed_tests']}\n")
        f.write(f"Başarısız: {results['total_tests'] - results['passed_tests']}\n")
        f.write("=" * 70 + "\n\n")
        
        for test in results['tests']:
            f.write(f"Test: {test['test_name']}\n")
            f.write("-" * 70 + "\n")
            for key, value in test.items():
                if key not in ['test_name']:
                    if isinstance(value, float):
                        f.write(f"  {key}: {value:.6f}\n")
                    elif isinstance(value, list):
                        f.write(f"  {key}: {value}\n")
                    else:
                        f.write(f"  {key}: {value}\n")
            f.write(f"  Sonuç: {'BAŞARILI' if test.get('passed', False) else 'BAŞARISIZ'}\n")
            f.write("\n")
    
    print("Test sonuçları 'test_results.txt' dosyasına kaydedildi.")

if __name__ == "__main__":
    main()

