#1.soru
karsilama= input('cümlenizi yazınız:')
karsilama_strip = karsilama.strip()
print(karsilama_strip)
karsilama_lower = karsilama.lower()
print(karsilama_lower) 

#2.soru 
cumle= input('string giriniz: ')
karakter= input('aramak istediğiniz karakteri giriniz: ')
karaktersayisi = cumle.count(karakter)
print(f"'{cumle}' cümlesinde '{karakter}' karakteri {karaktersayisi} kez geçiyor.")

#3.soru
cumle = input('cümlenizi giriniz: ')
harf = input('harf giriniz: ')
harfsayisi = cumle.count(harf)
print(f"'{cumle}' cümlesinde '{harf}' harfi {harfsayisi} kez geçiyor.")

#4.soru
#string1 = input(" Veri girin: ")
#string2 = input("İkinci veriyi girin: ")

##5.soru
cumle = input("Bir cümle girin: ")
kelimeler = cumle.split()
sirali_kelimeler = sorted(kelimeler)
print("Cümlenin alfabetik sıraya göre sıralanmış hali:", ' '.join(sirali_kelimeler))

#6.Soru
string1 = input("Birinci stringi girin: ")
string2 = input("İkinci stringi girin: ")
birlesik_string = (string1 + string2).lower()
print("Birleştirilmiş stringin küçük harfe çevrilmiş hali:", birlesik_string)

#7.Soru #substring
ana_string = input("Bir string girin: ")
aranan_substring = input("Aramak istediğiniz substring'i girin: ")
yerine_eklenecek_substring = input("Yerine eklemek istediğiniz substring'i girin: ")
yeni_string = ana_string.replace(aranan_substring, yerine_eklenecek_substring)
print("Yeni string:", yeni_string)

#8.Soru
kelime = input("Bir kelime girin: ")
kelime = kelime.replace('a', '@')
print(f"değiştirilmiş hali: {kelime}")

#9.Soru

#10.Soru
cumle = input("Bir cümle girin: ")
kelimeler = cumle.split()
en_uzun_kelime = max(kelimeler, key=len)
print(f"Cümledeki en uzun kelime: {en_uzun_kelime}")

#11.Soru
liste = [1, 2, 3, 4, 5, 6]
orta_eleman = liste[len(liste)//2]
print(f"Listenin ortasındaki eleman: {orta_eleman}")

#12.Soru
tuple_ = (10, 20, 30, 40, 50)
yeni_tuple = (tuple_[1], tuple_[3])
print(f"Yeni tuple: {yeni_tuple}")

#13.Soru

#14.Soru

#15.Soru
liste = [1, 2, 3, 4, 5]
yeni_sayi = 10
liste.insert(len(liste)//2, yeni_sayi)
print("Listeye eklenmiş yeni sayı:", liste)

#16.Soru
liste = [1, 2, 3, 4, 5]
orta_eleman = liste[len(liste)//2]
tuple_ = (orta_eleman,)
print("Listenin ortasındaki elemanı içeren tuple:", tuple_)

#17.Soru?
set_ = {2, 4, 6, 8, 10}
liste = list(set_)
toplam = sum(liste)
print("Set elemanlarının toplamı:", toplam)

#18.Soru

#19.Soru
liste = [4, 9, 2, 8, 5]
en_buyuk_sayi = max(liste + [0])
print("Listenin içindeki en büyük sayı:", en_buyuk_sayi)

#20.Soru 
sozluk = {'anahtar1': 'deger1', 'anahtar2': 'deger2', 'anahtar3': 'deger3'}
birlesik_string = ''.join(sozluk.values())
print("Dict içindeki değerlerin birleştirilmiş hali:", birlesik_string)


