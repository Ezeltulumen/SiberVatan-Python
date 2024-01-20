liste = [1,2,3,4,5]
print(liste)
print(liste[4])
print(type(liste))

liste[4]=50
print(liste)

alt_liste= liste[2:4]
print(alt_liste)

tuple= (10,10,20,30,40,50)
print(tuple)
print(tuple[1])

#tuple[1]=50
#print (tuple)
alt_tuple= tuple[1:4]
print(alt_tuple)

#kumeler(sets)
kume={100,200,300,400,500}
print(kume) 
kume.add(700)
print(kume)

kume.update([400,900])
print(kume)

#dict dictionary sözlük
dict ={'anahatar1':'deger1','anahtar2':'deger2'}
print(dict)

deger = dict ['anahatar1']
print(deger)

kume_list = list(kume)
print(kume_list)
print(type(kume_list))

#.keys() .values()
list_keys = list(dict.keys())
print(type(list_keys))
print(list_keys)

list_values = list(dict.values())
print(type(list_values))
print(list_values)

sayilar = [10,8,5,3,15]
en_buyuk= max(sayilar)
en_kucuk= min(sayilar)
print(en_buyuk)
print(en_kucuk)
sayilar.append(20)
sayilar.append(1)
yeni_en_buyuk= max(sayilar)
yeni_en_kucuk= min(sayilar)
print(yeni_en_buyuk)
print(yeni_en_kucuk)
print(sayilar)

sayilar.pop()
print(sayilar)

sayilar.sort()
print(sayilar)
sayilar.reverse()
print(sayilar)
sayilar.count
print(sayilar.count(10))

aralik = range(1,100)
print(list(aralik))
 
import random

rastgele_sayi = random.randint(1,100)
print('tutulan sayı', rastgele_sayi)
