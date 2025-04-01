
x,y,z=2,5,107
numbers=1,5,7,10,6
#Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkını yazdırınız.
# a=int(input("ilk sayiyi giriniz:"))
# b=int(input("ikinci sayiyi giriniz:"))

# print(a*b-(x+y+z))

    

#y'nin x'e kalansız bölümünü hesaplayınız.
print(y//x) #kalansız bölmeyi yaptık

#  (x,y,z) toplamının mod 3'ü nedir?
k=x+y+z
k%=3
print(k)
# y'nin x. kuvvetini hesaplayınız.
print(y**x)
# x,*y,z = numbers işlemine göre z'nin küpü kaçtır?
x,*y,z=numbers # x=1 y=[5,7,10] z=6
print(z,z**3)
# x,*y,z= numbers işlemine göre y nin değerleri toplamı kaçtır?
x,*y,z=numbers
print(sum(y))
