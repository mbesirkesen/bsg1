class CDSNG:
    def __init__(self, seed, a=5, b=17, c=41, d=13, m=2**31):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.m = m
        self.state = seed  # X0

    def next_int(self):
        """Bir sonraki tamsayıyı üretir."""
        x = self.state
        self.state = (self.a * (x ** 3) + self.b * (x ** 2) + self.c * x + self.d) % self.m
        return self.state

    def next_float(self):
        """[0, 1) aralığında sayı üretir."""
        return self.next_int() / self.m


if __name__ == "__main__":
    seed = int(input("Seed değerini gir: "))
    n = int(input("Kaç sayı üretilecek?: "))

    gen = CDSNG(seed)

    print("\nCDSNG ile üretilen sayılar:")
    for _ in range(n):
        print(gen.next_int())
