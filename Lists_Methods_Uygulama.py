names=['Ali','Veli','Ayse','Fatma']
years=[1990,1980,1970,1960,1980]

# "Cenk" ismini listenin sonuna ekleyiniz.
names.append("Cenk")

#"Sena" ismini listenin başına ekleyiniz.
names.insert(0,'Sena')
# names.insert(len(names),'Mehmet') #son elemanı ekler
# "Fatma" ismini listeden siliniz.
names.remove("Fatma") or names.remove(names[3]) or names.remove(names[-1]) or names.pop()

#"Ali" listenin bir elemanı mıdır?
result='Ali' in names
print(result)

#Listeyi ters cevirin.
names.reverse()

#Listeyi alfabetik olarak sıralayın.
names.sort()

#years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()

#str="Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str="Chevrolet,Dacia"
str=str.split()
print(str)

#years dizisinin en büyük ve en küçük elemanı nedir?
min_years=min(years)
max_years=max(years)
print({min_years},{max_years})

#years dizisinde kaç tae 1980 vardır?
years.count(1980)

#years dizisinin tüm elemanlarını siliniz.
years.clear()

#Kullanıcıdan alacağınız 3 marka bilgisini bir listede saklayınız.
markalar = []  # Marka listesini oluştur
for i in range(3):
    marka = input(f"{i+1}. markayi giriniz: ")  # Kullanıcıdan marka al
    markalar.append(marka)  # Listeye ekle

print(markalar)  # Girilen markaları ekrana yazdır

print(names)