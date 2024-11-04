def main():
    # Kıyafet fiyatları
    fiyatlar = {
        'Pantolon': 1350,
        'Gömlek': 850,
        'Ayakkabı': 1500,
        'Tişört': 250,
        'Çorap': 150,
        'Mont': 850
    }

    # Sipariş listesini tutacak
    siparis = []
    toplam_ucret = 0

    # Ana ürünleri al
    print("Sipariş vermek için 'Pantolon', 'Gömlek' veya 'Ayakkabı' seçebilirsiniz.")
    while True:
        urun = input("Sipariş vermek istediğiniz ürünü girin (çıkmak için 'q' yazın): ")
        if urun.lower() == 'q':
            break
        elif urun in fiyatlar:
            siparis.append(urun)
            toplam_ucret += fiyatlar[urun]
        else:
            print("Geçersiz ürün. Lütfen tekrar deneyin.")

    # Ekstra ürünleri al
    print("\nEkstra ürünler eklemek ister misiniz? (Tişört, Çorap, Mont)")
    while True:
        ekstra = input("Ekstra ürün (çıkmak için 'q' yazın): ")
        if ekstra.lower() == 'q':
            break
        elif ekstra in fiyatlar:
            siparis.append(ekstra)
            toplam_ucret += fiyatlar[ekstra]
        else:
            print("Geçersiz ekstra ürün. Lütfen tekrar deneyin.")

    # Sonuçları yazdır
    print("\nSiparişiniz:")
    for urun in siparis:
        print(f"- {urun}: {fiyatlar[urun]} TL")
    print(f"\nToplam Ücret: {toplam_ucret} TL")

if __name__ == "__main__":
    main()
