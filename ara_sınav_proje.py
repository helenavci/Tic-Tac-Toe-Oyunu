from random import randrange  # Rastgele sayı üretmek için

# liste içindeki listeler satırdaki sayılar olacak
tahta = [[1, 2, 3],[4, 'X', 6],[7, 8, 9]]

# tahtanın görüntüsü için iç liste her okunduğunda kareler oluşacak
# tahtanın düzenli olması için sayıları string yaptım
def tahta_goster(tahta):
    print("+-------+-------+-------+")
    for satir in tahta:
        print("|       |       |       |")
        print("|   " + str(satir[0]) + "   |   " + str(satir[1]) + "   |   " + str(satir[2]) + "   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

# hamle yapılabilecek kareleri bulmak için
def bos_kareleri_bul(tahta):
    bos_kareler = []
    for s in range(3):        # satır
        for s2 in range(3):   # sütun
            if tahta[s][s2] not in ['X', 'O']:  # boşsa
                bos_kareler.append((s, s2))
    return bos_kareler


# kazanma durumunu kontrol etmek için fonksiyon
def kazanan_kontrol(tahta, isaret):
    # satırın tamanıda istenen işaret var mı diye kontrol eder
    for satir in tahta:
        if all(hucre == isaret for hucre in satir):
            return True

    # sütunda işareti kontrol eder
    for s2 in range(3):
        if all(tahta[s][s2] == isaret for s in range(3)):
            return True

    # çarpraz olarak işareti kontrol eder
    if all(tahta[i][i] == isaret for i in range(3)):
        return True
    if all(tahta[i][2 - i] == isaret for i in range(3)):
        return True

    return False


# kullanıcı
def oyuncu_hamlesi(tahta):
    while True:
        try:
            kare = int(input("Hamle yapmak için sayıyı gir: "))
            if kare < 1 or kare > 9:
                print("1 ile 9 arasında bir sayı gir!")
                continue

            satir = (kare - 1) // 3 # girilen sayının kaçıncı satırda olduğunu buluyor
            sutun = (kare - 1) % 3  # girilen sayının kaçıncı sütunda olduğunu buluyor

            if tahta[satir][sutun] in ['X', 'O']: # satır ve sütuna göre hücre kontrolü yapıyor
                print("Bu kare dolu! Başka bir sayı gir.")
            else:
                tahta[satir][sutun] = 'O'
                break
        except ValueError:
            print("Hatalı giriş yaptın.Sadece sayı girebilirsin.")


# bilgisayardan rastgele sayı almak için
def bilgisayar_hamlesi(tahta):
    bos_kareler = bos_kareleri_bul(tahta)
    if bos_kareler:
        secim = bos_kareler[randrange(len(bos_kareler))] # boş kareler listesinden rastgele seçim yapıyor
        tahta[secim[0]][secim[1]] = 'X'


# oyunu çalıştıran fonksiyon
def oyun():
    tahta_goster(tahta)
    while True:
        oyuncu_hamlesi(tahta)
        tahta_goster(tahta)

        if kazanan_kontrol(tahta, 'O'):
            print("Kazandın!")
            break

        if not bos_kareleri_bul(tahta):
            print("Berabere!")
            break

        bilgisayar_hamlesi(tahta)
        tahta_goster(tahta)

        if kazanan_kontrol(tahta, 'X'):
            print("Bilgisayar kazandı!")
            break

        if not bos_kareleri_bul(tahta):
            print("Berabere!")
            break


# oyunun çalışması için
oyun()
