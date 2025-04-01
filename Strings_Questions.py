website='http://www.sadikturan.com'
course='Python Kursu: Bastan Sona Python Programlama Rehberiniz (40 saat)'

# 1 - 'course' karakter dizisinde kaç karakter olduğunu bulun.
solution=len(course)
print(f"course karakter dizisinde {solution} karakter var.")
# 2- 'website' içerisinden www karakterlerini alın.
solution=website[7:10]
print(f"{solution} ")
# 3- 'website' içerisinden com karakterlerini alın.
solution=website[-3:] and website[22:25]
print(f"{solution} ")
# 4- 'course' karakter dizisinin ilk 15 ve son 15 karakterlerini alın.
solution1=course[:15] 
solution2=course[-15:]
print(f"First 15: {solution1} \nLast 15: {solution2}")
# 5- 'course' ifadesinin karakterlerini tersten yazdırın.
solution=course[::-1]
print(f"{solution} ")

name,surname,age,job="Bora","Yilmaz",32,"muhendis"
# 6- Yukarıdaki değişkenleri kullanarak aşağıdaki ifadeyi oluşturun:
# Benim adım Bora Yilmaz, yaşım 32 ve mesleğim mühendis.
solution=f"Benim adim {name} {surname}, yasim {age} ve meslegim {job}."
print(solution)
# 7- 'Hello world' ifadesindeki 'w' harfini 'W' olarak yazdırın.
print("Hello world".replace("w","W"))
# 8- 'abc' ifadesini 3 defa yan yana yazdırın.
print("abc"*3)