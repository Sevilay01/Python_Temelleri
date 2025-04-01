# Girilen 2 sayıdan hangisi büyüktür?
# x=int(input("ilk sayiyi giriniz:"))
# y=int(input("ikinci sayiyi giriniz:"))
# if x>y:
#     print(x,"büyüktür",y)
# elif x==y:
#     print("esit")
# else:
#     print(y,"büyüktür",x)



#hoca çözümü
# a=int(input("ilk sayiyi giriniz:"))
# b=int(input("ikinci sayiyi giriniz:"))
# result=(a>b)
# print(f'a:{a} > b:{b} {result}')



# Kullanıcıdan 2 vize (%60 ) ve final (%40) notunu alıp ortalama hesaplayınız.
# Ortalamaya gore ortalama 50 den buyuk ise gectin, 50 den kucuk ise kaldın yazısı yazdırınız
# x=float(input("ilk vizenizi giriniz:"))
# y=float(input("ikinci vizenizi giriniz:"))
# z= float(input("final notunuzu giriniz:"))
# k=((x+y)*60/200)+40*z/100
# if k>50:
#     print("gecti")
# else:
#     print("kaldi")

#hoca çözümü
# vize1=float(input("ilk vizenizi giriniz:"))
# vize2=float(input("ikinci vizenizi giriniz:"))
# final=float(input("final notunuzu giriniz:"))
# ortalama=(vize1+vize2)*60/200+final*40/100
# print(f'not ortalamaniz {ortalama} ve gecme durumunuz {ortalama>=50}')




#Girilen bir sayının tek mi çift mi oldugunu yazdırınız.
# x=int(input("sayiyi giriniz:"))
# if x%2==0:
#     print("cift")
# else:
#     print("tek")

#hoca çözümü
# sayi=int(input("sayiyi giriniz:"))
# ciftmi=sayi%2==0
# print(f'girilen sayi {sayi} ve {ciftmi} cift sayi')


# Girilen bir sayının pozitif mi negatif mi oldugunu yazdırınız
# x=int(input("sayiyi giriniz:"))
# if x>0:
#     print("pozitif")
# else:
#     print("negatif")

#hoca çözümü
# sayi=int(input("sayiyi giriniz:"))
# pozitifmi=sayi>0
# print(f'girilen sayi {sayi} ve {pozitifmi} pozitif sayi')





# Parola ve email bilgisi isteyip doğruluğunu kontrol ediniz.
# user_parola="1234"
# user_email="ali@example.com"
# parola=input("parolayi giriniz:")
# email=input("emaili giriniz:")
# print(parola==user_parola and email==user_email)

#hoca çözümü
# parola=input("parolayi giriniz:")
# email=input("emaili giriniz:")
# paroladogru=parola=="1234"
# emaildogru=email=="ali@example.com"
# print(f'parola dogru mu{paroladogru} ve email dogru mu {emaildogru}')