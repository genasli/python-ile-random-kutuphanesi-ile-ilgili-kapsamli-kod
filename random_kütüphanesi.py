import random

def notlari_olustur(ogrenci_sayisi):
    notlar = [random.randint(0, 100) for _ in range(ogrenci_sayisi)]
    return notlar

def ortalama_hesapla(notlar):
    return sum(notlar) / len(notlar)

def ortalama_kontrol(notlar):
    yeni_notlar = [not_ + 10 if not_<=90 else not_ for not_ in notlar]
    return yeni_notlar
def harf_notunu_belirle(not_):
    if not_ < 20:
        return "FF"
    elif 20 <= not_ < 30:
        return "FD"
    elif 30 <= not_ < 40:
        return "DD"
    elif 40 <= not_ < 50:
        return "DC"
    elif 50 <= not_ < 60:
        return "CC"
    elif 60 <= not_ < 70:
        return "CB"
    elif 70 <= not_ < 80:
        return "BB"
    elif 80 <= not_ < 90:
        return "BA"
    else:
        return "AA"

def main():
    ogrenci_sayisi = 100
    notlar = notlari_olustur(ogrenci_sayisi)
    ortalama = ortalama_hesapla(notlar)

    print("{:->80s}".format("-"))
    print("Öğrenci Notları: {}".format(notlar))
    print("{:->80s}".format("-"))
    print("{:->80s}".format("-"))
    print("Sınıf Ortalaması: {:.2f}".format(ortalama))
    
    if ortalama < 50:
        yeni_notlar = ortalama_kontrol(notlar)
        yeni_ortalama = ortalama_hesapla(yeni_notlar)
        print(f"Herkesin notu 10 puan arttırılarak güncellenmiştir...\n")
        print(f"Yeni Notlar : {yeni_notlar}")
        print("{:->80s}".format("-"))
        for i, yeni_not in enumerate(yeni_notlar, 1):
            harf_notu = harf_notunu_belirle(yeni_not)
            print(f"{i}. Öğrencinin Notu: {yeni_not} Harf Notu: {harf_notu}")
            print("{:->80s}".format("-"))
    
    else:
        print("Sınıf ortalaması 50'nin üzerinde olduğu için notlar arttırılmamıştır...\n")
        print("{:->80s}".format("-"))
        for i, not_ in enumerate(notlar, 1):
            harf_notu = harf_notunu_belirle(not_)
            print(f"{i}. Öğrencinin Notu: {not_} Harf Notu: {harf_notu}")
            print("{:->80s}".format("-"))

if __name__ == "__main__":
    main()
