name='Ezel'
surname='Tülümen'
age=14
karsilama='benim adım'+' '+name+' '+surname+' '+'yaşım'+' '+str(age)+' '+'hoşgeldin'
print(karsilama)

uzunluk= len(karsilama)
print(uzunluk)
print(karsilama[3])
print(uzunluk-1)
print(karsilama[-1])
print(karsilama[4:10])
print(karsilama[0:10])
print(karsilama[:24])
print(karsilama[11:])
print(karsilama[2:25:3])
print(karsilama[:-3])
print(karsilama[::-1])
print(karsilama[::-2])

karsilama_upper = karsilama.upper()
print(karsilama_upper)

karsilama_lower = karsilama.lower()
print(karsilama_lower)

karsilama_strip = karsilama.strip()
print(karsilama_strip)

karsilama_split = karsilama.split()
print(karsilama_split[-3])

karsilama_strip = karsilama.strip()
print(karsilama_split[5])

karsilama_join = '-'.join(karsilama)
print(karsilama_join)

karsilama_find = karsilama.find('Ezel')
print(karsilama_find)

karsilama_startswith = karsilama.startswith('E')
print (karsilama_startswith)

karsilama_endswith = karsilama.endswith('n')
print (karsilama_endswith)

karsilama_replace = karsilama.replace ('Ezel','Tülümen')
print(karsilama_replace)
