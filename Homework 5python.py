# Bankamatik Uygulaması

# Hesap bilgileri tutulacak. (dictionary)
# menu, paraCekme, bakiyeSorgula, paraYatirma fonksiyonları tanımlanacak.
# çekilmek istenen tutar hesapta yoksa ek hesabın kullanılmak istendiği sorulacak.
isim=input("Lütfen hesap ismi giriniz:")
bakiye=float(input("Lütfen bakiyenizi giriniz:"))
while bakiye<0:
    bakiye=float(input("Lütfen geçerli bir miktar giriniz:"))
def menu():
    global isim
    print(f"      ----Merhaba {isim},Bankaya Hosgeldiniz!----")
    print("1)Para cekme \t\t\t 2)Bakiye sorgulama")
    print("3)Para Yatirma \t\t\t 4)Cikis")
    islem=int(input("Yapmak istediğiniz islemi rakamla yazınız:"))
    return islem

def paraCekme():
    global bakiye
    global isim
    cekme=float(input("Para cekmek istediginiz tutarı giriniz:"))
    if cekme>bakiye:
        print("Cekeceginiz miktar bakiyenizden daha büyük,ek hesabınızı kullanmak ister misiniz?")
        secim=input("Evet         Hayir\n")
        while secim!="Evet" and secim!="Hayir":
             secim=input("Yazim hatasi yaptiniz,lütfen yeniden deneyiniz!\n")
        if secim=="Hayir":
            print("Ana ekrana yönlendiriliyorsunuz...")
        elif secim=="Evet":
            print("Yeni hesap secmeye yönlendiriliceksiniz,lütfen bekleyiniz!")
            isim=input("Lütfen hesap ismi giriniz:")
            bakiye=float(input("Lütfen bakiyenizi giriniz:"))
          
    
    else:
        bakiye-=cekme
        print(f"Basariyla hesabinizdan {cekme:.2f}Tl para cektiniz!")
        
def bakiyeSorgula():
    global bakiye
    print(" ")
    print(f"Mevcut bakiyeniz:{bakiye:.2f} TL")
    print(" ")

def paraYatirma():
    global bakiye
    yatirma=float(input("Para yatirmak istediginiz miktari giriniz:"))
    bakiye+=yatirma
    print(f"Basariyla hesabiniza {yatirma:.2f}Tl para yatirdiniz!")


while bakiye>=0 :
    islem = menu()
    if islem == 1:
        paraCekme()
    elif islem == 2:
        bakiyeSorgula()
    elif islem == 3:
        paraYatirma()
    elif islem == 4:
        print("Başarıyla çıkış yaptiniz!")
        break
    else:
        print("Yanlış yazdınız,lütfen tekrar deneyiniz!")
