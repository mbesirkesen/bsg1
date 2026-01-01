"""
RSÜ İstatistiksel Test Modülü
Rastgele sayı üretecinin kalitesini test eder.

Testler:
- Ki-kare testi (Chi-square test)
- Runs testi
- Frequency testi
- Kolmogorov-Smirnov testi
"""

import math
from collections import Counter
from rsu import RSU


def chi_square_test(values, bins=10):
    """
    Ki-kare testi: Sayıların dağılımını test eder.
    
    Args:
        values (list): Test edilecek sayılar (0-1 arası)
        bins (int): Bölüm sayısı (varsayılan: 10)
    
    Returns:
        dict: Test sonuçları
    """
    n = len(values)
    expected_freq = n / bins
    
    # Sayıları bölümlere ayır
    observed = [0] * bins
    for value in values:
        bin_index = min(int(value * bins), bins - 1)
        observed[bin_index] += 1
    
    # Ki-kare istatistiği hesapla
    chi_square = sum((obs - expected_freq) ** 2 / expected_freq 
                     for obs in observed)
    
    # Serbestlik derecesi
    df = bins - 1
    
    # Kritik değer (α = 0.05 için)
    # Basitleştirilmiş: chi-square > 16.92 ise red (10 bins için)
    critical_value = 16.92 if bins == 10 else 9.49 if bins == 5 else 3.84
    
    passed = chi_square < critical_value
    
    return {
        'test_name': 'Chi-Square Test',
        'chi_square': chi_square,
        'degrees_of_freedom': df,
        'critical_value': critical_value,
        'passed': passed,
        'observed_frequencies': observed,
        'expected_frequency': expected_freq
    }


def runs_test(values):
    """
    Runs testi: Art arda gelen benzer değerlerin analizi.
    
    Args:
        values (list): Test edilecek sayılar (0-1 arası)
    
    Returns:
        dict: Test sonuçları
    """
    n = len(values)
    median = 0.5
    
    # Median'ın üstünde ve altında olanları işaretle
    sequence = ['+' if v >= median else '-' for v in values]
    
    # Runs sayısını hesapla
    runs = 1
    for i in range(1, n):
        if sequence[i] != sequence[i-1]:
            runs += 1
    
    # + ve - sayılarını say
    n1 = sequence.count('+')
    n2 = sequence.count('-')
    
    # Beklenen runs sayısı
    expected_runs = (2 * n1 * n2) / (n1 + n2) + 1
    
    # Varyans
    variance = (2 * n1 * n2 * (2 * n1 * n2 - n1 - n2)) / \
               ((n1 + n2) ** 2 * (n1 + n2 - 1))
    
    # Z skoru
    if variance == 0:
        z_score = 0
    else:
        z_score = (runs - expected_runs) / math.sqrt(variance)
    
    # Kritik değer (α = 0.05, two-tailed)
    critical_value = 1.96
    passed = abs(z_score) < critical_value
    
    return {
        'test_name': 'Runs Test',
        'runs': runs,
        'expected_runs': expected_runs,
        'z_score': z_score,
        'critical_value': critical_value,
        'passed': passed,
        'n1': n1,
        'n2': n2
    }


def frequency_test(values):
    """
    Frequency testi: 0 ve 1'lerin eşit dağılımını test eder.
    
    Args:
        values (list): Test edilecek sayılar (0-1 arası)
    
    Returns:
        dict: Test sonuçları
    """
    n = len(values)
    
    # 0-0.5 ve 0.5-1 aralıklarındaki sayıları say
    low = sum(1 for v in values if v < 0.5)
    high = n - low
    
    expected = n / 2
    difference = abs(low - high)
    
    # Yüzde farkı
    percent_diff = (difference / n) * 100
    
    # %5'ten az fark kabul edilebilir
    passed = percent_diff < 5.0
    
    return {
        'test_name': 'Frequency Test (0-1 Equality)',
        'low_range_count': low,
        'high_range_count': high,
        'expected': expected,
        'difference': difference,
        'percent_difference': percent_diff,
        'passed': passed
    }


def kolmogorov_smirnov_test(values):
    """
    Kolmogorov-Smirnov testi: Uniform dağılım testi.
    
    Args:
        values (list): Test edilecek sayılar (0-1 arası)
    
    Returns:
        dict: Test sonuçları
    """
    n = len(values)
    sorted_values = sorted(values)
    
    # D+ ve D- değerlerini hesapla
    d_plus = max((i + 1) / n - sorted_values[i] 
                 for i in range(n))
    d_minus = max(sorted_values[i] - i / n 
                  for i in range(n))
    
    d_statistic = max(d_plus, d_minus)
    
    # Kritik değer (α = 0.05, n > 50 için)
    if n > 50:
        critical_value = 1.36 / math.sqrt(n)
    else:
        # Küçük örnekler için tablo değeri (yaklaşık)
        critical_value = 0.19  # n=100 için
    
    passed = d_statistic < critical_value
    
    return {
        'test_name': 'Kolmogorov-Smirnov Test',
        'd_statistic': d_statistic,
        'd_plus': d_plus,
        'd_minus': d_minus,
        'critical_value': critical_value,
        'passed': passed
    }


def autocorrelation_test(values, lag=1):
    """
    Autocorrelation testi: Ardışık değerler arasındaki korelasyonu test eder.
    
    Args:
        values (list): Test edilecek sayılar
        lag (int): Gecikme (lag) değeri
    
    Returns:
        dict: Test sonuçları
    """
    n = len(values)
    if n <= lag:
        return {'test_name': 'Autocorrelation Test', 'passed': False, 
                'error': 'Sample size too small'}
    
    # Ortalama
    mean = sum(values) / n
    
    # Autocorrelation hesapla
    numerator = sum((values[i] - mean) * (values[i + lag] - mean) 
                    for i in range(n - lag))
    denominator = sum((values[i] - mean) ** 2 for i in range(n))
    
    if denominator == 0:
        autocorr = 0
    else:
        autocorr = numerator / denominator
    
    # Kritik değer (α = 0.05 için yaklaşık ±0.1)
    critical_value = 0.1
    passed = abs(autocorr) < critical_value
    
    return {
        'test_name': f'Autocorrelation Test (lag={lag})',
        'autocorrelation': autocorr,
        'critical_value': critical_value,
        'passed': passed
    }


def run_all_tests(values, sample_size=None):
    """
    Tüm istatistiksel testleri çalıştırır.
    
    Args:
        values (list): Test edilecek sayılar
        sample_size (int, optional): Örnek boyutu bilgisi
    
    Returns:
        dict: Tüm test sonuçları
    """
    if sample_size is None:
        sample_size = len(values)
    
    results = {
        'sample_size': sample_size,
        'tests': []
    }
    
    # Tüm testleri çalıştır
    tests = [
        chi_square_test(values),
        runs_test(values),
        frequency_test(values),
        kolmogorov_smirnov_test(values),
        autocorrelation_test(values, lag=1),
        autocorrelation_test(values, lag=2),
    ]
    
    results['tests'] = tests
    
    # Genel sonuç
    passed_count = sum(1 for t in tests if t.get('passed', False))
    results['total_tests'] = len(tests)
    results['passed_tests'] = passed_count
    results['all_passed'] = passed_count == len(tests)
    
    return results


def print_test_results(results):
    """
    Test sonuçlarını güzel formatta yazdırır.
    
    Args:
        results (dict): Test sonuçları
    """
    print("=" * 70)
    print("RSÜ İSTATİSTİKSEL TEST SONUÇLARI")
    print("=" * 70)
    print(f"Örnek Boyutu: {results['sample_size']}")
    print(f"Toplam Test: {results['total_tests']}")
    print(f"Başarılı: {results['passed_tests']}")
    print(f"Başarısız: {results['total_tests'] - results['passed_tests']}")
    print("=" * 70)
    print()
    
    for test in results['tests']:
        print(f"Test: {test['test_name']}")
        print("-" * 70)
        
        if 'error' in test:
            print(f"  Hata: {test['error']}")
        else:
            # Teste özel bilgileri yazdır
            for key, value in test.items():
                if key not in ['test_name', 'passed']:
                    if isinstance(value, float):
                        print(f"  {key}: {value:.6f}")
                    elif isinstance(value, list):
                        print(f"  {key}: {value}")
                    else:
                        print(f"  {key}: {value}")
        
        status = "✓ BAŞARILI" if test.get('passed', False) else "✗ BAŞARISIZ"
        print(f"  Sonuç: {status}")
        print()


if __name__ == "__main__":
    # Test için örnek üret
    print("RSÜ İstatistiksel Test Modülü")
    print("=" * 70)
    
    sample_size = int(input("Test için örnek boyutu (önerilen: 10000): ") or "10000")
    
    print(f"\n{sample_size} adet rastgele sayı üretiliyor...")
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

