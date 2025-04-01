ogrenciler={
    '120':{
        'ad':'Ali',
        'soyad':'Yilmaz',
        'cinsiyet':'Erkek'
    },
    '125':{
        'ad':'Ayse',
        'soyad':'Yilmaz',
        'cinsiyet':'Kadin'
    },
    '130':{
        'ad':'Hasan',
        'soyad':'Yilmaz',
        'cinsiyet':'Erkek'
    }
}

# Bilgileri verilen öğrencileri kullancıdan aldırınız.
ogrenciler.clear()
number=input("ogrenci no:")
name=input("ogrenci ad:")
surname=input("ogrenci soyad:")
phone=input("ogrenci telefon:")


# ogrenciler[number]={
#     'ad':name,
#     'soyad':surname,
#     'telefon':phone
# }


#birden fazla ogrenci eklenebilir
for i in range (2):
    number=input("ogrenci no:")
    name=input("ogrenci ad:")
    surname=input("ogrenci soyad:")
    phone=input("ogrenci telefon:")
    ogrenciler.update({
        number:{
            'ad':name,
            'soyad':surname,
            'telefon':phone
        }
    })

print(ogrenciler)

'''
ogrenciler adlı bir sözlük (dictionary) kullanılıyor. Ancak, bu kod öncesinde ogrenciler adlı bir sözlük oluşturulmuş olmalı, yoksa hata verir.
ogrenci_no=input("Ogrenci No Giriniz: ")
ogrenciler[ogrenci_no]={
        'ad':input("Ogrenci Ad Giriniz: "),
        'soyad':input("Ogrenci Soyad Giriniz: "),
        'cinsiyet':input("Ogrenci Cinsiyet Giriniz: ")
    }
print(ogrenciler)
''' 
'''
yanlış kullanım örneği
ogrenciler+= {
    input("Ogrenci No Giriniz: "):{
        'ad':input("Ogrenci Ad Giriniz: "),
        'soyad':input("Ogrenci Soyad Giriniz: "),
        'cinsiyet':input("Ogrenci Cinsiyet Giriniz: ")
    }
 }

'''


#Öğrenci numarasını kullanıcıdan alarak bilgilerini ekrana yazdırınız.

# ogrNo=input("ogrenci_no:")
# ogrenci=(ogrenciler[ogrNo])

# print(ogrenciler[ogrNo])


