# "Bmw,Mercedes,Opel,Mazda" elemanlarını listeye çevirin.
liste=["Bmw","Mercedes","Opel","Mazda"]
print(liste)

#Liste kaç elemanlıdır?
eleman_sayisi=len(liste)
print(eleman_sayisi)
#Listenin ilk ve son elemanını yazdırın.
ilk_son=liste[0],liste[-1]
print(ilk_son)
#Mazda değerini Toyota ile değiştirin.
liste[-1]="Toyota"
print(liste)
#Mercedes listenin bir elemanı mıdır?
mercedes=liste.__contains__("Mercedes")
# cevap='Mercedes' in liste
# print(cevap)
print(mercedes)
#Listenin -2 indeksindeki elemanı yazdırın.
print(liste[-2])
#Listenin ilk 3 elemanını yazdırın.
print(liste[0:3])
#Listenin son 2 elemanı yerine "Toyota" ve "Renault" ekleyin.
liste[-2:]=["Toyota","Renault"]
print(liste)
#Listenin üzerine "Audi" ve "Nissan" ekleyin.
liste.append("Audi")
liste.append("Nissan")
# cevap=liste+["Audi","Nissan"]
# print(cevap)
print(liste)
#Listenin son elemanını silin.
liste.remove(liste[-1])
print(liste)
#Liste elemanlarını tersten yazdırın.
#cevap=liste[::-1]
liste.reverse()
print(liste)

#Aşağıdaki verileri bir liste içinde saklayın:
# studentA:Yigit Bilgi 2010,(70,60,70)
# studentB:Ali Yilmaz 2011,(80,80,60)
# studentC:Ayse Yilmaz 2012,(90,80,70)

studentA=["Yigit","Bilgi",2010,(70,60,70)]
studentB=["Ali","Yilmaz",2011,(80,80,60)]  
studentC=["Ayse","Yilmaz",2012,(90,80,70)]
students=[studentA,studentB,studentC]
print(students)

